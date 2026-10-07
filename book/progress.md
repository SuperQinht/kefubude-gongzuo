# 进度记录（断点续作必读）

## 当前阶段
阶段 2：研究。用户已确认大纲（2026-10-07）：全本约 68 万字正文、不做附录、诗词可成段讲、书名《毛泽东：在不确定中下判断》、样章第 16 章（用户未另指定，按推荐）。
9 个研究员已并行派出（vol_01—vol_08、theory），说明见 research/BRIEF.md。下一步：审阅资料包 → 写样章第 16 章 → 核查 + 文风审读 → 发给用户确认。

## 已完成
- 阶段 0：环境检查。pandoc 3.1.3、Python 3.13、Java、epubcheck 4.2.6、Noto Sans CJK SC（/usr/share/fonts/opentype/noto/NotoSansCJK-*.ttc）、Pillow 均可用。注意：新会话容器中 fonts-noto-cjk 与 epubcheck 需重新 `apt-get install -y fonts-noto-cjk epubcheck`。
- 可复用：仓库 `luxun-daodu/build/` 中有上一个项目的 build.sh / normalize.py（引号规范化）/ epub.css / make_cover.py，可作为排版参考。
- 目录：book/{research,chapters,reviews,build,output}
- book/outline.md、book/STYLE.md、book/glossary.md、book/crossref.md

## 文件命名约定
- 章节：book/chapters/{卷号两位}_{章号两位}.md，例如第 16 章 → 04_16.md；序章 00_00.md；终卷 09_43/44/45；附录 10_xx。
- 资料包：book/research/vol_01.md … vol_08.md、theory.md
- 核查与审读意见：book/reviews/{章文件名}_fact.md、_style.md

## 章节状态
| 章 | 状态 |
|---|---|
| 资料包 vol_01—08、theory | 全部已交（大量【待核】，因 WebFetch 被拦截、搜索额度受限） |
| 第16章（样章） | 修改中（核查：5 条必须改；文风：需修改） |
| 其余 | 待样章确认后撰写 |

## 未解决问题
- 网络限制：WebFetch 对维基、爱思想、marxists.org、人民网等几乎全部被拦截，只能靠 WebSearch 摘要；已建议用户在环境设置中放宽 Allowed domains（2026-10-07），未获回复前按“核不到就删或标说法不一”执行。
- 附录已取消；如用户后续要求可加精简书目。
- 第 3 章注意：研究员称斯诺记录中毛可能提到一师时写过题为《心之力》的文章（原稿不存，流传全文为当代伪作，“105 分”为加码）——须核实斯诺原文后再定 STYLE.md 中的表述。
- 研究员报告搜索有会话级上限（CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION，约 200 次），需注意节省。
- 研究员修正：蒋在上海证券物品交易所是 1920—1922 年（非 1916）；“不动笔墨不读书”是徐特立的主张；“与天奋斗，其乐无穷”出自日记（同学回忆），非批注。
