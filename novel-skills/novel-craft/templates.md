# 故事制品模板集

本文件定义所有故事制品（角色卡、世界观条目、场景计划等）的标准格式。各方法论子文档在创建具体文件时引用此处的模板。

所有模板使用 YAML frontmatter 存放结构化元数据 + markdown sections 存放散文描述。

---

## 角色卡

存放于 `canon/characters/major-cast/` 或 `canon/characters/supporting-cast/`。

```yaml
---
name: 角色名
aliases: [别名, 绰号]
role: protagonist | antagonist | love-interest | mentor | ally | rival | minor
status: active | deceased | missing | unknown
first-appearance: vol-01/ch-001
---
```

**背景**：出身、来历、开局处境。

**外貌**：外形特征，一句话能让读者记住的标记性细节。

**性格**：核心性格维度（2-3 条），驱动行为的内在逻辑。

**动机**：当前阶段的目标和深层欲望。

**能力与限制**：擅长什么、受制于什么。

**语音标记**：口头禅、用词习惯、语气特征、句式偏好。用于写对话时区分不同角色。

**关系**：与其他角色的关系及当前状态。格式：`角色名 — 关系类型 — 当前状态`。

**角色弧线**：阶段性变化轨迹。格式：`卷/章 — 状态变化 — 触发事件`。

---

## 世界观条目

存放于 `canon/lore/world/`。

```yaml
---
type: world-setting
scope: macro | regional | local
---
```

**概述**：一段话概括这个世界/区域的核心特征。

**规则**：该层级下不可违反的硬性规则。

**与故事的关系**：这些设定如何影响主角和剧情。

---

## 地点条目

存放于 `canon/lore/locations/`。

```yaml
---
name: 地点名
type: city | town | village | wilderness | building | other
region: 所属区域
---
```

**描述**：地理特征、气氛、标志性细节。

**功能**：在故事中承担的叙事功能（冲突场、安全屋、交易点等）。

**关联角色**：与此地点有关的角色。

---

## 势力条目

存放于 `canon/lore/factions/`。

```yaml
---
name: 势力名
type: political | military | commercial | religious | criminal | other
status: active | dissolved | dormant
---
```

**概述**：定位、规模、影响力。

**核心人物**：关键成员及其角色。

**与主角的关系**：友好/敌对/中立/待定。

**剧情功能**：在故事中提供什么张力或资源。

---

## 体系条目

存放于 `canon/lore/systems/`。适用于种田体系、修仙等级、魔法系统、科技树等。

```yaml
---
name: 体系名
type: farming | cultivation | magic | technology | economy | other
---
```

**核心机制**：体系如何运作，用 3-5 条规则概括。

**等级/阶段**：如有层级结构，列出各级名称和关键差异。

**限制与代价**：边界在哪里、使用代价是什么。

**与剧情的关系**：如何驱动冲突和爽点。

---

## 总大纲

存放于 `canon/outline/master-outline.md`。

```yaml
---
type: master-outline
target-length: 预计总字数
target-volumes: 预计卷数
---
```

**总主线**：一段话概括整个故事。

**阶段划分**：列出每个大阶段的核心目标和转折点。

**终局设想**：故事的最终走向（可标注"待定"）。

---

## 卷大纲

存放于 `canon/outline/volumes/vol-{NN}.md`。

```yaml
---
type: volume-outline
volume: 卷号
title: 卷标题
chapters: 预计章数
word-target: 预计字数
status: planning | writing | complete
---
```

**卷目标**：本卷要解决的核心问题。

**起点状态**：开卷时主角和世界的状态。

**终点状态**：本卷结束时的状态。

**关键事件**：按顺序列出本卷的里程碑事件。

**本卷新角色**：如有。

**本卷新设定**：如有。

**角色出场规划**：主要角色在本卷各章的大致出场分布，标注长期缺席需重新介绍的角色。

---

## 剧情弧

存放于 `canon/outline/arcs/`。

```yaml
---
name: 弧名
type: main | subplot | character-arc
status: planning | active | resolved
span: vol-01 ~ vol-03
---
```

**目标**：这条弧要完成什么。

**节拍**：关键节拍点列表（设置 → 升级 → 危机 → 高潮 → 解决）。

**涉及角色**：参与这条弧的角色。

---

## 章节 Beats

存放于 `canon/outline/chapter-beats/`。文件名 `vol-{NN}-ch-{NNN}.md`。

```yaml
---
volume: 卷号
chapter: 章号
title: 章标题（可后定）
pov: 视角角色
location: 主场景地点
status: planning | drafted | revised | final
---
```

**本章目标**：这一章要推进什么。

**Beats**：
1. 场景/事件描述 — 涉及角色 — 叙事功能
2. …

**角色出场管理**：标注需要介绍或重新介绍的角色。
- 首次登场角色 → 安排初印象塑造
- 长期缺席角色（≥10 章未出场） → 安排自然的记忆唤醒
- 状态剧变后回归的角色 → 让读者感知变化

**信息揭示**：本章向读者透露哪些新信息。

**必须满足**：本章不能违反的设定点。

**钩子方向**：章末留什么悬念。

---

## 伏笔矩阵

存放于 `canon/outline/foreshadowing.md`。

| ID | 伏笔内容 | 埋设章节 | 发展章节 | 收回章节 | 状态 |
|----|---------|---------|---------|---------|------|
| F-001 | （描述） | vol-01/ch-003 | vol-01/ch-010 | vol-02/ch-005 | planted / developing / paid-off |

---

## 场景计划

存放于 `production/drafts/scene-plans/`。

**场景目标**：这个场景要完成什么叙事任务。

**参与角色**：出场角色及其当前状态。

**环境**：地点、时间、氛围。

**冲突/张力**：场景的核心矛盾是什么。

**结果**：场景结束时发生了什么变化。

**桥段参考**：如使用了 `research/` 中的桥段卡，注明出处。

---

## 交接记录

存放于 `ops/handoffs/`。文件名 `YYYY-MM-DD-HHMM-topic.md`。

**本次目标**：这轮工作要做什么。

**已完成**：完成了哪些事项。

**影响文件**：修改或新增了哪些文件。

**当前状态**：做到什么程度。

**下一步**：接下来该做什么。

**阻塞/待确认**：卡在哪里、需要用户确认什么。
