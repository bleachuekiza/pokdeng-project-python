from main import player, point_player, bot, point_bot

def check_win(x):
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
        psort = []
        for i in player:
            psort.append(i['Card'])
        psort.sort()
        scp = psort[0]+psort[1]+psort[2]
        print(scp)

        bsort = []
        for x in bot:
            bsort.append(i['Card'])
        bsort.sort()
        scb = bsort[0]+bsort[1]+bsort[2]

        xcard = ['23A', '234', '345', '456', '567', '678', '789', '1089', '109J', '10JQ']

        if scp != scb:
            for i in range(len(xcard)):
                if scp == xcard[i]:
                    if player[0]['Suit'] == player[1]['Suit'] == player[2]['Suit']:
                        print('Pเรียงฟลัช')
                    else:
                        print('Pเรียง')
                elif scb == xcard[i]:
                    if bot[0]['Suit'] == bot[1]['Suit'] == bot[2]['Suit']:
                        print('Bเรียงฟลัช')
                    else:
                        print('Bเรียง')
                elif scp == 'JKQ':
                    print('Pสามเหลือง')
                elif scb == 'JKQ':
                    print('Bสามเหลือง')
        elif scp == scb:
            print('เสมอ')
        else:
            if point_player > point_bot:
                if player[0]['Suit'] == player[1]['Suit'] and player[2]['Card'] == 'None':
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