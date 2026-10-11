# -*- coding: utf-8 -*-
"""清晨果园 · ORCHARD — 480x60 像素横幅(细化版)
保持原尺寸 480x60 与原构图(晨空/远山/栅栏/苹果树/红顶小屋),细化细节。
运行: python _draw_banner.py  →  assets/banner/orchard-480x60.png
"""
import math
from PIL import Image

W, H = 480, 60
im = Image.new("RGB", (W, H))
px = im.load()

# ---------- 基础调色 ----------
SKY_STOPS = [          # 晨空:上深下暖,近地平线泛晨光
    (0,  (112, 140, 163)),
    (6,  (126, 153, 173)),
    (11, (140, 166, 182)),
    (14, (167, 182, 184)),
    (17, (205, 205, 192)),
    (20, (234, 224, 199)),
]
RIDGE      = (179, 195, 153)   # 最远山脊(带雾感)
RIDGE_TOP  = (193, 204, 160)
HILL       = (163, 190, 147)   # 主山丘
HILL_TOP   = (180, 204, 140)   # 山脊受光边
HILL_ROW   = (138, 169, 126)   # 果园种植行斜纹
FENCE      = (230, 221, 190)   # 白栅栏
FENCE_DK   = (199, 190, 163)
MIDBAND    = (126, 156, 124)   # 山脚过渡带
MIDBAND_D  = (117, 146, 115)
FIELD      = (156, 184, 120)   # 主草地
FIELD_LT   = (180, 204, 140)
FIELD_DK   = (127, 160, 101)
FIELD_SUN  = (167, 192, 128)   # 阳光亮斑
TREE_DK    = (81, 117, 80)     # 树冠暗部
TREE       = (98, 136, 91)     # 树冠基色
TREE_LT    = (118, 155, 102)   # 受光面
TREE_HI    = (137, 170, 113)   # 高光点
TRUNK      = (122, 86, 56)
TRUNK_DK   = (94, 66, 44)
APPLE      = (217, 100, 89)
APPLE_LT   = (240, 150, 130)
WALL       = (241, 228, 199)
WALL_SH    = (228, 213, 180)   # 墙面阴影/檐下影
WALL_TRIM  = (216, 200, 164)
WALL_SIDING= (234, 221, 190)
ROOF       = (194, 91, 84)
ROOF_DK    = (150, 66, 61)
ROOF_ROW   = (184, 82, 76)
ROOF_HI    = (217, 100, 89)
DOOR       = (138, 115, 80)
DOOR_DK    = (122, 86, 56)
DOOR_DK2   = (94, 66, 44)
WINDOW     = (247, 222, 158)   # 亮着的暖黄窗
WINDOW_HI  = (252, 240, 196)
WIN_FRAME  = (196, 178, 140)
STEP       = (216, 200, 164)
STEP_DK    = (196, 178, 140)
PATH       = (196, 178, 140)
STONE      = (176, 174, 158)
STONE_LT   = (203, 201, 190)
CLOUD      = (243, 239, 227)
CLOUD_SH   = (222, 219, 204)
SMOKE      = (240, 236, 224)
SMOKE_SH   = (219, 216, 203)
BIRD       = (86, 104, 118)
FLOWER_R   = (217, 100, 89)
FLOWER_Y   = (247, 222, 158)
FLOWER_W   = (243, 239, 227)
STEM       = (81, 117, 80)

def P(x, y, c):
    if 0 <= x < W and 0 <= y < H:
        px[x, y] = c

def rect(x0, y0, x1, y1, c):
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            P(x, y, c)

def hline(x0, x1, y, c):
    for x in range(x0, x1 + 1):
        P(x, y, c)

def vline(x, y0, y1, c):
    for y in range(y0, y1 + 1):
        P(x, y, c)

def ell(cx, cy, rx, ry, c, tol=1.12):
    for y in range(cy - ry, cy + ry + 1):
        for x in range(cx - rx, cx + rx + 1):
            if ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= tol:
                P(x, y, c)

def bump(x, c, w):
    d = (x - c) / w
    return max(0.0, 1.0 - d * d)

def hill_y(x):   # 主山丘轮廓
    y = 19
    y -= int(4 * bump(x, 250, 150))
    y -= int(3 * bump(x, 80, 70))
    y -= int(3 * bump(x, 420, 90))
    return y

def ridge_y(x):  # 最远山脊轮廓
    y = 16
    y -= int(3 * bump(x, 140, 110))
    y -= int(4 * bump(x, 390, 130))
    y -= int(2 * bump(x, 30, 60))
    return y

def lerp(a, b, t):
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))

# ================= 1. 天空 =================
for y in range(0, 21):
    for i in range(len(SKY_STOPS) - 1):
        y0, c0 = SKY_STOPS[i]
        y1, c1 = SKY_STOPS[i + 1]
        if y0 <= y <= y1:
            t = (y - y0) / (y1 - y0)
            c = lerp(c0, c1, t)
            hline(0, W - 1, y, c)
            break
rect(0, 20, W - 1, 20, SKY_STOPS[-1][1])  # 兜底

SUN = (72, 12)
for y in range(H):
    for x in range(W):
        if y >= ridge_y(x) + 1:
            continue
        d2 = (x - SUN[0]) ** 2 + (y - SUN[1]) ** 2
        if d2 <= 16:                      # 日轮
            P(x, y, (250, 232, 178))
        elif d2 <= 25:                    # 内晕
            P(x, y, (250, 238, 196))
        elif d2 <= 36 and (x + y) % 2 == 0:
            P(x, y, (232, 224, 200))

# 飞鸟
def bird(x, y, big=False):
    if big:
        for dx, dy in ((0, 2), (1, 1), (2, 0), (3, 1), (4, 2)):
            P(x + dx, y + dy, BIRD)
    else:
        for dx, dy in ((0, 1), (1, 0), (2, 1)):
            P(x + dx, y + dy, BIRD)
bird(150, 5); bird(162, 8); bird(340, 7, True); bird(100, 5)

# ================= 2. 云 =================
def cloud(x0, y0, w):
    ins = max(2, w // 5)
    hline(x0 + ins, x0 + w - ins, y0, CLOUD)
    P(x0 + ins + 2, y0 - 1, CLOUD)
    P(x0 + w - ins - 3, y0 - 1, CLOUD)
    hline(x0, x0 + w, y0 + 1, CLOUD)
    hline(x0 + 1, x0 + w - 1, y0 + 2, CLOUD_SH)
    P(x0, y0 + 1, CLOUD_SH); P(x0 + w, y0 + 1, CLOUD_SH)
    hline(x0 + 3, x0 + w - 3, y0 + 3, CLOUD_SH)
    for x in range(x0 + 5, x0 + w - 4, 3):
        P(x, y0 + 3, (216, 213, 197) if (x // 3) % 2 else CLOUD_SH)
cloud(114, 3, 44)
cloud(286, 2, 52)
cloud(392, 8, 30)
cloud(180, 7, 12)
cloud(30, 3, 16)

# ================= 3. 远山 / 主山丘 =================
for x in range(W):
    yt = ridge_y(x)
    for y in range(yt, hill_y(x)):
        c = RIDGE_TOP if y == yt else RIDGE
        P(x, y, c)
for x in range(W):
    yt = hill_y(x)
    for y in range(yt, 29):
        c = HILL_TOP if y == yt else HILL
        P(x, y, c)
    for y in range(yt + 2, 28):        # 果园种植行:斜向虚线
        if (x - y) % 8 == 0:
            P(x, y, HILL_ROW)

# 白栅栏(横贯,房子后面)
for x in range(2, W, 7):
    vline(x, 16, 20, FENCE)
    P(x, 16, (243, 239, 227))
hline(0, W - 1, 17, (228, 220, 192))
hline(0, W - 1, 18, FENCE_DK)

# ================= 4. 山脚过渡带 =================
rect(0, 28, W - 1, 33, MIDBAND)
hline(0, W - 1, 28, (134, 164, 131))
for y in range(29, 34):
    for x in range(W):
        if (x * 2654435761 + y * 40503) % 89 < 5:
            P(x, y, MIDBAND_D)

# 中景一排小苹果树(栅栏前)
def small_tree(cx, gy, fruit=True):
    ell(cx + 1, gy - 5, 3, 2, TREE_DK)
    ell(cx, gy - 6, 3, 2, TREE)
    ell(cx - 1, gy - 7, 2, 1, TREE_LT)
    P(cx - 2, gy - 7, TREE_HI)
    vline(cx, gy - 4, gy - 1, TRUNK)
    P(cx, gy - 1, TRUNK_DK)
    hline(cx - 2, cx + 2, gy, FIELD_DK)
    if fruit:
        P(cx - 1, gy - 6, APPLE); P(cx + 1, gy - 5, APPLE)
for cx in (18, 54, 90, 126, 162, 178, 284, 318, 354, 390, 426, 462):
    small_tree(cx, 30, fruit=(cx % 3 != 0))

# ================= 5. 草地 =================
rect(0, 34, W - 1, H - 1, FIELD)
ell(110, 44, 62, 8, FIELD_SUN)   # 阳光亮斑
ell(356, 40, 52, 6, FIELD_SUN)
ell(238, 57, 88, 5, (146, 172, 112))  # 近景暗斑
for y in range(34, H):
    for x in range(W):
        h = (x * 2654435761 + y * 40503) % 97
        if h < 4:
            P(x, y, FIELD_DK)
        elif h > 93:
            P(x, y, FIELD_LT)

# ================= 6. 小屋 =================
def house():
    # 地面阴影(晨光从左来,影向右)
    rect(258, 55, 265, 57, FIELD_DK)
    hline(202, 262, 56, FIELD_DK)
    # 烟囱(先画,屋顶盖住底部)
    rect(210, 17, 215, 29, DOOR_DK)
    vline(215, 18, 28, DOOR_DK2)
    rect(209, 16, 216, 17, DOOR)
    for y in (20, 24):
        P(211, y, DOOR); P(213, y + 1, DOOR)
    # 炊烟(向左飘)
    smoke = [(212, 13, 2), (209, 10, 3), (205, 7, 2), (208, 4, 1), (203, 2, 1)]
    for sx, sy, r in smoke:
        for dx in range(-r, r + 1):
            c = SMOKE if dx <= 0 else SMOKE_SH
            P(sx + dx, sy, c)
        P(sx, sy + 1, SMOKE_SH)
    # 屋顶(梯形,出檐)
    for i, y in enumerate(range(24, 34)):
        x0 = 220 - 2 * i if 220 - 2 * i >= 201 else 201
        x1 = 242 + 2 * i if 242 + 2 * i <= 261 else 261
        if y == 24:
            hline(x0, x1, y, ROOF_HI)
        else:
            hline(x0, x1, y, ROOF)
            if y % 2 == 0:                     # 瓦行
                for x in range(x0, x1 + 1):
                    if x % 4 < 2:
                        P(x, y, ROOF_ROW)
            if y <= 27:                        # 左坡受光
                for x in range(x0, min(x1, 228) + 1):
                    if x % 4 < 2:
                        P(x, y, (205, 102, 92))
    hline(201, 261, 33, ROOF_DK)               # 檐口
    hline(204, 258, 34, WALL_SH)               # 檐下影
    # 墙体
    rect(204, 35, 258, 55, WALL)
    vline(256, 35, 55, WALL_SH); vline(257, 35, 55, WALL_SH); vline(258, 35, 55, WALL_SH)
    for y in range(37, 53, 3):                 # 壁板横缝
        hline(205, 255, y, WALL_SIDING)
    rect(204, 53, 258, 54, WALL_TRIM)          # 勒脚
    hline(204, 258, 55, STEP_DK)
    # 左窗
    def window(x0):
        rect(x0 - 1, 38, x0 + 8, 46, WALL_TRIM)
        rect(x0, 39, x0 + 7, 45, WINDOW)
        vline(x0 + 3, 39, 45, WIN_FRAME); vline(x0 + 4, 39, 45, WIN_FRAME)
        hline(x0, x0 + 7, 42, WIN_FRAME)
        P(x0 + 1, 40, WINDOW_HI); P(x0 + 2, 40, WINDOW_HI); P(x0 + 1, 41, WINDOW_HI)
        hline(x0 - 2, x0 + 9, 47, WALL_TRIM)   # 窗台
        hline(x0 - 1, x0 + 8, 48, DOOR)        # 花箱
        hline(x0 - 1, x0 + 8, 49, DOOR_DK)
        for i, fx in enumerate(range(x0, x0 + 8, 2)):
            P(fx, 47, (FLOWER_R, FLOWER_Y, FLOWER_R, FLOWER_W)[i % 4])
            P(fx + 1, 47, TREE)
    window(212)
    window(244)
    # 门
    rect(230, 42, 239, 55, DOOR_DK)
    rect(231, 43, 238, 55, DOOR)
    vline(234, 43, 55, DOOR_DK)
    vline(238, 43, 55, DOOR_DK)
    P(236, 49, FLOWER_Y)                        # 门把手
    rect(229, 56, 240, 56, STEP)
    rect(228, 57, 241, 57, STEP_DK)
house()

# 门前小径
hline(227, 243, 57, PATH)
hline(223, 247, 58, PATH)
hline(219, 251, 59, PATH)
for x, y in ((219, 57), (245, 58), (222, 59), (249, 59)):
    P(x, y, FIELD_DK)
for x, y in ((231, 58), (240, 59), (226, 59), (236, 58)):
    P(x, y, STONE)
    P(x + 1, y, STONE_LT) if x + 1 <= 251 else None

# ================= 7. 果树 =================
def tree(cx, gy, rx, ry, fruit=True):
    ell(cx + rx + 1, gy, rx, 1, FIELD_DK)           # 影子偏右
    rect(cx - 1, gy - 4, cx, gy - 1, TRUNK)
    vline(cx, gy - 4, gy - 1, TRUNK_DK)
    P(cx - 2, gy - 1, TRUNK); P(cx + 1, gy - 1, TRUNK_DK)
    cy = gy - 3 - ry
    ell(cx + 1, cy + 1, rx, ry, TREE_DK)
    ell(cx, cy, rx, ry, TREE)
    ell(cx - 1, cy - 1, rx - 2, ry - 1, TREE_LT)
    P(cx - rx + 2, cy - ry + 2, TREE_HI)
    P(cx - rx + 4, cy - ry + 1, TREE_HI)
    P(cx - rx + 3, cy - ry + 3, TREE_HI)
    if fruit:
        spots = [(-4, -2), (-1, -3), (2, -2), (4, -1), (-2, 1), (2, 2)]
        for dx, dy in spots:
            if (dx / rx) ** 2 + (dy / ry) ** 2 < 0.62:
                ax, ay = cx + dx, cy + dy
                P(ax, ay, APPLE)
                if (dx - 1) / rx > -1: P(ax - 1, ay, APPLE_LT)
    hline(cx - rx - 1, cx + rx + 2, gy + 1, FIELD_DK)

# 后排(远,小)
for cx, gy, rx, ry in ((30, 40, 3, 2), (76, 41, 5, 4), (132, 40, 3, 2),
                       (178, 41, 5, 4), (290, 40, 5, 4), (340, 41, 3, 2),
                       (390, 40, 5, 4), (442, 41, 3, 2)):
    tree(cx, gy, rx, ry)
# 前排(近,大)
for cx, gy, rx, ry in ((8, 56, 3, 2), (56, 53, 5, 4), (110, 54, 7, 6),
                       (160, 53, 5, 4), (302, 54, 7, 6), (358, 53, 5, 4),
                       (420, 54, 7, 6), (470, 55, 4, 3)):
    tree(cx, gy, rx, ry)

# 灌木
for cx, cy, rx, ry in ((185, 56, 4, 2), (262, 37, 3, 2), (462, 44, 4, 2)):
    ell(cx + 1, cy + 1, rx, ry, TREE_DK)
    ell(cx, cy, rx, ry, TREE)
    ell(cx - 1, cy - 1, rx - 2, ry - 1, TREE_LT)
    P(cx - 1, cy - 2, TREE_HI)

# 苹果木箱(屋右)
crate_x, crate_y = 268, 50
for dx, dy in ((3, 0), (8, 0), (5, -1)):        # 冒尖的苹果
    P(crate_x + dx, crate_y - 1 + dy, APPLE)
    P(crate_x + dx - 1, crate_y - 1 + dy, APPLE_LT)
rect(crate_x, crate_y, crate_x + 11, 56, DOOR)
hline(crate_x, crate_x + 11, crate_y, STEP_DK)
hline(crate_x, crate_x + 11, crate_y + 2, DOOR_DK)
hline(crate_x, crate_x + 11, crate_y + 4, DOOR_DK)
vline(crate_x, crate_y, 56, DOOR_DK); vline(crate_x + 11, crate_y, 56, DOOR_DK)
hline(crate_x - 1, crate_x + 13, 57, FIELD_DK)
P(crate_x + 12, crate_y - 1, TREE)              # 叶子

# 木牌(屋左,指向果园)
rect(188, 45, 199, 50, DOOR)
rect(189, 46, 198, 49, DOOR_DK)
hline(190, 197, 47, STEP_DK)
hline(190, 195, 48, STEP_DK)
rect(193, 51, 194, 56, TRUNK)
vline(194, 51, 56, TRUNK_DK)
hline(191, 197, 57, FIELD_DK)

# ================= 8. 前景花草 =================
flowers = [(14, 55, 'r'), (17, 56, 'y'), (20, 55, 'w'), (90, 57, 'r'), (94, 56, 'y'),
           (150, 56, 'w'), (153, 55, 'r'), (205, 58, 'y'), (214, 57, 'r'),
           (212, 58, 'y'), (258, 57, 'w'), (300, 57, 'y'), (305, 58, 'r'),
           (390, 56, 'r'), (394, 57, 'w'), (445, 57, 'y'), (470, 56, 'r')]
cmap = {'r': FLOWER_R, 'y': FLOWER_Y, 'w': FLOWER_W}
for fx, fy, kind in flowers:
    P(fx, fy, cmap[kind])
    if fy < 58:
        P(fx, fy + 1, STEM)
tufts = [22, 48, 85, 118, 146, 190, 262, 286, 318, 352, 376, 404, 432, 458, 68, 133, 246, 336]
for i, tx in enumerate(tufts):
    ty = 42 + (i * 7) % 15
    if 199 <= tx <= 283 and ty >= 34:
        continue
    P(tx, ty, (108, 142, 92)); P(tx + 1, ty - 1, (108, 142, 92)); P(tx + 2, ty, (108, 142, 92))

im.save("assets/banner/orchard-480x60.png")
print("saved", im.size)
