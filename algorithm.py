import random
import hotkeys
from tkinter import RAISED, GROOVE, SUNKEN

def create_game(field):
    for i in range(5000):
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        if field[row][col]['background'] not in ['black', 'lavender']:
            move = random.randint(1, 4)
            hotkeys.cur_pos_row = row
            hotkeys.cur_pos_col = col
            field[row][col]['relief'] = RAISED
            if move == 1:
                hotkeys.executeReturn(1)
                hotkeys.executeA(1)
                hotkeys.executeReturn(1)
            if move == 2:
                hotkeys.executeReturn(1)
                hotkeys.executeW(1)
                hotkeys.executeReturn(1)
            if move == 3:
                hotkeys.executeReturn(1)
                hotkeys.executeD(1)
                hotkeys.executeReturn(1)
            if move == 4:
                hotkeys.executeReturn(1)
                hotkeys.executeS(1)
                hotkeys.executeReturn(1)
            field[hotkeys.cur_pos_row][hotkeys.cur_pos_col]['relief'] = GROOVE
    hotkeys.cur_pos_col = 0
    hotkeys.cur_pos_row = 0
    hotkeys.fix_pos_row = 0
    hotkeys.fix_pos_col = 0

def check_win(field):
    check = False
    for row in range(5):
        if [field[row][0]['background'], field[row][2]['background'], field[row][4]['background']] != ['red', 'green', 'blue']:
            check = True
    if not check:
        field[hotkeys.cur_pos_row][hotkeys.cur_pos_col]['relief'] = GROOVE
    return check