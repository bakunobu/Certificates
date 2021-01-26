from termcolor import colored, cprint


def create_field(raws:int, cols:int, my_dict:dict) -> str:
    field = []
    raw = '---' + '--' * (cols-1)
    field.append(raw)
    for i in range(raws):
        raw = ''
        for j in range(cols):
            if j == 0:
                raw += '|{}|'.format(my_dict.get((i,j)))
            else:
                raw += '{}|'.format(my_dict.get((i,j)))
        field.append(raw)
        raw = '---' + '--' * (cols-1)
        field.append(raw)
    return(field)          


def create_default_dict(raws:int, cols:int, filler:str='*') -> dict:
    my_dict = dict()
    for i in range(raws):
        for j in range(cols):
            my_dict[(i, j)] = '*'
    return(my_dict)


def gen_conditions(raws:int, cols:int) -> list:
    conditions = []
    
    for raw in range(raws-1):
        for col in range(cols - 4):
            conditions.append([(raw, col),
                               (raw, col+1),
                               (raw, col+2),
                               (raw, col+3)])
    
    for col in range(cols-1):
        for raw in range(raws - 4):
            conditions.append([(col, raw),
                               (col, raw+1),
                               (col, raw+2),
                               (col, raw+3)])
            
    for raw in range(raws - 4):
        for col in range(cols - 4):
            conditions.append([(raw, col),
                               (raw+1, col+1),
                               (raw+2, col+2),
                               (raw+3, col+3)])
    
    for raw in range(raws-1, 3, -1):
        for col in range(cols-4):
            conditions.append([(raw, col),
                               (raw-1, col+1),
                               (raw-2, col+2),
                               (raw-3, col+3)])
    
    return(conditions)


def win_cond(raws:int, cols:int, my_dict:dict) -> bool:
    conditions = gen_conditions(raws, cols)
    for condition in conditions:
        if (my_dict[condition[0]] == my_dict[condition[1]] \
            == my_dict[condition[2]] == my_dict[condition[3]]) \
                and my_dict[condition[0]] != '*':
            return(True)
    return(False)


def draw_field(raws:int, cols:int, my_dict:dict) -> None:
    field = []
    raw = '---' + '--' * (cols-1)
    field.append(raw)
    for i in range(raws):
        raw = ''
        for j in range(cols):
            if j == 0:
                if my_dict.get((i,j)) == 'X':
                    raw += '|{}|'.format(colored(u'\u2B24', 'red'))
                elif my_dict.get((i,j)) == '0':
                    raw += '|{}|'.format(colored(u'\u2B24', 'cyan'))
            else:
                if my_dict.get((i,j)) == 'X':
                    raw += '{}|'.format(colored(u'\u2B24', 'red'))
                elif my_dict.get((i,j)) == '0':
                    raw += '{}|'.format(colored(u'\u2B24', 'cyan'))
        field.append(raw)
        raw = '---' + '--' * (cols-1)
        field.append(raw)
    return(field)  


def main_logic(raws:int, cols:int) -> None:
    field_dict = create_default_dict(raws, cols)
    game_field = create_field(raws, cols, field_dict)
    
    turn = 0
    
    while '*' in field_dict.values():
        if turn % 2 == 0:
            print('Player 1 turn')
            filler = 'X'
        else:
            filler = '0'
            print('Player 2 turn')
        try:
            col = int(input('Choose a column: '))
        except ValueError:
            col = int(input('Use an int number: '))
        
        raw = raws-1
        
        while raw >= 0:
            if field_dict[(raw, col)] in ('X', '0'):
                raw -= 1
            else:
                field_dict[(raw, col)] = filler
                break
       
        if field_dict[(0, col)] in ('X', '0'):
            print('No more moves in this column!')
        
        else:
            turn += 1
            
        game_field = draw_field(raws, cols, field_dict)
        print(* game_field, sep='\n')
        
        if win_cond(raws, cols, field_dict):
            if turn % 2 == 0:
                print('Player 2 win')
            else:
                print('Player 1 win')
            break



if __name__ == '__main__':
    main_logic(6, 7)

