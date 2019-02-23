"""==========zhuming=========="""
import pygame
from random import randint
from color import Color
import square_coordinate
from square import Square
import json


K_UP = 273
K_DOWN = 274
K_RIGHT = 275
K_LEFT = 276

# 基础列表，16个方框
base_list = [[0 for n1 in range(4)] for n2 in range(4)]
score = 0
best_score = 0


def print_base(base_list):
    base = '''
    | %d | %d | %d | %d |
    | %d | %d | %d | %d |
    | %d | %d | %d | %d |
    | %d | %d | %d | %d |
    ''' % (base_list[0][0],base_list[0][1],base_list[0][2],base_list[0][3],
           base_list[1][0],base_list[1][1],base_list[1][2],base_list[1][3],
           base_list[2][0],base_list[2][1],base_list[2][2],base_list[2][3],
           base_list[3][0],base_list[3][1],base_list[3][2],base_list[3][3],)
    print(base)


def first_rand(window):
    # 开局第一次产生两个随机数
    # 产生两个随机数
    rand1 = 2 if randint(0, 16) >= 4 else 4
    rand2 = 2 if randint(0, 16) >= 4 else 4
    # 产生两个随机坐标
    rand_coor1 = (randint(0, 3), randint(0, 3))
    rand_coor2 = (randint(0, 3), randint(0, 3))
    # 将随机数添加到随机坐标
    base_list[rand_coor1[0]][rand_coor1[1]] = rand1
    base_list[rand_coor2[0]][rand_coor2[1]] = rand2
    print_base(base_list)
    # 将数值添加到方块并改变方块颜色
    square_coordinate.change_color(window, rand1, rand_coor1[0], rand_coor1[1])
    square_coordinate.add_num_in_rect(window, rand1, rand_coor1[0], rand_coor1[1])

    square_coordinate.change_color(window, rand2, rand_coor2[0], rand_coor2[1])
    square_coordinate.add_num_in_rect(window, rand2, rand_coor2[0], rand_coor2[1])


def create_rand(window):
    # 开局之后每次产生一个随机数
    rand3 = 2 if randint(0, 16) >= 2 else 4
    # 产生一个随机坐标
    rand_coor3 = (randint(0, 3), randint(0, 3))

    while True:
        if base_list[rand_coor3[0]][rand_coor3[1]] == 0:
            base_list[rand_coor3[0]][rand_coor3[1]] = rand3
            print_base(base_list)
            # 将数值添加到方块中,并改变方块颜色
            square_coordinate.change_color(window, rand3, rand_coor3[0], rand_coor3[1])
            square_coordinate.add_num_in_rect(window, rand3, rand_coor3[0], rand_coor3[1])
            return
        else:
            rand_coor3 = (randint(0, 3), randint(0, 3))


def is_can_move(window):
    # 当数值满格的时候，判断有没有一对相邻的两个数是一样的，如果没有，游戏结束
    # 横向判断
    for i in range(4):
        for j in range(3):
            if base_list[i][j] == base_list[i][j+1]:
                return True
    # 竖向判断
    for i in range(4):
        for j in range(3):
            if base_list[j][i] == base_list[j+1][i]:
                return True
    # global best_score
    # best_score = score
    print('GAMEOVER')
    print('best_score:' + str(score))
    # 游戏结束，判断当前分数和上次分数的大小，大就更新，小就不更新
    with open('files/best_score.json', encoding='utf-8') as f:
        get_score = json.load(f)
    if get_score < score:
        # 游戏结束，更新本地化的最高分
        with open('files/best_score.json', 'w', encoding='utf-8') as f:
            json.dump(score, f)
        # 游戏结束，在游戏框中更新最高分
        square_coordinate.update_best_score(window, score)
    square_coordinate.gameover(window)


def move_right(window):
    # 按右键的循环
    count = 0
    for i in range(4):
        add_coor = []
        for j in range(3):
            for n in list(range(j+1))[::-1]:
                if not base_list[i][3-n]:
                    # 当有一个值不为0的时候，count+1才有效
                    if base_list[i][2-n] != 0:
                        count += 1
                        # 添加数字到相应方块中,并变换方块的颜色
                        square_coordinate.change_color(window, base_list[i][2-n], i, 3-n)
                        square_coordinate.add_num_in_rect(window, base_list[i][2-n], i, 3 - n)
                    # 交换相邻方块中的值
                    base_list[i][3-n] = base_list[i][2-n]
                    base_list[i][2-n] = 0
                    # 将数值为0的方块变为基础色
                    square_coordinate.return_base_color(window, i, 2-n)

                elif base_list[i][2-n] == base_list[i][3-n]:
                    # 判断后面一位值相同的数是否已经是改变过的，如果改变过就不会再被改变
                    if ((i, 3-n) not in add_coor) and ((i, 2-n) not in add_coor):
                        base_list[i][2-n] = 0
                        base_list[i][3 - n] *= 2
                        add_coor.append((i, 3-n))
                        count += 1
                        # 数值改变之后，有数值的方块颜色和值改变，数值为0的方块变为基础色
                        # 有数值的先被基础色覆盖，再添加值。后期添加颜色就直接用颜色方块覆盖了。
                        # square_coordinate.return_base_color(window, i, 3-n)
                        square_coordinate.change_color(window, base_list[i][3-n], i, 3-n)
                        square_coordinate.add_num_in_rect(window, base_list[i][3-n], i, 3-n)
                        square_coordinate.return_base_color(window, i, 2-n)

                        # 改变分数
                        global score
                        score += base_list[i][3 - n]
                        # 更新分数添加到得分方框中
                        square_coordinate.update_score(window, score)
                        # 判断是否够2048
                        if base_list[i][3 - n] == 2048:
                            square_coordinate.victory(window)
    # 如果按下方向键之后，count还是等于0，说明列表中的值以及值相应的坐标都没有任何改变，
    # 就要判断是不是数值已经满格了，如果没有满格，就不要产生新的数字，
    # 如果满格，就判断有无可相加的数字，如果有就还没结束，如果没有了，就GAMEOVER了

    # 如果count不等于0，证明按下方向键肯定有发生数值变化或者位移，那就肯定有空格可以添加数字
    if count != 0:
        create_rand(window)
    # 如果count等于0，判断数值是否满格
    else:
        for item in base_list:
            if 0 in item:
                # 数值不满格，就不添加，也没有gameover
                break
        # 数值满格，
        else:
            is_can_move(window)


def move_left(window):
    # 按左键的循环
    count = 0
    for i in range(4):
        add_coor = []
        for j in range(3):
            for n in list(range(j+1))[::-1]:
                if not base_list[i][n]:
                    if base_list[i][n+1] != 0:
                        count += 1
                        # 添加数字到相应方块中
                        square_coordinate.change_color(window, base_list[i][n + 1], i, n)
                        square_coordinate.add_num_in_rect(window, base_list[i][n+1], i, n)
                    base_list[i][n] = base_list[i][n+1]
                    base_list[i][n+1] = 0
                    # 将数值为0的方块变为基础色
                    square_coordinate.return_base_color(window, i, n+1)

                elif base_list[i][n+1] == base_list[i][n]:
                    if ((i, n) not in add_coor) and ((i, n+1) not in add_coor):
                        base_list[i][n+1] = 0
                        base_list[i][n] *= 2
                        add_coor.append((i, n))
                        count += 1
                        # 数值改变之后，有数值的方块颜色和值改变，数值为0的方块变为基础色
                        # 有数值的先被基础色覆盖，再添加值。后期添加颜色就直接用颜色方块覆盖了。
                        # square_coordinate.return_base_color(window, i, n)
                        square_coordinate.change_color(window, base_list[i][n], i, n)
                        square_coordinate.add_num_in_rect(window, base_list[i][n], i, n)
                        square_coordinate.return_base_color(window, i, n+1)

                        # 改变分数
                        global score
                        score += base_list[i][n]
                        # 更新分数添加到得分方框中
                        square_coordinate.update_score(window, score)
                        # 判断是否够2048
                        if base_list[i][n] == 2048:
                            square_coordinate.victory(window)

    # 如果count不等于0，证明按下方向键肯定有发生数值变化或者位移，那就肯定有空格可以添加数字
    if count != 0:
        create_rand(window)
    # 如果count等于0，判断数值是否满格
    else:
        for item in base_list:
            if 0 in item:
                # 数值不满格，就不添加，也没有gameover
                break
        # 数值满格，
        else:
            is_can_move(window)


def move_up(window):
    # 按上键的循环
    count = 0
    for i in range(4):
        add_coor = []
        for j in range(3):
            for n in list(range(j+1))[::-1]:
                if not base_list[n][i]:
                    if base_list[n+1][i] != 0:
                        count += 1
                        # 添加数字到相应方块中
                        square_coordinate.change_color(window, base_list[n + 1][i], n, i)
                        square_coordinate.add_num_in_rect(window, base_list[n+1][i], n, i)
                    base_list[n][i] = base_list[n+1][i]
                    base_list[n+1][i] = 0
                    # 将数值为0的方块变为基础色
                    square_coordinate.return_base_color(window, n+1, i)

                elif base_list[n+1][i] == base_list[n][i]:
                    if ((n, i) not in add_coor) and ((n+1, i) not in add_coor):
                        base_list[n+1][i] = 0
                        base_list[n][i] *= 2
                        add_coor.append((n, i))
                        count += 1
                        # 数值改变之后，有数值的方块颜色和值改变，数值为0的方块变为基础色
                        # 有数值的先被基础色覆盖，再添加值。后期添加颜色就直接用颜色方块覆盖了。
                        # square_coordinate.return_base_color(window, n, i)
                        square_coordinate.change_color(window, base_list[n][i], n, i)
                        square_coordinate.add_num_in_rect(window, base_list[n][i], n, i)
                        square_coordinate.return_base_color(window, n+1, i)

                        # 改变分数
                        global score
                        score += base_list[n][i]
                        # 更新分数添加到得分方框中
                        square_coordinate.update_score(window, score)
                        # 判断是否够2048
                        if base_list[n][i] == 2048:
                            square_coordinate.victory(window)
    # 如果count不等于0，证明按下方向键肯定有发生数值变化或者位移，那就肯定有空格可以添加数字
    if count != 0:
        create_rand(window)
    # 如果count等于0，判断数值是否满格
    else:
        for item in base_list:
            if 0 in item:
                # 数值不满格，就不添加，也没有gameover
                break
        # 数值满格，
        else:
            is_can_move(window)


def move_down(window):
    # 按下键的循环
    count = 0
    for i in range(4):
        add_coor = []
        for j in range(3):
            for n in list(range(j+1))[::-1]:
                if not base_list[3-n][i]:
                    if base_list[2-n][i] != 0:
                        count += 1
                        # 添加数字到相应方块中
                        square_coordinate.change_color(window, base_list[2 - n][i], 3 - n, i)
                        square_coordinate.add_num_in_rect(window, base_list[2-n][i], 3-n, i)
                    base_list[3-n][i] = base_list[2-n][i]
                    base_list[2-n][i] = 0
                    # 将数值为0的方块变为基础色
                    square_coordinate.return_base_color(window, 2-n, i)

                elif base_list[2-n][i] == base_list[3-n][i]:
                    if ((3-n, i) not in add_coor) and ((2-n, i) not in add_coor):
                        base_list[2-n][i] = 0
                        base_list[3-n][i] *= 2
                        add_coor.append((3-n, i))
                        count += 1
                        # 数值改变之后，有数值的方块颜色和值改变，数值为0的方块变为基础色
                        # 有数值的先被基础色覆盖，再添加值。后期添加颜色就直接用颜色方块覆盖了。
                        # square_coordinate.return_base_color(window, 3-n, i)
                        square_coordinate.change_color(window, base_list[3 - n][i], 3 - n, i)
                        square_coordinate.add_num_in_rect(window, base_list[3-n][i], 3-n, i)
                        square_coordinate.return_base_color(window, 2-n, i)

                        # 改变分数
                        global score
                        score += base_list[3-n][i]
                        # 更新分数添加到得分方框中
                        square_coordinate.update_score(window, score)
                        # 判断是否够2048
                        if base_list[3-n][i] == 2048:
                            square_coordinate.victory(window)
    # 如果count不等于0，证明按下方向键肯定有发生数值变化或者位移，那就肯定有空格可以添加数字
    if count != 0:
        create_rand(window)
    # 如果count等于0，判断数值是否满格
    else:
        for item in base_list:
            if 0 in item:
                # 数值不满格，就不添加，也没有gameover
                break
        # 数值满格，
        else:
            is_can_move(window)


def main():
    pygame.init()

    window = pygame.display.set_mode((400, 600))
    pygame.display.set_caption('woming2048')
    window.fill(Color.LightYellow2)
    # 显示游戏基础方块
    Square.square(window)
    # 显示基础方块和得分为0，最高分是上次的最终得分
    square_coordinate.box(window)
    square_coordinate.score_box(window)
    square_coordinate.best_score_box(window)
    square_coordinate.update_score(window, 0)
    with open('files/best_score.json', encoding='utf-8') as f:
        get_score = json.load(f)
    square_coordinate.update_best_score(window, get_score)
    # 添加第一次的随机数
    first_rand(window)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_RIGHT:
                    move_right(window)
                    # print('score:' + str(score))
                elif event.key == K_LEFT:
                    move_left(window)
                    # print('score:' + str(score))
                elif event.key == K_UP:
                    move_up(window)
                    # print('score:' + str(score))
                elif event.key == K_DOWN:
                    move_down(window)
                    # print('score:' + str(score))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 点击重新开始
                if 145 <= event.pos[0] <= 385 and 120 <= event.pos[1] <= 150:
                    # 游戏重新开始
                    global base_list
                    base_list = [[0 for n1 in range(4)] for n2 in range(4)]
                    window.fill(Color.LightYellow2)
                    Square.square(window)
                    # 显示基础方块和得分为0，最高分是上次的最终得分
                    square_coordinate.box(window)
                    square_coordinate.score_box(window)
                    square_coordinate.best_score_box(window)
                    with open('files/best_score.json', encoding='utf-8') as f:
                        get_score = json.load(f)
                    square_coordinate.update_best_score(window, get_score)
                    global score
                    score = 0
                    square_coordinate.update_score(window, score)
                    # 添加第一次的随机数
                    first_rand(window)

        pygame.display.update()


if __name__ == '__main__':
    main()



