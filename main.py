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

def check_win(x): # # Argument Count Card
    global player_win, bot_win
    if x == 2:
        CardPlayer = '\t' + player[0]['Emoji'] + '\t' + player[1]['Emoji']
        CardBot = '\t' + bot[0]['Emoji'] + '\t' + bot[1]['Emoji']
        if point_player >= 8 or point_bot >= 8:
            if point_player > point_bot:
                print('Your Point :' , point_player, '\nYour Card : ' , CardPlayer)
                print('Bot Point :' , point_bot, '\nBot Card : ' , CardBot)
                if player[0]['Suit'] == player[1]['Suit']:
                    print('You Win Pok{}Deng'.format(point_player))
                    player_win = player_win + 1
                else:
                    print('You Win Pok{}'.format(point_player))
                    player_win = player_win + 1
            elif point_player < point_bot: 
                print('Your Point :' , point_player, '\nYour Card : ' , CardPlayer)
                print('Bot Point :' , point_bot, '\nBot Card : ' , CardBot)
                if bot[0]['Suit'] == bot[1]['Suit']:
                    print('Bot Win Pok{}Deng'.format(point_bot))
                    bot_win = bot_win + 1
                else:
                    print('Bot Win Pok{}'.format(point_bot))
                    bot_win = bot_win + 1
            elif point_player == point_bot:
                print('Your Point :' , point_player, '\nYour Card : ' , CardPlayer)
                print('Bot Point :' , point_bot, '\nBot Card : ' , CardBot)
                print('Draw')
            player.clear()
            bot.clear()
            print('Clear Card on hand')
            sleep(2)
            continue_game()
        player_third_card()
    elif x == 3:
        CardPlayer = '\t' + player[0]['Emoji'] + '\t' + player[1]['Emoji'] + '\t' + player[2]['Emoji']
        BotPlayer = '\t' + bot[0]['Emoji'] + '\t' + bot[1]['Emoji'] + '\t' + bot[2]['Emoji']
        print('Your Point :' , point_player, '\nYour Card : ' , CardPlayer)
        print('Bot Point :' , point_bot, '\nBot Card : ' , BotPlayer)
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
    
def player_third_card():    
    global point_player
    if point_player < 8:
        player_draw = input('Draw more? [D] Draw [S] Stay : ')
        if player_draw == 'D' or player_draw == 'd':
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