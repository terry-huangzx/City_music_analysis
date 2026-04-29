# Demo Video Plan — Urban Music Pulse
**Group 50 | STA313 | Due: Monday Apr 14, 11:59pm | 10 min | 10%**

---

## 核心策略

评分最重的两项是 **Scientific Process (3pts)** 和 **Video Quality (3pts)**。
脚本v1的问题：科学过程太薄、只演示了hero没演示主产品、全程屏幕录制没出镜。

本方案用 **"三幕剧"叙事结构** 代替线性汇报——
- 第一幕：提出问题（为什么要做）
- 第二幕：展示产品（做了什么）
- 第三幕：揭示过程（怎么做到的）

每一幕都有情感弧度，不是干巴巴列要点。

---

## 镜头语言规划

整个视频交替使用三种画面：

| 类型 | 说明 | 使用场景 |
|------|------|----------|
| **出镜** | 演讲者正面或侧面，背景干净 | 开头、问题阐述、科学过程、结尾 |
| **屏幕录制** | 全屏展示网页产品 | Demo段落 |
| **画中画** | 屏幕录制 + 右下角演讲者小窗 | Demo讲解时保持人的存在感 |

> 关键：rubric明确说 "speaker's face is well integrated"、"voice over is much less engaging"。
> 至少在非Demo段落，演讲者必须出镜。Demo段落用画中画。

---

## 分镜脚本

### ACT 1 — 问题与动机
**目标：让观众30秒内被抓住，2分钟内理解这件事为什么重要。**

---

#### Scene 1: Hook (0:00–0:40) — 40s
**画面：** 屏幕录制 city_music_pulse.html hero画面，黑胶唱片旋转、dots闪烁、beat on。
叠加大字幕：_"Every city has a sound."_

**讲稿思路：**
> Every city has a sound. Not just a style of music — a rhythm, a density, a texture that is different from every other city on the continent.
>
> New York has ten thousand concerts a year. Ottawa has less than a thousand. Calgary leans country. Miami swings toward R&B and EDM. Montreal's scene is indie and jazz.
>
> We know this intuitively. But can we actually see it? Can we put thirteen cities on a map and make their musical character visible through data?

**要点：** 不要自我介绍、不要说课程名。直接用一个有画面感的问题抓住观众。

---

#### Scene 2: Problem framing (0:40–2:00) — 80s
**画面：** 切换到演讲者出镜（中景，背景简洁）。

**讲稿思路：**
> Live music is one of the most tangible signals of civic vitality. It drives local economies, defines neighborhoods, shapes tourism, and brings communities together.
>
> But there is no tool today that lets you compare the musical character of cities side by side. Concert data is scattered across dozens of ticketing platforms and fan databases. A venue operator deciding where to expand, a festival planner choosing a city, a cultural researcher studying urban identity — none of them have a single, interactive resource that answers basic comparative questions:
>
> Which city hosts the most concerts? Which genres dominate where? Are events concentrated in a few mega-venues or spread across hundreds of small rooms? And on which nights does audience demand outstrip what promoters actually schedule?
>
> That's the gap we set out to fill. Our guiding question was simple: **Where does live music happen in North America, and what does each city actually sound like?**

**rubric覆盖：** 问题是什么 ✓ 为什么是问题 ✓ 为谁 ✓ 为什么重要 ✓ 为什么没人解决 ✓

---

#### Scene 3: Audience & Impact (2:00–2:30) — 30s
**画面：** 继续出镜，或叠加简洁的文字slide（列出受众类型）。

**讲稿思路：**
> We designed this for two audiences. First, professionals who make decisions based on music culture: venue operators, festival organizers, tourism boards, cultural policy researchers. Second, any curious person who wants to explore how cities compare through their live music.
>
> This dual audience shaped every design decision: the product had to be analytically deep enough for experts, but immediately engaging for someone opening it for the first time.

---

#### Scene 4: Team Introduction (2:30–2:50) — 20s
**画面：** 切到一张设计好的slide——五人照片+姓名，Group 50, STA313, University of Toronto。

**讲稿思路：**
> We are Group 50 from STA313 Data Visualization at the University of Toronto. I'm [Speaker Name], and our team includes Yanting Fan, Zixiang Huang, Xiaoyao Wang, Jingyi Yang, and Yuxin Yao.

**要点：** 放在Act 1尾部，不要放最开头（打断hook），也不要放最后（rubric没要求放最后）。

---

### ACT 2 — 产品演示
**目标：完整走一遍 city_music_pulse.html，让观众理解产品怎么用、能回答什么问题。**

> 这是上一版脚本最大的修正——必须演示完整的scrollytelling产品，不能只演示hero。

---

#### Scene 5: Solution Overview (2:50–3:30) — 40s
**画面：** 画中画（屏幕录制 + 演讲者小窗）。打开 city_music_pulse.html，展示首屏。

**讲稿思路：**
> Our solution is **Urban Music Pulse** — a single, self-contained web page that transforms 56,000 concert records into a scrollytelling narrative.
>
> The experience is organized as a journey. It opens with an interactive vinyl-record map of North America, then guides the reader through four analytical movements — seasonal pulse, genre composition, venue distribution, and demand gap. Each movement is a full-screen interactive visualization with story cards that highlight key findings as you scroll.
>
> Let me walk you through it.

---

#### Scene 6: Hero Demo (3:30–5:00) — 90s
**画面：** 全屏录制 city_music_pulse.html，画中画小窗。操作要慢、光标清晰。

**演示流程和讲稿：**

**(a) 首屏 — 黑胶地图 (30s)**
> When you first open the page, you see thirteen cities, each represented as a spinning vinyl record on a map of North America. A synthesized 118 BPM beat drives the interface — the records pulse, the dots breathe. Each dot is a real concert from our dataset, color-coded by genre.
>
> Even before you interact, you can already see differences. New York's cluster is the densest. Miami's color profile skews toward warm tones — R&B, EDM. Calgary shows more orange and brown — country and rock.

**(b) Hover + Click dot (20s)**
> *(Hover over a dot)* Hovering previews the event. *(Click a dot)* Clicking opens a detail card: artist, venue, date, genre. Every dot is traceable back to a real concert record.

**(c) Click city marker → city panel (25s)**
> *(Click Toronto or New York)* Clicking a city opens a detail panel — total events, genre breakdown, top venues, and a browsable list of sampled concerts. This is the analytical layer: you can dig as deep as you want.

**(d) Scroll to "Enter the Full Story" → Soundwave Timeline (15s)**
> *(Scroll down past the story cards to the soundwave timeline)* Below the map, the page transitions into a soundwave timeline that previews the four analytical movements ahead. Each node is a chapter. Let me take you through them.

---

#### Scene 7: Four Chapters Demo (5:00–7:00) — 120s
**画面：** 继续全屏录制+画中画。每个章节约30秒。

**(a) Chapter 1 — Seasonal Pulse (30s)**
> *(Scroll to Chapter 1)* The first layer is a heatmap of monthly event volume across all thirteen cities. Most cities peak in summer — July through September. But Miami is the clearest outlier: its concert season peaks in winter, and nearly disappears in summer.
>
> *(点击一个heatmap cell)* Clicking any cell ranks all cities for that month. *(切换到 Per 100k toggle)* And toggling to per-capita mode reveals a hidden pattern: Detroit and Las Vegas, two smaller cities, punch well above their weight in live music intensity once population is accounted for.

**(b) Chapter 2 — Genre Composition (30s)**
> *(Scroll to Chapter 2)* The second layer asks: beyond volume, what genres does each city offer? This scatter plot maps total events against genre diversity. New York and LA are top-right — many events, many genres. But some smaller cities like Montreal achieve high diversity with far fewer events.
>
> *(点击某个城市圆点)* Clicking a city opens a genre treemap showing the exact breakdown.

**(c) Chapter 3 — Venue Distribution (30s)**
> *(Scroll to Chapter 3)* Layer three examines structure. Some cities funnel half their concerts through just ten venues. Others spread activity across hundreds of smaller rooms. This has real implications for how resilient and accessible a city's music scene is.
>
> *(交互操作)* The rank-ordered bar chart lets you compare venue concentration across any two cities.

**(d) Chapter 4 — Demand Gap (30s)**
> *(Scroll to Chapter 4)* The final layer crosses Spotify listening data with event supply. The radial chart shows, for each city, which days and times have the biggest gap between what audiences want to hear and what is actually scheduled.
>
> *(指出Monday)* One finding is universal: Monday nights are the most underserved slot across nearly every city. For event planners, that's a concrete, untapped programming opportunity.
>
> *(切换到Las Vegas)* Las Vegas is the only city where Saturday nights approach balance — every other market still has a gap even on its busiest night.

---

### ACT 3 — 科学过程与反思
**目标：说服评委这不是随便做的——有严谨的研究、迭代和批判性思考。这部分值3分，给足时间。**

---

#### Scene 8: Scientific Process (7:00–8:40) — 100s
**画面：** 前半段出镜（体现严肃性），后半段可切屏幕展示 exploratory layers 截图或数据pipeline流程图。

**讲稿思路：**

**(a) 数据选择 (20s)**
> Let me explain the scientific process behind this.
>
> We did not grab the first dataset we found. Our first candidate was the Ticketmaster Discovery API, but it only covers upcoming events, not historical records. That made it unsuitable for comparative analysis. We pivoted to setlist.fm — a community-maintained database with a much deeper historical footprint: 56,000 concert records across 13 metros.

**(b) 数据清洗挑战 (20s)**
> Cleaning the data was harder than collecting it. The raw records use inconsistent city names: a concert in Mississauga or Scarborough is still part of the Toronto metro, but the data does not know that. We wrote custom aggregation logic to map over 360 suburb names back to their parent metros. This step required manual curation and was one of the most labor-intensive parts of the project.

**(c) 迭代设计过程 (30s)**
> We did not jump straight to the final product. We built four separate exploratory prototypes first — the layers you just saw. Each one tested a different analytical angle: does seasonal volume differ by city? Do genres cluster? How concentrated are venues? Does supply match demand?
>
> These prototypes served as our hypothesis-testing phase. Only after confirming which findings were strong and surprising did we design the scrollytelling narrative to stitch them into a coherent story. The hero vinyl map was developed in parallel as an immersive entry point.

**(d) 设计决策的justification (30s)**
> Every major design choice has a reason.
>
> Why scrollytelling instead of a dashboard? Because our communication goal was to guide a general audience through a sequence of insights, not to give analysts a free-form exploration tool. Scrollytelling controls pacing and builds narrative tension — which is exactly what a "convince a donor" scenario requires.
>
> Why the vinyl record metaphor? It encodes the domain — music — directly into the visual form. That is a semantically meaningful mapping, not decoration. The annular scatter of concert dots preserves the clickability of each city marker while communicating event density through visual weight.
>
> Why canvas rendering instead of SVG or DOM nodes? With thousands of dots per city, DOM-based rendering would have been too slow. Layered HTML5 canvas gave us smooth 60fps interaction without any external library dependency.

---

#### Scene 9: Alternatives & Limitations (8:40–9:20) — 40s
**画面：** 出镜。体现诚实和批判性思维。

**讲稿思路：**

> We want to be transparent about limitations and alternatives we considered.
>
> Genre assignment is currently city-level, not per-artist. A more rigorous approach would pull verified tags from MusicBrainz or Spotify's artist API for every individual performer. That is a clear next step.
>
> The setlist.fm dataset has coverage bias: it is stronger for major artists and well-documented markets. Smaller acts and mid-size cities may be underrepresented.
>
> Our supply-demand mismatch layer uses Spotify chart data as a proxy for demand. It is a hypothesis-generating lens, not a causal claim.
>
> We also considered alternative designs — for instance, a Tableau dashboard or a static report with embedded Plotly charts. We chose a self-contained HTML scrollytelling approach because it required no server, no installation, and could be shared as a single link. That portability mattered for a product meant to reach non-technical audiences.

---

#### Scene 10: Closing (9:20–10:00) — 40s
**画面：** 切回 city_music_pulse.html hero画面，黑胶唱片旋转。最后5秒叠 title card fade out。

**讲稿思路：**
> Cities are not interchangeable. Their music scenes are not interchangeable. And the data proves it.
>
> Urban Music Pulse takes 56,000 concerts and makes the musical pulse of a continent visible, explorable, and felt. For researchers it provides a comparative lens that did not exist before. For venue operators and cultural planners it surfaces evidence-based insights — like the fact that Monday nights are universally underserved. And for anyone curious about cities and music, it offers a way to discover something true and surprising about the places they know.
>
> With more data, more cities, and continued development, this could become a reference tool for anyone who cares about live music culture.
>
> Thank you for watching. We hope you felt the pulse.

---

## Rubric对照检查

| 评分项 (满分) | 覆盖位置 | 策略 |
|---|---|---|
| **Problem & Motivation (2)** | Scene 1-3 (2min) | Hook抓人 → 具体gap → 受众和impact |
| **Solution Description (2)** | Scene 5-7 (4min10s) | 完整demo全产品：hero + 4个chapter，边操作边讲insight |
| **Scientific Process (3)** | Scene 8-9 (2min20s) | 数据选择理由、清洗挑战、迭代设计过程、每个设计决策的justification、替代方案批判、局限性 |
| **Video Quality (3)** | 全程 | 出镜+画中画+屏幕录制交替；流畅转场；专业tone |
| **团队介绍** | Scene 4 (20s) | 照片slide |

---

## 制作Checklist

- [ ] 录演讲者出镜段落（Scene 2, 3, 4, 8, 9）— 背景干净、灯光好、看镜头
- [ ] 录屏幕操作段落（Scene 1, 5, 6, 7, 10）— 光标慢、操作流畅、提前rehearse操作路径
- [ ] 制作team introduction slide（5人照片+姓名）
- [ ] 剪辑：出镜和屏幕录制之间加简短transition（fade或cut，不要花哨）
- [ ] 检查音频质量：用外置麦克风或安静环境
- [ ] 最终视频导出 → 上传YouTube/Vimeo → 确保链接teaching team可访问
- [ ] 制作 video.pdf（包含视频链接）
- [ ] 制作 contributions.pdf（表格格式，每人任务+时间）

---

## 与上一版脚本的关键差异

| 问题 | 旧版 | 本版 |
|------|------|------|
| Demo内容 | 只演示 hero-real-data.html | 完整演示 city_music_pulse.html（hero + 4章节） |
| Scientific Process | 90s，只提数据源切换 | 100s+40s，覆盖迭代设计、设计justification、替代方案、局限性 |
| 出镜 | 全程屏幕录制+画外音 | 出镜 / 画中画 / 屏幕录制交替 |
| 叙事结构 | 线性汇报（Section 1-10） | 三幕剧（问题→产品→过程），有情感弧度 |
| Team intro位置 | 最前面 | Act 1尾部，不打断hook |
| 时间分配 | Scientific Process被压缩 | 给最高权重项充足时间 |
