import random
from time import sleep
import os
from Modules.module_deck import *
from Modules.module_checkwin import *
import pygame

clear = lambda: os.system('cls')

status_table = 'hide'
deck_loop = []
cardloca = [
    {
        'name':'Player',
        'win':0,
        'cards':[
            NoneCard, NoneCard, NoneCard
        ]
    },
    {
        'name':'Dealer',
        'win':0,
        'cards':[
            NoneCard, NoneCard, NoneCard
        ]
    }
]

def main():
    global deck_loop
    deck_loop = create_new_deck()
    random_card()

def random_card():
    global status_table
    status_table = 'hide'
    clear()
    for x in range(2):
        for i in range(2):
            randomcard = random.randint(0, len(deck_loop)-1)
            print('[SYS] {} Draw'.format(cardloca[i]['name']))
            cardloca[i]['cards'][x] = deck_loop[randomcard]
            deck_loop.pop(randomcard)
            sleep(1)
    sleep(1)
    check_win(2)
    
def player_third_card():
    check_press_key = True
    if point_player < 8:
        print('Press [D]Draw [S]Stay')
        while check_press_key:
            pygame.time.delay(5)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_d]:
                check_press_key = False
                randomcard = random.randint(0, len(deck_loop)-1)
                print('Draw Card :\t', deck_loop[randomcard]['Emoji'])
                cardloca[0]['cards'][2] = deck_loop[randomcard]
                deck_loop.pop(randomcard)
                sleep(1)
                bot_third_card()
            if keys[pygame.K_s]:
                check_press_key = False
                print('You Stay')
                sleep(1)
                bot_third_card()
    
def bot_third_card():
    if point_bot < 5:
        randomcard = random.randint(0, len(deck_loop)-1)
        print('[BOT] Draw more')
        cardloca[1]['cards'][2] = deck_loop[randomcard]
        deck_loop.pop(randomcard)
        sleep(1)
        check_win(3)
    else:
        print('[BOT] Stay')
        sleep(1)
        check_win(3)

def check_win(x):
    global point_player, point_bot, status_table
    point_player = (cardloca[0]['cards'][0]['Point'] + cardloca[0]['cards'][1]['Point'] + cardloca[0]['cards'][2]['Point']) % 10
    point_bot = (cardloca[1]['cards'][0]['Point'] + cardloca[1]['cards'][1]['Point'] + cardloca[1]['cards'][2]['Point']) % 10
    Mcheckwin = Module_check_win(x, cardloca[0]['cards'], point_player, cardloca[1]['cards'], point_bot)
    cardloca[0]['win'] = cardloca[0]['win'] + Mcheckwin[0]
    cardloca[1]['win'] = cardloca[1]['win'] + Mcheckwin[1]
    if Mcheckwin[2] == 1:
        print('Your Point :\t', point_player)
        player_third_card()
    else:
        status_table = 'show'
        continue_game()

def continue_game():
    global point_player, point_bot, deck_loop
    check_press_key = True
    print('Press [C] Continue [X] Exit')
    while check_press_key:
        pygame.time.delay(5)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_c]:
            check_press_key = False
            cardloca[0]['cards'] = [NoneCard, NoneCard, NoneCard]
            cardloca[1]['cards'] = [NoneCard, NoneCard, NoneCard]
            print('Clear Card on hand')
            sleep(1.5)
            deck_loop = create_new_deck()
            random_card()
        if keys[pygame.K_x]:
            check_press_key = False
            print('Close Game')
            print('You Win :\t', cardloca[0]['win'], '\tRound\nBot Win :\t', cardloca[1]['win'], '\tRound')
            sleep(2)
            exit()

def status_show_cards():
    return status_table