# -*- coding:utf-8 -*-
import os
import copy
import time
import sys
import random
import pygame
from pygame.locals import *

SCREEN_SET = Rect(0, 0, 800, 700)
i_turn=0

###################################
#
# 　ここからメイン
#
###################################
def main():
    # 変数の初期化
    i_turn =0

    bord_list=[[0,0,0],[0,0,0],[0,0,0]]
    O_list=[[0,0,0],[0,0,0],[0,0,0]]
    X_list=[[0,0,0],[0,0,0],[0,0,0]]
    OX_list=[[0,0,0],[0,0,0],[0,0,0]]
    O_WIN_BF=[0,0,0,0, 0,0,0,0]
    X_WIN_BF=[0,0,0,0, 0,0,0,0]

    pygame.init()  # Pygameの初期化
    screen = pygame.display.set_mode((300, 160))  # 画面サイズを指定して画面を生成
    pygame.display.set_caption("GAME")  # タイトルバーに表示する文字
    screen.fill((0, 0, 0))  # 画面を黒色に塗りつぶし
    screen.fill((0, 0, 0))  # ウィンドウの背景色
    bord_img = pygame.image.load("./img/3x3bord.png")
    put_img(screen, bord_img, 0, 0)  # 画面に板を置く

    # ココからメインのループ
    while (1):
        time.sleep(1)  # 速度調整のsleep

        #キー入力のチェック
        i_turn,O_list,X_list = event_proc(OX_list, i_turn,O_list,X_list)

        # # 勝敗チェック
        i_turn = chek_win(O_WIN_BF, O_list, X_WIN_BF, X_list, i_turn)

        # 画面に駒を置く
        put_cat(screen, OX_list)

        if i_turn == 0:
            put_score(screen, 'O turn')  # スコアの表示
        elif i_turn == 1:
            put_score(screen, 'X turn')  # スコアの表示
        elif i_turn == 2:
            put_score(screen, 'O Win')  # スコアの表示
        elif i_turn == 3:
            put_score(screen, 'X Win')  # スコアの表示
        pygame.display.update()  # スクリーンの一部分のみを更新します。この命令はソフトウェア側での表示処理に最適化されています。
        if i_turn >= 2:
            pygame.display.update()  # スクリーンの一部分のみを更新します。この命令はソフトウェア側での表示処理に最適化されています。
            time.sleep(3)  # 速度調整のsleep
            pygame.quit()  # Pygameの終了(画面閉じられる)
            sys.exit()


def chek_win(O_WIN_BF, O_list, X_WIN_BF, X_list, i_turn):
    O_WIN_BF[0] = O_list[0][0] + O_list[0][1] + O_list[0][2]
    O_WIN_BF[1] = O_list[1][0] + O_list[1][1] + O_list[1][2]
    O_WIN_BF[2] = O_list[2][0] + O_list[2][1] + O_list[2][2]
    O_WIN_BF[3] = O_list[0][0] + O_list[1][0] + O_list[2][0]
    O_WIN_BF[4] = O_list[0][1] + O_list[1][1] + O_list[2][1]
    O_WIN_BF[5] = O_list[0][2] + O_list[1][2] + O_list[2][2]
    O_WIN_BF[6] = O_list[0][0] + O_list[1][1] + O_list[2][2]
    O_WIN_BF[7] = O_list[0][2] + O_list[1][1] + O_list[2][0]
    X_WIN_BF[0] = X_list[0][0] + X_list[0][1] + X_list[0][2]
    X_WIN_BF[1] = X_list[1][0] + X_list[1][1] + X_list[1][2]
    X_WIN_BF[2] = X_list[2][0] + X_list[2][1] + X_list[2][2]
    X_WIN_BF[3] = X_list[0][0] + X_list[1][0] + X_list[2][0]
    X_WIN_BF[4] = X_list[0][1] + X_list[1][1] + X_list[2][1]
    X_WIN_BF[5] = X_list[0][2] + X_list[1][2] + X_list[2][2]
    X_WIN_BF[6] = X_list[0][0] + X_list[1][1] + X_list[2][2]
    X_WIN_BF[7] = X_list[0][2] + X_list[1][1] + X_list[2][0]
    for idx in range(8):
        if X_WIN_BF[idx] == 3:
            i_turn = 3
        if O_WIN_BF[idx] == 3:
            i_turn = 2

    return i_turn


## スコアの表示
def put_score(screen, str):
    font = pygame.font.Font(None, 40)  # フォントの設定(55px)
    put_img(screen, get_block_img(0), 200, 50)  # スコア表示部分に黒ブロックを置いて消す
    put_img(screen, get_block_img(0), 250, 50)  # スコア表示部分に黒ブロックを置いて消す
    put_img(screen, get_block_img(0), 300, 50)  # スコア表示部分に黒ブロックを置いて消す
    screen.blit(font.render(str , True, (255, 255, 0)), [200, 50])  # 文字列の表示位置


## キー入力など、イベント処理
##　矢印キーでブロックの座標他仕込みも行う
def event_proc(OX_list: list, i_turn:int, O_list, X_list) -> object:
    # イベント処理
    for event in pygame.event.get():
        if event.type == QUIT:  # 閉じるボタンが押されたら終了
            pygame.quit()  # Pygameの終了(画面閉じられる)
            sys.exit()
        # キー操作(追加したとこ)
        elif event.type == KEYDOWN:
            x = -1
            y = -1
            print("event.type=" + str(event.type))
            print("event.key=" + str(event.key))
            if event.key == K_q:
                print("q")
                y=0
                x=0
            elif event.key == K_w:
                print("w")
                y=0
                x=1
            elif event.key == K_e:
                print("e")
                y=0
                x=2
            elif event.key == K_a:
                print("a")
                y=1
                x=0
            elif event.key == K_s:
                print("s")
                y=1
                x=1
            elif event.key == K_d:
                print("d")
                y=1
                x=2
            elif event.key == K_z:
                print("z")
                y=2
                x=0
            elif event.key == K_x:
                print("x")
                y=2
                x=1
            elif event.key == K_c:
                print("c")
                y=2
                x=2
            if x>=0 and y>=0:
                if OX_list[y][x] == 0:
                    OX_list[y][x]= i_turn + 1
                    if i_turn==0:
                        O_list[y][x]=1
                    else:
                        X_list[y][x]=1
                    i_turn = ((i_turn + 1) & 1)
    return i_turn,O_list,X_list

##　指定のブロック絵柄（猫など）をイメージオブジェクトに入れて返す
def get_block_img(cat_color: int):
    if cat_color == 0:
        ret_img = pygame.image.load("./img/blank.png")  # 画像を読み込む(今回追加したとこ)
    elif cat_color == 1:
        ret_img = pygame.image.load("./img/block.png")  # 画像を読み込む(今回追加したとこ)
    elif cat_color == 2:
        ret_img = pygame.image.load("./img/neko0.png")  # 画像を読み込む(今回追加したとこ)
    elif cat_color == 3:
        ret_img = pygame.image.load("./img/neko2.png")  # 画像を読み込む(今回追加したとこ)
    elif cat_color == 4:
        ret_img = pygame.image.load("./img/neko1.png")  # 画像を読み込む(今回追加したとこ)
    elif cat_color == 5:
        ret_img = pygame.image.load("./img/neko3.png")  # 画像を読み込む(今回追加したとこ)
    elif cat_color == 6:
        ret_img = pygame.image.load("./img/neko4.png")  # 画像を読み込む(今回追加したとこ)
    elif cat_color == 7:
        ret_img = pygame.image.load("./img/neko5.png")  # 画像を読み込む(今回追加したとこ)
    elif cat_color == 8:
        #ret_img = pygame.image.load("./img/cat.png")  # 画像を読み込む(今回追加したとこ)
        ret_img = pygame.image.load("./img/u_cat.png")  # 画像を読み込む(今回追加したとこ)
    elif cat_color == 9:
        ret_img = pygame.image.load("./img/r_cat.png")  # 画像を読み込む(今回追加したとこ)
    elif cat_color == 10:
        ret_img = pygame.image.load("./img/d_cat.png")  # 画像を読み込む(今回追加したとこ)
    elif cat_color == 11:
        ret_img = pygame.image.load("./img/l_cat.png")  # 画像を読み込む(今回追加したとこ)
    else:
        ret_img = pygame.image.load("./img/block.png")  # 画像を読み込む(今回追加したとこ)
    return ret_img


##　移動ブロック（猫）を画面に置く
def put_cat(screen, OX_list: list):
    for x in range(3):
        print(x)
        for y in range(3):
            print(y)
            drop_cat_img = get_block_img(int(OX_list[y][x])+1)
            screen.blit(drop_cat_img, ((x*53), (y*53)))


##フレーム内を描き直す
def put_frame(screen, list):
    # 枠のブロックを表示する。
    y_idx = 0
    for val1 in list:
        x_idx = 0
        for val2 in val1:
            # idBlokck = list2[0][index2]
            id_blokck = int(val2)
            put_block(screen, get_block_img(id_blokck), x_idx, y_idx)
            x_idx += 1
        y_idx += 1


## 絵を表示する
def put_img(screen, img_obj, x, y):
    screen.blit(img_obj, (x, y, 50, 50))  # 絵を画面に貼り付ける


## ブロックを画面に置く ※50ドット単位
def put_block(screen, img_obj, x, y):
    screen.blit(img_obj, (50 * x, 50 * y, 50, 50))  # 絵を画面に貼り付ける


##画面に四角を書く
def put_rect(screen, x, y):
    RED = (255, 0, 0)
    rect = ((50 * x), (50 * y), 50, 50)
    pygame.draw.rect(screen, RED, rect)
    # screen.blit(font.render( in_chr, True, (255, 255, 0)), [(50 * x_idx), (40 * y_idx)])  # 文字列の表示位置


##　既定　これが無いと動かない    #############################
if __name__ == "__main__":
    main()
