def computer(user1, user2):#computer 
    usernoone = user1 + user2
    lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    a = len(user1) 
    for i in range(8):
        b = 0
        for j in range(3):
            for k in range(a):
                if(lst[i][j] == user1[k]): 
                    b=b+1
            if(b==2):
                for do in range(0,3):
                    if((lst[i][do] not in user1) and(lst[i][do] not in usernoone)): 
                        return lst[i][do],b
    return None, 1