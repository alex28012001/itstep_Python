import pygame

window = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Игра 1.0")

screen = pygame.Surface((1000, 600))

kv = pygame.Surface((60, 60))
kv.fill((255, 255, 0))

kv_3 = pygame.Surface((60, 60))
kv_3.fill((0, 238, 118))

x = 0
y = 0
x_2 = 700
y_2 = 550

kv_1_go = True
kv_down = True

kv_3_go = True
kv_3_down = True

done = True
while done :
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

    screen.fill((50, 50, 50))







    if kv_1_go == True:
        x +=1

        if x  > 940:
            kv_1_go = False

    else:
        x -=1
        if x < 0:
            kv_1_go = True


    if kv_down == True:
        y +=1
        if y>540 :
            kv_down = False

    else:
        y -=1
        if y<0:
            kv_down = True








    if kv_3_go == True:
        x_2 +=1

        if x_2  > 940:
            kv_3_go = False

    else:
        x_2 -=1
        if x_2 <0:
            kv_3_go = True


    if kv_3_down == True:
        y_2 +=1
        if y_2>540 :
            kv_3_down = False

    else:
        y_2 -=1
        if y_2<0:
            kv_3_down = True





    screen.blit(kv_3, (x_2, y_2))
    screen.blit(kv, (x, y))
    window.blit(screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(-20)
