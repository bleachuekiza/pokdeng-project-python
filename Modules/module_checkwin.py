def Module_check_win(x, player, point_player, bot, point_bot):
    player_third_card = 0
    player_win = 0; bot_win = 0
    CardPlayer = '\t' + player[0]['Emoji'] + '\t' + player[1]['Emoji'] + '\t' + player[2]['Emoji']
    CardBot = '\t' + bot[0]['Emoji'] + '\t' + bot[1]['Emoji'] + '\t' + bot[2]['Emoji']
    if x == 2:
        if point_player >= 8 or point_bot >= 8:
            if point_player > point_bot:
                print('Your Point :\t' , point_player, '\nYour Card : ' , CardPlayer)
                print('Bot Point :\t' , point_bot, '\nBot Card : ' , CardBot)
                if player[0]['Suit'] == player[1]['Suit'] or player[0]['Card'] == player[1]['Card']:
                    print('Player win Pok{} (2 Deng)'.format(point_player))
                    player_win = player_win + 1
                else:
                    print('Player win Pok{}'.format(point_player))
                    player_win = player_win + 1
            elif point_player < point_bot: 
                print('Your Point :' , point_player, '\nYour Card : ' , CardPlayer)
                print('Bot Point :' , point_bot, '\nBot Card : ' , CardBot)
                if bot[0]['Suit'] == bot[1]['Suit'] or bot[0]['Card'] == bot[1]['Card']:
                    print('Bot Win Pok{} (2 Deng)'.format(point_bot))
                    bot_win = bot_win + 1
                else:
                    print('Bot Win Pok{}'.format(point_bot))
                    bot_win = bot_win + 1
            elif point_player == point_bot:
                print('Your Point :' , point_player, '\nYour Card : ' , CardPlayer)
                print('Bot Point :' , point_bot, '\nBot Card : ' , CardBot)
                print('Draw (Pok)')
        else:
            player_third_card = 1
    if x == 3:
        print('Your Point :' , point_player, '\nYour Card : ' , CardPlayer)
        print('Bot Point :' , point_bot, '\nBot Card : ' , CardBot)

        psort = []
        for i in player:
            psort.append(i['Card'])
        psort.sort()
        scp = psort[0]+psort[1]+psort[2]
        bsort = []
        for x in bot:
            bsort.append(x['Card'])
        bsort.sort()
        scb = bsort[0]+bsort[1]+bsort[2]

        xcard = ['23A', '234', '345', '456', '567', '678', '789', '1089', '109J', '10JQ', 'JKQ']
        xcard2 = ['JQQ', 'JKK', 'JJQ', 'JJK', 'KKQ', 'KQQ']
        tongcard = ['AAA', '222', '333', '444', '555', '666', '777', '888', '999', '101010', 'JJJ', 'QQQ', 'KKK']

        if scp in tongcard or scb in tongcard:
            if scp != scb:
                if scp in tongcard and scb not in tongcard:
                    print('Player win (Tong)')
                    player_win = player_win + 1
                elif scb in tongcard and scp not in tongcard:
                    print('Bot win (Tong)')
                    bot_win = bot_win + 1
                else:
                    print('1Draw (Tong)')
            elif scp == scb:
                print('2Draw (Tong)')
        elif scp in xcard or scb in xcard:
            if scp != scb:
                if scp in xcard and scb not in xcard:
                    if player[0]['Suit'] == player[1]['Suit'] == player[2]['Suit']:
                        print('Player win (Straight Flush)')
                        player_win = player_win + 1
                    else:
                        print('Player win (Straight)')
                        player_win = player_win + 1
                elif scb in xcard and scp not in xcard:
                    if bot[0]['Suit'] == bot[1]['Suit'] == bot[2]['Suit']:
                        print('Bot win (Straight Flush)')
                        bot_win = bot_win + 1
                    else:
                        print('Bot win (Straight)')
                        bot_win = bot_win + 1
                else:
                    print('1Draw (Straight)')
            elif scp == scb:
                print('2Draw (Straight)')
        elif scp in xcard2 or scp in xcard2:
            if scp != scb:
                if scp in xcard and scb not in xcard2:
                    print('Player win (Sam lueang)')
                    player_win = player_win + 1
                elif scb in xcard and scp not in xcard2:
                    print('Bot win (Sam lueang)')
                    bot_win = bot_win + 1
                else:
                    print('1Draw (Sam lueang)')
            elif scp == scb:
                print('2Draw (Sam lueang)')
        else:
            if point_player > point_bot:
                if player[0]['Suit'] == player[1]['Suit'] and player[2]['Suit'] == '' or player[0]['Card'] == player[1]['Card'] and player[2]['Card'] == '':
                    print('Player win {} (2 Deng)'.format(point_player))
                    player_win = player_win + 1
                elif player[0]['Suit'] == player[1]['Suit'] == player[2]['Suit']:
                    print('Player win {} (3 Deng)'.format(point_player))
                    player_win = player_win + 1
                else:
                    print('Player win {}'.format(point_player))
                    player_win = player_win + 1
            elif point_player < point_bot: 
                if bot[0]['Suit'] == bot[1]['Suit'] and bot[2]['Suit'] == '' or bot[0]['Card'] == bot[1]['Card'] and bot[2]['Card'] == '':
                    print('Bot win {} (2 Deng)'.format(point_bot))
                    bot_win = bot_win + 1
                elif bot[0]['Suit'] == bot[1]['Suit'] == bot[2]['Suit']:
                    print('Bot win {} (3 Deng)'.format(point_bot))
                    bot_win = bot_win + 1
                else:
                    print('Bot win {}'.format(point_bot))
                    bot_win = bot_win + 1
            elif point_player == point_bot:
                print('Draw (Normal)')
    return player_win, bot_win, player_third_card