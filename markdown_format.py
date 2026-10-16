"""Conservative Markdown cleanup for the Cheatsheets/Tinycast reader."""
import argparse
import html
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import urljoin

# Only presentation tags are unwrapped; placeholders such as <ENVNAME> survive.
PRESENTATION_TAGS = 'pur|yel|red|green|blue|pink|orange|sub|sup|span|sapn|div|p|b|strong|i|em|u|del|s|mark|small|center|label|form|fieldset|legend|select|datalist|option|textarea|ruby|rp|rt|bdi|thead|tbody|tfoot|caption|colgroup|col|ul|ol|li'
TOKEN = '\x00PROTECTED{}\x00'


def protect_code(source):
    protected = []
    def stash(value):
        token = TOKEN.format(len(protected))
        protected.append(value)
        return token
    lines = source.splitlines(keepends=True)
    result = []
    i = 0
    raw_block = None
    while i < len(lines):
        match = re.match(r'^ {0,3}(`{3,}|~{3,})', lines[i])
        if match:
            start = i
            i += 1
            close = re.compile(r'^ {0,3}' + re.escape(match[1][0]) + '{' + str(len(match[1])) + r',}\s*$')
            while i < len(lines) and not close.match(lines[i]):
                i += 1
            if i < len(lines):
                i += 1
            block = ''.join(lines[start:i])
            result.append(stash(block.rstrip('\n')) + ('\n' if block.endswith('\n') else ''))
            continue
        line = lines[i]
        opening = re.match(r'^ {0,3}<(audio|video|table|iframe|progress)\b', line, re.I)
        if opening and raw_block is None:
            raw_block = opening[1].lower()
        in_raw_block = raw_block is not None
        if raw_block and re.search(r'</' + raw_block + r'\s*>', line, re.I):
            raw_block = None
        if not in_raw_block and re.match(r'^( {4,}|\t+)\S', line):
            result.append(stash(line.rstrip('\n')) + ('\n' if line.endswith('\n') else ''))
        else:
            def inline(match):
                if match.group("htmlcode"):
                    value = html.unescape(re.sub(r"^<code\b[^>]*>|</code\s*>$", "", match[0], flags=re.I))
                    value = value.replace("\\`", "`")
                    ticks = "`" * (max((len(run) for run in re.findall(r"`+", value)), default=0) + 1)
                    padding = " " if value.startswith("`") or value.endswith("`") else ""
                    return stash(ticks + padding + value + padding + ticks)
                return stash(match[0])
            result.append(re.sub(r'(?P<htmlcode>(?<!\\)<code\b[^>]*>.*?</code\s*>)|(?<![\\`])(?P<ticks>`+)(?!`)(.+?)(?<!`)(?P=ticks)(?!`)', inline, line, flags=re.I))
        i += 1
    return ''.join(result), protected


def table_cells(line):
    # Use a scanner so even/odd backslash counts are handled without capture groups.
    cells = []
    start = slashes = 0
    for index, char in enumerate(line):
        if char == '|' and slashes % 2 == 0:
            cells.append(line[start:index].strip())
            start = index + 1
        slashes = slashes + 1 if char == '\\' else 0
    if not cells:
        return None
    cells.append(line[start:].strip())
    if not cells[0]:
        cells.pop(0)
    if cells and not cells[-1]:
        cells.pop()
    return cells


class HTMLTable(HTMLParser):
    def __init__(self):
        super().__init__()
        self.rows, self.row, self.cell = [], [], None
        self.cell_color = None
    def handle_starttag(self, tag, attrs):
        if tag == 'tr':
            self.row = []
        elif tag in ('td', 'th'):
            self.cell = []
            style = dict(attrs).get('style', '')
            color = re.search(r'background-color\s*:\s*([^;]+)', style, re.I)
            self.cell_color = color[1].strip() if color else None
        elif tag == 'br' and self.cell is not None:
            self.cell.append(' / ')
    def handle_data(self, data):
        if self.cell is not None:
            self.cell.append(data)
    def handle_endtag(self, tag):
        if tag in ('td', 'th') and self.cell is not None:
            value = ' '.join(''.join(self.cell).split())
            self.row.append((value or self.cell_color or '').replace('|', '\\|'))
            self.cell = None
        elif tag == 'tr' and self.row:
            self.rows.append(self.row)
    def markdown(self):
        if not self.rows:
            return ''
        width = max(map(len, self.rows))
        rows = [row + [''] * (width - len(row)) for row in self.rows]
        rows.insert(1, ['---'] * width)
        return '\n\n' + '\n'.join('| ' + ' | '.join(row) + ' |' for row in rows) + '\n\n'


def format_markdown(source):
    source = source.replace('\r\n', '\n')
    # Preserve existing attribution as visible Markdown, not a rendering comment.
    attribution = re.search(r'<!--\s*Source:\s*(\S+)\s+Retrieved on:\s*([^\n]+)\s*-->', source)
    source_url = attribution[1] if attribution else None
    footer = f'来源：[{source_url}]({source_url})\n\n获取日期：{attribution[2].strip()}\n' if attribution else ''
    if attribution:
        source = source[:attribution.start()] + source[attribution.end():]
    text, protected = protect_code(source)
    # YAML metadata delimiters are not visual horizontal rules.
    if text.startswith('---\n'):
        end = text.find('\n---', 4)
        if end != -1:
            metadata = text[:end + 4]
            token = TOKEN.format(len(protected))
            protected.append(metadata)
            text = token + text[end + 4:]
    text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
    def html_table(match):
        parser = HTMLTable()
        parser.feed(match[0])
        return parser.markdown()
    text = re.sub(r'(?<!\\)<table\b[^>]*>.*?</table\s*>', html_table, text, flags=re.I | re.S)
    def anchor(match):
        target, label = html.unescape(match[2]), match[3]
        if target.lower().startswith(('javascript:', 'data:')):
            return label
        return f'[{label}]({target})'
    text = re.sub(r'(?<!\\)<a\b[^>]*\bhref\s*=\s*([\'"])(.*?)\1[^>]*>(.*?)</a\s*>', anchor, text, flags=re.I | re.S)
    text = re.sub(r'(?<!\\)<img\b[^>]*\bsrc\s*=\s*([\'"])(.*?)\1[^>]*>', lambda m: f'![图片]({m[2]})', text, flags=re.I)
    text = re.sub(r'(?<!\\)<br\s*/?>', ' / ', text, flags=re.I)
    text = re.sub(r'(?<!\\)<(?P<media>progress|iframe|video|audio)\b[^>]*>.*?</(?P=media)\s*>', '', text, flags=re.I | re.S)
    text = re.sub(r'(?<!\\)</?(?:input|progress|iframe|video|audio|source|hr)\b[^>]*>', '', text, flags=re.I)
    text = re.sub(r'(?<!\\)<code\b[^>]*>(.*?)</code\s*>', lambda m: '`' + m[1] + '`', text, flags=re.I | re.S)
    text = re.sub(r'(?<!\\)((?:\\\\)*)</?(?:' + PRESENTATION_TAGS + r')\b[^>]*>', lambda m: m[1], text, flags=re.I)
    text = re.sub(r'\{\.[\w-]+(?:[ \t]+[\w.=-]+)*\}', '', text)
    # Decode layout spaces only; leave documented entity examples intact.
    text = text.replace('&nbsp;', ' ')
    if source_url:
        text = re.sub(r'(!?\[[^\]\n]*\]\()((?:\.\.?/)[^\s)]+)(\))', lambda m: m[1] + urljoin(source_url, m[2]) + m[3], text)
    lines, output = text.split('\n'), []
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        # Setext headings must become ATX headings before removing dividers.
        if i + 1 < len(lines) and line.strip() and '\x00' not in line and not re.match(r'^[#>|*-]', line):
            underline = lines[i + 1].strip()
            if re.fullmatch(r'=+|-+', underline):
                output.append(('# ' if underline[0] == '=' else '## ') + line.strip())
                i += 2
                continue
        if re.fullmatch(r'\s*(?:-{3,}|(?:\*\s*){3,}|(?:_\s*){3,})\s*', line):
            output.append('')
            i += 1
            continue
        header = table_cells(line)
        separator = table_cells(lines[i + 1]) if i + 1 < len(lines) else None
        if header and separator and len(header) == len(separator) and all(re.fullmatch(r':?-+:?', cell) for cell in separator):
            if output and output[-1].strip():
                output.append('')
            output.extend(('| ' + ' | '.join(header) + ' |', '| ' + ' | '.join(separator) + ' |'))
            i += 2
            while i < len(lines):
                row = table_cells(lines[i])
                if not row:
                    break
                output.append('| ' + ' | '.join(row) + ' |')
                i += 1
            if i < len(lines) and lines[i].strip():
                output.append('')
            continue
        output.append(line)
        i += 1
    result = re.sub(r'\n{3,}', '\n\n', '\n'.join(output)).strip() + '\n'
    if footer:
        result += '\n' + footer
    for index, value in enumerate(protected):
        result = result.replace(TOKEN.format(index), value)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('paths', nargs='*', default=['docs', 'prompts'])
    parser.add_argument('--check', action='store_true', help='Report files needing formatting without writing')
    args = parser.parse_args()
    changed = []
    for target in args.paths:
        path = Path(target)
        files = sorted(path.rglob('*.md')) if path.is_dir() else [path]
        for file in files:
            original = file.read_text(encoding='utf-8')
            formatted = format_markdown(original)
            if original != formatted:
                changed.append(str(file))
                if not args.check:
                    file.write_text(formatted, encoding='utf-8')
    print(f'{len(changed)} file(s) ' + ('need formatting' if args.check else 'formatted'))
    if args.check and changed:
        print('\n'.join(changed))
        raise SystemExit(1)

if __name__ == '__main__':
    main()
