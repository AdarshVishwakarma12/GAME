import pygame

class enviornment:
    instance = list()
    
    def __init__(self, pos):
        enviornment.instance.append(self)
        self.pos = pos
        if(pos[0] == 0 or pos[0] == 1): agent_black.instance.append(self)
        elif(pos[0] == 6 or pos[0] == 7): agent_white.instance.append(self)
        else: raise ('unexpected index!')
        
    def reset():
        enviornment.images_()
        enviornment.instance = list()
        agent_black.reset()
        agent_white.reset()
        print('DONE SUCCESSFULLY!')
        
    def images_():
        lst_img = [ 'Chessboard480.svg.png',
         'Chess_Board.svg.png',
         'bishop_b.svg.png',
         'bishop_w.svg.png',
         'elephant_black.svg.png',
         'elephant_w.svg.png',
         'horse_b.svg.png',
         'horse_w.svg.png',
         'king_b.png',
         'king_w.svg.png',
         'pawn_b.svg.png',
         'pawn_w.svg.png',
         'queen_b.svg.png',
         'queen_w.svg.png']
        
        PIECE_img_size = (81, 75)
        B_w = pygame.transform.scale(pygame.image.load('images/'+lst_img[3]), PIECE_img_size)
        B_b = pygame.transform.scale(pygame.image.load('images/'+lst_img[2]), PIECE_img_size)
        E_b = pygame.transform.scale(pygame.image.load('images/'+lst_img[4]), PIECE_img_size)
        E_w = pygame.transform.scale(pygame.image.load('images/'+lst_img[5]), PIECE_img_size)
        H_b = pygame.transform.scale(pygame.image.load('images/'+lst_img[6]), PIECE_img_size)
        H_w = pygame.transform.scale(pygame.image.load('images/'+lst_img[7]), PIECE_img_size)
        K_b = pygame.transform.scale(pygame.image.load('images/'+lst_img[8]), PIECE_img_size)
        K_w = pygame.transform.scale(pygame.image.load('images/'+lst_img[9]), PIECE_img_size)
        P_b = pygame.transform.scale(pygame.image.load('images/'+lst_img[10]), PIECE_img_size)
        P_w = pygame.transform.scale(pygame.image.load('images/'+lst_img[11]), PIECE_img_size)
        Q_b = pygame.transform.scale(pygame.image.load('images/'+lst_img[12]), PIECE_img_size)
        Q_w = pygame.transform.scale(pygame.image.load('images/'+lst_img[13]), PIECE_img_size)
        enviornment.image_piece = [P_b, P_w, B_w, B_b, E_b, E_w, H_b, H_w, K_b, K_w, Q_b, Q_w]

class pawn(enviornment):
    def __init__(self, pos):
        super().__init__(pos)
        if(pos[0] == 0 or pos[0] == 1): self.image = enviornment.image_piece[0]
        elif(pos[0] == 6 or pos[0]==7): self.image = enviornment.image_piece[1]
    def move(self, lst):
        #According to the agent
        #According to enemy
        lst[0].append([self.pos[0]+1, self.pos[1]])
        lst[0].append([self.pos[0]+2, self.pos[1]])
        return lst

class elephant(enviornment):
    def __init__(self, pos):
        super().__init__(pos)
        if(pos[0] == 0 or pos[0] == 1): self.image = enviornment.image_piece[4]
        elif(pos[0] == 6 or pos[0]==7): self.image = enviornment.image_piece[5]
    def move(self, lst):
        for i in range(self.pos[0]+1, 8, 1):
            lst[0].append([i, self.pos[1]])
        for i in range(self.pos[1]+1, 8, 1):
            lst[6].append([self.pos[0], i])
        for i in range(self.pos[0]-1, -1, -1):
            lst[4].append([i, self.pos[1]])
        for i in range(self.pos[1]-1, -1, -1):
            lst[2].append([self.pos[0], i])
        return lst

class bishop(enviornment):
    def __init__(self, pos):
        super().__init__(pos)
        if(pos[0] == 0 or pos[0] == 1): self.image = enviornment.image_piece[3]
        elif(pos[0] == 6 or pos[0]==7): self.image = enviornment.image_piece[2]
    def move(self, lst):
        for count, _ in enumerate(list(range(0, 8))):
            count = count + 1
            if self.pos[0]+count > 7 or self.pos[1]-count < 0: break
            lst[1].append([self.pos[0]+count, self.pos[1]-count])
        for count, _ in enumerate(list(range(0, 8))):
            count = count + 1
            if self.pos[0]-count < 0 or self.pos[1]-count < 0: break
            lst[3].append([self.pos[0]-count, self.pos[1]-count])
        for count, _ in enumerate(list(range(0, 8))):
            count = count + 1
            if self.pos[0]-count < 0 or self.pos[1]+count > 7: break
            lst[5].append([self.pos[0]-count, self.pos[1]+count])
        for count, _ in enumerate(list(range(0, 8))):
            count = count + 1
            if self.pos[0]+count > 7 or self.pos[1]+count > 7: break
            lst[7].append([self.pos[0]+count, self.pos[1]+count])
        return lst

class knight(enviornment):
    def __init__(self, pos):
        super().__init__(pos)
        if(pos[0] == 0 or pos[0] == 1): self.image = enviornment.image_piece[6]
        elif(pos[0] == 6 or pos[0]==7): self.image = enviornment.image_piece[7]
    def move(self, lst):
        if self.pos[0]+2<8 and self.pos[1]-1>-1:
            lst[0].append([self.pos[0]+2, self.pos[1]-1])
        if self.pos[0]+1<8 and self.pos[1]-2>-1:
            lst[1].append([self.pos[0]+1, self.pos[1]-2])   
        if self.pos[0]-1>-1 and self.pos[1]-2>-1: 
            lst[2].append([self.pos[0]-1, self.pos[1]-2])
        if self.pos[0]-2>-1 and self.pos[1]-1>-1:
            lst[3].append([self.pos[0]-2, self.pos[1]-1])
        if self.pos[0]-2>-1 and self.pos[1]+1<8: 
            lst[4].append([self.pos[0]-2, self.pos[1]+1])
        if self.pos[0]-1>-1 and self.pos[1]+2<8:
            lst[5].append([self.pos[0]-1, self.pos[1]+2])
        if self.pos[0]+1<8 and self.pos[1]+2<8:
            lst[6].append([self.pos[0]+1, self.pos[1]+2])
        if self.pos[0]+2<8 and self.pos[1]+1<8:
            lst[7].append([self.pos[0]+2, self.pos[1]+1])
        return lst

class queen(enviornment):
    def __init__(self, pos):
        super().__init__(pos)
        if(pos[0] == 0 or pos[0] == 1): self.image = enviornment.image_piece[10]
        elif(pos[0] == 6 or pos[0]==7): self.image = enviornment.image_piece[11]
    def move(self, lst):
        lst = elephant.move(self, lst)
        lst = bishop.move(self, lst)
        return lst

class king(enviornment):
    def __init__(self, pos):
        super().__init__(pos)
        if(pos[0] == 0 or pos[0] == 1): self.image = enviornment.image_piece[8]
        elif(pos[0] == 6 or pos[0]==7): self.image = enviornment.image_piece[9]
    def move(self, lst):
        if self.pos[0]+1<7: lst[0].append([self.pos[0]+1, self.pos[1]])
        if self.pos[0]+1<7 and self.pos[1]-1>0: lst[1].append([self.pos[0]+1, self.pos[1]-1])
        if self.pos[1]-1>-1: lst[2].append([self.pos[0], self.pos[1]-1])
        if self.pos[0]-1>0 and self.pos[1]-1>0: lst[3].append([self.pos[0]-1, self.pos[1]-1])
        if self.pos[0]-1>-1: lst[4].append([self.pos[0]-1, self.pos[1]])
        if self.pos[0]-1>0 and self.pos[1]+1<7: lst[5].append([self.pos[0]-1, self.pos[1]+1])
        if self.pos[1]+1<7: lst[6].append([self.pos[0], self.pos[1]+1])
        if self.pos[0]+1<7 and self.pos[1]+1<7: lst[7].append([self.pos[0]+1, self.pos[1]]+1)
        return lst

class agent_black:
    instance = list()
    
    def __init__(self, pos):
        super().__init__(self, pos)
        agent_black.instance.append(self)
    
    def valid_moves(instance):
        #find how the instance move
        lst = [[], [], [], [], [], [], [], []]
        lst = instance.move(lst)
        lst = agent_black.friend(lst)
        valid, enemy = agent_black.enemy(lst)
        return valid, enemy
    
    def friend(lst):
        i1 = list()
        for i in agent_black.instance: i1.append(i.pos)
        valid = list()
        for c1, i in enumerate (lst):
            flag = 0; valid.append([])
            for c2, j in enumerate (i):
                if j in i1: flag = 1
                if flag == 0: valid[c1].append(j)
        return valid
    
    def enemy(lst):
        valid, enemy, i1 = list(), list(), list()
        for i in agent_white.instance: i1.append(i.pos)
        for c1, i in enumerate (lst):
                flag = 0; valid.append([])
                for c2, j in enumerate (i):
                    if j in i1 and flag != 1: flag = 1; enemy.append(j)
                    if flag == 0: valid[c1].append(j)
        return valid, enemy
    
    def create_all():
        # for i in range(0, 8): pawn([1, i])
        elephant([0, 0]), elephant([0, 7])
        knight([0, 1]), knight([0, 6])
        bishop([0, 2]), bishop([0, 5])
        queen([0, 3]), king([0, 4])
    
    def reset():
        agent_black.instance = list()
        agent_black.create_all()

class agent_white:
    instance = list()
    
    def __init__(self, pos):
        super().__init__(self, pos)
        agent_white.instance.append(self)
    
    def valid_moves(instance):
        lst = [[], [], [], [], [], [], [], []]
        lst = instance.move(lst)
        lst = agent_white.friend(lst)
        valid, enemy = agent_white.enemy(lst)
        return valid, enemy
    
    def friend(lst):
        i1 = list()
        for i in agent_white.instance: i1.append(i.pos)
        valid = list()
        for c1, i in enumerate (lst):
            flag = 0; valid.append([])
            for c2, j in enumerate (i):
                if j in i1: flag = 1
                if flag == 0: valid[c1].append(j)
        return valid
    
    def enemy(lst):
        valid, enemy, i1 = list(), list(), list()
        for i in agent_black.instance: i1.append(i.pos)
        for c1, i in enumerate (lst):
                flag = 0; valid.append([])
                for c2, j in enumerate (i):
                    if j in i1 and flag != 1: flag = 1; enemy.append(j)
                    if flag == 0: valid[c1].append(j)
        return valid, enemy
    
    def create_all():
        # for i in range(0, 8): pawn([6, i])
        elephant([7, 0]), elephant([7, 7])
        knight([7, 1]), knight([7, 6])
        bishop([7, 2]), bishop([7, 5])
        queen([7, 3]), king([7, 4])
    
    def reset():
        agent_white.instance = list()
        agent_white.create_all()