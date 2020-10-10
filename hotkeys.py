field = []
from tkinter import RAISED, GROOVE, SUNKEN

fix_pos_col = 0
fix_pos_row = 0
cur_pos_col = 0
cur_pos_row = 0
fixed = False


def swap(x1, y1, x2, y2):
    global fix_pos_col, fix_pos_row
    t = field[x2][y2]['relief']
    field[x2][y2]['relief'] = field[x1][y1]['relief']
    field[x1][y1]['relief'] = t
    fix_pos_col = cur_pos_col
    fix_pos_row = cur_pos_row
    if field[cur_pos_row][cur_pos_col]['relief'] == SUNKEN:
        t = field[x2][y2]['background']
        field[x2][y2]['background'] = field[x1][y1]['background']
        field[x1][y1]['background'] = t


def executeReturn(e):

    global fix_pos_col, fix_pos_row, fixed
    if field[cur_pos_row][cur_pos_col]['background'] not in ['lavender', 'black']:
        fix_pos_col = cur_pos_col
        fix_pos_row = cur_pos_row
        if field[fix_pos_row][fix_pos_col]['relief'] == RAISED:
            field[fix_pos_row][fix_pos_col]['relief'] = SUNKEN
            fixed = True
        else:
            field[fix_pos_row][fix_pos_col]['relief'] = RAISED
            fixed = False


def executeA(e):
    global cur_pos_col
    if cur_pos_col != 0:
        if not fixed or fixed and checkOnFree(cur_pos_row, cur_pos_col - 1):
            cur_pos_col -= 1
            swap(fix_pos_row, fix_pos_col, cur_pos_row, cur_pos_col)



def executeW(e):
    global cur_pos_row
    if cur_pos_row != 0:
        if not fixed or fixed and checkOnFree(cur_pos_row - 1, cur_pos_col):
            cur_pos_row -= 1
            swap(fix_pos_row, fix_pos_col, cur_pos_row, cur_pos_col)



def executeD(e):
    global cur_pos_col
    if cur_pos_col != 4:
        if not fixed or fixed and checkOnFree(cur_pos_row, cur_pos_col + 1):
            cur_pos_col += 1
            swap(fix_pos_row, fix_pos_col, cur_pos_row, cur_pos_col)



def executeS(e):
    global cur_pos_row
    if cur_pos_row != 4:
        if not fixed or fixed and checkOnFree(cur_pos_row + 1, cur_pos_col):
            cur_pos_row += 1
            swap(fix_pos_row, fix_pos_col, cur_pos_row, cur_pos_col)




def checkOnFree(cur_pos_row, cur_pos_col):
    if field[cur_pos_row][cur_pos_col]['background'] == 'lavender':
        return True
    return False
