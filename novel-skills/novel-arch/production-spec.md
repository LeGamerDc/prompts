# 生产区管理规范

> 触发条件：写章节、审稿、场景计划等生产活动。

`production/` 存放写作过程中产生的材料：草稿、场景计划、审稿记录。这些是**过程产物**，不构成故事事实（事实以 `canon/` 为准）。

---

## 1. 草稿管理

### 1.1 章节草稿

**路径**：`production/drafts/chapters/vol-{NN}/ch-{NNN}.md`

第一卷第三章 → `production/drafts/chapters/vol-01/ch-003.md`

**Frontmatter**：

```yaml
---
volume: 1
chapter: 3
title: [章名]
pov: [视角角色]
location: [主要场景]
word-count: 0
status: drafting
---
```

**状态流转**：

```
outline → drafting → drafted → revised → final
   ↑                              |
   └──────── rejected ────────────┘
```

| 状态 | 含义 |
|------|------|
| `outline` | 仅有章纲，正文未开始 |
| `drafting` | 正在写作中 |
| `drafted` | 初稿完成，待审 |
| `revised` | 经过审稿修订 |
| `final` | 定稿，可发布 |
| `rejected` | 审稿后需要重写，退回 outline 或 drafting |

**状态更新时机**：

- 开始写章节 → `drafting`，更新 `word-count: 0`
- 初稿完成 → `drafted`，更新 `word-count` 为实际字数
- 审稿修订完成 → `revised`
- 确认可发布 → `final`

### 1.2 场景计划（L5）

**路径**：`production/drafts/scene-plans/`

场景计划是大纲第五级（L5），属于写作过程产物，不归入 `canon/outline/`。

**命名**：`vol-{NN}-ch-{NNN}-scene-plan.md` 或按弧命名 `vol-{NN}-expanded-outline.md`

**Frontmatter**：

```yaml
---
type: scene-plan
volume: [卷号]
scope: [覆盖范围，如 ch-001~ch-010]
status: draft | active | superseded
---
```

**内容结构**：

```markdown
# 场景展开：[范围描述]

## ch-XXX [章名]

### 场景1：[场景标题]
- **地点**：[具体地点]
- **在场角色**：[角色列表]
- **场景目标**：[要传达什么/推进什么]
- **情绪基调**：[紧张/轻松/悲伤/热血]
- **关键对话要点**：
  - [要点1]
  - [要点2]
- **衔接下一场景**：[如何过渡]

### 场景2：[场景标题]
...
```

---

## 2. 审稿管理

### 2.1 自动审稿

**路径**：`production/reviews/auto-reviews/`

**命名**：`vol-{NN}-ch-{NNN}-review-{N}.md`

- 单章审稿：`vol-01-ch-003-review-1.md`
- 批量审稿：`vol-01-beats-001-010-review.md`（章节 1-10 的跨章审稿）
- 同一章的多次审稿用序号递增：`review-1`、`review-2`

**Frontmatter**：

```yaml
---
type: auto-review
scope: vol-XX/ch-XXX | vol-XX/ch-XXX~ch-XXX
review-round: 1
review-type: structure | setting | style | consistency
date: YYYY-MM-DD
---
```

**审稿类型**：

| 类型 | 关注点 |
|------|--------|
| `structure` | 叙事结构、节奏、章节目标达成度、钩子有效性 |
| `setting` | 与 canon 的一致性、设定数据是否矛盾 |
| `style` | 文风是否符合 style-guide、语言质量、对话自然度 |
| `consistency` | 跨章一致性、人名地名准确、时间线合理性 |

### 2.2 一致性检查

**路径**：`production/reviews/consistency-checks/`

**触发时机**：

- 每 10 章进行一次（来自行业最佳实践）
- 每卷结束时进行一次全卷检查

**命名**：`vol-{NN}-ch-{NNN}-{NNN}-consistency.md`

**内容结构**：

```markdown
# 一致性检查：vol-XX ch-XXX ~ ch-XXX

## 检查日期
YYYY-MM-DD

## 角色一致性
- [ ] 人名/称呼前后一致
- [ ] 角色性格表现与角色卡吻合
- [ ] 角色能力/实力等级与设定吻合
- [结果/发现的问题]

## 设定一致性
- [ ] 地名/距离/旅行时间前后一致
- [ ] 力量体系规则未被违反
- [ ] 物品/装备描述前后一致
- [结果/发现的问题]

## 时间线一致性
- [ ] 事件发生的先后顺序合理
- [ ] 时间跨度与描述吻合
- [结果/发现的问题]

## 伏笔健康度
- [ ] 无超期未推进的伏笔（>8章）
- [ ] 本段内的伏笔/推进/转折/高潮/收束分布均衡
- [结果/发现的问题]

## 需要修正的问题
1. [问题描述] → [修正方案] → [涉及文件]
```

### 2.3 修改任务

**路径**：`production/reviews/revision-tasks/`

**命名**：`YYYY-MM-DD-[简述].md`

**Frontmatter**：

```yaml
---
type: revision-task
priority: high | medium | low
scope: [涉及章节范围]
source: auto-review | consistency-check | human-note
status: open | in-progress | resolved
---
```

**内容结构**：

```markdown
# [任务标题]

## 问题描述
[具体问题]

## 修正方案
[如何修改]

## 涉及文件
- [文件路径1]
- [文件路径2]

## 完成检查
- [ ] 正文已修正
- [ ] canon 已同步更新（如涉及设定变更）
- [ ] 伏笔矩阵已更新（如涉及伏笔）
```

### 2.4 人工批注

**路径**：`production/reviews/human-notes/`

自由格式，命名建议 `YYYY-MM-DD-[主题].md`。用于记录人工审读时的随手批注、灵感、改进方向。

---

## 3. 状态联动

production 中的活动完成后，需要联动更新其他区域：

### 章节初稿完成时

1. 更新草稿 frontmatter：`status: drafted`，填入 `word-count`
2. 更新 `ops/status.md`：已完成章数、总字数、最新章节
3. 检查本章是否引入新角色/新设定 → 录入 `canon/`
4. 检查本章是否埋设/推进/回收伏笔 → 更新 `canon/outline/foreshadowing.md`
5. 新术语/专有名词 → 更新 `index/glossary.md`

### 审稿完成时

1. 如发现设定问题 → 创建 revision-task 或直接修正
2. 如发现伏笔异常 → 更新 foreshadowing.md + unresolved-threads.md
3. 更新 `ops/todo.md` 中的修订任务

### 每卷完稿时

1. 触发全卷一致性检查
2. 更新 `ops/status.md` 中的里程碑
3. 复盘伏笔矩阵：本卷计划回收的伏笔是否全部完成
4. 细化下一卷的 L3 弧和 L4 章纲
