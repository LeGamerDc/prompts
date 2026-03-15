# 项目初始化

> 触发条件：用户要求新建小说项目、初始化目录结构。

---

## 初始化流程

### 第一步：收集基本信息

在创建目录前，向用户确认以下信息：

| 信息项 | 必需 | 示例 |
|--------|------|------|
| 项目名称 | 是 | `farm`、`sword-immortal` |
| 题材类型 | 是 | 玄幻/都市/悬疑/种田/言情/历史/其他 |
| 目标平台 | 推荐 | 起点/番茄/晋江/其他 |
| 预计篇幅 | 可选 | 100万字/300万字 |

### 第二步：根据题材选择分区

以下分区为**可选**，根据题材类型决定是否创建：

| 分区 | 玄幻/修仙 | 都市/现实 | 悬疑/推理 | 种田/经营 | 言情/女频 | 历史 |
|------|----------|----------|----------|----------|----------|------|
| `world/systems/` | 必需 | 可选 | 可选 | 可选 | 跳过 | 可选 |
| `world/items/` | 必需 | 跳过 | 可选 | 可选 | 跳过 | 可选 |
| `world/factions/` | 必需 | 可选 | 可选 | 必需 | 可选 | 必需 |
| `world/economy/` | 可选 | 可选 | 跳过 | 必需 | 跳过 | 可选 |
| `world/customs/` | 可选 | 跳过 | 跳过 | 可选 | 跳过 | 必需 |
| `world/timeline/` | 可选 | 可选 | 必需 | 可选 | 可选 | 必需 |
| `research/history/` | 可选 | 跳过 | 可选 | 可选 | 跳过 | 必需 |
| `research/competitive/` | 推荐 | 推荐 | 推荐 | 推荐 | 推荐 | 推荐 |

标记为"跳过"的分区不创建目录；"可选"的分区创建空目录（含 `.gitkeep`）；"必需"的分区创建目录并生成骨架文件。

### 第三步：创建目录树

完整目录结构如下。标注 `[可选]` 的目录根据第二步结果决定是否创建。

```
{project-name}/
├── core/
│   ├── high-concept.md
│   ├── positioning.md
│   ├── style-guide.md
│   ├── quality-bar.md
│   └── workflow.md
│
├── canon/
│   ├── characters/
│   │   ├── major/
│   │   │   └── .gitkeep
│   │   └── supporting/
│   │       └── .gitkeep
│   ├── world/
│   │   ├── overview.md
│   │   ├── locations/
│   │   │   └── .gitkeep
│   │   ├── factions/            [可选]
│   │   │   └── .gitkeep
│   │   ├── systems/             [可选]
│   │   │   └── .gitkeep
│   │   ├── items/               [可选]
│   │   │   └── .gitkeep
│   │   ├── economy/             [可选]
│   │   │   └── .gitkeep
│   │   ├── customs/             [可选]
│   │   │   └── .gitkeep
│   │   └── timeline/            [可选]
│   │       └── .gitkeep
│   └── outline/
│       ├── master.md
│       ├── volumes/
│       │   └── .gitkeep
│       ├── arcs/
│       │   └── .gitkeep
│       ├── chapter-beats/
│       │   └── .gitkeep
│       └── foreshadowing.md
│
├── research/
│   ├── history/                 [可选]
│   │   └── .gitkeep
│   ├── domain/
│   │   └── .gitkeep
│   ├── competitive/             [可选]
│   │   └── .gitkeep
│   └── plot-patterns/
│       ├── cards/
│       │   └── .gitkeep
│       └── case-notes/
│           └── .gitkeep
│
├── production/
│   ├── drafts/
│   │   ├── chapters/
│   │   │   └── .gitkeep
│   │   └── scene-plans/
│   │       └── .gitkeep
│   └── reviews/
│       ├── auto-reviews/
│       │   └── .gitkeep
│       ├── consistency-checks/
│       │   └── .gitkeep
│       ├── revision-tasks/
│       │   └── .gitkeep
│       └── human-notes/
│           └── .gitkeep
│
├── ops/
│   ├── status.md
│   ├── todo.md
│   ├── decisions.md
│   ├── insights.md
│   └── handoffs/
│       └── .gitkeep
│
└── index/
    ├── canon-index.md
    ├── glossary.md
    └── unresolved-threads.md
```

### 第四步：生成骨架文件

以下为每个骨架文件的初始内容。

#### core/high-concept.md

```yaml
---
type: high-concept
status: draft
---
```

```markdown
# 核心概念

## 一句话故事线

> [用一句话概括：谁、在哪、遇到什么、怎么做、结果如何]

## 总纲摘要

[用一段话（5-8句）概括全书的起因、三个主要灾难/转折、结局方向]

## 核心卖点

- [卖点1]
- [卖点2]
- [卖点3]
```

#### core/positioning.md

```yaml
---
type: positioning
status: draft
---
```

```markdown
# 平台与定位

## 基本信息

- **题材类型**：[如：种田经营 / 玄幻修仙 / 都市异能]
- **目标平台**：[如：番茄小说 / 起点中文网 / 晋江文学城]
- **目标读者**：[核心读者画像]
- **预计篇幅**：[如：200万字 / 50卷]
- **更新节奏**：[如：日更4000字]

## 标签定位

- 主标签：[平台一级标签]
- 副标签：[二级标签列表]

## 市场参照

- [参照作品1]：借鉴 [哪个方面]
- [参照作品2]：借鉴 [哪个方面]
```

#### core/style-guide.md

```yaml
---
type: style-guide
status: draft
---
```

```markdown
# 文风规范

## 叙事视角

- **主视角**：[第一人称 / 第三人称有限 / 第三人称全知]
- **POV 角色**：[如：仅主角 / 主角+核心配角]

## 语言风格

- **基调**：[如：轻松幽默 / 沉稳厚重 / 热血激昂]
- **文白比例**：[如：现代白话为主，古风点缀]
- **对话风格**：[如：口语化，避免书面腔]

## 禁忌项

- [如：不使用网络缩写]
- [如：不直接抄录诗词原文]
```

#### core/quality-bar.md

```yaml
---
type: quality-bar
status: draft
---
```

```markdown
# 质量标准

## 每章必须满足

- [ ] 有明确的场景目标
- [ ] 至少一个信息增量（新情报/新变化/新冲突）
- [ ] 章末有钩子（悬念/期待/转折）
- [ ] 无设定矛盾（与 canon 一致）
- [ ] 字数在平台要求范围内

## 每卷必须满足

- [ ] 有完整的叙事弧（起-承-转-合）
- [ ] 主角有可感知的成长/变化
- [ ] 本卷伏笔基本回收
- [ ] 留有下卷钩子
```

#### core/workflow.md

```yaml
---
type: workflow
status: draft
---
```

```markdown
# 工作流程

## 标准写作流程

1. **写前**：加载 canon 上下文（角色卡 + 当前卷纲 + 章纲 + 伏笔矩阵）
2. **写中**：按章纲展开，标注偏离点
3. **写后**：回写变更到 canon，更新 ops/status，检查伏笔状态

## 回写检查清单

每次写作完成后：

- [ ] 新角色/新设定已录入 canon
- [ ] 章节 frontmatter 中 status 已更新
- [ ] ops/status.md 已更新当前进度
- [ ] 伏笔矩阵已标注本章的埋设/推进/回收
- [ ] index/canon-index.md 已更新（如有新增 canon 文件）
- [ ] index/glossary.md 已更新（如有新术语）
```

#### canon/world/overview.md

```yaml
---
type: world-overview
status: draft
---
```

```markdown
# 世界观框架

## 世界起源与历史

[简述世界的起源和关键历史节点]

## 核心规则

[这个世界与现实世界的关键差异：物理法则、超自然规则等]

## 时代背景

[故事发生的时代特征、社会状态、科技/文明水平]

## 价值观与社会结构

[主流价值观、社会阶层、权力结构]
```

#### canon/outline/master.md

```yaml
---
type: master-outline
status: draft
total-volumes: 0
target-words: 0
---
```

```markdown
# 总大纲

## 一句话故事线

> [与 high-concept.md 保持同步]

## 全书阶段划分

| 阶段 | 卷 | 字数范围 | 核心目标 |
|------|-----|---------|---------|
| 开篇 | vol-01 | 0-10万 | [建立世界+角色+核心冲突] |
| 前期 | vol-02~03 | 10-30万 | [扩展+首个大目标] |
| 中期 | vol-04~06 | 30-60万 | [格局升级+主要矛盾深化] |
| 后期 | vol-07~09 | 60-90万 | [最终冲突+高潮] |
| 结局 | vol-10 | 90-100万 | [收束+结局] |

## 主角成长路径

[概述主角从起点到终点的核心蜕变]

## 结局方向

[全书的结局走向，HE/BE/OE]
```

#### canon/outline/foreshadowing.md

```yaml
---
type: foreshadowing-matrix
status: active
---
```

```markdown
# 伏笔矩阵

## 状态说明

- **planted**：已埋设，未有后续推进
- **progressing**：已有推进，尚未回收
- **resolved**：已完成回收
- **abandoned**：主动放弃（需记录原因）

## 活跃伏笔

（暂无）

<!-- 条目格式：
### F-001 [伏笔名称]
- **首埋**：vol-XX/ch-XXX
- **状态**：planted | progressing | resolved | abandoned
- **类型**：短线（5章内） | 中线（1卷内） | 长线（跨卷）
- **事件记录**：
  - [日期] vol-XX/ch-XXX — 埋设：[描述]
  - [日期] vol-XX/ch-XXX — 推进：[描述]
  - [日期] vol-XX/ch-XXX — 回收：[描述]
- **预期回收**：vol-XX/ch-XXX 前后
- **说明**：[补充信息]
-->

## 已回收伏笔

（暂无）

## 已放弃伏笔

（暂无）
```

#### ops/status.md

```yaml
---
type: project-status
last-updated: YYYY-MM-DD
---
```

```markdown
# 项目状态

## 当前阶段

[如：构思阶段 / 大纲规划 / 第一卷写作 / 第N卷连载中]

## 进度概览

- **已完成卷数**：0
- **已完成章数**：0
- **总字数**：0
- **最新章节**：无

## 已完成里程碑

（暂无）

## 下一步

- [ ] [下一步行动1]
- [ ] [下一步行动2]

## 阻塞项

（暂无）

## 待确认决策

（暂无）
```

#### ops/todo.md

```yaml
---
type: todo-list
last-updated: YYYY-MM-DD
---
```

```markdown
# 任务清单

## 紧急

（暂无）

## 创作任务

- [ ] [任务描述]

## 修订任务

（暂无）

## 调研任务

（暂无）

## 设定任务

（暂无）
```

#### ops/decisions.md

```yaml
---
type: decision-log
last-updated: YYYY-MM-DD
---
```

```markdown
# 决策日志

## 已确认决策

（暂无）

<!-- 条目格式：
### D-001 [决策标题]
- **日期**：YYYY-MM-DD
- **决策**：[具体内容]
- **理由**：[为什么这么决定]
- **影响范围**：[影响了哪些文件/设定/情节]
-->

## 待确认决策

（暂无）
```

#### ops/insights.md

```yaml
---
type: insights
last-updated: YYYY-MM-DD
last-processed: null
---
```

```markdown
# 创作经验收集池

## 待处理

（暂无）

<!-- 条目格式：
### I-001 [简短描述]
- **日期**：YYYY-MM-DD
- **来源**：[发现时的工作上下文]
- **类型**：best-practice | anti-pattern | conflict | observation
- **内容**：[经验描述]
- **状态**：raw
-->

## 已纳入

（暂无）

## 不采纳

（暂无）
```

#### index/canon-index.md

```yaml
---
type: canon-index
last-updated: YYYY-MM-DD
---
```

```markdown
# 事实源索引

## 角色

### 主要角色 (`canon/characters/major/`)

（暂无）

### 配角 (`canon/characters/supporting/`)

（暂无）

## 世界观 (`canon/world/`)

- [overview.md](../canon/world/overview.md) — 世界观框架

## 大纲 (`canon/outline/`)

- [master.md](../canon/outline/master.md) — 总大纲
- [foreshadowing.md](../canon/outline/foreshadowing.md) — 伏笔矩阵
```

#### index/glossary.md

```yaml
---
type: glossary
last-updated: YYYY-MM-DD
---
```

```markdown
# 术语表

按首字母/拼音排序。每个条目格式：**术语** — 定义（首次出现：vol-XX/ch-XXX）

（暂无）

<!-- 示例：
- **灵石** — 修仙者通用货币，含微量天地灵气（首次出现：vol-01/ch-003）
- **筑基** — 修炼体系第二大境界，标志是丹田凝形（首次出现：vol-01/ch-001）
-->
```

#### index/unresolved-threads.md

```yaml
---
type: unresolved-threads
last-updated: YYYY-MM-DD
---
```

```markdown
# 未闭合线头

## 活跃线头

（暂无）

<!-- 条目格式：
### T-001 [线头描述]
- **来源**：[发现位置，如 vol-01/ch-005 或构思阶段]
- **类型**：伏笔未收 | 设定空洞 | 角色去向 | 逻辑缺口
- **优先级**：高 | 中 | 低
- **关联 canon**：[相关的 canon 文件]
- **说明**：[补充信息]
-->

## 已解决线头

（暂无）
```

---

## 第五步：初始化检查清单

项目创建完成后，逐项确认：

- [ ] 目录树已创建，所有空目录含 `.gitkeep`
- [ ] `core/` 下 5 个骨架文件已生成
- [ ] `canon/world/overview.md` 已生成
- [ ] `canon/outline/master.md` 已生成
- [ ] `canon/outline/foreshadowing.md` 已生成
- [ ] `ops/` 下 4 个骨架文件已生成
- [ ] `index/` 下 3 个骨架文件已生成
- [ ] 可选分区已根据题材正确裁剪
- [ ] git 初始化完成（如适用）

---

## 渐进式启动指引

项目初始化后，不要求一次填满所有文件。推荐的最小启动集：

### 必须在开写前完成

1. `core/high-concept.md` — 明确核心概念
2. `core/positioning.md` — 确定平台和定位
3. `canon/outline/master.md` — L1 总纲 + L2 至少前2卷的阶段划分

### 推荐在开写前完成

4. `canon/outline/volumes/vol-01.md` — 第一卷卷纲
5. 至少 1 个主角的角色卡 — `canon/characters/major/`
6. `canon/world/overview.md` — 世界观基本框架
7. `core/style-guide.md` — 文风基调

### 可在连载中逐步补充

- 后续卷的卷纲和章纲（提前 1-2 卷细化）
- 配角卡（登场时创建）
- 世界观子分类（涉及时补充）
- 研究资料（按需积累）
- 术语表（随写随录）
