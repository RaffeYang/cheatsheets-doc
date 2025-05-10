#!/usr/bin/env python3
import argparse
import glob
import os
import re
import shutil
from datetime import datetime

import requests
import yaml


def load_config(config_file):
    """加载配置文件"""
    with open(config_file, "r") as f:
        return yaml.safe_load(f)


def download_file(owner, repo, branch, file_path):
    """从 GitHub 下载特定文件的内容"""
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{file_path}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        print(f"Error downloading {url}: {response.status_code}")
        return None


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
        "pnpm": "pnpm",
        "pip": "pip",
        "conda": "Conda",
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
    }

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


def save_file(content, destination):
    """保存文件内容到目标路径"""
    # 确保目标目录存在
    os.makedirs(os.path.dirname(destination), exist_ok=True)

    # 确保文件名首字母大写
    destination = capitalize_filename(destination)

    with open(destination, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Saved to {destination}")


def update_references(config):
    """根据配置更新参考资料"""
    for repo_config in config["repositories"]:
        owner = repo_config["owner"]
        repo = repo_config["repo"]
        branch = repo_config.get("branch", "main")

        print(f"\nProcessing {owner}/{repo}...")

        for file_config in repo_config["files"]:
            file_path = file_config["path"]
            destination = file_config["destination"]
            start_marker = file_config.get("start_marker")
            end_marker = file_config.get("end_marker")
            transformations = file_config.get("transformations")

            print(f"  Downloading {file_path}...")
            content = download_file(owner, repo, branch, file_path)

            if content:
                # 添加归属信息
                content = add_attribution(content, owner, repo, file_path, branch)

                # 过滤内容（如果指定了标记）
                content = filter_content(content, start_marker, end_marker)

                # 转换内容（如果指定了转换）
                content = transform_content(content, transformations)

                # 保存到目标位置
                save_file(content, destination)


def process_custom_files():
    """处理用户自定义的 .md 文件"""
    print("\nProcessing custom .md files...")

    # 定义源目录和目标目录映射
    directory_mapping = {
        "custom/languages": "docs/languages",
        "custom/frameworks": "docs/frameworks",
        "custom/tools": "docs/tools",
        "custom/formats": "docs/formats",
        "custom/references": "docs/references",
        "custom/prompts": "prompts",
        "custom/snippets": "snippets",
        "custom/misc": "misc",
    }

    # 确保所有自定义目录存在
    for src_dir in directory_mapping.keys():
        os.makedirs(src_dir, exist_ok=True)

    # 处理每个自定义目录中的 .md 文件
    for src_dir, dest_dir in directory_mapping.items():
        md_files = glob.glob(f"{src_dir}/*.md")

        for md_file in md_files:
            # 获取文件名
            _, filename = os.path.split(md_file)

            # 创建目标路径（确保首字母大写）
            dest_path = os.path.join(dest_dir, filename)
            dest_path = capitalize_filename(dest_path)

            # 确保目标目录存在
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            # 复制文件
            shutil.copy2(md_file, dest_path)
            print(f"Copied custom file: {md_file} -> {dest_path}")


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
    args = parser.parse_args()

    if args.init:
        create_initial_structure()

    if not args.custom_only:
        config = load_config(args.config)
        update_references(config)

    # 处理用户自定义的 .md 文件
    process_custom_files()

    print("\nAll references updated successfully!")


if __name__ == "__main__":
    main()
