import pygame.font
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 700))

white = (255, 255, 255)
black = (0, 0, 0)
gray = (125, 125, 125)
light_blue = (64, 128, 255)
green = (0, 200, 64)
yellow = (255, 255, 0)
blue = (50, 170, 205)
pink = (255, 50, 255)
red = (255, 0, 0)
blue_green = (0, 255, 100)
maroon = (115, 0, 0)
lime = (230, 255, 101)
purple = (240, 0, 255)
magenta = (255, 0, 230)
brown = (100, 40, 0)
forest_green = (5, 100, 5)
navy_blue = (0, 0, 100)
rust = (210, 150, 75)
light_yellow = (255, 200, 0)
highlighter = (255, 255, 100)
sky_blue = (0, 255, 255)
light_gray = (200, 200, 200)
dark_gray = (50, 50, 50)
tan = (230, 220, 170)
coffee_brown = (200, 190, 140)
moon_glow = (235, 245, 255)
pi = 3.14159


def sky():
    rect(screen, sky_blue, (0, 0, 600, 250))


def grass():
    rect(screen, blue_green, (0, 250, 600, 450))


def sun():
    circle(screen, yellow, (550, 60), 120)


def head():
    ellipse(screen, white, (430, 362, 61, 115))
    circle(screen, white, (472, 352), 37)
    circle(screen, white, (517, 364), 19)
    polygon(screen, white, [(485, 316), (523, 346), (517, 363), (485, 316)])


def body():
    circle(screen, white, (450, 473), 50)
    rect(screen, white, (332, 434, 118, 77))
    circle(screen, white, (345, 478), 44)


def leg():
    ellipse(screen, white, (308, 481, 46, 86))
    circle(screen, white, (323, 568), 16)
    rect(screen, white, (309, 570, 30, 44))
    rect(screen, light_yellow, (308, 592, 33, 24))
    ellipse(screen, white, (441, 484, 40, 87))
    circle(screen, white, (467, 571), 15)
    rect(screen, white, (453, 578, 28, 37))
    rect(screen, light_yellow, (451, 591, 32, 25))


def eye():
    circle(screen, magenta, (486, 341), 13)
    circle(screen, black, (487, 341), 7)
    circle(screen, white, (485, 338), 2)


def mane():
    ellipse(screen, light_yellow, (417, 298, 47, 25))
    ellipse(screen, light_yellow, (405, 327, 35, 107))
    arc(screen, yellow, (429, 319, 20, 70), 3 * pi / 10, 16.5 * pi / 10, 7)
    arc(screen, pink, (404, 330, 25, 70), pi / 2, 125 * pi / 100, 8)
    arc(screen, magenta, (404, 335, 20, 73), pi / 2, 13.5 * pi / 10, 8)
    arc(screen, rust, (384, 357, 30, 59), -6*pi/10, 1*pi/10, 7)
    arc(screen, blue, (433, 366, 35, 59), 1.1 * pi, 1.58 * pi, 8)
    arc(screen, pink, (409, 380, 30, 59), -4. * pi / 10, 2 * pi / 10, 6)
    arc(screen, light_yellow, (437, 321, 20, 50), 4.5*pi/10, 14*pi/10, 6)
    arc(screen, yellow, (389, 370, 30, 64), -7 * pi / 10, 2 * pi / 10, 10)
    arc(screen, red, (401, 375, 30, 54), -7 * pi / 10, 2 * pi / 10, 9)
    arc(screen, red, (418, 310, 35, 110), 3 * pi / 8, 12 * pi / 10, 10)
    arc(screen, pink, (411, 301, 46, 77), 5.6 * pi / 10, 1.13 * pi, 9)
    arc(screen, pink, (440, 296, 56, 32), 0.25 * pi, 1.2 * pi, 7)
    arc(screen, light_yellow, (448, 310, 56, 26), 0.35 * pi, 1 * pi, 7)
    arc(screen, red, (448, 301, 50, 26), 0.35 * pi, 0.9 * pi, 8)
    arc(screen, pink, (480, 284, 40, 26), 1.2 * pi, 1.91 * pi, 4)
    arc(screen, yellow, (480, 289, 50, 26), 1.2 * pi, 1.81 * pi, 6)
    arc(screen, rust, (482, 297, 60, 26), 1.0 * pi, 1.5 * pi, 6)


def ear():
    polygon(screen, (20, 50, 70), [(459, 321), (438, 304), (436, 308), (445, 338), (459, 321)])
    polygon(screen, (255, 255, 200), [(459, 323), (439, 306), (437, 308), (446, 337), (459, 323)])


def horn():
    polygon(screen, (50, 50, 0), [(463, 314), (485, 256), (484, 318), (463, 314)])
    polygon(screen, lime, [(464, 316), (484, 263), (483, 318), (464, 316)])


def tail():
    ellipse(screen, light_yellow, (280, 443, 40, 25))
    ellipse(screen, blue, (265, 466, 35, 107))
    arc(screen, yellow, (289, 464, 20, 70), 3 * pi / 10, 16.5 * pi / 10, 7)
    arc(screen, pink, (264, 475, 25, 70), 0.5 * pi, 125 * pi / 100, 7)
    arc(screen, magenta, (264, 480, 20, 73), 0.1 * pi, 13.5 * pi / 10, 8)
    arc(screen, rust, (244, 502, 30, 59), -6*pi/10, 1*pi/10, 7)
    arc(screen, blue, (293, 511, 35, 59), 1.1 * pi, 1.58 * pi, 8)
    arc(screen, pink, (269, 525, 30, 59), -4. * pi / 10, 2 * pi / 10, 6)
    arc(screen, yellow, (249, 515, 30, 64), -7 * pi / 10, 2 * pi / 10, 10)
    arc(screen, red, (261, 520, 30, 54), -7 * pi / 10, 4 * pi / 10, 9)
    arc(screen, red, (268, 455, 35, 110), 3 * pi / 8, 12 * pi / 10, 10)
    arc(screen, light_yellow, (276, 456, 38, 134), 0.6 * pi, 1.1 * pi, 9)
    arc(screen, pink, (261, 446, 46, 77), 0.4 * pi, 1.13 * pi, 9)


def tree():
    ellipse(screen, forest_green, (70, 410, 100, 70))
    polygon(screen, coffee_brown, [(80, 599), (130, 594), (105, 410), (92, 410)])
    ellipse(screen, forest_green, (3, 380, 120, 80))
    ellipse(screen, forest_green, (30, 320, 180, 120))
    ellipse(screen, forest_green, (10, 280, 100, 70))
    ellipse(screen, forest_green, (40, 240, 150, 100))
    ellipse(screen, forest_green, (142, 276, 67, 44))
    ellipse(screen, forest_green, (59, 140, 98, 135))
    ellipse(screen, forest_green, (100, 190, 80, 105))
    ellipse(screen, forest_green, (25, 175, 70, 140))
    ellipse(screen, forest_green, (29, 160, 50, 40))
    ellipse(screen, forest_green, (97, 120, 80, 60))
    ellipse(screen, forest_green, (70, 90, 70, 100))
    circle(screen, red, (69, 200), 7)
    circle(screen, red, (139, 350), 7)
    circle(screen, red, (159, 240), 7)


sky()
grass()
sun()
head()
body()
leg()
eye()
ear()
mane()
horn()
tail()
tree()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
