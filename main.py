import pygame
from threading import Thread
from game import *
pygame.init()

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


if __name__ == "__main__":
    Thread(target=main).start()
    run = True
    while run:
        # x = status_show_cards()
        showcard(status_show_cards())
        pygame.time.delay(30)
        
        for eventget in pygame.event.get():
            pygame.display.flip()
            if eventget.type == pygame.QUIT:
                run = False

        screen.blit(bg, (0, 0))
        screen.blit(card_player1[0], position_player1[0])
        screen.blit(card_player1[1], position_player1[1])
        screen.blit(card_player1[2], position_player1[2])
        
        screen.blit(card_dealer[0], position_dealer[0])
        screen.blit(card_dealer[1], position_dealer[1])
        screen.blit(card_dealer[2], position_dealer[2])
        pygame.display.update()
    pygame.quit()