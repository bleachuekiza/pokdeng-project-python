import random
from time import sleep
import os
from Modules.origin_deck import *
from Modules.module_checkwin import *

clear = lambda: os.system('cls')

deck_loop = []
player = []
point_player = 0
player_win = 0
bot = []
point_bot = 0
bot_win = 0

def create_new_deck():
    global deck_loop, point_player, point_bot
    sleep(2)
    point_player = 0
    point_bot = 0
    deck_loop = deck.copy()
    random_card('first')

def random_card(x):
    global point_player, point_bot
    if x == 'first':
        clear()
        for x in range(2):
            for i in range(2):
                if i == 1:
                    randomcard = random.randint(0, len(deck_loop)-1)
                    print('[BOT] Draw Card')
                    bot.append(deck_loop[randomcard])
                    deck_loop.pop(randomcard)
                    sleep(1)
                else:
                    randomcard = random.randint(0, len(deck_loop)-1)
                    print('Draw Card :\t', deck_loop[randomcard]['Emoji'])
                    player.append(deck_loop[randomcard])
                    deck_loop.pop(randomcard)
                    sleep(1)
        # # Calculator Point
        point_player = (player[0]['Point'] + player[1]['Point']) % 10
        point_bot = (bot[0]['Point'] + bot[1]['Point']) % 10
        print('Your Point :\t', point_player)
        sleep(1)
        check_win(2)
    elif x == 'second':
        randomcard = random.randint(0, len(deck_loop)-1)
        print('Draw Card :\t', deck_loop[randomcard]['Emoji'])
        player.append(deck_loop[randomcard])
        deck_loop.pop(randomcard)
        sleep(1)
        point_player = ((player[0]['Point'] + player[1]['Point'] + player[2]['Point']) % 10)
        bot_third_card()
    
def player_third_card():    
    global point_player
    if point_player < 8:
        player_draw = input('Draw more? [D] Draw [S] Stay : ')
        if player_draw in ['D', 'd']:
            random_card('second')
        else:
            print('You Stay')
            player.append(NoneCard)
            sleep(1)
            bot_third_card()
    
def bot_third_card():  
    global point_bot
    if point_bot < 5:
        randomcard = random.randint(0, len(deck_loop)-1)
        print('[BOT] Draw more')
        bot.append(deck_loop[randomcard])
        deck_loop.pop(randomcard)
        point_bot = ((bot[0]['Point'] + bot[1]['Point'] + bot[2]['Point']) % 10)
        sleep(1)
        check_win(3)
    else:
        print('[BOT] Stay')
        bot.append(NoneCard)
        sleep(1)
        check_win(3)

def check_win(x):
    global player_win, bot_win
    Mcheckwin = Module_check_win(x, player, point_player, bot, point_bot)
    player_win = player_win + Mcheckwin[0]
    bot_win = bot_win + Mcheckwin[1]
    if Mcheckwin[2] == 1:
        player_third_card()
    else:
        player.clear()
        bot.clear()
        print('Clear Card on hand')
        sleep(2)
        continue_game()

def continue_game():
    while True:
        con = input('[C] Continue [X] Exit : ')
        if con in ['c', 'C']:
            print('Starting new game')
            create_new_deck()
        elif con in ['x', 'X']:
            print('Close Game')
            print('You Win :\t', player_win, '\tRound\nBot Win :\t', bot_win, '\tRound')
            sleep(2)
            exit()

if __name__ == "__main__":
    create_new_deck()