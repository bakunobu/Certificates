# song info as a dict
fav_song = {'Artist': 'The Offspring',
            'Genre': 'punk rock',
            'Song': 'Walla Walla',
            'DurationInSeconds':177,
            'Language': 'English',
            'Album': 'Americana',
            'Year': 1998,
            'RollingStoneGuideScore': 3.5,
            'IsSingle': False}


# print info from a dict
def print_info(my_dict:dict) -> None:
    for k, v in my_dict.items():
        print(f'{k}: {v}')


#check func for an extra credit
def check_func(my_key:str, my_val:str) -> bool:
    if my_key in fav_song.keys():
        if str(fav_song.get(my_key)) == my_val:
            return(True)
    return(False)


# main game func
def guess_game() -> bool:
    while True:
        my_key = input('Please choose the field (q for quit): ')
        if my_key.lower() == 'q':
            break
        my_val = input('True to guess a value of this parameter: ')
        print(check_func(my_key, my_val))


