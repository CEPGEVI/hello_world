def greet():
    print('----------------------')
    print('Привет! Давай сыграем!')
    print('----------------------')
    print('Поочередно вводите координаты X и 0')
def show():
     print ('  0 1 2')
     for i, row in enumerate(field):
          row_str = str(i) + ' ' + ' '.join(row)
          print (row_str)

def ask():
     while True:
         coord=(input('    ваш ход: ').split())
         if len(coord)!= 2:
             print('Введите две координаты')
             continue
         x, y = coord
         if not(x.isdigit()) or not(y.isdigit()):
             print('введите числа!')
             continue
         x,y=int(x),int(y)
         if 0<=x<=2 and 0<=y<=2 :
             if field[x][y] == ' ':
                 return x, y
             else:
                 print('клетка занята!')
         else:
              print('координаты вне диапазона')


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbol = []
        for c in cord:
            symbol.append(field[c[0]][c[1]])
        if symbol == ['X', 'X', 'X']:
            print('Выиграл X!')
            return True
        if symbol == ['0', '0', '0']:
            print('Выиграл 0!')
            return True
    return False

greet()
field = [[' '] * 3 for i in range(3)]
num=0
while True:
    num+=1
    show()
    if num % 2 == 1:
        print('Ходит крестик')
    else:
        print('Ходит нолик')
    x, y = ask()
    if num % 2 == 1:
        field[x][y]='X'
    else:
        field[x][y]='0'

    if num==9:
        print('Ничья')
        break
    if check_win():
        print('Победа')
        break