from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random, sys
F = sys.argv[1]  # font dir
W, H = 1600, 2400
random.seed(7)
bg = (24, 22, 20); paper = (236, 228, 212); red = (168, 38, 30); dim = (120, 112, 100)
img = Image.new("RGB", (W, H), bg)
d = ImageDraw.Draw(img)
# 纸纹噪点
for _ in range(60000):
    x, y = random.randrange(W), random.randrange(H)
    c = random.randint(26, 40); d.point((x, y), (c, c-2, c-4))
# 铁屋：一个大方框 + 高处一扇小窗透光
hx0, hy0, hx1, hy1 = 260, 330, 1340, 1330
d.rectangle([hx0, hy0, hx1, hy1], outline=(70, 66, 60), width=14)
for i in range(6):  # 铁板接缝
    x = hx0 + (hx1-hx0)*(i+1)//7
    d.line([(x, hy0+7), (x, hy1-7)], fill=(44, 41, 38), width=4)
# 窗与光
wx0, wy0, wx1, wy1 = 980, 430, 1160, 600
glow = Image.new("L", (W, H), 0); g = ImageDraw.Draw(glow)
g.polygon([(wx0, wy0), (wx1, wy0), (760, 1330), (520, 1330)], fill=70)
glow = glow.filter(ImageFilter.GaussianBlur(40))
img.paste(Image.new("RGB", (W, H), (210, 196, 160)), (0, 0), glow)
d = ImageDraw.Draw(img)
d.rectangle([wx0, wy0, wx1, wy1], fill=(240, 226, 186))
d.line([((wx0+wx1)//2, wy0), ((wx0+wx1)//2, wy1)], fill=(60, 56, 50), width=8)
d.line([(wx0, (wy0+wy1)//2), (wx1, (wy0+wy1)//2)], fill=(60, 56, 50), width=8)
d.rectangle([wx0, wy0, wx1, wy1], outline=(60, 56, 50), width=10)
# 地上的路：从屋外向远方延伸，脚印式短线
for k in range(26):
    t = k/25
    y = 1400 + t*520
    w = 40 + t*260
    cx = 800 + (t-0.5)*120
    d.line([(cx-w/2, y), (cx-w/2+w*0.28, y)], fill=(150, 138, 118), width=int(3+t*6))
    d.line([(cx+w/2-w*0.28, y), (cx+w/2, y)], fill=(150, 138, 118), width=int(3+t*6))
# 文字
title = ImageFont.truetype(f"{F}/NotoSansCJKsc-Black.otf", 230)
sub = ImageFont.truetype(f"{F}/NotoSansCJKsc-Medium.otf", 72)
small = ImageFont.truetype(f"{F}/NotoSansCJKsc-Regular.otf", 44)
def ctext(y, s, font, fill):
    w = d.textlength(s, font=font); d.text(((W-w)/2, y), s, font=font, fill=fill)
# 标题叠放在铁屋下半部，先垫一块底板，避免铁板接缝穿过文字
d.rectangle([hx0+7, 800, hx1-7, 1220], fill=(28, 26, 24))
ctext(820, "铁屋与路", title, paper)
ctext(1110, "鲁迅名篇历史导读", sub, paper)
# 红色印章
sx, sy = 1170, 110
d.rectangle([sx, sy, sx+170, sy+170], fill=red)
seal = ImageFont.truetype(f"{F}/NotoSansCJKsc-Bold.otf", 64)
d.text((sx+21, sy+12), "导", font=seal, fill=paper); d.text((sx+21+64, sy+12), "读", font=seal, fill=paper)
d.text((sx+21, sy+86), "鲁", font=seal, fill=paper); d.text((sx+21+64, sy+86), "迅", font=seal, fill=paper)
ctext(1990, "希望本无所谓有，无所谓无。", small, dim)
ctext(2060, "这正如地上的路；其实地上本没有路，", small, dim)
ctext(2130, "走的人多了，也便成了路。", small, dim)
ctext(2260, "从清末到五四 · 从《呐喊》到《野草》", small, (170, 160, 140))
# 印章挪到右上避免与文字重叠
img.save(sys.argv[2], quality=92)
