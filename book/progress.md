# 进度记录（断点续作必读）

## 当前阶段
阶段 1：大纲已完成，**等待用户确认**（含：字数方案选择、样章选择、书名）。确认前不要进入阶段 2。

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
| 全部 | 未开始 |

## 未解决问题
- 等待用户确认大纲。
