# -*- coding: utf-8 -*-
import os
os.system('cls')
print('============================================================')
print('The White Heron Princess Elemental Burst Calculator')
print('created by: @naayu1012')
print('============================================================')
print('\n')

def isfloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def showmenu():
    print('menu:')
    print('1. 攻撃判定がすべて会心だった場合の計算')
    print('2. 会心率を考慮した大まかな期待値(厳密な計算は行いません)')
    mode = input('火力を計算するモードを選択してください(1 or 2): ')
    if mode != '1' and  mode != '2':
        print('1か2を入力してください')
        showmenu()
    return mode
    
def all_critical_damage():
    A=input('会心時の咲きダメ―ジを入力してください:')
    if A.isdecimal() == False:
        print('数字を入力してください')
        all_critical_damage()
    A=int(A)
    B=input('会心時の斬撃ダメ―ジを入力してください:')
    if B.isdecimal() == False:
        print('数字を入力してください')
        all_critical_damage()
    B=int(B)
    print('計算結果:')
    print(A+19*B)

def expected_damage():
    A=input('会心率を入力してください:')
    if isfloat(A) == False:
        print('数字を入力してください')
        expected_damage()
    if int(A) >= 100:
        A = 1
    A=float(A)/100
    C=input('非会心時の咲きダメ―ジを入力してください:')
    if C.isdecimal() == False:
        print('数字を入力してください')
        expected_damage()
    C=int(C)
    D=input('非会心時の1発当たりの斬撃ダメ―ジを入力してください:')
    if D.isdecimal() == False:
        print('数字を入力してください')
        expected_damage()
    D=int(D)
    E=input('会心ダメ―ジを入力してください:')
    if isfloat(E) == False:
        print('数字を入力してください')
        expected_damage()
    E=float(E)/100
    B = 1 - A
    print("計算結果:")
    print(B*(C+19*D)+A*E*(C+19*D))
    
def main():
    mode = showmenu()
    if mode == '1':
        all_critical_damage()
    elif mode == '2':
        expected_damage()

main()