Excel 备忘清单

### 导航与单元格选择

| 操作         | 快捷键               |
| ---------- | ----------------- |
| 上移一格       | ↑                 |
| 下移一格       | ↓ 或 Return ↩      |
| 左移一格       | ← 或 ⇧ Shift + Tab |
| 右移一格       | → 或 Tab           |
| 移动至当前行首    | Fn + ←            |
| 移动至第一个单元格  | ⌘ + Fn + ←        |
| 移动至最后一个单元格 | ⌘ + Fn + →        |
| 下移一页       | Fn + ↓            |
| 上移一页       | Fn + ↑            |

### 编辑与操作

| 操作      | 快捷键                 |
| ------- | ------------------- |
| 剪切      | ⌘ + X               |
| 复制      | ⌘ + C               |
| 粘贴      | ⌘ + V               |
| 撤销      | ⌘ + Z               |
| 重做      | ⇧ Shift + ⌘ + Z     |
| 查找      | ⌘ + F               |
| 替换      | ⌘ + H               |
| 编辑当前单元格 | Control + U 或 双击单元格 |
| 清除单元格内容 | Delete ⌫            |

### 格式化

| 操作       | 快捷键                     |
| -------- | ----------------------- |
| 加粗       | ⌘ + B                   |
| 斜体       | ⌘ + I                   |
| 下划线      | ⌘ + U                   |
| 打开格式设置窗口 | Control + ⌘ + Shift + F |
| 选择整行     | ⇧ Shift + 空格键           |
| 选择整列     | Control + 空格键           |
| 隐藏选中行    | ⌘ + 9                   |
| 隐藏选中列    | ⌘ + 0                   |

### 函数与公式

| 函数/操作           | 示例或说明                          |
| --------------- | ------------------------------ |
| 绝对引用            | \$A\$1（使用 F4 切换引用类型）           |
| 多工作表引用          | =Sheet2!A1                     |
| 多工作簿引用          | =\[Book1.xlsx]Sheet1!\$A\$1    |
| CONCAT 拼接文本     | =CONCAT(A1,B1)                 |
| IF 条件判断         | =IF(A1>0, "正数", "负数")          |
| AND 多条件与        | =AND(A1>0,B1>0)                |
| OR 多条件或         | =OR(A1>0,B1>0)                 |
| NOT 逻辑非         | =NOT(A1>0)                     |
| SUMIF 条件求和      | =SUMIF(A1\:A5,">0")            |
| AVERAGEIF 条件平均  | =AVERAGEIF(B1\:B5,">10")       |
| VLOOKUP 查找值     | =VLOOKUP("张三",A2\:C10,2,FALSE) |
| HLOOKUP 水平查找    | =HLOOKUP("一月",A1\:Z3,2,FALSE)  |
| LEFT/RIGHT 截取字符 | =LEFT(A1,3)；=RIGHT(A1,2)       |
| MID 提取中间字符      | =MID(A1,3,2)                   |
| INDEX 返回区域值     | =INDEX(A1\:C3,2,3)             |
| MATCH 查找位置      | =MATCH(50,A1\:A10,0)           |
| PMT 计算贷款        | =PMT(利率,期数,现值)                 |

### 图表与数据分析

| 操作     | 步骤                   |
| ------ | -------------------- |
| 插入图表   | 选择数据 → 插入 → 图表类型     |
| 更改图表类型 | 选择图表 → 图表设计 → 更改图表类型 |
| 添加趋势线  | 图表设计 → 添加图表元素 → 趋势线  |
| 插入迷你图  | 插入 → 迷你图（折线、柱形）      |
| 数据透视表  | 选择数据 → 插入 → 数据透视表    |
| 筛选透视表  | 拖字段至“筛选区域”，选择值       |

### 打印与分页设置

| 操作      | 快捷方式                 |
| ------- | -------------------- |
| 设置打印区域  | 页面布局 → 打印区域 → 设置打印区域 |
| 添加页眉/页脚 | 插入 → 页眉/页脚           |
| 设置页面边距  | 页面布局 → 边距            |
| 页面方向    | 页面布局 → 方向（纵向/横向）     |
| 页面大小    | 页面布局 → 大小（A4等）       |

### 工作表管理

| 操作      | 快捷方式               |
| ------- | ------------------ |
| 插入新工作表  | ⇧ Shift + Fn + F11 |
| 删除工作表   | 右键工作表标签 → 删除       |
| 重命名工作表  | 双击工作表标签            |
| 更改标签颜色  | 右键 → 标签颜色          |
| 冻结窗格    | 视图 → 冻结窗格          |
| 切换工作簿窗口 | 视图 → 切换窗口          |

### 协作与保护

| 操作      | 步骤                   |
| ------- | -------------------- |
| 添加评论    | 选择单元格 → 审阅 → 新建批注    |
| 邀请协作    | 文件 → 共享 → 输入邮箱       |
| 设置工作表保护 | 审阅 → 保护工作表 → 设置可编辑项  |
| 添加文件密码  | 文件 → 另存为 → 工具 → 常规选项 |
