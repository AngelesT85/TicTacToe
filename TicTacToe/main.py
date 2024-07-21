import pygame as pg
from functions import *
from classes import *
from time import sleep
'''
 1 | 2 | 3 
 4 | 5 | 6
 7 | 8 | 9

coords of left up angle on field:

 1 - 240|438 - 336|534
 2 - 352|438 - 448|534
 3 - 464|438 - 560|534
 4 - 240|550 - 336|646
 5 - 352|550 - 448|646
 6 - 464|550 - 560|646
 7 - 240|662 - 336|758
 8 - 352|662 - 448|758
 9 - 464|662 - 560|758

'''

y_coords = ((438, 534), (550, 646), (662, 758))
x_coords = ((240, 336), (352, 448), (464, 560))

pg.init()
screen = pg.display.set_mode((800, 800))
screen.fill((255, 255, 255))

# install images
TryAgain1 = pg.image.load("images/try again 1.png") 
HorImg = pg.image.load("images/horisontal.png")
VertImg = pg.image.load("images/vertical.png")
MDiag = pg.image.load("images/MDiag.png")
NMDiag = pg.image.load("images/NMDiag.png")
TacToeImg = pg.image.load(tactoe.image)
TicImg = pg.image.load(tic.image)
FieldImg = pg.image.load(field.image)

figures = (tic, tactoe)
images = (TicImg, TacToeImg)

screen.blit(FieldImg, (0, 0))

num_of_moves = 0
is_again = False
is_game = True

while is_game:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_game = False

        elif event.type == pg.MOUSEBUTTONDOWN:
            coords = pg.mouse.get_pos()
            x = coords[0]
            y = coords[1]

            if is_again and (135 <= x <= 665) and (129 <= y <= 197):
                num_of_moves, is_again = again(screen, FieldImg, field)

            elif not is_again:
                num_of_moves = move(screen, x_coords, y_coords, figures, num_of_moves, field, x, y, images)
                if num_of_moves >= 5:
                    result = check_win(field.field, screen, HorImg, VertImg, MDiag, NMDiag)
                    if result[0]:
                        screen.blit(TryAgain1, (135, 129))
                        is_again = True

    if num_of_moves >= 9:
        screen.blit(TryAgain1, (135, 129))
        is_again = True

        
    
    pg.display.flip()

