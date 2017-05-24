import pygame,glob

import human_player, bot_player


class Game:


    def __init__(self,screen_size,player_info):
        pygame.init()
        self.mat = [[0,0,0],[0,0,0],[0,0,0]]
        self.winner = 0

        self.turn = 1

        if player_info == 10:
            self.player1 = human_player.Human_player()
            self.player2 = human_player.Human_player()
        elif player_info == 20:
            self.player1 = human_player.Human_player()
            self.player2 = bot_player.Bot(2)
        else:
            self.player1 = bot_player.Bot(1)
            self.player2 = human_player.Human_player()
        
        #graphics
        self.area = pygame.image.load("assets/Area.png")
        self.cross = pygame.image.load("assets/Cross.png")
        self.knot = pygame.image.load("assets/Circle.png")
        self.back = pygame.image.load("assets/bg.jpg")
        

        self.turn = 1
        self.screen = pygame.Surface(screen_size)

        self.font = pygame.font.SysFont("monospace",30)


    def update(self, mouse):
        self.screen.blit(self.back, (0,0))
        
        textx,texty = 300,20
        if self.turn == 1:
            label = self.font.render("TURN : CROSS",2,(0,0,0))
        else:
            label = self.font.render("TURN : KNOT", 2, (0, 0, 0))

        self.screen.blit(label, (textx,texty))

        xoff,yoff = 180,100
        soff = 5
        gap = 140

        self.screen.blit(self.area, (xoff,yoff))
        if self.turn == 1:
            (i, j) = self.player1.make_move(mouse, self.mat)
        else:
            (i, j) = self.player2.make_move(mouse, self.mat)

        if (i == j  and i!=-1) or i!=j:
            self.mat[i][j] = self.turn
            self.turn = self.turn%2 + 1

        self.winner = self.check_win()
        
        for i in range(3):
            for j in range(3):
                if self.mat[i][j] == 1:
                    self.screen.blit(self.cross, (xoff+j*gap,yoff+i*gap))
                elif self.mat[i][j] == 2:
                    self.screen.blit(self.knot, (xoff+j*gap, yoff+i*gap))

        return self.screen

    def check_win(self):

        for i in range(3):
            if self.mat[i][0] == self.mat[i][1] == self.mat[i][2] and self.mat[i][0] != 0:
                return self.mat[i][0]
            if self.mat[0][i] == self.mat[1][i] == self.mat[2][i] and self.mat[0][i] != 0:
                return self.mat[0][i]

        if self.mat[0][0] == self.mat[1][1] == self.mat[2][2] and self.mat[0][0] != 0:
            return self.mat[0][0]

        if self.mat[0][2] == self.mat[1][1] == self.mat[2][0] and self.mat[0][2] != 0:
            return self.mat[0][2]

        for i in range(3):
            for j in range(3):
                if self.mat[i][j] == 0:
                    return 0

        return -1
