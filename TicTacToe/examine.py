# Examine result
def examine(user):
    lst=[[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    a = len(user) 
    for i in range(8):
        b=0
        for j in range(0,3):
            for k in range(0,a):
                if(lst[i][j] == user[k]): b = b + 1
        if(b==3): return 0