# 使用说明

## 结构如下

```markdown
custom/
├── README.md           # 使用说明
├── languages/          # 放置编程语言相关的自定义 .md 文件
├── frameworks/         # 放置框架相关的自定义 .md 文件
├── tools/              # 放置工具相关的自定义 .md 文件
├── formats/            # 放置格式相关的自定义 .md 文件
├── references/         # 放置参考资料相关的自定义 .md 文件
├── prompts/            # 放置 AI 提示词相关的自定义 .md 文件
├── snippets/           # 放置代码片段相关的自定义 .md 文件
└── misc/               # 放置其他内容的自定义 .md 文件
```

## 使用方法

1. 将你自己创建的 .md 文件放在 custom 目录下的相应子目录中
2. 当你提交这些文件到 GitHub 时，GitHub Actions 会自动触发
3. 脚本会将这些文件复制到相应的目标目录，并确保文件名首字母大写原始文件仍保留在 custom 目录中，作为源文件
> 例如，如果你创建了一个自定义的 Swift 笔记：
> 1. 将文件保存为custom/languages/my-swift-notes.md
> 2. 提交并推送到 GitHub
> 3. GitHub Actions 会自动将其复制到docs/languages/My-Swift-Notes.md
