# 项目初始化工作流

## 触发条件

`project/arch.md` 不存在，或用户明确要求初始化新开发项目。

## 流程

### 1. 了解游戏设计

首先读取 GDD 文档获取设计上下文：

1. 读取 `gdd/vision/overview.md`（项目概述）
2. 读取 `gdd/vision/pillars.md`（设计支柱）
3. 读取 `gdd/vision/core-loop.md`（核心循环）
4. 读取 `gdd/memory/project.md`（设计进度）

如果 `gdd/` 不存在，提醒用户先完成游戏设计（使用 gdd-assistant），或至少提供基本的游戏类型和核心玩法方向。

### 2. 确定技术方向

通过对话了解以下信息（逐步讨论，不要一次性全问）：

**前端/客户端：**
- 目标平台（Web/桌面/移动/多端）
- 渲染需求（2D/3D/混合）
- 引擎或框架倾向
- 性能约束（帧率目标、内存预算）

**服务端：**
- 是否需要服务端（纯单机 vs 联网）
- 服务端语言/框架倾向
- 实时性要求（回合制 vs 实时同步）
- 数据持久化需求

**通信：**
- 协议格式：Protobuf（已确定）
- 传输方式（WebSocket/HTTP/UDP）
- 同步模型（状态同步/帧同步/混合）

**工具链：**
- 包管理器
- 构建工具
- 版本控制约定

### 3. 批判性讨论

对每个技术选型，**主动质疑**：

- "这个选型能满足 GDD 中 `<设计支柱>` 的要求吗？"
- "有没有更轻量的替代方案？"
- "最坏情况下（玩家规模/内容量上限）这个技术栈扛得住吗？"
- "团队对这个技术栈的熟悉度如何？学习成本是否值得？"
- "这个选型会不会限制未来的扩展方向？"

每个选型讨论后，记录决策和理由。

### 4. 创建目录结构

```
project/
├── arch.md
├── memory/
│   ├── project.md
│   └── modules/
├── tech-stack/
│   ├── frontend.md
│   ├── server.md
│   └── toolchain.md
├── architecture/
│   ├── frontend.md
│   ├── server.md
│   ├── data-model.md
│   └── protocols/
│       └── overview.md
├── code-structure/
│   ├── frontend.md
│   └── server.md
├── testing/
│   └── strategy.md
├── conventions/
│   ├── coding.md
│   └── error-handling.md
└── gdd-mapping.md
```

### 5. 填充初始文档

**`arch.md`**（架构索引，始终载入）：

```markdown
# <项目名> 架构总览

## 技术概述
<一句话概括技术栈和架构风格>

## 文档索引

### 技术栈
- [前端技术栈](tech-stack/frontend.md) — <一句话摘要>
- [服务端技术栈](tech-stack/server.md) — <一句话摘要>
- [工具链](tech-stack/toolchain.md) — <一句话摘要>

### 架构设计
- [前端架构](architecture/frontend.md) — <一句话摘要>
- [服务端架构](architecture/server.md) — <一句话摘要>
- [数据模型](architecture/data-model.md) — <一句话摘要>
- [通信协议](architecture/protocols/overview.md) — <一句话摘要>

### 代码结构
- [前端代码结构](code-structure/frontend.md) — <一句话摘要>
- [服务端代码结构](code-structure/server.md) — <一句话摘要>

### 质量保障
- [测试策略](testing/strategy.md) — <一句话摘要>
- [编码规范](conventions/coding.md) — <一句话摘要>
- [错误处理](conventions/error-handling.md) — <一句话摘要>

### 映射
- [GDD 映射表](gdd-mapping.md) — GDD 系统与代码模块的对应关系

## 架构概览

<用简洁文字或 ASCII 图描述客户端-服务端关系、主要组件>
```

**`memory/project.md`**：

```markdown
# 项目 Memory

## 状态
- 阶段: 设计
- 最后更新: <today>

## 模块进度
（初始化完成，尚无模块设计）

## 技术决策
- [<today>] 项目启动，初始化开发架构工程

## 技术债务
（暂无）

## 待解决
- 完善各技术栈选型文档
- 设计前端架构
- 设计服务端架构
- 定义通信协议
- 规划代码目录结构
- 制定测试策略

## 回顾
- [<today>] 项目初始化完成
```

**`gdd-mapping.md`**：

```markdown
# GDD 系统 → 代码模块映射表

此表记录游戏设计系统与代码实现模块的对应关系，便于开发时快速定位相关文档。

| GDD 系统 | GDD 文档路径 | 代码模块（前端） | 代码模块（服务端） | 状态 |
|----------|-------------|----------------|------------------|------|
| （随设计和开发推进填充） | | | | |
```

**其他子文档**：创建空模板，包含标题和主要章节骨架，标注"待设计讨论后填充"。

### 6. 引导下一步

初始化完成后，建议用户按以下优先级推进：

1. **技术选型深化** — 逐个完善 `tech-stack/` 下的文档（建议从与核心玩法最相关的开始）
2. **架构设计** — 先设计与核心循环最相关的模块架构
3. **协议定义** — 确定客户端-服务端通信的核心协议
4. **代码结构** — 规划目录结构并创建脚手架
5. **规范制定** — 在写第一行代码之前确定编码规范

提醒用户：可以进入设计讨论模式逐个深入讨论每个主题。
