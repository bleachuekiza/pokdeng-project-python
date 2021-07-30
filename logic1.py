player = [
    {'Card':'8'},
    {'Card':'9'},
    {'Card':'7'}
    ]

psort = []
for i in player:
    psort.append(i['Card'])
psort.sort()
scp = psort[0]+psort[1]+psort[2]

bsort = []
for x in bot:
    bsort.append(i['Card'])
bsort.sort()
scb = bsort[0]+bsort[1]+bsort[2]

if scp != scb:
    if scp == '23A' or scp == '234' or scp == '345' or scp == '456' or scp == '567' or scp == '678' or scp == '789' or scp == '1089' or scp == '109J' or scp == '10JQ':
        if player[0]['Suit'] == player[1]['Suit'] == player[2]['Suit']:
            print('เรียงฟลัช')
        else:
            print('เรียง')
    elif scb == '23A' or scb == '234' or scb == '345' or scb == '456' or scb == '567' or scb == '678' or scb == '789' or scb == '1089' or scb == '109J' or scb == '10JQ':
        if bot[0]['Suit'] == bot[1]['Suit'] == bot[2]['Suit']:
            print('เรียงฟลัช')
        else:
            print('เรียง')
    elif scp == 'JKQ':
        print('สามเหลือง')
    elif scb == 'JKQ':
        print('สามเหลือง')
else:
    if player[0]['Suit'] == player[1]['Suit'] and player[2]['Card'] == 'None':
        print('สองเด้ง')
    elif player[0]['Suit'] == player[1]['Suit'] == player[2]['Suit']:
        print('สามเด้ง')
    else:
        print('ปกติ')