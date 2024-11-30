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

def predict_common(user1, user2, val):# ready to deploy  #prediction++
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