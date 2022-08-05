with open(f'./saves/map1.txt') as f:
    with open(f'./saves/fix.txt', 'w') as fw:
        for line in f:
            n = int(line)
            tw = 0
            if (n == 4):
                tw = 5
            elif (n == 5):
                tw = 6
            elif (n == 6):
                tw = 7
            elif (n == 7):
                tw = 8
            elif (n == 8):
                tw = 9
            elif (n == 9):
                tw = 10
            elif (n == 10):
                tw = 11
            elif (n == 11):
                tw = 12
            elif (n == 12):
                tw = 13
            elif (n == 13):
                tw = 14
            elif (n == 14):
                tw = 15
            elif (n == 15):
                tw = 16
            elif (n == 16):
                tw = 17
            elif (n == 17):
                tw = 18
            elif (n == 18):
                tw = 19
            elif (n == 19):
                tw = 20
            elif (n == 20):
                tw = 4
            else:
                tw = n

            fw.write(f"{str(tw)}\n")