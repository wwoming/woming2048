"""==========zhuming=========="""

import pygame

"""
a.游戏还能继续
1.格子不满的情况下，按方向键没有发生位移和数值变化
2.格子满了，但是还有可相加的数值，也就是至少有一对相邻的两个数是相同的情况

b.游戏结束
3.格子满了，但没有可相加的数值，就是gameover的情况
"""

"""
分数管理：
1.得分，每次置零
2.最高分，游戏结束的时候，判断当次游戏的最终得分和上次游戏最高得分，谁高保存谁
3.创建一个json文件保存分数

游戏重新开始：
设计一个按钮，点击重新开始
怎么实现重新开始呢？


"""


def init():
    # 初始化
    return game()


Q = 0
press = '按下按钮'
win = '赢了'
failure = '输了'
tie = '不输不赢'
restart = '重来'


def you_win():
    print(win)
    # 给出选择，判断重来还是退出
    if restart:
        return init()
    else:
        return


def you_failure():
    print(failure)
    # 给出选择，判断重来还是退出
    if restart:
        return init()
    else:
        return


def start_game():
    print('开始游戏')


def game():
    pygame.init()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 判断鼠标坐标，如果在给定范围内，指令有效
                if event.pos:
                    start_game()
                    # 每进行一步操作都有一个结果，判断结果
                    if win:
                        you_win()
                    elif failure:
                        you_failure()


game()