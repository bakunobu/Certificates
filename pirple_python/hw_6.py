def draw_table(r:int, c:int) -> bool:
    for i in range(r):
        if i % 2 == 0:
            for col in range(1, c+1):
                if col % 2 == 1:
                    if col != c:
                        print(' ', end='')
                    else:
                        print(' ')
                else:
                    if col != c:
                        print('|', end='')
                    else:
                        print(' ')
        else:
            if c % 2 == 0:
                print('-' * (c-1))
            else:
                print('-' * c)     
    if r > 21 or c > 176:
        return(False)
    else:
        return(True)

