from typing import Any

# writing options
file_options = {1: 'r',
                2: 'w',
                3: 'a'}


# interface options
editing_options ={1: 'read file',
                  2: 'clean and save new file',
                  3: 'add data to file',
                  4: 'edit file'}


def option_choice(my_dict:dict=editing_options) -> int:
    print('Please choose one option:')
    for k, v in my_dict.items():
        print(f'{k}: {v}')
    while True:
        try:
            option = int(user_input('Please choose (1-4): '))
            if 1 <= option <= 4:
                break
            else:
                print('No such an option!')
        except ValueError:
            print('Please use 1-4 keys!')
    return(option)


def user_input(message:str) -> Any:
    return(input(message))


def show_content(filename:str) -> None:
    with open(filename, 'r') as f:
        data = f.readlines()
        for line in data:
            print(line.strip('\n'))


def mod_file() -> None:
    choice = option_choice()
    if choice == 1:
        show_content(filename)
    elif choice == 4:
        edit_file(filename)
    else:
        content = user_input('Add a text to save: ')
        try:
            with open(filename, file_options.get(choice)) as f:
                f.write(content+'\n')
        except IOError:
            print('Something went wrong')


def replace_line(filename:str, max_num:int) -> None:
    while True:
        try:
            option = int(user_input('Please choose (0-{}): '.format(max_num-1)))
            if 0 <= option < max_num:
                break
        except ValueError:
            print('Please use num keys!')
    return(option)            
    

def create_file() -> None:
    filename = user_input('Create a new file: ')
    content = user_input('Add a text to save: ')
    with open(filename, 'w') as f:
        f.write(content+'\n')


def edit_file(filename: str) -> None:
    with open(filename, 'r') as f:
        lines = f.readlines()
        i = len(lines)
    print(f'{i} lines of text available')
    num_line = replace_line(filename, i)
    content = user_input('Add a text to save: ')
    lines[num_line] = content
    print(lines)
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line.strip('\n')+'\n')


def check_file_exists(filename) -> None:
    try:
        with open(filename) as f:
            pass
        mod_file()
    except IOError:
        print('File doesn\'t exist!')
        create_file()


if __name__ == '__main__':
    filename = user_input('Enter a file name: ')
    check_file_exists(filename)
    