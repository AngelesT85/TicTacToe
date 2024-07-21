def move(screen, x_coords, y_coords, figures, num_of_moves, field, x, y, images):
    for iy in range(len(y_coords)):
        for jx in range(len(x_coords)):
            if (x_coords[jx][0] <= x <= x_coords[jx][1]) and (y_coords[iy][0] <= y <= y_coords[iy][1]) and field.field[iy][jx] == "":
                screen.blit(images[num_of_moves % 2], (x_coords[jx][0], y_coords[iy][0]))
                field.field[iy][jx] = figures[num_of_moves % 2].comp_value
                num_of_moves += 1
    return num_of_moves

def again(screen, FieldImg, field):
    screen.fill((255, 255, 255))
    screen.blit(FieldImg, (0, 0))
    field.field = [["" for _ in range(3)] for i in range(3)]
    num_of_moves = 0
    is_again = False
    return num_of_moves, is_again

def check_win(field, screen, HorImg, VertImg, MImg, NMImg):
    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2]:
            if field[i][0] !="":
                screen.blit(HorImg, (224, (438 + 112 * i)))
                return True, field[i][0], 1

        elif field[0][i] == field[1][i] == field[2][i]:
            if field[0][i] != "":
                screen.blit(VertImg, ((240 + 112 * i), 422))
                return True, field[0][i], 2
        
    if field[0][0] == field[1][1] == field[2][2]:
        if field[0][0] != "":
            screen.blit(MImg, (240, 438))
            return True, field[0][0], 3
        
    elif field[0][2] == field[1][1] ==  field[2][0]:
        if field[0][2] != "":
            screen.blit(NMImg, (240, 438))
            return True, field[0][2], 4
    
    return [False]


