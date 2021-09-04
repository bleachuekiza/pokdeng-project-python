# -*- coding: utf-8 -*-

import pygame
import pygame.freetype
from threading import Thread
from game import *
pygame.init()

GAME_FONT = pygame.freetype.Font("tahomabd.ttf", 24)

pygame.display.set_caption('Pokdeng Game Card')
icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)
# # 720p
screen = pygame.display.set_mode((1280, 720))

bgload = pygame.image.load('assets/background.png')
bg = pygame.transform.scale(bgload, (1280, 720))
# # 720p

imgbackcard = 'assets/backcard.jpg'
load_backcard = pygame.image.load(imgbackcard)
position_dealer = [(528, 168), (548, 188), (573, 203)]
position_player1 = [(553, 423), (573, 443), (593, 463)]

card_dealer = ['None', 'None', 'None']
card_player1 = ['None', 'None', 'None']

def showcard(status):
    username = 'Player'
    if status == 'hide':
        # Player 1
        if username == cardloca[0]['name']:
            for i in range(3):
                load_card = pygame.image.load(cardloca[0]['cards'][i]['Imgage'])
                card_player1[i] = pygame.transform.scale(load_card, (90, 135))
        else:
            for i in range(3):
                if cardloca[0]['cards'][i]['Card'] != 'None':
                    card_player1[i] = pygame.transform.scale(load_backcard, (90, 135))
                else:
                    load_card = pygame.image.load(cardloca[0]['cards'][i]['Imgage'])
                    card_player1[i] = pygame.transform.scale(load_card, (90, 135))
        for i in range(3):
            if cardloca[1]['cards'][i]['Card'] != 'None':
                card_dealer[i] = pygame.transform.scale(load_backcard, (90, 135))
            else:
                load_card = pygame.image.load(cardloca[1]['cards'][i]['Imgage'])
                card_dealer[i] = pygame.transform.scale(load_card, (90, 135))

    elif status == 'show':
        for i in range(3):
            load_card = pygame.image.load(cardloca[0]['cards'][i]['Imgage'])
            card_player1[i] = pygame.transform.scale(load_card, (90, 135))
        for i in range(3):
            load_card = pygame.image.load(cardloca[1]['cards'][i]['Imgage'])
            card_dealer[i] = pygame.transform.scale(load_card, (90, 135))
    else:
        print('Show Card Error')

posX = 400
posY = 400

if __name__ == "__main__":
    Thread(target=main).start()
    run = True
    while run:
        x = score_win()
        dis_stu = status_game()
        win_stu = status_win()
        showcard(status_show_cards())
        pygame.time.delay(30)
        
        for eventget in pygame.event.get():
            pygame.display.flip()
            if eventget.type == pygame.QUIT:
                run = False
        ## ไว้สำหรับหาค่า X Y
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            posX-=5
        if keys[pygame.K_RIGHT]:
            posX+=5
        if keys[pygame.K_UP]:
            posY-=5
        if keys[pygame.K_DOWN]:
            posY+=5
        if keys[pygame.K_SPACE]:
            print('X {}\nY {}'.format(posX, posY))
        ## ไว้สำหรับหาค่า X Y

        screen.blit(bg, (0, 0))
        screen.blit(card_player1[0], position_player1[0])
        screen.blit(card_player1[1], position_player1[1])
        screen.blit(card_player1[2], position_player1[2])
        
        screen.blit(card_dealer[0], position_dealer[0])
        screen.blit(card_dealer[1], position_dealer[1])
        screen.blit(card_dealer[2], position_dealer[2])
        score_player, rect = GAME_FONT.render('Player Win:{}'.format(x[0]), (255, 255, 255))
        screen.blit(score_player, (330, 75))
        score_bot, rect = GAME_FONT.render('Bot Win:{}'.format(x[1]), (255, 255, 255))
        screen.blit(score_bot, (330, 120))
        if dis_stu == 'Tcard':
            text_surface3, rect = GAME_FONT.render('Press [D]Draw More [P]Pass', (255, 255, 255))
            screen.blit(text_surface3, (475, 350))
        elif dis_stu == 'Continue':
            text_surface3, rect = GAME_FONT.render('Press [C] New Game', (255, 255, 255))
            screen.blit(text_surface3, (520, 355))
        if win_stu != 'None':
            text_win, rect = GAME_FONT.render('{} Win'.format(win_stu), (255, 255, 255))
            screen.blit(text_win, (370, 210)
        # text_surface, rect = GAME_FONT.render('เทสภาษาไทย อิอ ตี้ ทั่ว อี้  อี่', (0, 0, 0))
        # screen.blit(text_surface, (posX, posY))
        pygame.display.update()
    pygame.quit()