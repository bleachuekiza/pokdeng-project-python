import random
from time import sleep
import os
from Modules.origin_deck import *

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
    random_card()

def random_card():
    global point_player, point_bot
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
    point_player = (player[0]['Point'] + player[1]['Point']) % 10
    point_bot = (bot[0]['Point'] + bot[1]['Point']) % 10
    sleep(1)
    check_win()

def check_win():
    global player_win, bot_win
    CardPlayer = '\t' + player[0]['Emoji'] + '\t' + player[1]['Emoji']
    CardBot = '\t' + bot[0]['Emoji'] + '\t' + bot[1]['Emoji']
    if point_player >= 8 or point_bot >= 8:
        if point_player > point_bot:
            print('Your Point :' , point_player, '\nYour Card : ' , CardPlayer)
            print('Bot Point :' , point_bot, '\nBot Card : ' , CardBot)
            sleep(2)
            print('You Win Pok{}'.format(point_player))
            player_win = player_win + 1
        elif point_player < point_bot: 
            print('Your Point :' , point_player, '\nYour Card : ' , CardPlayer)
            print('Bot Point :' , point_bot, '\nBot Card : ' , CardBot)
            sleep(2)
            print('Bot Win Pok{}'.format(point_bot))
            bot_win = bot_win + 1
        elif point_player == point_bot:
            print('Your Point :' , point_player, '\nYour Card : ' , CardPlayer)
            print('Bot Point :' , point_bot, '\nBot Card : ' , CardBot)
            sleep(2)
            print('Draw')
        player.clear()
        bot.clear()
        print('Clear Card on hand')
        sleep(2)
        continue_game()
    else:
        print('Your Point :' , point_player, '\nYour Card : ' , CardPlayer)
        print('Bot Point :' , point_bot, '\nBot Card : ' , CardBot)
        sleep(2)
        if point_player > point_bot:
            print('You Win')
            player_win = player_win + 1
        elif point_player < point_bot: 
            print('Bot Win')
            bot_win = bot_win + 1
        elif point_player == point_bot:
            print('Draw')
        player.clear()
        bot.clear()
        print('Clear Card on hand')
        sleep(2)
        continue_game()

def continue_game():
    while True:
        con = input('[C] Continue [X] Exit : ')
        if con == 'c' or con == 'C':
            print('Starting new game')
            create_new_deck()
        elif con == 'x' or con == 'X':
            print('Close Game')
            print('You Win :\t', player_win, '\tRound\nBot Win :\t', bot_win, '\tRound')
            sleep(2)
            exit()

if __name__ == "__main__":
    create_new_deck()