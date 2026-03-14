# 项目脚手架

## 使用时机

- 用户要求"开始写一部新小说"、"新建小说项目"、"初始化项目"
- 用户要求"重建项目结构"
- 检测到工作目录没有 `AGENTS.md`（项目未初始化）

## 操作流程

1. 与用户确认项目根目录路径和小说标题（kebab-case 命名）
2. 创建下方完整目录结构
3. 按模板生成所有骨架文件，`{placeholder}` 替换为项目实际值
4. 更新 `ops/status.md` 为"阶段 0：项目已初始化"
5. 返回 conception.md 继续构思流程

## 目录结构

```
{novel-title}/
├── AGENTS.md
├── core/
│   ├── positioning.md
│   ├── high-concept.md
│   ├── style-guide.md
│   ├── quality-bar.md
│   ├── workflow.md
│   └── context-assembly.md
├── canon/
│   ├── lore/
│   │   ├── world/
│   │   ├── locations/
│   │   ├── factions/
│   │   ├── economy/
│   │   ├── customs/
│   │   └── systems/
│   ├── characters/
│   │   ├── major-cast/
│   │   └── supporting-cast/
│   └── outline/
│       ├── master-outline.md
│       ├── foreshadowing.md
│       ├── volumes/
│       ├── arcs/
│       └── chapter-beats/
├── production/
│   ├── drafts/
│   │   ├── chapters/
│   │   └── scene-plans/
│   └── reviews/
│       ├── checklist.md
│       ├── auto-reviews/
│       ├── consistency-checks/
│       ├── human-notes/
│       └── revision-tasks/
├── research/
│   └── setting/
├── index/
│   ├── canon-index.md
│   └── unresolved-threads.md
└── ops/
    ├── status.md
    ├── todo.md
    ├── decisions.md
    └── handoffs/
```

---

## 文件模板

按以下模板创建每个文件。`{placeholder}` 替换为项目实际值，`（待填）` 标记在构思阶段由用户确认后填入。

---

### AGENTS.md

~~~
# AGENTS Guide

## 适用范围
- 本文件适用于仓库根目录 `{project-root}`。
- 默认使用中文维护文档与交接。
- 不要依赖聊天记忆；一切稳定信息都必须落盘。

## 起手顺序
在开始任何任务前，按下面顺序读取：
1. `ops/status.md`
2. `ops/todo.md`
3. `ops/decisions.md`
4. `ops/handoffs/` 中最新的 1-3 份交接记录
5. `index/canon-index.md`
6. 再根据任务进入对应目录

## 记忆与计划维护
- 长期进度、阶段、阻塞、下一步写入 `ops/status.md`。
- 可执行事项写入 `ops/todo.md`，完成后及时勾选。
- 明确确认过的规则、取舍和方向写入 `ops/decisions.md`。
- 短期工作记忆只写入 `ops/handoffs/`。
- `ops/handoffs/` 文件名固定为 `YYYY-MM-DD-HHMM-topic.md`。
- 每次完成一轮实质工作后，新增或更新一份 handoff。
- handoff 只做短期交接，不是最终事实源；稳定结论必须回写到 `core/`、`canon/`、`index/` 或 `ops/`。

## 目录职责
- `core/` — 全局规则源。项目定位、故事引擎、质量标准、工作流、上下文组装规则、文风规范。定义"整部作品长期不轻易变化的约束"。
- `canon/` — 故事事实源。所有可被正文直接引用的世界、人物、剧情结构。
- `canon/lore/` — 世界、地点、经济、制度、风俗、势力、题材专属体系。
- `canon/characters/` — 主角、核心配角、次要人物的人物卡与关系状态。
- `canon/outline/` — 总大纲、分卷大纲、剧情弧、章节 beats。
- `production/` — 生产过程材料，不是最高事实源。
- `production/drafts/` — 正文章节、场景计划、草稿性写作材料。
- `production/reviews/` — 审稿清单、自动审稿、设定核对、人工审阅、返工任务。
- `research/` — 外部研究资料。桥段卡、案例摘记、验证样例。只能作为参考，不能直接当本书 canon。
- `research/setting/` — 设定调研资料。时代速写卡、设定事实卡，为 worldbuilding 提供真实世界知识基础。
- `index/` — 跨目录导航层。`canon-index.md` 维护事实源导航，`unresolved-threads.md` 维护未回收线头。
- `ops/` — 项目运行态与会话记忆。

## 任务路由
- **写作任务** — 先读 `core/`，再读 `canon/outline/`，再读相关 `canon/lore/` 和 `canon/characters/`，然后进入 `production/drafts/`，最后按需查 `research/`。
- **审稿任务** — 先读目标章节，再读 `production/reviews/checklist.md`，再核对相关 canon，最后把返工项写回 `ops/todo.md` 或 `production/reviews/`。
- **设定修改** — 先改 `core/` 或 `canon/`，再同步 `index/`，最后补 `ops/` 和最新 handoff。
- **素材检索** — 先用 `research/` 找素材，再把真正采用的内容转写进 `canon/` 或 `production/drafts/scene-plans/`。

## 回写规则
- 不允许只改 `production/`、`research/` 或 handoff，而不改对应事实源。
- 不允许把本书设定只留在聊天里。
- 新增 canonical 文件后，同步更新 `index/canon-index.md`。
- 新增未定线头、伏笔或待确认事项后，同步更新 `index/unresolved-threads.md`。
- 任何新文档都必须归入 `core/`、`canon/`、`production/`、`research/`、`index/`、`ops/` 六类之一。

## 交接模板
每份 `ops/handoffs/*.md` 至少包含：
- 本次目标
- 已完成
- 影响文件
- 当前状态
- 下一步
- 阻塞/待确认
~~~

---

### core/positioning.md

~~~
# 项目定位

## 平台与题材
（待填：目标平台、主类型、子类型）

## 目标读者
（待填：读者画像、阅读偏好）

## 核心卖点
（待填：3-5 条核心卖点）

## 差异化方向
（待填：与同类作品的区别）

## 写作禁忌
（待填：本作不做什么）

## 作品关键词
（待填）
~~~

---

### core/high-concept.md

~~~
# 故事引擎

## 一句话故事
（待填）

## 三句话故事
（待填）

## 核心爽点
（待填：按重要性排列）

## 核心问题
（待填：主角为什么必须行动？优势是什么？外部压力来自哪里？）

## 长线成长路线
（待填：阶段性目标链）

## 剧情推进轮子
（待填：2-4 个持续产出剧情的循环机制）
~~~

---

### core/style-guide.md

~~~
# 文风规范

## 基调
- 白话为主，不用文言腔
- 句子短、段落短，移动端友好
- 对话多，内心独白适量
- 说明不压过事件本身

## 叙事
- 第三人称限制视角（默认，可改）
- 过去时态
- 场景驱动，少用大段总结叙述

## 节奏
- 每章至少一个明确推进和一个情绪点
- 结尾留钩子
- 信息密度足够，不灌水

## 对话
- 符合角色身份和语音标记
- 有潜台词，不全部说白
- 避免大段独白式对话

## 禁止
- 过度抒情和作者感慨
- 重复表达同一信息
- 无冲突的流水账日常
- 脱离角色身份的书面腔
~~~

---

### core/quality-bar.md

~~~
# 质量标准

## 开篇质量线
- 第 1 章必须迅速交代主角处境与核心难题
- 前 3 章必须让读者看到明确的破局方向
- 前 5 章必须出现至少一个可持续期待点
- 前 20 章必须初步建立全书主卖点与长线乐趣

## 单章质量线
- 每章至少有一个明确推进：信息、关系、资源、局势、目标中的一种发生变化
- 每章至少有一个可感知的情绪点
- 结尾留下继续读的动力
- 段落表达以白、顺、清楚为主

## 设定一致性
- 人物称呼、关系、动机保持稳定
- 时间、地点、资源数量、规则不可随意漂移
- 能力边界不能想起一出是一出
- 重要伏笔记录到 `index/unresolved-threads.md`

## 审稿判定
### 自动审稿重点
- 节奏是否拖沓 / 设定是否冲突 / 信息是否重复 / 钩子是否偏弱 / 文风是否偏离
### 人工审稿重点
- 这章到底好不好看 / 是否想看下一章 / 哪些地方无聊 / 哪些爽点不到位
~~~

---

### core/workflow.md

~~~
# 小说生产工作流

## 总流程
1. 立项与定位 — 明确题材、平台调性、目标读者、核心卖点
2. 故事引擎设计 — 定义主角长线目标、核心矛盾、爽点循环、推进轮子
3. 设定资产化 — 将世界、人物、体系拆分为独立文档
4. 多层大纲 — 总大纲、分卷大纲、剧情弧、章节 beats
5. 章节写作 — 每次写作前按 `context-assembly.md` 拼装注入包
6. 审稿与修订 — 自动审稿发现问题，人工终审判断好不好看
7. 状态维护 — 重大决策、进度、待办、阻塞写入 `ops/`，稳定事实回写 `core/` 或 `canon/`

## 执行原则
- 先搭系统，再批量写正文
- 资产文件化，不把关键设定只留在聊天里
- 提示词模板化，减少临场发挥
- 大纲分层，避免只靠一个总纲硬撑
- 每写完一章必须进入审稿闭环

## 当前阶段
阶段 0：项目已初始化，进入构思与设定阶段
~~~

---

### core/context-assembly.md

~~~
# 上下文组装规则

## 目标
在长篇创作中，用固定的上下文拼装方式减少遗忘、跑偏、崩设定与节奏失控。

## 注入分层

### 1. 恒定层（几乎每次都注入）
来源：`core/positioning.md`、`core/style-guide.md`、`core/quality-bar.md`
内容：平台风格、作品调性、叙事原则、文风限制、禁止事项

### 2. 全局剧情层
来源：`core/high-concept.md`、`canon/outline/master-outline.md`、当前卷大纲
内容：总主线、当前卷目标、当前剧情弧目标、当前章在全局中的作用

### 3. 局部上下文层
来源：`canon/outline/chapter-beats/`、`ops/handoffs/` 最近记录、`index/unresolved-threads.md`、相关人物卡
内容：最近 1-3 章摘要、当前人物状态、当前地点/时间、本章 beats、本章不能写错的设定点

### 4. 桥段层（按需）
来源：`research/` 中的桥段卡
原则：只取 1-2 张最贴近当前问题的卡片。先改写桥段 sequence 再生成 beats。桥段是解法，不替代人物动机。

### 5. 检索层（按需）
来源：`canon/lore/`、`canon/characters/`、`index/canon-index.md`
原则：不把所有资料一股脑塞入。只注入当前章强相关的设定。`research/` 只作外部参考，不充当 canon。

## 写作前拼装顺序
1. 恒定层
2. 当前卷/弧摘要
3. 当前章要解决的叙事问题
4. 候选桥段卡 1-2 张
5. 最近剧情摘要
6. 当前章 beats
7. 当前章涉及的人物/地点关键信息
8. 本章写作目标与结尾钩子要求

## 审稿也要分层
- 结构审稿：节奏、钩子、信息密度
- 设定审稿：一致性、逻辑、遗忘点
- 风格审稿：平台适配、白话程度、爽点表达
- 桥段审稿：解法聪明度、人物服务度
- 改写提示：只针对指定问题返工，不整章无目标重写

## 回写要求
- `ops/handoffs/` 只存短期交接，不是最终事实源。
- 确认采用的设定、人物状态或剧情结构，必须回写 `core/` 或 `canon/`。
- `production/` 里的正文和审稿材料不能替代 canon。
- `research/` 的素材只能作为外部参考。
~~~

---

### index/canon-index.md

~~~
# Canon Index

## 用途
事实源导航页。需要查设定、人物、结构时，先看这里。新增或重命名 canonical 文档后必须同步更新。

## 全局规则源
- `core/positioning.md`：平台定位、目标读者、卖点
- `core/high-concept.md`：故事引擎与核心爽点
- `core/quality-bar.md`：质量标准
- `core/workflow.md`：生产流程
- `core/context-assembly.md`：上下文组装规则
- `core/style-guide.md`：文风规范

## 世界设定
（随 canon/lore/ 内容补充而更新）

## 人物设定
（随 canon/characters/ 内容补充而更新）

## 剧情结构
（随 canon/outline/ 内容补充而更新）

## 非 canon 但常用
- `index/unresolved-threads.md`：未回收线头
- `ops/decisions.md`：已确认决策
- `research/`：素材参考库
~~~

---

### index/unresolved-threads.md

~~~
# 未回收线头与待确认事项

## 使用规则
- 只记录仍未闭环的问题。
- 确认或解决后，回写对应事实源，从这里删除或标记已闭环。

## 当前待确认
（初始化时为空）

## 当前待补事实源
（初始化时为空）

## 当前长线线头
（初始化时为空）
~~~

---

### ops/status.md

~~~
# 项目状态

## 当前阶段
阶段 0：项目已初始化

## 已完成
- 建立项目目录骨架
- 生成全部骨架文件

## 下一步
1. 完成项目定位（core/positioning.md）
2. 设计故事引擎（core/high-concept.md）
3. 补完文风规范（core/style-guide.md）

## 当前缺口
- 所有 core/ 文件待填充
- canon/ 全部为空
~~~

---

### ops/todo.md

~~~
# 待办事项

- [ ] 完成项目定位
- [ ] 设计故事引擎
- [ ] 补完文风规范
~~~

---

### ops/decisions.md

~~~
# 已确认决策

（记录明确确认过的规则、取舍和方向。格式：日期 + 决策内容 + 原因。）
~~~

---

### production/reviews/checklist.md

~~~
# 审稿清单

## 一、自动审稿
### 结构审稿
- 开头是否快速进入局面
- 本章是否有明确推进
- 中段是否灌水
- 结尾是否有继续读的动力

### 设定审稿
- 人物称呼、身份、关系是否一致
- 时间线是否合理
- 地点与行动路径是否合理
- 规则、能力、资源是否前后冲突
- 与既有伏笔、未解决线头是否矛盾

### 风格审稿
- 是否白、顺、易读
- 是否有过度抒情或解释
- 爽点是否表达清楚
- 是否存在重复表达

## 二、人工审稿
- 这章好不好看
- 是否想追更
- 最无聊的部分在哪
- 最有劲的部分在哪

## 三、返工类型
- 提速：删冗余，强化推进
- 增钩：加强章末期待感
- 强爽点：把获得、反制、成长的反馈写明确
- 补逻辑：修设定冲突，补因果链
- 调文风：更口语、更顺读、更贴平台
~~~
