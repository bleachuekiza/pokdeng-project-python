import random
from time import sleep
import os
from Modules.module_deck import *
from Modules.module_checkwin import *

clear = lambda: os.system('cls')

deck_loop = []
player = []; point_player = 0; player_win = 0
bot = []; point_bot = 0; bot_win = 0

def random_card():
    clear()
    # print(len(deck_loop))
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
    player.append(NoneCard)
    bot.append(NoneCard)
    sleep(1)
    check_win(2)
    
def player_third_card():  
    if point_player < 8:
        player_draw = input('Draw more? [D] Draw [S] Stay : ')
        if player_draw in ['D', 'd']:
            randomcard = random.randint(0, len(deck_loop)-1)
            print('Draw Card :\t', deck_loop[randomcard]['Emoji'])
            player[2]= deck_loop[randomcard]
            deck_loop.pop(randomcard)
            sleep(1)
            bot_third_card()
        else:
            print('You Stay')
            sleep(1)
            bot_third_card()
    
def bot_third_card():
    if point_bot < 5:
        randomcard = random.randint(0, len(deck_loop)-1)
        print('[BOT] Draw more')
        bot[2]= deck_loop[randomcard]
        deck_loop.pop(randomcard)
        sleep(1)
        check_win(3)
    else:
        print('[BOT] Stay')
        sleep(1)
        check_win(3)

def check_win(x):
    global player_win, bot_win
    point_player = (player[0]['Point'] + player[1]['Point'] + player[2]['Point']) % 10
    point_bot = (bot[0]['Point'] + bot[1]['Point'] + bot[2]['Point']) % 10
    Mcheckwin = Module_check_win(x, player, point_player, bot, point_bot)
    player_win = player_win + Mcheckwin[0]
    bot_win = bot_win + Mcheckwin[1]
    if Mcheckwin[2] == 1:
        print('Your Point :\t', point_player)
        player_third_card()
    else:
        player.clear(), bot.clear()
        print('Clear Card on hand')
        sleep(2)
        continue_game()

def continue_game():
    global point_player, point_bot, deck_loop
    while True:
        # print(len(deck_loop))
        con = input('[C] Continue [X] Exit : ')
        if con in ['c', 'C']:
            print('Starting new game')
            deck_loop = create_new_deck()
            sleep(2)
            random_card()
        elif con in ['x', 'X']:
            print('Close Game')
            print('You Win :\t', player_win, '\tRound\nBot Win :\t', bot_win, '\tRound')
            sleep(2)
            exit()

if __name__ == "__main__":
    deck_loop = create_new_deck()
    random_card()