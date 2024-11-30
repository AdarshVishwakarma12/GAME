#DISPLAY Module

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

# Zero and cross function is at best!!!
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
