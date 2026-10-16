"""Offline documentation checks; remote requests are explicit opt-in only."""
import argparse
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit
from markdown_format import format_markdown, protect_code


def fenced_blocks(content):
    blocks = []
    current = None
    for line in content.splitlines():
        if current is None:
            match = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', line)
            if match:
                current = [match[1], [line]]
        else:
            current[1].append(line)
            if re.fullmatch(r' {0,3}' + re.escape(current[0][0]) + '{' + str(len(current[0])) + r',}\s*', line):
                blocks.append('\n'.join(current[1]))
                current = None
    if current:
        raise ValueError('Unclosed code fence')
    return blocks


def config_entries(config):
    seen = set()
    for repository in config['repositories']:
        for item in repository['files']:
            destination = Path(item['destination'])
            if destination.is_absolute() or '..' in destination.parts or destination.suffix != '.md':
                raise ValueError(f'Unsafe destination: {destination}')
            key = str(destination).casefold()
            if key in seen:
                raise ValueError(f'Duplicate destination: {destination}')
            seen.add(key)
            yield repository['owner'], repository['repo'], repository.get('branch', 'main'), item


def read_destinations(path):
    """Read destination scalars from this repository's simple config offline."""
    result = re.findall(r'^\s+destination:\s*["\']?([^"\'\n#]+)', path.read_text(encoding='utf-8'), re.M)
    values = [value.strip() for value in result]
    if len({value.casefold() for value in values}) != len(values):
        raise ValueError('Duplicate config destination')
    for value in values:
        if Path(value).is_absolute() or '..' in Path(value).parts or not value.endswith('.md'):
            raise ValueError(f'Unsafe destination: {value}')
    return values


def check_document(content, path, links=True):
    errors = []
    if not content.strip() or '\x00' in content:
        errors.append(f'{path}: empty or NUL-containing document')
    try:
        fenced_blocks(content)
    except ValueError as exc:
        errors.append(f'{path}: {exc}')
    plain, _ = protect_code(content)
    if re.search(r'\{:\s*[^}]+\}', plain):
        errors.append(f'{path}: unconverted presentation annotation')
    if links:
        for target in re.findall(r'\]\(([^\s)]+)', plain):
            url = urlsplit(target.strip('<>'))
            if url.scheme or url.netloc or not url.path or target.startswith('/'):
                continue
            if not (path.parent / unquote(url.path)).exists():
                errors.append(f'{path}: missing local link {target}')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-remote-links', action='store_true', help='Explicitly enable bounded remote link requests')
    args = parser.parse_args()
    errors = []
    destinations = read_destinations(Path('config.yaml'))
    for directory in ('docs', 'prompts'):
        for path in sorted(Path(directory).rglob('*.md')):
            content = path.read_text(encoding='utf-8')
            errors.extend(check_document(content, path))
            if format_markdown(content) != content:
                errors.append(f'{path}: formatting is not normalized')
            if str(path) in destinations:
                if not re.search(r'(?:Source:|来源：).*https://github\.com/', content):
                    errors.append(f'{path}: missing upstream source')
                if not re.search(r'(?:Retrieved on:|获取日期：)\s*\d{4}-\d{2}-\d{2}', content):
                    errors.append(f'{path}: missing retrieval date')
            if args.check_remote_links:
                from urllib.request import urlopen
                plain, _ = protect_code(content)
                for url in sorted(set(re.findall(r'\]\((https?://[^\s)]+)', plain))):
                    try:
                        with urlopen(url, timeout=15) as response:
                            if response.status >= 400:
                                raise ValueError(response.status)
                    except Exception as exc:
                        errors.append(f'{path}: remote link {url}: {exc}')
    for destination in destinations:
        target = Path(destination)
        if target.exists() and target.name not in {item.name for item in target.parent.iterdir()}:
            errors.append(f'Configured filename case mismatch: {destination}')
        if not target.is_file():
            errors.append(f'Missing configured document: {destination}')
    print('\n'.join(errors) if errors else 'Documentation quality checks passed (offline).' )
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
