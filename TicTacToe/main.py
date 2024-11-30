import random
from examine import *
from DisplayModule import *
from LevelEasy import *
from LevelMedium import *
from LevelHard import *

# driver (MAIN) program
a = 0
b = 0
user1 = []
user2 = []
usernoone = []
scoreo1 = scoreo2 = 0
t11 = 'change'

while True:
    if(t11=='change'):
        print('Welcome  To Tic Tac Toe Game ')
        print('1. USER1 VS USER2')
        print('2. USER VS COMPUTER(recommended)')
        print('Enter Your Choise:', end=' ')

        while True:
            usch = input()
            if(usch==''):
                usch=2
                break
            try: 
                usch = int(usch)
            except:
                print('Invalid value !')
                print('enter value again(1/2):', end='')
                continue
            if(usch<1 or usch>2):
                print('Invalid value !')
                print('enter value again(1/2):', end='')
            else: 
                break
        uschlevel=None
        if(usch==2):
            print('1. Easy Level')
            print('2. Medium Level (recommended)')
            print('3. Hard Level')
            print('Enter Your Choise:', end='')
            while True: 
                uschlevel = input()
                if(uschlevel==''):
                    uschlevel=2
                    print()
                    break
                try:
                    uschlevel = int(uschlevel)
                except:
                    print('INVALID VALUE!')
                    print('enter value again(1/2/3):', end='')
                    continue
                if(uschlevel<1 or uschlevel>3):
                    print('INVALID VALUE!')
                    print('enter value again(1/2/3):', end='')
                else:
                    break
        print("ALL SET, LET'S START THE GAME!!!")
        print()
    printing1([None], user2)
    for o in range(5):
        usernoone = user1 + user2
        if(usch==1):
            print('User 1 -', end='')
        num=int(input(' Enter Value:'))
        for i in range(13):
            if(num not in usernoone):
                if(num<0 or num>9):
                    print('value out of range ,please enter value between 1-9:')
                    num=int(input())
                    continue
                user1.append(num)
                break
            else:
                print('sorry that value is used, plz enter another number:')
                num = int(input())
        printing1(user1, user2)
        g = examine(user1)
        if(g==0):
            if(usch==1): print('USER 1 WINS!!!')
            else: print('YOU WIN!!!')
            scoreo1 = scoreo1 + 1
            break
        if(o==4):
            print('DRAW')
            break
        #_#__#__#_#__#__#_
        usernoone = user1 + user2
        if(usch==1):
            num = int(input('User 2 - Enter Value'))
            for i in range(13):
                if(num not in usernoone):
                    if(num<0 or num>9):
                        print('value out of range ,please enter value between 1-9:')
                        num = int(input())
                        continue
                    user2.append(num)
                    break
                else:
                    print('sorry that value is used, plz enter another number:')
                    num=int(input()) 
        else:
            usernoone = user1 + user2
            if(o==0):#for first chance
                if(uschlevel==3):
                    user2.append(5)
                else:
                    if(user1[0]!=5):
                        for i in range(33):
                            pop = random.randrange(1,9)
                            if(pop!=user1[0]):
                                user2.append(pop)
                                break
                    else:
                        for i in range(33):
                            pop=random.randrange(1,9)
                            if((pop!=user1[0]) and (pop not in [2, 4, 6, 8])):
                                    user2.append(pop)
                                    break
            get, k = computer(user1, user2)
            got, l = computer(user2, user1)
            usernoone = user1 + user2
            pop = None
            if(l==2 and uschlevel!=1):#winning chance
                user2.append(got)
            elif(k==2 and uschlevel!=1):#defeating chance
                user2.append(get)
            elif(o==1 and uschlevel!=1):#4 din ki mehnat[#main code*]
                pop=main_o2(user1,user2)
                if(pop!=999): user2.append(pop)
            if(uschlevel==1): k=l=1
            if(k==1 and l==1 and o!=0 and pop==None):#ignore for first chance
                lst1_1, nc, c, lstc1_2 = ret_hvalue(user2, user1)
                lst2_1, nc1, c1, lstc2_1 = ret_hvalue(user1, user2)
                pop_1, pop_2 = stage2(user1, user2)
                pp, pp1 = stage2(user2, user1)
                if(c>0 and uschlevel!=1): user2.append(lstc1_2[0])
                elif(pop_1!=None and uschlevel!=1 ):
                    if(pop_2 in lstc2_1): user2.append(pop_2)
                    else: user2.append(pop_1)
                elif(pp!=None): user2.append(pp)
                else:
                    for i in range(33):            
                        pop=random.randrange(1,9)
                        if(pop not in usernoone):
                            user2.append(pop)
                            break
        printing1(user1, user2)
        g = examine(user2)
        if(g==0):
            if(usch==1): print('USER 2 WINS!!!')
            else: print('YOU LOOSE!')
            scoreo2=scoreo2+1
            break
    if(usch==1): print('USER1 SCORE >>> ',scoreo1,'                  USER2 SCORE >>> ',scoreo2)
    else: print('USER SCORE >>> ',scoreo1,'                  COMPUTER SCORE >>> ',scoreo2)
    print()
    t=input('If you want to play again enter y(yes) or else n(no):')
    if(t=='y' or t=='Y' or t==''):
        user1=[]
        user2=[]
        t11=input("enter 'change' to change the () or else press the enter key _")
        if(t11=='change'): scoreo1 = scoreo2 = 0
        continue
    elif(t=='n' or t=='N' or t=='no'):
        break
    else:
        print('invalid value enter, program break!')
        break
print('THANK YOU')