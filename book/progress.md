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
| 全部 | 研究中 |

## 未解决问题
- 附录已取消；如用户后续要求可加精简书目。
