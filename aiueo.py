import os
import time
from random import choice, shuffle
from termcolor import colored as Color
from pygame import mixer as player

from kana import kana_d
from msgs import msgs


def main():

    wel_msg = '\n' + msgs['a'] + '\n' + msgs['b']
    print(wel_msg)

    while(True):

        menu_msg = msgs['c'] + '\n' + msgs['d']
        mode = input(menu_msg)

        if mode == '1' or mode == '2' or mode == '3':
            exer_kana(mode)

        elif mode == '4':
            shuffle_kana()

        elif mode == '5':
            show_kana(False)

        elif mode == '6':
            show_kana(True)

        elif mode == '0':
            exit(msgs['n'])

        else:
            continue


def play(pinyin):
    player.init()
    player.music.load(f'./media/{pinyin}.mp3')
    player.music.play()


def shuffle_kana():

    kana_l = [[py, k[0], k[2], k[3]] for py, k in kana_d.items()]
    kana_l += [[py, k[1], k[2], k[3]] for py, k in kana_d.items()]

    # kana_l = [['me', 'め', 'メ', '(me)美女(め)与玫(メ)瑰', '美女与玫瑰'], [
    #     'me', 'め', 'メ', '(me)美女(め)与玫(メ)瑰', '美女与玫瑰']]

    shuffle(kana_l)
    time_start = time.time()

    r_c = 0  # 正确次数
    s_c = 0  # 跳过次数
    w_c = []  # 错误列表
    c_c = 0  # 提交次数

    print(msgs['s'], msgs['f'])

    for index, kana in enumerate(kana_l):

        while(True):

            msg = Color(msgs['g'] % (kana[1]), 'blue')
            user_input = input(msg)

            if user_input == kana[0]:
                play(kana[0])

                r_c += 1
                c_c += 1

                msg1 = msgs['p'] % (index + 1, 92)
                msg2 = msgs['h'] + msgs['o'] % (kana[2])

                print(msg1, msg2)
                break

            elif user_input == '1':
                play(kana[0])

                s_c += 1
                c_c += 1

                msg1 = msgs['j'] % (kana[1], kana[0])
                msg2 = msgs['o'] % (kana[2])
                msg3 = msgs['p'] % (index + 1, 92)

                print(msg1, msg2, '\t', msg3)
                break

            elif user_input == '0':
                print(msgs['m'] % ("打乱复习"))
                return

            else:
                if index not in w_c:
                    w_c.append(index)
                c_c += 1

                print(f"{msgs['i']}{msgs['k'] % (kana[3])}")
                continue

    time_end = time.time()
    interval = int(time_end - time_start)
    print(msgs['q'])
    wrong_kana = ''
    for index in w_c:
        wrong_kana += str(kana_l[index]) + '\n'
    print(msgs['r'] % (interval, r_c, r_c, c_c, s_c, wrong_kana))


def show_kana(hasFomular=False):

    kana_str = ''
    item_number = 1 if hasFomular else 5

    for index in range(46):

        is_n = '\t\n' if (index + 1) % item_number == 0 else '\t'

        pinyin = list(kana_d.keys())[index]
        hiragana = list(kana_d.values())[index][0]
        katakana = list(kana_d.values())[index][1]

        kana = Color(f'{hiragana} / {katakana}', 'yellow')

        fomular = f"\t口诀: {list(kana_d.values())[index][2]}" if hasFomular else " "
        fomular = Color(f"{fomular}{is_n}", "cyan")

        kana_str += kana + ' : ' + Color(f'{pinyin}', 'green') + fomular

    print(kana_str)


def exer_kana(mode):

    maps = {'1': [0, '平假名'], '2': [1, '片假名'], '3': [2, '混合假名']}
    print(msgs['e'] % (maps[mode][1]), msgs['f'])

    while(True):
        pinyin = choice(list(kana_d.keys()))

        if maps[mode][0] == 2:
            kana = choice(kana_d[pinyin][0:2])

        else:
            kana = kana_d[pinyin][maps[mode][0]]

        while(True):

            msg = Color(msgs['g'] % (kana), 'blue')
            user_input = input(msg)

            if user_input == pinyin:
                play(pinyin)

                print(f"{msgs['h']}{msgs['o'] % (kana_d[pinyin][2])}")
                break

            elif user_input == '1':
                play(pinyin)

                msg1 = msgs['j'] % (kana, pinyin)
                msg2 = msgs['o'] % (kana_d[pinyin][2])

                print(msg1, msg2)
                break

            elif user_input == '0':
                print(msgs['m'] % (maps[mode][1]))
                return

            elif user_input == 'kana':
                show_kana()
                continue

            else:
                print(f"{msgs['i']}{msgs['k'] % (kana_d[pinyin][3])}")
                continue


if __name__ == '__main__':
    main()
