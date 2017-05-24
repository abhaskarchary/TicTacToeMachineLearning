

import pygame,glob

class Mainmenu:


    def __init__(self, screen_size):
        
        pygame.init()
        self.phase = 1
        self.background = pygame.image.load("assets/bg.jpg")
        self.now = 0

        self.title = glob.glob("assets/Logo/Toe*.png")
        self.title.sort()
        self.screen = pygame.Surface(screen_size)
        
        #temporaries
        self.font = pygame.font.SysFont("monospace", 30)


    def update(self, mouse):
        self.screen.blit(self.background, (0,0))
        self.screen.blit(pygame.image.load(self.title[self.now]), (180,100))
        if self.now == len(self.title)-1:
            self.now = 0
        else:
            self.now += 1

       
        if self.phase == 1:
            #main game menu play button
            self.phase1(mouse)
        elif self.phase == 2:
            #game menu 1p or 2p
            self.phase2(mouse)
        elif self.phase == 3:
            #if 1p play as cross or play as knot
            self.phase3(mouse)
        
        
        return self.screen

    def phase1(self, mouse):
        ((mx, my),clicked) = mouse
        if clicked == 1:
            self.phase = 2
        xoff,yoff = 250,350
        label = self.font.render("Play Game",2, (0,0,0))
        self.screen.blit(label, (xoff,yoff))
        
        if xoff - 50<=mx<= xoff + 250 and yoff - 25 <=my<= yoff + 75:
            pygame.draw.rect(self.screen, (0,0,0), (xoff - 50 , yoff -25,275,75), 1)

    def phase2(self, mouse):
        ((mx,my),clicked) = mouse

        xoff,yoff,xoff1,yoff1 = 250,300,250,450
        label = self.font.render("1 Player",2, (0,0,0))
        label1 = self.font.render("2 Player",3, (0,0,0))
        self.screen.blit(label, (xoff, yoff))

        if xoff - 50<=mx<= xoff + 250 and yoff - 25 <=my<= yoff + 75:
            pygame.draw.rect(self.screen, (0,0,0), (xoff - 50 , yoff -25,275,75), 1)
            if clicked == 1:
                self.phase = 3

        self.screen.blit(label1, (xoff1, yoff1))

        if xoff1 - 50<=mx<= xoff1 + 250 and yoff1 - 25 <=my<= yoff1 + 75:
            pygame.draw.rect(self.screen, (0,0,0), (xoff1 - 50 , yoff1 -25,275,75), 1)
            if clicked == 1:
                self.phase = 10 #start a 2 player game

    def phase3(self, mouse):
        ((mx,my),clicked) = mouse

        xoff,yoff,xoff1,yoff1 = 250,300,250,450

        label = self.font.render("Play as X",1,(0,0,0))
        label1 = self.font.render("Play as O",1,(0,0,0))

        self.screen.blit(label, (xoff, yoff))

        if xoff - 50<=mx<= xoff + 250 and yoff - 25 <=my<= yoff + 75:
            pygame.draw.rect(self.screen, (0,0,0), (xoff - 50 , yoff -25,275,75), 1)
            if clicked == 1:
                self.phase = 20 #start a one player game as x
        
        self.screen.blit(label1, (xoff1, yoff1))
         
        if xoff1 - 50<=mx<= xoff1 + 250 and yoff1 - 25 <=my<= yoff1 + 75:
            pygame.draw.rect(self.screen, (0,0,0), (xoff1 - 50 , yoff1 -25,275,75), 1)
            if clicked == 1:
                self.phase = 30 #start a one player game with o
  



        

