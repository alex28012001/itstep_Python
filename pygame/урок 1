import pygame

window = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Игра 1.0")

screen = pygame.Surface((800, 400))

kv = pygame.Surface((50, 50))
kv.fill((255, 255, 0))

kv_2 = pygame.Surface((50, 50))
kv_2.fill((255, 140, 0))

kv_3 = pygame.Surface((50, 50))
kv_3.fill((0, 238, 118))

x = 0
y = 0
x_2 = 500
y_2 = 0

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
        x +=0.3

        if x  > 750:
            kv_1_go = False

    else:
        x -=0.3
        if x <0:
            kv_1_go = True


    if kv_down == True:
        y +=0.3
        if y>350 :
            kv_down = False

    else:
        y -=0.3
        if y<0:
            kv_down = True








    if kv_3_go == True:
        x_2 +=0.3

        if x_2  > 750:
            kv_3_go = False

    else:
        x_2 -=0.3
        if x_2 <0:
            kv_3_go = True


    if kv_3_down == True:
        y_2 +=0.3
        if y_2>350 :
            kv_3_down = False

    else:
        y_2 -=0.3
        if y_2<0:
            kv_3_down = True





    screen.blit(kv_3, (x_2, y_2))
    screen.blit(kv, (x, y))
    window.blit(screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(-10)
