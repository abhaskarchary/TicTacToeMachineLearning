import pygame

class GameOver:


    def __init__(self, msg, screen_size):
        
        self.message = msg
        self.retry = 0

        #graphics and stuff
        self.font = pygame.font.SysFont("monospace",30)
        self.background = pygame.image.load("assets/bg.jpg")

        self.screen = pygame.Surface(screen_size)

    
    def update(self, mouse):
        
        self.screen.blit(self.background, (0, 0))
        ((mx, my), clicked) = mouse

        game_over_label = self.font.render("GAME OVER!!", 2, (0, 0, 0))
        message_label = self.font.render(self.message, 2, (0, 0, 255))
        retry_label = self.font.render("Tap to replay", 2, (0, 0, 0))

        go_x,go_y, gapx, gapy = 300, 200, 10, 100
        self.screen.blit(game_over_label, (go_x, go_y))
        self.screen.blit(message_label, (go_x+gapx, go_y+gapy))

        self.screen.blit(retry_label, (go_x - 50, go_y + 200))

        if clicked == 1:
            self.retry = 1

        

        return self.screen

