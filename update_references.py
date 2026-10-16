import argparse
import glob
import os
import re
import tempfile
import time
from datetime import datetime

from pathlib import Path

from markdown_format import format_markdown


def load_config(config_file):
    """加载配置文件"""
    import yaml

    with open(config_file, "r") as f:
        return yaml.safe_load(f)


def download_file(owner, repo, branch, file_path, attempts=3):
    """Download with bounded timeout and retry; failures reach the caller."""
    import requests
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{file_path}"
    for attempt in range(attempts):
        try:
            response = requests.get(url, timeout=(10, 30))
            response.raise_for_status()
            if not response.text.strip():
                raise ValueError(f"Empty upstream file: {url}")
            return response.text
        except (requests.RequestException, ValueError):
            if attempt + 1 == attempts:
                raise
            time.sleep(2 ** attempt)


def add_attribution(content, owner, repo, file_path, branch):
    """添加归属信息到文件内容"""
    attribution = f"""
<!-- 
Source: https://github.com/{owner}/{repo}/blob/{branch}/{file_path}
Retrieved on: {datetime.now().strftime("%Y-%m-%d")}
-->

"""
    return attribution + content


def filter_content(content, start_marker=None, end_marker=None):
    """提取文件的特定部分"""
    if start_marker and end_marker:
        start = content.find(start_marker)
        end = content.find(end_marker, start)
        if start != -1 and end != -1:
            return content[start : end + len(end_marker)]
    return content


def transform_content(content, transformations=None):
    """应用转换到内容"""
    if not transformations:
        return content

    result = content
    for transformation in transformations:
        if transformation["type"] == "replace":
            result = result.replace(transformation["search"], transformation["replace"])
        elif transformation["type"] == "regex_replace":
            result = re.sub(
                transformation["pattern"], transformation["replace"], result
            )
    return result


def capitalize_filename(filename):
    """将文件名按照特定规则处理，同时尊重特定技术名称的大小写约定"""
    # 分割路径和文件名
    path, name = os.path.split(filename)

    # 处理文件扩展名
    name_parts = name.rsplit(".", 1)
    base_name = name_parts[0]
    extension = name_parts[1] if len(name_parts) > 1 else ""

    # 特殊技术名称的大小写映射
    special_cases = {
        "swiftui": "SwiftUI",
        "mysql": "MySQL",
        "mariadb": "MariaDB",
        "postgresql": "PostgreSQL",
        "mongodb": "MongoDB",
        "redis": "Redis",
        "latex": "LaTeX",
        "openssl": "OpenSSL",
        "javascript": "JavaScript",
        "typescript": "TypeScript",
        "nodejs": "Node.js",
        "nextjs": "Next.js",
        "reactjs": "React.js",
        "vuejs": "Vue.js",
        "angularjs": "AngularJS",
        "expressjs": "Express.js",
        "css": "CSS",
        "html": "HTML",
        "http": "HTTP",
        "https": "HTTPS",
        "json": "JSON",
        "yaml": "YAML",
        "xml": "XML",
        "api": "API",
        "rest": "REST",
        "graphql": "GraphQL",
        "sql": "SQL",
        "nosql": "NoSQL",
        "php": "PHP",
        "ios": "iOS",
        "macos": "macOS",
        "linux": "Linux",
        "unix": "UNIX",
        "windows": "Windows",
        "github": "GitHub",
        "gitlab": "GitLab",
        "bitbucket": "Bitbucket",
        "git": "Git",
        "svn": "SVN",
        "ssh": "SSH",
        "ftp": "FTP",
        "sftp": "SFTP",
        "tcp": "TCP",
        "ip": "IP",
        "dns": "DNS",
        "url": "URL",
        "uri": "URI",
        "jwt": "JWT",
        "oauth": "OAuth",
        "saml": "SAML",
        "ldap": "LDAP",
        "ui": "UI",
        "ux": "UX",
        "cli": "CLI",
        "gui": "GUI",
        "sdk": "SDK",
        "ide": "IDE",
        "vscode": "VSCode",
        "intellij": "IntelliJ",
        "aws": "AWS",
        "azure": "Azure",
        "gcp": "GCP",
        "docker": "Docker",
        "kubernetes": "Kubernetes",
        "k8s": "K8s",
        "nginx": "NGINX",
        "apache": "Apache",
        "webpack": "Webpack",
        "babel": "Babel",
        "eslint": "ESLint",
        "prettier": "Prettier",
        "npm": "npm",
        "yarn": "Yarn",
        "pnpm": "PNPM",
        "pip": "Pip",
        "uv": "UV",
        "rust": "Rust",
        "homebrew": "Homebrew",
        "apt": "APT",
        "yum": "YUM",
        "ffmpeg": "FFmpeg",
        "iso": "ISO",
        "ascii": "ASCII",
        "utf": "UTF",
        "mime": "MIME",
        "css3": "CSS3",
        "html5": "HTML5",
        "es6": "ES6",
        "ecmascript": "ECMAScript",
        "dom": "DOM",
        "bom": "BOM",
        "regex": "RegEx",
        "regexp": "RegExp",
        "ai": "AI",
        "ml": "ML",
        "nlp": "NLP",
        "cv": "CV",
        "chatgpt": "ChatGPT",
        "openai": "OpenAI",
        "copilot": "Copilot",
        "stylex": "StyleX",
        "chakraui": "Chakra UI",
        "materialui": "Material UI",
        "tailwindcss": "Tailwind CSS",
        "bootstrap": "Bootstrap",
        "sass": "Sass",
        "scss": "SCSS",
        "less": "Less",
        "golang": "Go",
        "dotnet": ".NET",
        "csharp": "C#",
        "fsharp": "F#",
        "cpp": "C++",
        "aspnet": "ASP.NET",
        "webapi": "Web API",
        "mvc": "MVC",
        "mvvm": "MVVM",
        "crud": "CRUD",
        "restapi": "REST API",
        "websocket": "WebSocket",
        "sse": "SSE",
        "seo": "SEO",
        "analytics": "Analytics",
        "cicd": "CI/CD",
        "devops": "DevOps",
        "sre": "SRE",
        "tdd": "TDD",
        "bdd": "BDD",
        "ddd": "DDD",
        "solid": "SOLID",
        "package.json": "package.json",
        "tsconfig.json": "tsconfig.json",
        "webpack.config.js": "webpack.config.js",
        "babel.config.js": "babel.config.js",
        "eslintrc": ".eslintrc",
        "gitignore": ".gitignore",
        "npmrc": ".npmrc",
        "dockerignore": ".dockerignore",
        "editorconfig": ".editorconfig",
        "shapr3d": "Shapr3D",  # 添加 Shapr3D 支持
    }

    # 检查文件名是否已经匹配任何特殊情况的正确大小写
    for _, correct_case in special_cases.items():
        if base_name == correct_case:
            # 如果已经是正确的格式，直接返回原文件名
            return filename

    # 将连字符替换为空格
    words = base_name.replace("-", " ").split()

    # 处理每个单词，检查特殊情况
    processed_words = []
    for word in words:
        word_lower = word.lower()
        if word_lower in special_cases:
            processed_words.append(special_cases[word_lower])
        else:
            processed_words.append(word.capitalize())

    # 重新组合文件名
    new_base_name = " ".join(processed_words)

    # 处理特殊的复合名称
    for compound, replacement in special_cases.items():
        if " " in compound:  # 只处理包含空格的复合名称
            compound_pattern = compound.replace(" ", "").lower()
            if compound_pattern == new_base_name.replace(" ", "").lower():
                new_base_name = replacement
                break

    # 重新组合文件名和扩展名
    if extension:
        new_name = f"{new_base_name}.{extension}"
    else:
        new_name = new_base_name

    # 重新组合路径
    return os.path.join(path, new_name)


def prepare_content(content, destination):
    from doc_quality import fenced_blocks, check_document
    formatted = format_markdown(content)
    if fenced_blocks(content) != fenced_blocks(formatted):
        raise ValueError(f"Code fences changed: {destination}")
    if Path(destination).name == "UV.md":
        formatted = re.sub(r"(?m)^# uv(?=\s|$)", "# UV", formatted, count=1)
    errors = check_document(formatted, Path(destination), links=False)
    if errors:
        raise ValueError("; ".join(errors))
    return formatted


def save_file(content, destination):
    """Validate first, then atomically replace a single UTF-8 document."""
    destination = Path(destination)
    formatted = prepare_content(content, destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=destination.parent,
                                         prefix=".reference-", delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(formatted)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, destination)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


CUSTOM_MAPPING = {
    "custom/languages": "docs/languages", "custom/frameworks": "docs/frameworks",
    "custom/tools": "docs/tools", "custom/formats": "docs/formats",
    "custom/references": "docs/references", "custom/prompts": "prompts",
    "custom/snippets": "snippets", "custom/misc": "misc",
}


def custom_contents():
    result = {}
    for source, target in CUSTOM_MAPPING.items():
        for path in sorted(Path(source).glob("*.md")):
            destination = str(Path(target) / path.name)
            if not Path(destination).exists():
                destination = str(Path(target) / capitalize_filename(path.name))
            if destination.casefold() in {p.casefold() for p in result}:
                raise ValueError(f"Duplicate custom destination: {destination}")
            result[destination] = path.read_text(encoding="utf-8")
    return result


def update_references(config):
    """Stage every candidate and aggregate errors before replacing any output."""
    from doc_quality import config_entries
    pending, errors = {}, []
    custom = custom_contents()
    entries = list(config_entries(config))
    for owner, repo, branch, item in entries:
        destination = item["destination"]
        if destination in custom:
            continue
        try:
            raw = download_file(owner, repo, branch, item["path"])
            start, end = item.get("start_marker"), item.get("end_marker")
            if start or end:
                if not start or not end or raw.find(start) < 0 or raw.find(end, raw.find(start)) < 0:
                    raise ValueError("Filter markers missing or incomplete")
            content = filter_content(raw, start, end)
            content = transform_content(content, item.get("transformations"))
            content = add_attribution(content, owner, repo, item["path"], branch)
            pending[destination] = prepare_content(content, destination)
        except Exception as exc:
            errors.append(f"{destination}: {exc}")
    for destination, content in custom.items():
        try:
            pending[destination] = prepare_content(content, destination)
        except Exception as exc:
            errors.append(f"{destination}: {exc}")
    if errors:
        raise ValueError("Update aborted; no documents replaced:\n" + "\n".join(errors))
    for destination, content in pending.items():
        save_file(content, destination)
    return len(pending)


def process_custom_files():
    pending = {path: prepare_content(content, path) for path, content in custom_contents().items()}
    for path, content in pending.items():
        save_file(content, path)
    return len(pending)


def create_initial_structure():
    """创建初始目录结构"""
    directories = [
        # docs 目录 - 代码 cheatsheet
        "docs",
        "docs/languages",
        "docs/frameworks",
        "docs/tools",
        "docs/formats",
        "docs/environments",
        "docs/references",
        # prompts 目录 - AI prompts
        "prompts",
        "prompts/coding",
        "prompts/content",
        "prompts/models",
        "prompts/domains",
        # snippets 目录 - 各种代码片段
        "snippets",
        "snippets/frontend",
        "snippets/backend",
        "snippets/algorithms",
        "snippets/utilities",
        # misc 目录 - 其他内容
        "misc",
        "misc/checklists",
        "misc/resources",
        "misc/templates",
        # 自定义内容目录
        "custom",
        "custom/languages",
        "custom/frameworks",
        "custom/tools",
        "custom/formats",
        "custom/references",
        "custom/prompts",
        "custom/snippets",
        "custom/misc",
    ]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        # 在每个目录中创建一个 .gitkeep 文件，确保空目录也被 Git 跟踪
        with open(f"{directory}/.gitkeep", "w") as f:
            f.write("")

    # 创建自定义文件说明
    with open("custom/README.md", "w") as f:
        f.write("""# 自定义内容目录

将你自己创建的 .md 文件放在此目录下的相应子目录中，它们将在下次更新时自动处理：

- `custom/languages/` - 编程语言相关文件将移动到 `docs/languages/`
- `custom/frameworks/` - 框架相关文件将移动到 `docs/frameworks/`
- `custom/tools/` - 工具相关文件将移动到 `docs/tools/`
- `custom/formats/` - 格式相关文件将移动到 `docs/formats/`
- `custom/references/` - 参考资料将移动到 `docs/references/`
- `custom/prompts/` - AI 提示词将移动到 `prompts/`
- `custom/snippets/` - 代码片段将移动到 `snippets/`
- `custom/misc/` - 其他内容将移动到 `misc/`

所有文件名将自动转换为首字母大写格式。
""")

    print("Initial directory structure created.")


def format_existing_files(check=False):
    """离线规范化已存在的文档，默认不重新下载上游。"""
    changed = 0
    for directory in ("docs", "prompts"):
        for path in sorted(Path(directory).rglob("*.md")):
            original = path.read_text(encoding="utf-8")
            formatted = format_markdown(original)
            if original != formatted:
                changed += 1
                print(f"{'Needs formatting' if check else 'Formatted'}: {path}")
                if not check:
                    save_file(formatted, path)
    return changed


def main():
    parser = argparse.ArgumentParser(
        description="Update reference materials from GitHub repositories"
    )
    parser.add_argument(
        "--config", default="config.yaml", help="Path to configuration file"
    )
    parser.add_argument(
        "--init", action="store_true", help="Create initial directory structure"
    )
    parser.add_argument(
        "--custom-only", action="store_true", help="Only process custom files"
    )
    parser.add_argument("--format-only", action="store_true", help="Format local docs without downloading")
    parser.add_argument("--check", action="store_true", help="With --format-only, check without writing")
    args = parser.parse_args()
    if args.check and not args.format_only:
        parser.error("--check requires --format-only")
    if args.format_only:
        changed = format_existing_files(check=args.check)
        print(f"{changed} file(s) {'need formatting' if args.check else 'formatted'}")
        if args.check and changed:
            raise SystemExit(1)
        return

    if args.init:
        create_initial_structure()

    if not args.custom_only:
        config = load_config(args.config)
        update_references(config)

    if args.custom_only:
        process_custom_files()

    print("\nAll references updated successfully!")


if __name__ == "__main__":
    main()
