import random

countInput = int(input('何回戦しますか: '))

win = 0
same = 0
lose = 0

print('')
print('じゃんけんスタート')
print('')

#1がグー、2がチョキ、3がパー
for i in range(countInput):
    userInput = int(input('グー=1 チョキ=2 パー=3: '))
    randomString = random.randint(1,3)
    if randomString==1:
        print('相手はグーを出しました')
        if userInput==1:
            print('あいこ')
            print('')
            same += 1
        elif userInput==2:
            print('負け')
            print('')
            lose += 1
        elif userInput==3:
            print('勝ち')
            print('')
            win += 1
    elif randomString==2:
        print('相手はチョキを出しました')
        if userInput==2:
            print('あいこ')
            print('')
            same += 1
        elif userInput==3:
            print('負け')
            print('')
            lose += 1
        elif userInput==1:
            print('勝ち')
            print('')
            win += 1
    elif randomString==3:
        print('相手はパーを出しました')
        if userInput==3:
            print('あいこ')
            print('')
            same += 1
        elif userInput==1:
            print('負け')
            print('')
            lose += 1
        elif userInput==2:
            print('勝ち')
            print('')
            win += 1

#結果発表
if countInput==win+same+lose:
    print('='*10,'最終結果','='*10)
    if win==same==lose or win==lose:
        print('あいこ')
    elif win>lose:
        print('勝ち')
    elif lose>win:
        print('まけ')