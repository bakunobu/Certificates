import random
import os


# needs for sh: command not found error handling
class ConsoleClearError(Exception):
    '''
    Exception raised if command os.system('cls') doesn\'t execute correctly
    (in case one uses Linux or MacOS: not Linux)
    
    Attrs:
    ======
    response: int
    a result of os.system('cls') execution (0 if sucessful)
    
    message: explanation of the error
    '''
    
    def __init__(self, response:int, 
                 message:str='\'cls\' can\'t be executed, use \'clear\'') -> None:
        self.response = response
        self.message = message
        super().__init__(self.message)

        
# ValueError handling
def choose_option() -> int:
    print('Please choose an option:')
    print('\t1. Play with computer')
    print('\t2. Play with another player')
    print('\t0. Quit')
    while True:
        try:
            answ = int(input('Your choise: '))
            if 0 <= answ <= 2:
                return(answ)
        except ValueError:
            print('Please use integers (0-2)')


words = ['grammar', 'sherif', 'jewellery', 'freedom',
             'rechargeable', 'before', 'correctly',]


class HangmanGame:

    def __init__(self, word_dict:list=words, two_pl:bool=False):
        self.two_pl = two_pl
        # first Error Handling
        try:
            self.words = word_dict
        except NameError:
            self.words = ['hangman', 'error', 'handling', 'homework']
        self.attempts = 0
        self.guess = []
        self.hang_ico = {0:'''
                _____
                |
                |
                |
                |
                -----
                ''',
                1: '''
                _____
                |   |
                |
                |
                |
                -----
                ''',
                2: '''
                _____
                |   |
                |   0
                |
                |
                -----
                ''',
                3:'''
                _____
                |   |
                |   0
                |   |
                |
                -----
                ''',
                4:'''
                _____
                |   |
                |   0
                |  -|
                |
                -----
                ''',
                5:'''
                _____
                |   |
                |   0
                |  -|-
                |
                -----
                ''',
                6:'''
                _____
                |   |
                |   0
                |  -|-
                |  /
                -----
                ''',
                7:'''
                _____
                |   |
                |   0
                |  -|-
                |  / \\
                -----
                ''',
                8:'''
                _____
                |   |
                |   X
                |  -|-
                |  / \\
                -----
                '''}


    def clear_screen(self) -> None:
        # custom exception raise and handling
        try:
            a = os.system('cls')
            if a != 0:
                raise ConsoleClearError(a)
        except ConsoleClearError:
            os.system('clear')
                
        
    def choose_word(self) -> str:
        if self.two_pl:
            self.word = input('Type in a word to guess: ').lower()
            self.clear_screen()
        
        else:
            self.word = random.choice(self.words)

    
    def create_filler(self) -> None:
        self.filler = ['-' for x in self.word]
        
    
    def create_word_dict(self) -> None:
        self.letters = dict()
        for i in range(len(self.word)):
            if self.word[i] not in self.letters.keys():
                self.letters[self.word[i]] = [i,]
            
            else:
                self.letters[self.word[i]].append(i)
                
    
    def update_filler(self, letter:str) -> None:
        for i in self.letters[letter]:
            self.filler[i] = letter
            
        
    def guess_letter(self) -> str:
        if self.guess:
            print('letters used:', end=' ')
            print(* self.guess)
        while True:
            letter = input('Guess a letter: ')
            if letter.lower() not in self.guess:
                self.guess.append(letter.lower())
                return(letter.lower())
            
            else:
                print('You\'ve tried this one already!')
    
    
    def game_logic(self):
        print('Welcome to the game of Hangman')
        print('Rules can be fiond on https://www.wikihow.com/Play-Hangman')
        self.choose_word()
        self.create_filler()
        self.create_word_dict()
        while self.attempts < 8:
            letter = self.guess_letter()
            if letter in self.word:
                print('That\'s correct')
                self.update_filler(letter)
                print(* self.filler, sep='')
                if set(list(self.word)).issubset(self.guess):
                    print('You win!')
                    break
            
            else:
                self.attempts += 1
                print(self.hang_ico[self.attempts])
                if self.attempts == 8:
                    print('You lose')
                    print('I\'ve guessed {}'.format(self.word))
                
                else:
                    print(* self.filler, sep='')


if __name__ == '__main__':
    
    while True:
        answer = input('Wanna play? (y to play, q to quit): ').lower()
        if answer == 'q':
            break

        option = choose_option()
        if option == 0:
            break
        
        elif option == 1:
            game = HangmanGame()

        else:
            game = HangmanGame(two_pl=True)
        
        game.game_logic()

