from PIL import Image, ImageDraw, ImageFont
import random, sys
FONT = "/usr/share/fonts/opentype/noto/NotoSansCJK-%s.ttc"
def f(w, size): return ImageFont.truetype(FONT % w, size, index=2)  # index 2 = SC
W, H = 1600, 2400
random.seed(3)
bg, ink, red, dim = (238, 232, 220), (30, 28, 26), (160, 36, 28), (110, 104, 96)
img = Image.new("RGB", (W, H), bg); d = ImageDraw.Draw(img)
for _ in range(50000):
    x, y = random.randrange(W), random.randrange(H); c = random.randint(226, 236)
    d.point((x, y), (c, c-4, c-12))
# 一条红色竖线与若干分岔的路径：象征“在不确定中下判断”
d.rectangle([180, 260, 196, 2140], fill=red)
def cx(s, font): return (W - d.textlength(s, font=font)) / 2
t = f("Bold", 300); d.text((cx("毛泽东", t), 420), "毛泽东", font=t, fill=ink)
s = f("Bold", 96); d.text((cx("在不确定中下判断", s), 860), "在不确定中下判断", font=s, fill=red)
# 分岔路线
y0 = 1250
for k, (dx, col) in enumerate([(-360, dim), (0, ink), (360, dim)]):
    d.line([(800, y0), (800, y0+220)], fill=ink, width=10)
    d.line([(800, y0+220), (800+dx, y0+620)], fill=col, width=10 if dx == 0 else 6)
d.ellipse([780, y0-20, 820, y0+20], fill=red)
sm = f("Regular", 52)
for i, line in enumerate(["他的一生与他的文章", "1893 — 1976"]):
    d.text((cx(line, sm), 2020 + i*90), line, font=sm, fill=dim)
img.save(sys.argv[1], quality=92)
