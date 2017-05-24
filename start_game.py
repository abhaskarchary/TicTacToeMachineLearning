#!/usr/bin/python

import pygame,mainmenu,game,Gameover

#game params
screen_size = (800, 600)
quit_game = False

screen = pygame.display.set_mode(screen_size)
m = mainmenu.Mainmenu(screen_size)
g = game.Game(screen_size,10)
go = Gameover.GameOver("TIE",screen_size)
clock = pygame.time.Clock()
pygame.init()

game_state = "init"

def handle_events():
    global quit_game,game_state,g,go,m
    mouse_pos = pygame.mouse.get_pos()
    clicked = 0
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit_game = True
        if e.type ==pygame.MOUSEBUTTONUP:
            clicked = 1

    if game_state == "start":
        screen.blit(m.update((mouse_pos, clicked)), (0,0))
        if m.phase >5:
            game_state = "play"
            g = game.Game(screen_size, m.phase)
    elif game_state == "play":
        screen.blit(g.update((mouse_pos, clicked)), (0,0))
        if g.winner !=0:
            if g.winner == 1:
                go = Gameover.GameOver("CROSS WINS!!", screen_size)
            elif g.winner == 2:
                go = Gameover.GameOver("KNOT WINS!!", screen_size)
            else:
                go = Gameover.GameOver("TIE!!", screen_size)

            game_state = "over"
    elif game_state == "over":
        screen.blit(go.update((mouse_pos, clicked)), (0, 0))
        if go.retry == 1:
            game_state = "init"
            m.phase = 1
                


def game_loop():
    global game_state
    while not quit_game:
        if game_state == "init":
            m = mainmenu.Mainmenu(screen_size)
            game_state = "start"
        elif game_state == "start":
            clock.tick(24)
            handle_events()
            pygame.display.update()
        elif game_state == "play":
            handle_events()
            pygame.display.update()
        elif game_state == "over":
            handle_events()
            pygame.display.update()


game_loop()
pygame.quit()
quit()

