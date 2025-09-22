Claude Code 备忘清单

### 安装与启动

| 操作 | 命令 |
|------|------|
| 安装（脚本） | `curl -sL https://install.anthropic.com \| sh` |
| 安装（npm） | `npm install -g @anthropic-ai/claude-code` |
| 启动交互式 REPL | `claude` |
| 直接运行指令 | `claude "summarize this project"` |
| 查看版本 | `claude --version` |
| 更新 | `claude update` |

### 基础命令

| 操作 | 命令 |
|------|------|
| 启动 REPL | `claude` |
| 一次性输出并退出 | `claude -p "explain"` |
| 继续最近会话 | `claude -c` / `claude --continue` |
| 恢复指定会话 | `claude -r <session_id>` |
| 查看帮助 | `/help` |
| 清理上下文 | `/clear` |
| 退出 | `/exit` |

### 快捷键与会话控制

| 操作 | 快捷键 |
|------|--------|
| 取消当前操作 | Ctrl + C |
| 退出 REPL | Ctrl + D |
| 历史记录 | ↑ / ↓ |
| 自动补全 | Tab |

### 模型与上下文

| 操作 | 命令 |
|------|------|
| 切换模型 | `claude --model sonnet` / `opus` / `haiku` |
| 添加目录 | `claude --add-dir ../apps ../lib` |
| 设置最大轮次 | `claude --max-turns 5` |
| 输出格式 | `--output-format json|text|stream-json` |
| 输入格式 | `--input-format text|json` |

### 工具与权限

| 操作 | 命令 |
|------|------|
| 允许工具 | `claude --allowedTools "Bash(git log:*)" "Write"` |
| 禁用工具 | `claude --disallowedTools "Bash(rm:*)" "Bash(sudo:*)"` |
| 权限提示工具 | `claude -p --permission-prompt-tool mcp_auth_tool "query"` |
| 跳过权限检查（危险） | `claude --dangerously-skip-permissions` |

### MCP（Model Context Protocol）

| 操作 | 命令 |
|------|------|
| 启用 MCP | `claude --mcp` |
| 打开 MCP 管理 | `/mcp` |
| 构建自定义 MCP 服务 | 按官方教程（如天气服务） |
| 用法示例 | `git log \| claude -p "summarize"` |

### Git 与集成

| 操作 | 命令 |
|------|------|
| 总结 Git log | `git log | claude -p "summarize commits"` |
| 审查 PR | `git diff HEAD~1 | claude -p "review this PR"` |
| 生成 Changelog | `git log --oneline -10 | claude -p "create changelog"` |

### 脚本与自动化

| 操作 | 脚本示例 |
|------|----------|
| 分析代码库 | `claude -p "analyze codebase" --output-format json > analysis.json` |
| 生成测试 | `claude -p "generate tests" --max-turns 3 > tests.txt` |
| 文档生成 | `for f in src/*.py; do claude -p "docstring for $f"; done` |

### 故障排查

| 操作 | 命令 |
|------|------|
| 健康检查 | `/doctor` |
| IDE 集成 | `/ide` 或 IDE 内置终端执行 `claude` |
| 压缩对话 | `/compact` |
| 查看成本/耗时 | `/cos` |

### 最佳实践与安全

| 建议 | 说明 |
|------|------|
| 拆分任务 | 避免超长对话 |
| 限制上下文 | 使用 `--max-turns`、`/compact` |
| 禁止危险命令 | 用黑名单屏蔽 `rm`、`sudo` |
| 保持更新 | 定期运行 `claude update` |
