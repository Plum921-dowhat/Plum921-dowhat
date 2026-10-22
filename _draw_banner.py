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
bird(150, 5); bird(162, 8); bird(340, 7, True); bird(100, 5); bird(270, 4)
bird(227, 3); bird(236, 6)

# 热气球
def balloon(cx, cy):
    ell(cx, cy, 3, 4, ROOF)
    for dx, dy in ((-2, -2), (-2, -1), (-2, 0), (-1, -3)):
        P(cx + dx, cy + dy, ROOF_HI)
    for dx, dy in ((2, 0), (2, 1), (1, 2), (2, -1)):
        P(cx + dx, cy + dy, ROOF_DK)
    P(cx, cy + 4, ROOF_DK)
    P(cx - 1, cy + 5, DOOR_DK2); P(cx + 1, cy + 5, DOOR_DK2)   # 吊绳
    rect(cx - 1, cy + 6, cx + 1, cy + 7, DOOR)
    hline(cx - 1, cx + 1, cy + 7, DOOR_DK)
balloon(257, 5)

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
cloud(114, 2, 44)
cloud(286, 2, 52)
cloud(392, 8, 30)
cloud(180, 7, 12)
cloud(30, 3, 16)

# ================= 3. 远山 / 主山丘 =================
hline(348, 364, 12, (228, 224, 210))          
hline(352, 360, 13, (216, 212, 198))
hline(176, 186, 12, (226, 222, 208))          
hline(178, 184, 13, (216, 212, 198))
hline(216, 228, 14, (224, 220, 206))
for x in range(W):
    yt = ridge_y(x)
    for y in range(yt, hill_y(x)):
        c = RIDGE_TOP if y == yt else RIDGE
        P(x, y, c)

# 山脊远树(雾中剪影)
def ridge_tree(x):
    rt = ridge_y(x)
    P(x, rt - 2, (166, 182, 136))
    P(x - 1, rt - 1, (166, 182, 136))
    P(x, rt - 1, (166, 182, 136))
    P(x + 1, rt - 1, (166, 182, 136))
for x in (96, 167, 188, 240, 262, 286, 336, 372, 384, 410, 428):
    ridge_tree(x)

# 远景小村落(山脊上,带雾感)
def hamlet():
    # A:晨窗亮灯的小屋
    hline(117, 123, 9, (206, 146, 136))
    hline(114, 126, 10, (184, 126, 118))
    rect(115, 11, 125, 13, (210, 200, 174))
    vline(124, 11, 13, (190, 180, 156)); vline(125, 11, 13, (190, 180, 156))
    P(120, 13, (150, 140, 118))
    P(118, 12, WINDOW)
    vline(123, 7, 8, (160, 140, 120))
    P(122, 6, (200, 196, 184))
    # B:两层坡顶屋,烟囱冒烟
    vline(133, 8, 9, (160, 140, 120))
    P(132, 7, (200, 196, 184))
    hline(131, 143, 10, (196, 138, 128))
    hline(130, 144, 11, (176, 120, 112))
    rect(131, 12, 143, 14, (200, 190, 164))
    vline(142, 12, 14, (180, 170, 146)); vline(143, 12, 14, (180, 170, 146))
    P(134, 14, (150, 140, 118))
    P(138, 13, (222, 210, 182))
    # C:矮屋
    hline(147, 155, 11, (176, 134, 112))
    rect(147, 12, 155, 14, (206, 196, 170))
    P(151, 14, (150, 140, 118))
    P(148, 13, (222, 210, 182))
    # 小教堂(尖顶)
    P(159, 8, (150, 134, 128))
    P(159, 9, (150, 134, 128))
    hline(158, 160, 10, (150, 134, 128))
    rect(158, 11, 160, 14, (206, 196, 170))
    P(159, 14, (150, 140, 118))
hamlet()

# 远处谷仓与筒仓(山脊上)
def distant_barn():
    hline(306, 314, 10, (206, 146, 136))
    hline(303, 317, 11, (196, 138, 128))
    hline(303, 317, 12, (176, 120, 112))
    rect(305, 13, 315, 15, (200, 190, 164))
    vline(314, 13, 15, (180, 170, 146)); vline(315, 13, 15, (180, 170, 146))
    rect(309, 13, 311, 15, (150, 140, 118))
    rect(318, 9, 320, 15, (206, 196, 170))
    P(318, 8, (186, 176, 150)); P(319, 7, (186, 176, 150)); P(320, 8, (186, 176, 150))
    vline(320, 9, 15, (180, 170, 146))
distant_barn()

for x in range(W):
    yt = hill_y(x)
    for y in range(yt, 29):
        c = HILL_TOP if y == yt else HILL
        P(x, y, c)
    for y in range(yt + 2, 28):        # 果园种植行:斜向虚线
        if (x - y) % 8 == 0:
            P(x, y, HILL_ROW)

# 荷兰风车(栅栏外的田边)
def windmill(cx, gy):
    SPINE = (110, 92, 66)
    CLOTH_A, CLOTH_B = (216, 200, 164), (176, 158, 124)
    # 塔身(下宽上窄)
    rect(cx - 2, 9, cx + 2, 11, (203, 191, 159))
    rect(cx - 3, 12, cx + 3, 14, (203, 191, 159))
    rect(cx - 4, 15, cx + 4, gy, (203, 191, 159))
    for y in range(9, gy + 1):                      # 右侧背光
        w = 2 if y < 12 else (3 if y < 15 else 4)
        P(cx + w, y, (176, 164, 134))
    rect(cx - 3, 6, cx + 3, 8, (139, 118, 96))      # 顶帽
    hline(cx - 2, cx + 2, 5, (160, 138, 112))
    rect(cx - 1, 15, cx + 1, gy, (94, 66, 44))      # 门
    # 风叶:斜十字,带格栅布面
    for sx, sy in ((1, -1), (1, 1), (-1, -1), (-1, 1)):
        for i in range(1, 6):
            bx, by = cx + sx * i, 8 + sy * i
            c = CLOTH_A if i == 5 else SPINE        # 叶尖受光
            P(bx, by, c)
            if i < 5:
                P(bx, by - sy, CLOTH_A if i % 2 else CLOTH_B)
    P(cx, 8, WINDOW)                                # 轴心
windmill(449, 17)

# 白栅栏(横贯,房子后面)
for x in range(2, W, 7):
    vline(x, 16, 20, FENCE)
    P(x, 16, (243, 239, 227))
hline(0, W - 1, 17, (228, 220, 192))
hline(0, W - 1, 18, FENCE_DK)

# 远处麦田(栅栏外,晨光金黄)
def wheat_field():
    rect(348, 22, 402, 27, (214, 196, 130))
    for y in (23, 25, 27):
        for x in range(348, 403):
            if x % 3 < 2:
                P(x, y, (192, 172, 120))       # 麦垄
    hline(348, 402, 22, (226, 208, 148))       # 受光顶行
    for x, y in ((348, 22), (349, 23), (402, 22), (401, 23),
                 (348, 27), (402, 27), (360, 27), (390, 27)):
        P(x, y, HILL)                          # 边缘融入草地
wheat_field()

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
    small_tree(cx, 30, fruit=cx in (18, 90, 162, 178, 284, 354, 426))

# 山坡上的羊群(远处牧场)
def sheep(cx, cy):
    rect(cx - 1, cy, cx + 1, cy + 1, (238, 234, 222))
    P(cx - 2, cy, (228, 224, 210))
    P(cx + 2, cy - 1, (70, 70, 74))
    P(cx - 1, cy + 2, (120, 120, 124)); P(cx + 1, cy + 2, (120, 120, 124))
sheep(250, 24); sheep(263, 26); sheep(338, 23)

# ================= 5. 草地 =================
rect(0, 34, W - 1, H - 1, FIELD)
ell(110, 44, 62, 8, FIELD_SUN)   # 阳光亮斑
ell(356, 40, 52, 6, FIELD_SUN)
ell(238, 57, 88, 5, (146, 172, 112))  # 近景暗斑
for y in range(34, H):
    for x in range(W):
        h = (x * 2654435761 + y * 40503) % 97
        if h < 2 and y > 34:
            P(x, y - 1, FIELD_DK); P(x, y, FIELD_DK)   # 草叶
        elif h < 4:
            P(x, y, FIELD_DK)
        elif h > 93:
            P(x, y, FIELD_LT)
hline(0, W - 1, 59, (150, 178, 114))     # 近景压暗
ell(136, 47, 22, 2, (148, 174, 114))     # 云影
ell(312, 44, 24, 2, (148, 174, 114))

# 池塘(晨光下的水面)与芦苇
def pond():
    ell(330, 57, 8, 2, (146, 178, 188))
    hline(324, 336, 55, (178, 206, 212))
    for x, y in ((327, 56), (332, 57), (335, 56), (325, 58)):
        P(x, y, (222, 240, 240))
    for x, y in ((326, 59), (330, 58), (334, 59), (337, 58)):
        P(x, y, (128, 158, 170))
    for x in (322, 338):
        P(x, 56, FIELD_DK); P(x, 57, FIELD_DK)
    # 芦苇
    vline(340, 52, 56, STEM); P(340, 51, DOOR)
    vline(342, 53, 56, STEM); P(342, 52, DOOR)
    P(341, 56, STEM)
    # 绿头鸭
    P(326, 56, (222, 214, 190))
    hline(327, 329, 56, (238, 234, 222))
    P(330, 55, (238, 234, 222))
    P(331, 55, (247, 222, 158))
    P(330, 57, (178, 206, 212))
pond()

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
    for sx in (210, 221, 242, 253):             # 红木窗板
        vline(sx, 39, 45, ROOF)
        P(sx, 39, (217, 100, 89))
    vline(231, 21, 23, (94, 66, 44))            # 屋顶风向标
    hline(229, 233, 22, (94, 66, 44))
    P(232, 21, ROOF_HI); P(233, 21, ROOF_HI)    # 小旗
    # 门
    rect(230, 42, 239, 55, DOOR_DK)
    rect(231, 43, 238, 55, DOOR)
    vline(234, 43, 55, DOOR_DK)
    vline(238, 43, 55, DOOR_DK)
    P(236, 49, FLOWER_Y)                        # 门把手
    rect(229, 56, 240, 56, STEP)
    rect(228, 57, 241, 57, STEP_DK)
house()
P(237, 22, BIRD); P(238, 23, BIRD); P(239, 22, BIRD); P(240, 22, FLOWER_Y)  # 屋顶歇脚的小鸟

# 门前小径
hline(227, 243, 57, PATH)
hline(223, 247, 58, PATH)
hline(219, 251, 59, PATH)
for x, y in ((219, 57), (245, 58), (222, 59), (249, 59)):
    P(x, y, FIELD_DK)
for x, y in ((231, 58), (240, 59), (226, 59), (236, 58)):
    P(x, y, STONE)
    P(x + 1, y, STONE_LT) if x + 1 <= 251 else None

# 小狗(屋前晒太阳)
def dog(cx, cy):
    rect(cx, cy, cx + 3, cy + 2, (176, 138, 102))     # 身体
    rect(cx - 3, cy - 1, cx - 2, cy + 1, (182, 144, 108))  # 头
    P(cx - 3, cy - 1, (94, 66, 44))                   # 耳朵
    P(cx - 2, cy, (40, 34, 28))                       # 眼睛
    P(cx - 3, cy + 1, (140, 108, 78))                 # 嘴鼻
    P(cx + 4, cy - 1, (176, 138, 102))                # 尾巴
    P(cx + 4, cy - 2, (94, 66, 44))
    P(cx, cy + 3, (140, 108, 78)); P(cx + 3, cy + 3, (140, 108, 78))  # 腿
    hline(cx - 2, cx + 5, cy + 4, FIELD_DK)           # 影子
dog(248, 52)

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

# 稻草人(头顶乌鸦)
def scarecrow(cx, gy):
    hline(cx - 3, cx + 4, gy + 1, FIELD_DK)
    vline(cx, gy - 9, gy - 1, TRUNK_DK)             # 杆
    hline(cx - 4, cx + 4, gy - 6, TRUNK_DK)         # 横杆
    rect(cx - 1, gy - 6, cx + 1, gy - 2, (194, 91, 84))   # 红上衣
    P(cx, gy - 4, (150, 66, 61))                    # 补丁
    rect(cx - 1, gy - 11, cx + 1, gy - 9, (243, 239, 227))  # 头
    P(cx - 1, gy - 10, (74, 66, 58)); P(cx + 1, gy - 10, (74, 66, 58))
    hline(cx - 3, cx + 3, gy - 12, (138, 115, 80))  # 帽檐
    rect(cx - 1, gy - 14, cx + 1, gy - 13, (138, 115, 80))  # 帽顶
    P(cx + 4, gy - 7, (54, 62, 70))                 # 乌鸦
    P(cx + 5, gy - 8, (54, 62, 70))
    P(cx + 6, gy - 8, (247, 222, 158))              # 喙
scarecrow(66, 47)

# 前排(近,大)
for cx, gy, rx, ry in ((8, 56, 3, 2), (56, 53, 5, 4), (110, 54, 7, 6),
                       (160, 53, 5, 4), (302, 54, 7, 6), (358, 53, 5, 4),
                       (420, 54, 7, 6), (470, 55, 4, 3)):
    tree(cx, gy, rx, ry)

# 采果梯(靠在大树上)
def ladder(x0, gy):
    for t in range(9):
        y = gy - t
        x = x0 + round(t / 3)
        P(x, y, (196, 178, 140))
        P(x + 4, y, (176, 158, 124))
    for y in (gy - 2, gy - 4, gy - 6, gy - 8):
        x = x0 + round((gy - y) / 3)
        hline(x, x + 4, y, (196, 178, 140))
ladder(296, 53)
# 摘苹果的人(梯子顶端,刚摘下一个)
P(300, 40, (243, 239, 227))                     # 头
rect(299, 41, 301, 43, (122, 86, 56))           # 身子
P(302, 41, (122, 86, 56)); P(303, 40, (122, 86, 56))   # 伸向树冠的手臂
P(304, 39, APPLE)                               # 手里的苹果
P(299, 44, (94, 66, 44)); P(301, 44, (94, 66, 44))     # 腿

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

# 掉落的苹果(木箱旁)
for ax, ay in ((264, 58), (284, 57)):
    P(ax, ay, APPLE); P(ax - 1, ay, APPLE_LT)

# 啄食的母鸡(木箱旁)
P(284, 49, FLOWER_R)                            # 鸡冠
P(284, 50, (240, 234, 222))                     # 头
P(283, 50, (247, 222, 158))                     # 喙
rect(285, 51, 287, 52, (240, 234, 222))         # 身体
P(288, 51, (216, 200, 164))                     # 尾羽
P(285, 53, FIELD_DK); P(287, 53, FIELD_DK)      # 爪

# 小蘑菇(大树下)
for mx, my in ((42, 58), (122, 57), (256, 58)):
    hline(mx - 1, mx + 1, my, ROOF)
    P(mx - 1, my, APPLE_LT)
    P(mx, my + 1, (240, 234, 220))

# 干草捆(右前景)
def hay_bale(cx, cy):
    ell(cx, cy, 4, 3, (224, 199, 132))
    ell(cx, cy, 2, 1, (210, 186, 118))
    P(cx, cy, (198, 173, 104))
    P(cx - 2, cy - 2, (240, 220, 160)); P(cx - 1, cy - 2, (240, 220, 160))
    P(cx + 3, cy + 2, (198, 173, 104))
hay_bale(443, 55)
hay_bale(456, 57)
hline(440, 447, 58, FIELD_DK)
hline(453, 461, 59, FIELD_DK)

# ================= 8. 前景花草 =================
flowers = [(14, 55, 'r'), (17, 56, 'y'), (20, 55, 'w'), (35, 58, 'r'), (90, 57, 'r'), (92, 56, 'w'), (94, 56, 'y'),
           (150, 56, 'w'), (153, 55, 'r'), (155, 57, 'y'), (205, 58, 'y'), (214, 57, 'r'),
           (212, 58, 'y'), (256, 58, 'w'), (300, 57, 'y'), (305, 58, 'r'),
           (390, 56, 'r'), (392, 58, 'y'), (394, 57, 'w'), (424, 56, 'y'), (434, 58, 'w'), (470, 56, 'r')]
cmap = {'r': FLOWER_R, 'y': FLOWER_Y, 'w': FLOWER_W}
for fx, fy, kind in flowers:
    P(fx, fy, cmap[kind])
    if fy < 58:
        P(fx, fy + 1, STEM)
tufts = [22, 48, 85, 118, 146, 190, 262, 286, 318, 346, 376, 404, 432, 458, 68, 133, 246, 336,
         14, 105, 288, 408]
for i, tx in enumerate(tufts):
    ty = 42 + (i * 7) % 15
    if (199 <= tx <= 283 and ty >= 34) or (322 <= tx <= 342 and ty >= 53) or (438 <= tx <= 462 and ty >= 52):
        continue
    P(tx, ty, (108, 142, 92)); P(tx + 1, ty - 1, (108, 142, 92)); P(tx + 2, ty, (108, 142, 92))

im.save("assets/banner/orchard-480x60.png")
print("saved", im.size)
