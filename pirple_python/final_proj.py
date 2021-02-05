"""
It\'s a variation of the War card game (https://en.wikipedia.org/wiki/War_(card_game))
is being playing in Russia that called Drunk Man (\'Pyanitsa\'). Description (in Russian):
(https://ru.wikipedia.org/wiki/%D0%9F%D1%8C%D1%8F%D0%BD%D0%B8%D1%86%D0%B0_(%D0%BA%D0%B0%D1%80%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F_%D0%B8%D0%B3%D1%80%D0%B0))
Can be played using 36, 52 or 54 card deck.


In this version we use only 36 and 52 card decks and a two player game and no card can\'t beat ace


The idea of the game (can be played by 2-8 players) is quite simple:
1) at the beginning of the game all the cards are being destributed among the players (in equal amounts);
2) players don\'t see their cards: they put the stacks of cards (faces down) in front of them;
3) on every turn all the players cast their upper cards and put it face up on the table - a player can't choose the order of cards being casted;
4) the player with the highest ranked card wins the turn (suites doesn\'t play any role) and takes all the cards played this turn
and put the cards to another stack that is called Beated (\'Otboy\');
4a) if there is a tie - that is two or more players has the highest ranked card of the same rank - contesting players cast one more card from the top of
their stacks while one has the card with a higher rank that his opponents do;
5) each set lasts as long as at least two players have cards in their main stacks (if a draw is being played during last turn the winner is being chosen randomly);
5a) if a player has any cards in his main stack at the end of a set he puts it on the top of his Beated stack;
6) if a player doesn't have any cards at the end the set (in his main or Beated stack) he's being pulled out of the game;
7) at the beginning of a new set players use their Beated stacks as their main stacks, shuffle their stacks and repeat steps (2-6) while there are at least two players in the game;
8) a player that collects all the deck cards in his hand wins the whole game.
"""

import random
import time

class Card:
    points = {'2':2, '3':3, '4':4, '5':5,
              '6':6, '7':7, '8':8, '9':9,
              '10':10, 'J':11, 'Q':12, 'K':13,
              'A':14, 'Joker':15}
    
    def __init__(self, card:str, faceup:bool=True,
                 point_dic:dict=points) -> None:
        self.suit = card[-1]
        self.rank = card[:-1]
        self.points = point_dic.get(self.rank, 0)
        self.is_faceup = faceup


    def __repr__(self) -> None:
        if self.is_faceup:
            if self.rank == 'Joker':
                return(repr(f'{self.rank}'))
            else:
                return(repr(f'{self.rank} {self.suit}'))
        else:
            return(repr('XX'))
        
        
# создаем колоду
def deck_generator(num_cards:int=36, need_joker:bool=False) -> list:
    suites = ['S', 'H', 'D', 'C']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9',
                 '10', 'J', 'Q', 'K', 'A']
    if num_cards == 36:
        deck = [Card(r+s) for s in suites for r in ranks[4:]]
    else:
        deck = [Card(r+s) for s in suites for r in ranks]
    if need_joker:
        for _ in range(2):
# technically Joker has its own Suite - 0, but we use a special repr stetement not to print it.
            deck.append(Card('Joker0'))
    return(deck) 


class GameDeck:

    def __init__(self, deck:list):
        self.deck = deck
        self.num_cards = len(deck)
        
        
    def shuffle(self) -> None:
        random.shuffle(self.deck)
        
        
    def cast(self) -> str:
        if self.deck:
            card = self.deck.pop()
            return(card)


class Hand(GameDeck):
    
    def __init__(self, deck:list=[]):
        GameDeck.__init__(self, deck)
    
    
    def get_card(self, card:Card) -> None:
        self.deck.append(card)
        
    
    def __repr__(self) -> None:
        return(repr(f'{len(self.deck)} cards'))
    

class Beated(Hand):
    
    def __init__(self, deck:list = []):
        Hand.__init__(self, deck)
    
    
    def shuffle(self) -> None:
        pass  
    
    
    def cast(self) -> str:
        pass
    
    
    def get_cards(self, cards:list) -> None:
        self.deck = self.deck + cards
        

class Player:
    
    def __init__(self, name:str, hand:list) -> None:
        self.name = name
        self.hand = Hand(hand)
        self.beated = Beated()
        self.score = len(self.hand.deck)
        
    def update_hand(self):
        self.hand = Hand(self.hand.deck + self.beated.deck)
        self.hand.shuffle()
        self.beated = Beated()
        self.score = len(self.hand.deck)


def option_chooser(question:str, show_menu:bool=False,
                   menu:str='',
                   int_output:bool=False,
                   low_lim:int=0, up_lim:int=2):
    
    if show_menu:
        print(menu)

    if int_output:
        while True:
            try:
                ans = int(input(question))
                if low_lim <= ans <= up_lim:
                    return(ans)
            
            except ValueError:
                print(f'Please use integers from range{low_lim}-{up_lim}!')
    
    else:
        ans = input(question)
        return(ans)


def type_name(player:str) -> str:
    name_quest = f'Enter {player} name: '
    name = option_chooser(name_quest)
    return(name)

if __name__ == '__main__':
    
    # geme flow
    
    while True:
        
        pl_1 = type_name('Player 1')
        pl_2 = type_name('Player 2')
        player_1 = Player(pl_1, [])
        player_2 = Player(pl_2, [])
        
        # 36 or 52 card deck
        
        deck_menu = '''
Please choose deck mode:
\t1. 36 card deck;
\t2. 52 card deck;
\t0. Quit.
        '''
        
        num_question = 'Which deck should be used? '
        num_cards = option_chooser(num_question, show_menu=True,
                                   menu=deck_menu, int_output=True)
        
        if num_cards == 0:
            break
        elif num_cards == 1:
            n_c = 36 
        else:
            n_c = 52     

        deck = deck_generator(n_c)
        playing_deck = GameDeck(deck)
        playing_deck.shuffle()

        for x in range(playing_deck.num_cards):
            card = playing_deck.cast()
            if x % 2 == 0:
                player_1.hand.get_card(card)
            else:
                player_2.hand.get_card(card)


        r = 1
        while player_1.hand.deck and player_2.hand.deck:
            print(f'Round {r}')
            j = min(len(player_1.hand.deck), len(player_2.hand.deck))
            stack = []
            for _ in range(1, j):
                print(f'Turn {_}')
                p_1_card = player_1.hand.cast()
                p_2_card = player_2.hand.cast()

                stack.append(p_1_card)
                stack.append(p_2_card)
                if _ % 2 != 0:
                    print(f'{player_1.name}\'s card:\n{p_1_card}')
                    print(f'{player_2.name}\'s card:\n{p_2_card}')
                        
                else:
                    print(f'{player_2.name}\'s card:\n{p_2_card}')
                    print(f'{player_1.name}\'s card:\n{p_1_card}')
                
                

                if p_1_card.points > p_2_card.points:
                    player_1.beated.get_cards(stack)
                    print(f'{player_1.name} wins this turn!')
                    stack = []
                
                elif p_2_card.points > p_1_card.points:
                    player_2.beated.get_cards(stack)
                    print(f'{player_2.name} wins this turn!')
                    stack = []
                
                else:
                    print('Draw')
                print('-----')
                time.sleep(0.2)
            print(f'Turn {j}')
            p_1_card = player_1.hand.cast()
            p_2_card = player_2.hand.cast()
            if j % 2 != 0:
                print(f'{player_1.name}\'s card:\n{p_1_card}')
                print(f'{player_2.name}\'s card:\n{p_2_card}')
                        
            else:
                print(f'{player_2.name}\'s card:\n{p_2_card}')
                print(f'{player_1.name}\'s card:\n{p_1_card}')
                
            stack.append(p_1_card)
            stack.append(p_2_card)
            if p_1_card.points > p_2_card.points:
                player_1.beated.get_cards(stack)
                print(f'{player_1.name} wins this turn!')
                stack = []
                
            elif p_2_card.points > p_1_card.points:
                player_2.beated.get_cards(stack)
                print(f'{player_2.name} wins this turn!')
                stack = []
            
            else:
                cast = random.randint(0,1)
                if cast:
                    player_1.beated.get_cards(stack)
                else:
                    player_2.beated.get_cards(stack)
                    
            
                    
            player_1.update_hand()
            player_2.update_hand()

            print(f'{player_1.name} score: {player_1.score}')
            print(f'{player_2.name} score: {player_2.score}')
            
            r+= 1
            print('* * *')
            time.sleep(1.0)
            
        if player_1.score == playing_deck.num_cards:
            print(f'{player_1.name} wins!')
        else:
            print(f'{player_2.name} wins!')
        
        new_game_menu = '''
Wanna play another game:
\t1. Yes
\t0. No
        '''
        new_game = option_chooser('Start new game? ', show_menu=True,
                                menu=new_game_menu, int_output=True,
                                low_lim=0, up_lim=1)
        if new_game == 0:
            print('Bye')
            break
        else:
            print('Starting new game')
            time.sleep(1)
        
