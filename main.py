from tkinter import *
from hotkeys import *
from algorithm import *

root = Tk()
root.title('Test game')



def new_game():
    for row in range(5):
        color = ['red', 'lavender', 'green', 'lavender', 'blue']
        for col in range(5):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = color[col]
            field[row][col]['relief'] = GROOVE
    field[0][1]['background'] = 'black'
    field[0][3]['background'] = 'black'
    field[2][1]['background'] = 'black'
    field[2][3]['background'] = 'black'
    field[4][1]['background'] = 'black'
    field[4][3]['background'] = 'black'
    create_game(field)
    field[0][0]['relief'] = RAISED
    lbl1.config(text=" ")



def create_help():
    t = Toplevel()
    t.wm_title("Help")
    l1 = Label(t, text="WSAD - клавиши для выбора или передвижении фишки")
    l1.grid(row=0, column=0)
    l2 = Label(t, text="Enter - фиксирует фишку. После этого фишку можно передвинуть")
    l2.grid(row=1, column=0)
    l3 = Label(t, text="Фишки мы можем передвигать на соседнее свободное место по горизонтали или вертикали.\n"
                       " Требуется,передвигая фишки, выставить их в три вертикальных ряда соответственно цветам,\n"
                       " стоящим над полем.")
    l3.grid(row=2, column=0)
    l4 = Label(t, text="Черные клетки - это блокированные фишки")
    l4.grid(row=3, column=0)


lbl1 = Label(root, text=" ")
lbl1.grid(row=0, column=0, columnspan=5)
for col, color in [[0, 'red'], [2, 'green'], [4, 'blue']]:

    label = Label(root, text=' ', width=4, height=2,
                  font=('Verdana', 20, 'bold'),
                  background=color)
    label.grid(row=1, column=col, sticky='nsew')
lbl2 = Label(root, text=" ")
lbl2.grid(row=2, column=0, columnspan=5)

for row in range(5):
    line = []
    for col in range(5):
        label = Label(root, text=' ', width=4, height=2,
                      font=('Verdana', 20, 'bold'),
                      background='lavender')
        label.grid(row=row+3, column=col, sticky='nsew')
        line.append(label)
    field.append(line)
play_button = Button(root, text='new game', command=new_game)
play_button.grid(row=8, column=0, columnspan=5, sticky='nsew')
help_button = Button(root, text='help', command=create_help)
help_button.grid(row=9, column=0, columnspan=5, sticky='nsew')

root.bind('<Return>', lambda event: executeReturn(event) if check_win(field) else lbl1.config(text="YOU WIN!!!"))
root.bind('w', executeW)
root.bind('a', executeA)
root.bind('d', executeD)
root.bind('s', executeS)

root.resizable(width=False, height=False)
root.mainloop()
