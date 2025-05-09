# Cheatsheets

个人精选的编程语言速查表、框架参考和AI提示词集合。这个仓库专注于我日常使用的技术栈，通过自动化工具保持内容的更新和组织。

## 📚 关于本仓库

这是一个**个人定制**的开发参考资料集合，具有以下特点：

- **自动更新**：通过 GitHub Actions 自动从原始源获取最新内容
- **精选内容**：专注于我日常使用的技术，而非尝试涵盖所有可能的语言和框架
- **结构化组织**：按照类别清晰分类，便于快速查找
- **支持自定义**：可以轻松添加自己创建的参考资料

## 🗂️ 内容分类

本仓库内容分为四个主要类别：

### docs/ - 编程语言和工具参考

包含各种编程语言、框架和工具的速查表，如：
- 编程语言：Swift、Go、TypeScript、Python 等
- 框架：React、NextJS 等
- 工具：Git、Vim、Sublime Text 等
- 格式：Markdown、JSON、YAML 等
- 参考资料：正则表达式、HTTP状态码、颜色代码等

### prompts/ - AI提示词收集

收集各种有效的 AI 提示词模板，用于：
- 代码生成和重构
- 技术文档编写
- 特定模型的优化提示
- 领域特定任务

### snippets/ - 实用代码片段

包含各种可复用的代码片段：
- 前端开发常用功能
- 后端处理模式
- 算法实现
- 实用工具函数

### misc/ - 其他资源

其他有用的开发资源：
- 项目模板
- 检查清单
- 学习资源链接

## 🔄 自动更新机制

本仓库使用 GitHub Actions 实现自动更新：

- **定期更新**：每周自动从源仓库获取最新内容
- **手动触发**：可以随时手动触发更新流程
- **自定义内容**：当添加自定义内容时自动处理

## 🚀 使用指南

### 浏览内容

直接浏览仓库中的文件，或克隆到本地：

```bash
git clone https://github.com/RaffeYang/Cheatsheets.git
```

### 添加自定义内容

1. 在 `custom/` 目录下相应的子文件夹中创建 .md 文件
2. 提交并推送到 GitHub
3. GitHub Actions 会自动处理并将文件移动到正确的位置

例如，添加自己的 Swift 笔记：
```bash
# 创建文件
echo "# 我的 Swift 笔记" > custom/languages/my-swift-notes.md

# 提交更改
git add .
git commit -m "添加 Swift 笔记"
git push
```

### 添加新的内容源

修改 `config.yaml` 文件，添加新的仓库和文件：

```yaml
repositories:
  - owner: "新仓库所有者"
    repo: "仓库名称"
    branch: "main"
    files:
      - path: "docs/some-file.md"
        destination: "docs/languages/Some-File.md"
```

## 💡 为什么创建这个仓库？

- **集中管理**：将常用参考资料集中在一处
- **保持更新**：自动从原始源获取最新内容
- **个人定制**：只包含我实际使用的技术
- **跨设备访问**：通过 GitHub 在任何设备上访问

## 🛠️ 技术实现

本仓库使用以下技术实现自动化：

- **Python 脚本**：处理文件下载、转换和保存
- **GitHub Actions**：自动运行更新脚本
- **YAML 配置**：灵活定义内容源和目标位置

## 🤝 贡献

虽然这是个人仓库，但欢迎提出建议或报告问题：

1. Fork 这个仓库
2. 创建你的特性分支 (`git checkout -b feature/suggestion`)
3. 提交你的更改 (`git commit -m 'Add some suggestion'`)
4. 推送到分支 (`git push origin feature/suggestion`)
5. 创建一个 Pull Request

## 📄 许可

本项目采用 MIT 许可证 - 详情请查看 [LICENSE](LICENSE) 文件。

## 🙏 致谢

特别感谢以下项目提供了宝贵的参考资料：

- [jaywcjlove/reference](https://github.com/jaywcjlove/reference) - 提供了大量高质量的速查表
- 其他贡献内容的开源项目和作者

---

**注意**：这个仓库是个人学习和工作的辅助工具，不试图成为全面的参考资料集合。它的价值在于精选内容和自动化维护，使我能够专注于实际开发工作。

