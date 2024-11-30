def ret_hvalue(user1, user2): #retrive(stage2++)
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
    return None  #support [fail Safe]