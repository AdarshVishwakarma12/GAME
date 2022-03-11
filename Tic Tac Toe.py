import random
#DISPLAY
def printing1(user1, user2):
    user = user1 + user2
    if(None not in user1):
        print('user :', user1)
        print('computer :', user2)
    for i in range(1, 18):
        if(i==6 or i==12):
            for i in range(1, 19): print('_', end='')
            print()
        else:
            for j in range(1,18):                  
                if(j==6 or j==12): print('|',end='')
                else:
                    printing2(i,j,user,user1)
                    if(j==17): print()

def printing2(i, j, user, user1):
    p = [[1, 5], [1, 5], [1, 5], [7, 11], [7, 11], [7, 11], [13, 17], [13, 17], [13, 17]]
    q = [[1, 5], [7, 11], [13, 17]] * 3
    for k in range(9):
        if((i>=p[k][0] and i<=p[k][1]) and (j>=q[k][0] and j<=q[k][1])):
            k=k+1
            if(k in user): printing3(user1,k,i,j,p,q)
            else:
                k=k-1
                if(i == (p[k][0] + 2) and j == (q[k][0] + 2)): print(k + 1, end='')
                else: print(' ', end='')
#0 and cross function is at best!!!
def printing3(user1,k,i,j,p,q):
    if(k in user1):
        k=k-1
        if(i==p[k][0] or i==p[k][1]):
            if(j==q[k][0] or j==q[k][1]): print('*',end='')
            else: print(' ',end='')
        elif(i==(p[k][0]+1) or i==(p[k][1]-1)):
            if(j==(q[k][0]+1) or j==(q[k][1]-1)): print('*',end='')
            else: print(' ',end='')
        else:
            if(j==(q[k][0]+2)): print('*',end='')
            else: print(' ',end='')
    else:
        k=k-1
        if((i==p[k][0] or i==p[k][1]) and (j>=q[k][0] or j<=q[k][1])): print('*', end='')
        elif((i>p[k][0] and i<p[k][1]) and (j==q[k][0] or j==q[k][1])): print('*', end='')
        elif((i>p[k][0] and i<p[k][1]) and (j>q[k][0] and j<q[k][1])): print(' ', end='')
#to examine result
def examine(user):
    lst=[[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    a = len(user) 
    for i in range(8):
        b=0
        for j in range(0,3):
            for k in range(0,a):
                if(lst[i][j] == user[k]): b = b + 1
        if(b==3): return 0
def computer(user1,user2):#computer 
    usernoone = user1 + user2
    lst=[[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    a = len(user1) 
    for i in range(8):
        b=0
        for j in range(3):
            for k in range(a):
                if(lst[i][j] == user1[k]): b=b+1
            if(b==2):
                for do in range(0,3):
                    if((lst[i][do] not in user1) and(lst[i][do] not in usernoone)): return lst[i][do],b
    return None, 1

def stage2(user1, user2):
    usernoone = user1 + user2
    lst=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    a = len(user2) 
    for i in range(8):
        b=0
        for j in range(0,3):
            for k in range(0,a):
                if(lst[i][j]==user2[k]): b=b+1
            if(b==1):
                for p in range(0,3):
                    if(lst[i][p]in user2):
                        if(p==0): q, r=1, 2
                        if(p==1): q, r=0, 2
                        if(p==2): q, r=1, 0
                        if(lst[i][q] not in usernoone):
                            if(lst[i][r] not in usernoone): return lst[i][q],lst[i][r]
    return None, None

def predict(user1, user2, val):
    usernoone2 = list(user2)
    usernoone2.append(val)
    usernoone1 = list(user1)
    get, b = computer(usernoone2, usernoone1)
    usernoone1.append(get)
    get, b=computer(usernoone1, usernoone2)
    if(b == 1): return val,1
    return get, None

def predict_common(user1, user2, val):#not ready yet  #prediction++
    usernoone2 = list(user2)
    usernoone2.append(val)
    usernoone1 = list(user1)
    get, b = computer(usernoone2, usernoone1)
    usernoone1.append(get)
    get, b=computer(usernoone1, usernoone2)
    if(b != 1): usernoone2.append(get)
    else: return None, None#worst case
    lst1, nc, c, lst2 = ret_hvalue(usernoone1, usernoone2)
    if(c==0):
        get,b=computer(usernoone1,usernoone2)
        if(b==1): return val, 1
    return val, None
def ret_hvalue(user1, user2):#retrive(stage2++)
    lst = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    lst1, lst2, lst3, lst4, lst5=[], [], [], [], []
    l = len(lst)
    u1, u2 = len(user1), len(user2)
    for i in range(l):
        b=0
        for j in range(0,3):
            for k in range(0,u1):
                if(lst[i][j]==user1[k]): b = b + 1
        if(b==1):
            if((lst[i][0] not in user2) and (lst[i][1] not in user2) and (lst[i][2] not in user2)): lst1.append(lst[i])
    l1 = len(lst1)
    for i in range(l1):
        for j in range(3):
            if(lst1[i][j] not in user1): lst2.append(lst1[i][j])
    l2 = len(lst2)
    if(l2 > 0):
        for i in range(0,l2):
            p1=lst2.count(lst2[i])
            if(p1==2): lst3.append(lst2[i])
            elif(p1==1): lst4.append(lst2[i])
            elif(p1>3): lst2.pop(i)
    lst3.sort()
    l3, nc = len(lst3), len(lst4)
    for i in range(l3):
        if(i%2!=0): lst5.append(lst3[i])
    c = len(lst5)
    return lst4, nc, c, lst5

def main_o2(user1, user2):#the game logic :)
    lstnc1, nc1, c1, lstc1 = ret_hvalue(user1, user2)
    lstnc2, nc2, c2, lstc2 = ret_hvalue(user2, user1)
    ncc1, ncc2 = nc1 + c1, nc2 + c2
    lst1_2 = lstnc1 + lstc1
    if(ncc2 == 0):#rare case
        usernoone2=[]
        for i in range(ncc1):
            pop = lst1_2[i]
            usernoone2 = list(user2)
            usernoone2.append(pop)
            lstnc1_1, nc_1, c11, lst1c1_1 = ret_hvalue(user1, usernoone2)
            if(c11>=1): continue
            else: return pop
        return None
    elif(ncc2==2):#easiest one to predicte*
        for i in range(0,ncc2):
            if(lstnc2[i] in lstc1):
                return lstnc2[i]
        print('ok we can fix it')
        return None
    elif(ncc2>=4):
        #Use prediction
        for i in range(0,ncc2):
            get, b = predict(user1, user2, lstnc2[i])
            if(b!=None):
                return lstnc2[i]
    if(b==None):#using of prediction at high level..
        for i in range (ncc2):
            get, b = predict_common(user1, user2, lstnc2[i])
            if(b != None): return lstnc2[i]
    return None  #support [not to fail].
#driver (MAIN) program
a = 0
b = 0
user1 = []
user2 = []
usernoone = []
scoreo1 = scoreo2 = 0
t11 = 'change'
for t in range(40):
    if(t11=='change'):
        print('Welcome  To Tic Tac Toe Game ')
        print('1. USER1 VS USER2')
        print('2. USER VS COMPUTER(recommended)')
        print('Enter Your Choise:',end=' ')
        for qw in range(12):
            usch = input()
            if(usch==''):
                usch=2
                break
            usch = int(usch)
            if(usch<1 or usch>2):
                print('invalid value !')
                print('enter value again(1/2):',end='')
            else: break
        uschlevel=None
        if(usch==2):
            print('1.Easy Level')
            print('2. Medium Level(recommended)')
            print('3. Hard Level')
            print('Enter Your Choise:', end='')
            for qw in range(12): 
                uschlevel = input()
                if(uschlevel==''):
                    uschlevel=2
                    print()
                    break
                uschlevel = int(uschlevel)
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
        print('invalid value enter,program break!')
        break
print('THANK YOU')
