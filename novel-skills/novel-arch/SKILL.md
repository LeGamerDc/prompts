---
name: novel-arch
description: >
  网文小说项目的目录架构管理器。管理项目目录结构、文件命名与格式规范、运行态维护协议。
  Triggers: "新建小说项目", "初始化小说目录", "创建小说工程", "项目结构",
  "文件放哪", "目录规范", "添加角色文件", "添加设定", "更新大纲",
  "写章节", "审稿", "更新状态", "记录决策", "交接", "整理调研",
  "记录经验", "整理经验", "经验回流"
  Use when the user wants to create, organize, or maintain a web novel project's
  file structure, or when any file needs to be created/moved/renamed within a novel project.
---

# novel-arch — 网文项目架构管理器

## 定位

novel-arch 管理网文小说项目的**目录结构、文件格式和运行态**。

它回答三个问题：

1. **东西放哪里？** — 目录规范
2. **文件怎么组织？** — 命名与格式标准
3. **项目状态怎么维护？** — 运行态协议

它**不涉及**创作方法论（怎么写大纲、怎么塑造角色、怎么写章节正文）。

---

## 目录结构速览

项目采用 **6 区结构**，每个区域职责明确、互不替代：

| 区域 | 目录 | 职责 | 权威性 |
|------|------|------|--------|
| 身份层 | `core/` | 项目定位、文风、质量标准、工作流 | 全局规则 |
| 事实层 | `canon/` | 角色、世界观、大纲、伏笔 | **唯一故事事实源** |
| 参考层 | `research/` | 历史考据、领域知识、竞品、桥段 | 外部参考，非事实 |
| 生产层 | `production/` | 草稿、场景计划、审稿 | 过程产物，非事实 |
| 运行层 | `ops/` | 状态、任务、决策、交接 | 项目管理 |
| 导航层 | `index/` | 事实源索引、术语表、未闭合线头 | 导航工具 |

**Canon 权威性原则**：`canon/` 是唯一的故事事实源。`research/` 和 `production/` 中的内容不构成故事事实，不可被正文直接引用为设定依据。

---

## 全局约定

### 文件命名

- 一律使用 **kebab-case**：`vol-01-ch-003.md`、`protagonist.md`、`song-dynasty-economy.md`
- 卷号两位补零：`vol-01`、`vol-12`
- 章号三位补零：`ch-001`、`ch-024`
- 日期格式：`YYYY-MM-DD`，时间戳：`YYYY-MM-DD-HHMM`

### 文档格式

- 所有 `.md` 文件以 **YAML frontmatter** 开头（`---` 包裹）
- frontmatter 之后为 **Markdown** 正文
- frontmatter 中的 `status` 字段反映文件当前状态

### 回写规则

任何改变故事事实的操作完成后，必须：

1. 将变更回写到 `canon/` 对应文件
2. 更新 `index/canon-index.md`（新增/重命名/删除条目时）
3. 检查 `index/glossary.md` 是否需要新增术语
4. 检查 `index/unresolved-threads.md` 是否有线头可闭合或需新增

### 经验回流规则

在**任何创作工作**（写章节、审稿、扩展大纲、调研、设定补充）中，如果发现以下情况，立即追加到 `ops/insights.md`：

- **值得复用的做法**：某种写法/技巧/流程效果显著
- **应当避免的做法**：某种做法导致了问题或返工
- **与现有规则的矛盾**：实践经验与 `core/` 中的规则冲突
- **有趣的发现**：其他值得记录的创作洞察

**记录格式**（追加到文件末尾）：

```
### I-[NNN] [简短描述]
- **日期**：YYYY-MM-DD
- **来源**：[发现时的工作上下文，如"写 vol-02 ch-015 时"]
- **类型**：best-practice | anti-pattern | conflict | observation
- **内容**：[经验描述]
- **状态**：raw
```

**行为要求**：

1. **随手记，不犹豫** — 记录门槛要低，宁可多记后删，不要遗漏
2. **只追加，不改规则** — 记录时不得直接修改 `core/` 下任何文件
3. **冲突标记，等待裁决** — 类型为 `conflict` 的条目由用户决定如何处理，agent 不得自行解决
4. **批量消化** — 积累的 insights 在里程碑节点（每卷完成/阶段切换）批量处理，详见 [ops-spec.md § 6](ops-spec.md)

---

## 意图路由表

根据当前工作意图，加载对应子文档：

| 触发信号 | 子文档 | 说明 |
|---------|--------|------|
| 新建小说项目、初始化目录 | [project-init.md](project-init.md) | 创建目录树 + 骨架文件 + 题材裁剪 |
| 添加/修改角色、设定、大纲、伏笔 | [canon-spec.md](canon-spec.md) | 角色卡格式、世界观分类、五级大纲、伏笔矩阵 |
| 写章节、审稿、场景计划 | [production-spec.md](production-spec.md) | 草稿命名、审稿流程、状态流转 |
| 更新状态、记录决策、交接、任务管理、整理经验 | [ops-spec.md](ops-spec.md) | status/todo/decisions/handoffs/insights 协议 |
| 整理调研、历史考据、桥段收集、竞品分析 | [research-spec.md](research-spec.md) | 资料分类、桥段卡格式、canon 转化管道 |

**加载原则**：只加载当前工作所需的子文档，不要一次性加载全部。
