# 调研区管理规范

> 触发条件：整理调研资料、历史考据、桥段收集、竞品分析。

`research/` 存放外部参考资料。**这些内容不构成故事事实**——只有经过验证并录入 `canon/` 的信息才能被正文引用为设定依据。

---

## 1. 目录结构

```
research/
├── history/           # 历史考据
├── domain/            # 领域专业知识
├── competitive/       # 竞品分析/同类作品研究
└── plot-patterns/     # 叙事套路与技巧
    ├── cards/         # 桥段卡
    └── case-notes/    # 案例摘记
```

---

## 2. 历史考据（history/）

### 2.1 适用场景

历史文、穿越文、架空历史文的朝代制度、器物服饰、社会文化等考据。

### 2.2 文件命名

使用描述性名称，体现内容范围：

```
song-dynasty-social-culture.md
tang-military-system.md
ming-commercial-economy.md
```

也可按主题打包：`song-five-dynasties-fictional-dynasty-kit.md`

### 2.3 Frontmatter

```yaml
---
type: historical-research
period: [朝代/时期]
topics: [主题列表]
sources: [主要参考来源]
date: YYYY-MM-DD
---
```

### 2.4 内容格式

自由组织，但推荐使用分层结构：

```markdown
# [资料包标题]

## 概述
[本资料包覆盖的范围和用途]

## [主题1]
### [子主题]
[内容]
> 来源：[引用出处]

## [主题2]
...

## 创作应用建议
[这些史实如何转化为故事元素的建议]
```

### 2.5 引用格式

资料中引用外部来源时，使用 blockquote + 来源标注：

```markdown
> 宋代边境榷场贸易中，茶叶、丝绸为主要出口物资...
> — 《宋史·食货志》
```

---

## 3. 领域知识（domain/）

### 3.1 适用场景

非历史类的专业知识：医学常识、法律程序、军事战术、科技原理、农业技术等。

### 3.2 文件命名

按领域分类：

```
traditional-medicine-basics.md
ancient-farming-techniques.md
military-formation-tactics.md
```

### 3.3 Frontmatter

```yaml
---
type: domain-research
domain: [领域名称]
topics: [主题列表]
date: YYYY-MM-DD
---
```

### 3.4 事实卡格式

当需要提取可直接使用的知识点时，使用事实卡格式：

```markdown
### 事实卡：[知识点名称]
- **领域**：[所属领域]
- **要点**：[核心事实，1-3句]
- **来源**：[参考来源]
- **创作用途**：[这个知识点可以用在哪里]
- **注意事项**：[使用时需要注意的准确性问题]
```

---

## 4. 竞品分析（competitive/）

### 4.1 适用场景

开书前的市场调研、同类作品分析、爽点逆推、套路提炼。

### 4.2 文件命名

```
genre-overview-farming-2026.md
competitor-analysis-[书名缩写].md
tag-trend-qidian-2026-q1.md
```

### 4.3 Frontmatter

```yaml
---
type: competitive-analysis
scope: genre-overview | single-work | tag-trend
platform: [平台名]
date: YYYY-MM-DD
---
```

### 4.4 单部作品分析模板

```markdown
# 竞品分析：[作品名]

## 基本信息
- **作者**：
- **平台**：
- **字数/状态**：
- **成绩**：[订阅/收藏/评分等]

## 核心卖点
[这部作品最吸引读者的 1-3 个点]

## 爽点结构
[分析其爽点的分布节奏和实现方式]

## 套路提炼
[可复用的叙事套路和技巧]

## 差异化空间
[我们的作品可以在哪些方面做出差异]

## 读者口碑
[读者评价中的高频关键词和情绪倾向]
```

### 4.5 标签风向记录

```markdown
# 标签风向：[平台] [时间段]

## 热门标签
| 标签 | 热度趋势 | 代表作品 | 备注 |
|------|---------|---------|------|
| [标签1] | 上升/稳定/下降 | [作品名] | |
```

---

## 5. 桥段库（plot-patterns/）

### 5.1 桥段卡（cards/）

**路径**：`research/plot-patterns/cards/`

**命名**：`SP-{NNN}-[桥段名缩写].md`（SP = Story Pattern）

```
SP-001-fake-weakness.md
SP-002-mentor-sacrifice.md
SP-015-hidden-identity-reveal.md
```

**Frontmatter**：

```yaml
---
id: SP-[NNN]
name: [桥段名称]
scope: scene | chapter | arc | volume
source: [桥段来源/参考作品]
---
```

**内容结构**：

```markdown
# SP-[NNN] [桥段名称]

## 核心问题
[这个桥段解决什么叙事问题？]

## 读者回报
[读者从中获得什么体验？爽感/感动/震撼/好奇]

## 前置条件
[使用这个桥段需要什么铺垫？]

## 机制
[桥段的核心运作逻辑]

## 执行步骤
1. [步骤1]
2. [步骤2]
3. [步骤3]

## 变体
- **变体A**：[描述]
- **变体B**：[描述]

## 风险与代价
[使用不当可能导致的问题]

## 题材适配
[如何适配到本项目的题材/世界观]

## 参考案例
[1-2个经典实现的简要描述]
```

### 5.2 案例摘记（case-notes/）

**路径**：`research/plot-patterns/case-notes/`

**命名**：`[来源作品缩写]-[场景名].md`

```
three-kingdoms-empty-fort.md
erta-identity-switch.md
count-of-monte-cristo-revenge-setup.md
```

**Frontmatter**：

```yaml
---
type: case-note
source-work: [来源作品全名]
scene-or-arc: [具体场景/弧名]
---
```

**内容结构**：

```markdown
# [来源作品]：[场景/弧名]

## 问题
[这个场景/弧解决了什么叙事问题？]

## 机制
[它是怎么做到的？核心技巧是什么？]

## 步骤链
1. [步骤1]
2. [步骤2]
...

## 读者回报
[读者/观众的情绪反应]

## 适配到本项目
[如何将这个技巧移植到我们的作品中]

## 风险
[照搬可能带来的问题]

## 爆发信号
[如果成功，读者应该出现什么反应/指标]
```

---

## 6. Research → Canon 管道

调研材料要成为故事设定，必须经过**验证-转化-录入**三步：

### 6.1 流程

```
research/ 中的原始资料
    ↓ 验证：事实是否准确？是否适合本作品世界观？
    ↓ 转化：从史实/知识提炼为故事设定（可能需要修改以适配虚构世界）
    ↓ 录入：写入 canon/ 对应文件
    ↓ 索引：更新 index/canon-index.md 和 index/glossary.md
```

### 6.2 验证标准

| 检查项 | 说明 |
|--------|------|
| 事实准确性 | 历史考据是否有可靠来源？ |
| 世界观兼容 | 是否与已有 canon 设定矛盾？ |
| 叙事必要性 | 录入 canon 是否对故事有实际作用？ |
| 复杂度控制 | 是否过于复杂导致读者难以理解？ |

### 6.3 转化原则

- **不是照搬而是改编**：历史事实需要适配虚构世界的设定
- **简化优于精确**：读者不需要学术级精度，需要故事级合理性
- **标注来源**：canon 文件中可用注释标注原始参考，方便后续追溯

```markdown
<!-- 基于宋代榷场贸易制度改编，原始资料见 research/history/song-border-trade.md -->
```

### 6.4 反向追溯

当需要回查某个 canon 设定的调研依据时：

1. 查看 canon 文件中的注释标注
2. 在 `research/` 中搜索相关关键词
3. 如无法找到原始资料，在 `index/unresolved-threads.md` 中记录为"设定空洞"
