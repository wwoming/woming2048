"""==========zhuming=========="""
import pygame
from color import Color

window_width = 400
window_height = 600
length = 370

x = (window_width - length) / 2
y = window_height - length - (window_width - length) / 2

l_len = 80
gap_len = 10
gap_x = l_len + gap_len

rect_list = [[(x+gap_len, y+gap_len),
              (x+gap_len+gap_x*1, y+gap_len),
              (x+gap_len+gap_x*2, y+gap_len),
              (x+gap_len+gap_x*3, y+gap_len)],
             [(x+gap_len, y+gap_len+gap_x*1),
              (x+gap_len+gap_x*1, y+gap_len+gap_x*1),
              (x+gap_len+gap_x*2, y+gap_len+gap_x*1),
              (x+gap_len+gap_x*3, y+gap_len+gap_x*1)],
             [(x+gap_len, y+gap_len+gap_x*2),
              (x+gap_len+gap_x*1, y+gap_len+gap_x*2),
              (x+gap_len+gap_x*2, y+gap_len+gap_x*2),
              (x+gap_len+gap_x*3, y+gap_len+gap_x*2)],
             [(x+gap_len, y+gap_len+gap_x*3),
              (x+gap_len+gap_x*1, y+gap_len+gap_x*3),
              (x+gap_len+gap_x*2, y+gap_len+gap_x*3),
              (x+gap_len+gap_x*3, y+gap_len+gap_x*3)]
             ]


# 将不为0的数字添加到方块中, 当数字是4位数的时候，要把字体变小，不然就超出方块了
def add_num_in_rect(window, value, i, j):
    if value < 1024:
        font = pygame.font.Font('files/font2.ttf', 40)
        text = font.render(str(value), True, Color.black)
        a, b = rect_list[i][j]
        x, y = text.get_size()
        x = (80-x)/2 + a
        y = (80-y)/2 + b
        window.blit(text, (x, y))
    else:
        font = pygame.font.Font('files/font2.ttf', 20)
        text = font.render(str(value), True, Color.black)
        a, b = rect_list[i][j]
        x, y = text.get_size()
        x = (80 - x) / 2 + a
        y = (80 - y) / 2 + b
        window.blit(text, (x, y))


# 将数值为0的方块变为基础色
def return_base_color(window, i, j):
    pygame.draw.rect(window, Color.base_square, (*rect_list[i][j], 80, 80))


# 将数值不为0的方块变为相应的颜色
def change_color(window, num, i, j):
    if num == 2:
        pygame.draw.rect(window, Color.two, (*rect_list[i][j], 80, 80))
    elif num == 4:
        pygame.draw.rect(window, Color.four, (*rect_list[i][j], 80, 80))
    elif num == 8:
        pygame.draw.rect(window, Color.eight, (*rect_list[i][j], 80, 80))
    elif num == 16:
        pygame.draw.rect(window, Color.sixteen, (*rect_list[i][j], 80, 80))
    elif num == 32:
        pygame.draw.rect(window, Color.thirty_two, (*rect_list[i][j], 80, 80))
    elif num == 64:
        pygame.draw.rect(window, Color.sixty_four, (*rect_list[i][j], 80, 80))
    elif num == 128:
        pygame.draw.rect(window, Color.one_two_eight, (*rect_list[i][j], 80, 80))
    elif num == 256:
        pygame.draw.rect(window, Color.two_five_six, (*rect_list[i][j], 80, 80))
    elif num == 512:
        pygame.draw.rect(window, Color.five_one_two, (*rect_list[i][j], 80, 80))
    elif num == 1024:
        pygame.draw.rect(window, Color.ten_two_four, (*rect_list[i][j], 80, 80))
    elif num == 2048:
        pygame.draw.rect(window, Color.twenty_four_eight, (*rect_list[i][j], 80, 80))


# 设计显示2048的框框，得分的框框，最高分的框框
def box(window):
    # 2048的框框
    pygame.draw.rect(window, Color.game, (15, 40, 110, 110))
    font = pygame.font.Font('files/font2.ttf', 40)
    text = font.render('2048', True, Color.white)
    a, b = 15, 40
    x, y = text.get_size()
    x = (110 - x) / 2 + a
    y = (110 - y) / 2 + b
    window.blit(text, (x, y))
    # 重新开始的框框
    pygame.draw.rect(window, Color.score, (145, 120, 240, 30))
    font = pygame.font.Font('files/font2.ttf', 15)
    text = font.render('点我就给你一个重新来过的机会', True, Color.twenty_four_eight)
    a, b = 145, 120
    x, y = text.get_size()
    x = (240 - x) / 2 + a
    y = (30 - y) / 2 + b
    window.blit(text, (x, y))


def score_box(window):
    # 得分的框框
    pygame.draw.rect(window, Color.score, (145, 40, 110, 70))
    font = pygame.font.Font('files/font2.ttf', 20)
    text1 = font.render('得分', True, Color.white)
    a, b = 145, 40
    x, y = text1.get_size()
    x = (110 - x) / 2 + a
    y = (70 - y) / 4 + b
    window.blit(text1, (x, y))


def best_score_box(window):
    # 最高分的框框
    pygame.draw.rect(window, Color.score, (275, 40, 110, 70))
    font = pygame.font.Font('files/font2.ttf', 20)
    text = font.render('最高分', True, Color.white)
    a, b = 275, 40
    x, y = text.get_size()
    x = (110 - x) / 2 + a
    y = (70 - y) / 4 + b
    window.blit(text, (x, y))


# 更新分数
def update_score(window, value):
    pygame.draw.rect(window, Color.score, (145, 70, 110, 30))
    font = pygame.font.Font('files/font2.ttf', 20)
    text2 = font.render(str(value), True, Color.white)
    a, b = 145, 70
    x, y = text2.get_size()
    x = (110 - x) / 2 + a
    y = (30 - y) / 2 + b
    window.blit(text2, (x, y))


# 更新最高分
def update_best_score(window, value):
    pygame.draw.rect(window, Color.score, (275, 70, 110, 30))
    font = pygame.font.Font('files/font2.ttf', 20)
    text = font.render(str(value), True, Color.white)
    a, b = 275, 70
    x, y = text.get_size()
    x = (110 - x) / 2 + a
    y = (30 - y) / 2 + b
    window.blit(text, (x, y))


# GAMEOVER
def gameover(window):
    font = pygame.font.Font('files/font2.ttf', 50)
    text = font.render('GAMEOVER!', True, (2, 168, 155))
    x, y = text.get_size()
    x = (400 - x) / 2
    y = (600 - y) / 2
    window.blit(text, (x, y))


# 游戏胜利
def victory(window):
    pygame.draw.rect(window, (2, 168, 155), (15, 40, 110, 110))
    font = pygame.font.Font('files/font2.ttf', 30)
    text = font.render('你赢啦!', True, Color.white)
    a, b = 15, 40
    x, y = text.get_size()
    x = (110 - x) / 2 + a
    y = (110 - y) / 2 + b
    window.blit(text, (x, y))

