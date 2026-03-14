# 素材搜集方法论

## 触发场景

- 写作过程中缺乏某类桥段/场景的灵感
- 需要了解特定叙事手法的定义、范例和变体
- 需要参考经典作品中某类场景的写法
- 为特定类型的小说预研可用的套路/模式
- 大纲/beats 需要为某个场景选择叙事解法

> 如果需要的是真实世界的社会、历史或领域知识（如"宋代货币"、"法医工作流程"），请使用 [setting-research.md](setting-research.md)。

## 与 setting-research.md 的区别

| | plot-research.md（本文档） | setting-research.md |
|---|---|---|
| 回答的问题 | **怎么写**（叙事手法、桥段套路、情节结构） | **写什么**（真实世界的社会、历史、领域知识） |
| 典型素材源 | TV Tropes、写作博客、经典文学 | Wikipedia、古籍数据库、学术搜索 |
| 输出格式 | 桥段卡、技巧卡 | 设定事实卡、时代速写卡 |
| 存放位置 | `research/plot/` | `research/setting/` |

## 工作流

采用**自治模式**：agent 自主完成搜索、整理和回写。

### 第一步：需求定义

明确本次搜集的目标：

- **搜集类型**：桥段（叙事套路/情节模式）、技巧（写作手法/叙事技术）、还是结构参考（经典作品的处理方式）
- **叙事问题**：当前面临的具体问题（如"第一卷高潮需要一个揭示身份的反转"、"对话场景总是平淡"）
- **关联上下文**：涉及哪些角色、场景、剧情弧

### 第二步：搜索执行

根据需求类型选择搜索策略（见下方），执行搜索并收集原始素材。

### 第三步：整理输出

将原始素材整理为标准格式的桥段卡或技巧卡（见下方"输出格式"），写入 `research/plot/` 目录。

### 第四步：回写与衔接

按回写清单更新项目文件。如素材直接关联当前写作任务，进入下方"桥段适配"流程。

## 素材源

### Tier 1：直接抓取

| 素材源 | 核心价值 | 获取方式 | URL 模式 |
|--------|---------|---------|---------|
| **TV Tropes** | 叙事套路百科：trope 定义、变体、跨作品范例 | `WebFetch` | `https://tvtropes.org/pmwiki/pmwiki.php/Main/{TropeName}` |
| **Wikipedia** | 叙事技巧的学术定义、分类体系 | `WebFetch` | `https://en.wikipedia.org/wiki/{Article}` |
| **Project Gutenberg** | 公版文学作品全文 | `WebFetch` | `https://www.gutenberg.org/files/{id}/{id}-0.txt` |

### Tier 2：搜索引擎中介

| 素材源 | 获取方式 | 搜索模式 |
|--------|---------|---------|
| **写作博客** | `WebSearch` → `WebFetch` | `"{技巧}" writing craft blog` |
| **Reddit 写作社区** | `WebSearch` → `WebFetch` old.reddit.com | `site:reddit.com/r/writing {关键词}` |
| **知乎** | `WebSearch` 间接获取 | `site:zhihu.com {中文关键词}` |
| **中文网文论坛** | `WebSearch` 间接获取 | `龙的天空 {关键词}` 或 `网文写作 {关键词}` |

### TV Tropes 关键索引

| 索引 | URL 后缀 | 用途 |
|------|---------|------|
| Plots | `Main/Plots` | 情节类型总索引 |
| Narrative Devices | `Main/NarrativeDevices` | 叙事手法 |
| Plot Twist | `Main/PlotTwist` | 反转类型 |
| Beginning Tropes | `Main/BeginningTropes` | 开场方式 |
| Ending Tropes | `Main/EndingTropes` | 结局方式 |
| Romance Arc | `Main/RomanceArc` | 感情线套路 |
| The Hero's Journey | `Main/TheHerosJourney` | 英雄之旅 |
| Conflict | `Main/Conflict` | 冲突类型 |
| Gambit Index | `Main/GambitIndex` | 计谋与博弈 |
| Power-Up | `Main/PowerUp` | 升级与强化 |
| Reveal Tropes | `Main/RevealTropes` | 揭秘与反转 |

## 中文网文桥段分类导引

从中文网文的常见叙事需求出发，映射到 TV Tropes 和搜索关键词。先在此表定位需求类别，再用对应关键词进入搜索策略。

| 叙事需求 | 中文网文常用名 | TV Tropes 入口 | 搜索提示 |
|---------|-------------|---------------|---------|
| **逆袭打脸** | 打脸、反杀、碾压、扮猪吃虎 | The Dog Bites Back, Curb-Stomp Battle, Bullying a Dragon, Obfuscating Stupidity | `underdog victory trope` |
| **升级突破** | 突破、进阶、觉醒、变强 | Took a Level in Badass, Super Mode, Power-Up, Training from Hell | `power up trope` |
| **反转揭秘** | 反转、揭秘、真相大白、身份曝光 | The Reveal, Wham Episode, Luke I Am Your Father, Tomato Surprise | `plot twist types` |
| **感情发展** | 感情线、暧昧升温、冤家变情人 | Relationship Upgrade, Will They or Won't They, Belligerent Sexual Tension, Rescue Romance | `romance arc tropes` |
| **开场钩子** | 开局、悬念引入、倒叙 | In Medias Res, Action Prologue, How We Got Here, Cold Open | `opening hook techniques` |
| **危机解困** | 破局、翻盘、绝境逢生 | Batman Gambit, Indy Ploy, Xanatos Gambit, Crazy Enough to Work | `gambit tropes` |
| **金手指展开** | 系统、外挂、穿越、重生 | New Game Plus, Peggy Sue, Trapped in Another World, Story-Breaker Power | `isekai tropes` |
| **势力博弈** | 势力战、宗门对抗、朝堂 | Gambit Pileup, Enemy Mine, The Alliance, Faction Calculus | `faction conflict tropes` |

## 搜索策略

### A：寻找特定桥段

**场景**：需要一个特定效果的桥段（如"揭示反派身份的反转"）

1. 从桥段分类导引定位需求类别，或从 TV Tropes 索引页浏览相关分类
2. `WebFetch` 匹配的 trope 详情页
3. 顺着 "See Also" / "Compare" 发现关联套路
4. 回到创作上下文，适配到当前故事

```
示例搜索链路：
需求：「主角身份反转，揭示隐藏的贵族血统」
→ 桥段分类导引 → 反转揭秘类 → The Reveal, Luke I Am Your Father
→ WebFetch: tvtropes.org/.../Main/TheReveal → 读定义和变体
→ 追踪 See Also: LukeIAmYourFather / TomatoSurprise
→ WebFetch: tvtropes.org/.../Main/LukeIAmYourFather → 身份揭秘范例
→ 输出: 桥段卡「身份揭秘反转」
```

### B：学习写作技巧

**场景**：需要掌握某种叙事手法（如"展示而非告知"）

1. `WebSearch` 英文写作博客：`"{technique}" writing craft techniques`
2. `WebFetch` 2-3 篇排名靠前的博文
3. 如需中文补充：`WebSearch` `site:zhihu.com {中文关键词}`
4. 整理为可操作的技巧清单

```
示例搜索链路：
需求：「掌握 show don't tell 的技巧」
→ WebSearch: "show don't tell" writing craft techniques examples
→ WebFetch: 排名前 2 的博文 → 提取操作方法和 before/after 示例
→ WebSearch: site:zhihu.com 展示而非告知 写作技巧 → 补充中文语境
→ 输出: 技巧卡「展示而非告知」
```

### C：分析经典场景

**场景**：参考经典作品处理特定场景的方式

1. `WebSearch` 确认作品在 Project Gutenberg 的编号
2. `WebFetch` 获取全文，定位目标章节
3. 分析叙事结构、节奏、技巧

```
示例搜索链路：
需求：「参考《傲慢与偏见》如何处理求婚被拒场景」
→ WebSearch: Pride and Prejudice Project Gutenberg
→ WebFetch: gutenberg.org/files/1342/1342-0.txt → 定位 Chapter 34
→ 分析: 场景前张力铺垫、对话潜台词、拒绝层层递进、场景后情绪余波
→ 输出: 技巧卡「高张力对话场景：求婚被拒」
```

### D：批量预研类型套路

**场景**：开始新小说前，批量搜集该类型常用桥段

1. TV Tropes 搜索类型专属页面
2. 批量 `WebFetch` 感兴趣的 trope
3. Wikipedia 补充叙事结构理论
4. 按「开场 → 发展 → 高潮 → 结局」分类整理

```
示例搜索链路：
需求：「新开修仙小说，搜集常用桥段」
→ 桥段分类导引 → 升级突破类 + 势力博弈类 + 逆袭打脸类
→ WebFetch: tvtropes.org 的 Wuxia 相关页面
→ 批量 WebFetch: TookALevelInBadass, TournamentArc, CurbStompBattle, TheRival...
→ WebSearch: 修仙小说 常用桥段 套路 site:zhihu.com → 中文网文特有模式
→ 输出: 按阶段分类的多张桥段卡
```

### E：中文网文桥段定向搜索

**场景**：需要搜集中文网文特有的桥段模式（TV Tropes 覆盖不足的部分）

1. 从桥段分类导引定位需求
2. `WebSearch` 中文写作社区：`{桥段类型} 写法 网文 技巧`
3. `WebSearch` 知乎补充：`site:zhihu.com {桥段类型} 怎么写`
4. 如有对应 TV Tropes 入口，`WebFetch` 补充西方叙事理论视角
5. 整理为桥段卡，标注中文网文特有的变体和禁忌

```
示例搜索链路：
需求：「搜集"扮猪吃虎"桥段的写法和变体」
→ 桥段分类导引 → 逆袭打脸类
→ WebSearch: 扮猪吃虎 网文 桥段 写法 技巧
→ WebSearch: site:zhihu.com 扮猪吃虎 怎么写好
→ WebFetch: tvtropes.org/.../Main/ObfuscatingStupidity → 西方对应概念
→ 输出: 桥段卡「扮猪吃虎」（含中文网文变体和常见雷点）
```

> 如果需要搜集真实世界背景细节（特定时代器物、制度、生活方式），请使用 [setting-research.md](setting-research.md)。

## 桥段适配方法论

搜集到的桥段是通用叙事模式，不能直接套用。以下流程将桥段转化为本作可用的场景要素，对接 `core/context-assembly.md` 桥段层的要求（"先改写桥段 sequence 再生成 beats。桥段是解法，不替代人物动机"）。

### 1. 选择

从 `research/` 中选出 1-2 张与当前叙事问题最相关的桥段卡。选择标准：

- 桥段的叙事功能匹配当前需要（反转、升温、高潮、破局……）
- 桥段可以被当前角色的性格和动机支撑
- 桥段与已有设定和伏笔不冲突

### 2. 改写

将桥段的通用 sequence 替换为本作元素：

- 通用角色 → 本作角色（保留角色性格和动机的一致性）
- 通用场景 → 本作场景（利用已有的地点和设定）
- 通用冲突 → 本作冲突（服务于当前剧情弧的目标）

### 3. 验证

检查改写后的桥段：

- 角色的行为是否符合其性格和动机？
- 是否推进了剧情而非只是制造效果？
- 是否与已有伏笔和设定兼容？（核对 `index/unresolved-threads.md`）

### 4. 转化

将验证通过的桥段转化为下游制品：

- **场景计划**（`production/drafts/scene-plans/`）— 需要详细规划时
- **章节 beats**（`canon/outline/chapter-beats/`）— 直接进入写作流程时

在场景计划或 beats 的"桥段参考"字段标注来源卡片。

## 输出格式

搜集到的素材整理后写入项目的 `research/` 目录。

### 桥段卡

```markdown
## 桥段：{名称}

- **原名**: {英文 trope 名}
- **来源**: {TV Tropes / Wikipedia / 博客名}
- **标签**: {检索关键词，如: 反转, 揭秘, 高潮}
- **适用阶段**: 开场 / 发展 / 高潮 / 结局
- **一句话**: {概括}
- **机制**: {如何运作，为什么有效}
- **经典范例**: {1-2 个}
- **变体**: {常见变体或颠覆方式}
- **适用场景**: {什么情况下使用}
- **本作适配笔记**: （搜集时留空，适配阶段填写）
```

### 技巧卡

```markdown
## 技巧：{名称}

- **来源**: {出处}
- **标签**: {检索关键词，如: 对话, 节奏, 视角}
- **适用阶段**: 开场 / 发展 / 高潮 / 结局 / 通用
- **定义**: {准确定义}
- **操作方法**: {分步骤}
- **好的示例**: {做得好的例子}
- **常见错误**: {容易犯的错误}
- **适用场景**: {什么情况下使用}
```

## 回写清单

完成素材搜集后执行以下回写（不可跳过）：

1. **保存素材卡** → `research/plot/` 目录
2. **已决定采用的素材** → 转写关键信息到 `canon/` 或 `production/drafts/scene-plans/`
3. **更新 ops/todo.md** → 标记素材搜集完成，添加后续待办
4. **新增 handoff** → `ops/handoffs/` 交接记录，记录搜集了什么、关联哪个叙事问题
5. **叙事决策** → 如产出涉及新的叙事方向选择，记入 `ops/decisions.md`

## 注意事项

1. TV Tropes 页面较大（50-140KB），优先读顶部定义和范例，按需深入
2. Project Gutenberg 文件很大（500KB+），先定位章节再截取
3. Reddit 必须用 `old.reddit.com` 域名
4. 知乎只能通过 WebSearch 间接获取，直接 WebFetch 会超时
5. 英文源优先——TV Tropes 和 Wikipedia 的叙事理论远比中文源系统
6. `WebFetch` 失败时，退回 `WebSearch` 获取摘要信息，不要卡在单一来源上
7. 豆瓣读书可作为补充书目信息来源（`https://book.douban.com/subject/{id}/`），但反爬严重，成功率不稳定
