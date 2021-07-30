import random
from time import sleep
import os
from Modules.origin_deck import *
# from checkwin import *
import unittest

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

def check_win(x):
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
    if x == 3:
        CardPlayer = '\t' + player[0]['Emoji'] + '\t' + player[1]['Emoji'] + '\t' + player[2]['Emoji']
        CardBot = '\t' + bot[0]['Emoji'] + '\t' + bot[1]['Emoji'] + '\t' + bot[2]['Emoji']
        print('Your Point :' , point_player, '\nYour Card : ' , CardPlayer)
        print('Bot Point :' , point_bot, '\nBot Card : ' , CardBot)
        psort = []
        for i in player:
            psort.append(i['Card'])
        psort.sort()
        scp = psort[0]+psort[1]+psort[2]
        # print(scp)

        bsort = []
        for x in bot:
            bsort.append(x['Card'])
        bsort.sort()
        scb = bsort[0]+bsort[1]+bsort[2]

        xcard = ['23A', '234', '345', '456', '567', '678', '789', '1089', '109J', '10JQ', 'JKQ']
        xcard2 = ['JQQ', 'JKK', 'JJQ', 'JJK', 'KKQ', 'KQQ']
        xcheck = 0
        for xc in range(len(xcard)):
            if xcard[xc] == scp or xcard[xc] == scb:
                # xcheck = 1
                # break
        for xs in range(len(xcard2)):
            if xcard2[xs] == scp or xcard2[xs] == scb:
                xcheck = 2
                break
        if xcheck == 1:
            if scp != scb:
                for i in range(len(xcard)):
                    if scp == xcard[i]:
                        if player[0]['Suit'] == player[1]['Suit'] == player[2]['Suit']:
                            print('Pเรียงฟลัช')
                        elif scp == xcard[i]:
                            print('Pเรียง')
                    elif scb == xcard[i]:
                        if bot[0]['Suit'] == bot[1]['Suit'] == bot[2]['Suit']:
                            print('Bเรียงฟลัช')
                        elif scb == xcard[i]:
                            print('Bเรียง')
                    else:
                        print('เรียงเสมอ')
            elif scp == scb:
                print('เรียงเสมอ')
        elif xcheck == 2:
            if scp == 'JQQ' or scp == 'JKK' or scp == 'JJQ' or scp == 'JJK' or scp == 'KKQ' or scp == 'KQQ':
                print('Pสามเหลือง')
            elif scb == 'JQQ' or scb == 'JKK' or scb == 'JJQ' or scb == 'JJK' or scb == 'KKQ' or scb == 'KQQ':
                print('Bสามเหลือง')
        else:
            if point_player > point_bot:
                if player[0]['Suit'] == player[1]['Suit'] != player[2]['Suit']:
                    print('Pสองเด้ง')
                elif player[0]['Suit'] == player[1]['Suit'] == player[2]['Suit']:
                    print('Pสามเด้ง')
                else:
                    print('Pปกติ')
            elif point_player < point_bot: 
                if bot[0]['Suit'] == bot[1]['Suit'] and bot[2]['Card'] == 'None':
                    print('Bสองเด้ง')
                elif bot[0]['Suit'] == bot[1]['Suit'] == bot[2]['Suit']:
                    print('Bสามเด้ง')
                else:
                    print('Bปกติ')
            elif point_player == point_bot:
                print('เสมอ')
        
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
            
def Testsys():
    global player, bot , point_player, point_bot
    # # Player None Card
    # player = [
    #     {'Card':'', 'Suit':'', 'Point': 0, 'Emoji' : '', 'Imgage':''},
    #     {'Card':'', 'Suit':'', 'Point': 0, 'Emoji' : '', 'Imgage':''},
    #     {'Card':'', 'Suit':'', 'Point': 0, 'Emoji' : '', 'Imgage':''}
    # ]
    # # เรียงฟลัช
    # player = [
    #     {'Card':'A', 'Suit':'Clubs', 'Emoji' : 'A♣', 'Unicode': '🃑', 'Point': 1, 'Imgage':'Ac.png'},
    #     {'Card':'2', 'Suit':'Clubs', 'Emoji' : '2♣', 'Unicode': '🃒', 'Point': 2, 'Imgage':'2c.png'},
    #     {'Card':'3', 'Suit':'Clubs', 'Emoji' : '3♣', 'Unicode': '🃓', 'Point': 3, 'Imgage':'3c.png'}
    # ]
    # # เรียง
    player = [
        {'Card':'A', 'Suit':'Clubs', 'Emoji' : 'A♣', 'Unicode': '🃑', 'Point': 1, 'Imgage':'Ac.png'},
        {'Card':'2', 'Suit':'Clubs', 'Emoji' : '2♣', 'Unicode': '🃒', 'Point': 2, 'Imgage':'2c.png'},
        {'Card':'3', 'Suit':'Diamonds', 'Emoji' : '3♦', 'Unicode': '🃃', 'Point': 3, 'Imgage':'3d.png'}
    ]
    # # สามเหลือง
    # KKQ QKK = KKQ
    # player = [
    #     {'Card':'K', 'Suit':'Hearts', 'Emoji' : 'K♥', 'Unicode': '🂾', 'Point': 0, 'Imgage':'kh.png'},
    #     {'Card':'K', 'Suit':'Spades', 'Emoji' : 'K♠', 'Unicode': '🂮', 'Point': 0, 'Imgage':'ks.png'}, 
    #     {'Card':'Q', 'Suit':'Hearts', 'Emoji' : 'Q♥', 'Unicode': '🂽', 'Point': 0, 'Imgage':'qh.png'}
    # ]
    # KKJ JKK = JKK
    # QQJ JQQ = JQQ
    # KQQ QQK = KQQ
    # JJQ QJJ = JJQ
    # JJK KJJ = JJK
    # player = [
    #     {'Card':'K', 'Suit':'Clubs', 'Emoji' : 'K♣', 'Unicode': '🃞', 'Point': 0, 'Imgage':'kc.png'},
    #     {'Card':'J', 'Suit':'Clubs', 'Emoji' : 'J♣', 'Unicode': '🃛', 'Point': 0, 'Imgage':'jc.png'},  
    #     {'Card':'Q', 'Suit':'Hearts', 'Emoji' : 'Q♥', 'Unicode': '🂽', 'Point': 0, 'Imgage':'qh.png'}
    # ]
    # # ปกติ 2 เด้ง 7 แต้ม
    # player = [
    #     {'Card':'A', 'Suit':'Clubs', 'Emoji' : 'A♣', 'Unicode': '🃑', 'Point': 1, 'Imgage':'Ac.png'},
    #     {'Card':'6', 'Suit':'Clubs', 'Emoji' : '6♣', 'Unicode': '🃖', 'Point': 6, 'Imgage':'6c.png'},
    #     {'Card':'', 'Suit':'', 'Point': 0, 'Emoji' : '', 'Imgage':''}
    # ]
    # # ปกติ 3 เด้ง 7 แต้ม
    # player = [
    #     {'Card':'A', 'Suit':'Clubs', 'Emoji' : 'A♣', 'Unicode': '🃑', 'Point': 1, 'Imgage':'Ac.png'},
    #     {'Card':'2', 'Suit':'Clubs', 'Emoji' : '2♣', 'Unicode': '🃒', 'Point': 2, 'Imgage':'2c.png'},
    #     {'Card':'4', 'Suit':'Clubs', 'Emoji' : '4♣', 'Unicode': '🃔', 'Point': 4, 'Imgage':'4c.png'}
    # ]
    # # ปกติ
    # player = [
    #     {'Card':'A', 'Suit':'Clubs', 'Emoji' : 'A♣', 'Unicode': '🃑', 'Point': 1, 'Imgage':'Ac.png'},
    #     {'Card':'3', 'Suit':'Clubs', 'Emoji' : '3♣', 'Unicode': '🃓', 'Point': 3, 'Imgage':'3c.png'},
    #     {'Card':'A', 'Suit':'Spades', 'Emoji' : 'A♠', 'Unicode': '🂡', 'Point': 1, 'Imgage':'As.png'}
    # ]
    point_player = ((player[0]['Point'] + player[1]['Point'] + player[2]['Point']) % 10)

    # # Bot None Card
    # bot = [
    #     {'Card':'', 'Suit':'', 'Point': 0, 'Emoji' : '', 'Imgage':''},
    #     {'Card':'', 'Suit':'', 'Point': 0, 'Emoji' : '', 'Imgage':''},
    #     {'Card':'', 'Suit':'', 'Point': 0, 'Emoji' : '', 'Imgage':''}
    # ]
    # # เรียงฟลัช
    # bot = [
    #     {'Card':'A', 'Suit':'Clubs', 'Emoji' : 'A♣', 'Unicode': '🃑', 'Point': 1, 'Imgage':'Ac.png'},
    #     {'Card':'2', 'Suit':'Clubs', 'Emoji' : '2♣', 'Unicode': '🃒', 'Point': 2, 'Imgage':'2c.png'},
    #     {'Card':'3', 'Suit':'Clubs', 'Emoji' : '3♣', 'Unicode': '🃓', 'Point': 3, 'Imgage':'3c.png'}
    # ]
    # # เรียง
    bot = [
        {'Card':'4', 'Suit':'Clubs', 'Emoji' : '4♣', 'Unicode': '🃔', 'Point': 4, 'Imgage':'4c.png'},
        {'Card':'2', 'Suit':'Clubs', 'Emoji' : '2♣', 'Unicode': '🃒', 'Point': 2, 'Imgage':'2c.png'},
        {'Card':'3', 'Suit':'Diamonds', 'Emoji' : '3♦', 'Unicode': '🃃', 'Point': 3, 'Imgage':'3d.png'}
    ]
    # # สามเหลือง
    # KKQ QKK = KKQ
    # bot = [
    #     {'Card':'K', 'Suit':'Hearts', 'Emoji' : 'K♥', 'Unicode': '🂾', 'Point': 0, 'Imgage':'kh.png'},
    #     {'Card':'K', 'Suit':'Spades', 'Emoji' : 'K♠', 'Unicode': '🂮', 'Point': 0, 'Imgage':'ks.png'}, 
    #     {'Card':'Q', 'Suit':'Hearts', 'Emoji' : 'Q♥', 'Unicode': '🂽', 'Point': 0, 'Imgage':'qh.png'}
    # ]
    # KKJ JKK = JKK
    # QQJ JQQ = JQQ
    # KQQ QQK = KQQ
    # JJQ QJJ = JJQ
    # JJK KJJ = JJK
    # bot = [
    #     {'Card':'K', 'Suit':'Clubs', 'Emoji' : 'K♣', 'Unicode': '🃞', 'Point': 0, 'Imgage':'kc.png'},
    #     {'Card':'J', 'Suit':'Clubs', 'Emoji' : 'J♣', 'Unicode': '🃛', 'Point': 0, 'Imgage':'jc.png'},  
    #     {'Card':'Q', 'Suit':'Hearts', 'Emoji' : 'Q♥', 'Unicode': '🂽', 'Point': 0, 'Imgage':'qh.png'}
    # ]
    # # ปกติ 2 เด้ง 7 แต้ม
    # bot = [
    #     {'Card':'A', 'Suit':'Clubs', 'Emoji' : 'A♣', 'Unicode': '🃑', 'Point': 1, 'Imgage':'Ac.png'},
    #     {'Card':'6', 'Suit':'Clubs', 'Emoji' : '6♣', 'Unicode': '🃖', 'Point': 6, 'Imgage':'6c.png'},
    #     {'Card':'', 'Suit':'', 'Point': 0, 'Emoji' : '', 'Imgage':''}
    # ]
    # # ปกติ 3 เด้ง 7 แต้ม
    # bot = [
    #     {'Card':'A', 'Suit':'Clubs', 'Emoji' : 'A♣', 'Unicode': '🃑', 'Point': 1, 'Imgage':'Ac.png'},
    #     {'Card':'2', 'Suit':'Clubs', 'Emoji' : '2♣', 'Unicode': '🃒', 'Point': 2, 'Imgage':'2c.png'},
    #     {'Card':'4', 'Suit':'Clubs', 'Emoji' : '4♣', 'Unicode': '🃔', 'Point': 4, 'Imgage':'4c.png'}
    # ]
    # # ปกติ
    # bot = [
    #     {'Card':'A', 'Suit':'Clubs', 'Emoji' : 'A♣', 'Unicode': '🃑', 'Point': 1, 'Imgage':'Ac.png'},
    #     {'Card':'3', 'Suit':'Clubs', 'Emoji' : '3♣', 'Unicode': '🃓', 'Point': 3, 'Imgage':'3c.png'},
    #     {'Card':'A', 'Suit':'Spades', 'Emoji' : 'A♠', 'Unicode': '🂡', 'Point': 1, 'Imgage':'As.png'}
    # ]
    point_bot = ((bot[0]['Point'] + bot[1]['Point'] + bot[2]['Point']) % 10)

    check_win(3)
        

if __name__ == "__main__":
    # create_new_deck()
    Testsys()