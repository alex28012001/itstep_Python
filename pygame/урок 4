import pygame

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Игра 2.0")
screen = pygame.Surface((800, 600))

myimage = pygame.image.load("hero.png").convert()
myimage = pygame.transform.scale(myimage, (60, 60))

myimage_2 = pygame.image.load("krest.png").convert()
myimage_2 = pygame.transform.scale(myimage_2, (60, 60))


x = 0
y = 300
x_2 = 740
y_2 = 300
go_right = True
go_right_2 = True


def Intersect(x1, x2, y1, y2):
    if (x1 > x2-60) and (x1 < x2+60) and (y1 < y2+60):
        return 1
    else:
        return 0


done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

    screen.fill((50, 50, 50))




    if go_right == True:
        x += 1
        if x > 740:
            go_right = False

    else:
        x -= 1
        if x < 0:
            go_right = True



    if go_right_2== True:
        x_2 += 1
        if x_2 >740:
            go_right_2 = False

    else :
        x_2 -= 1
        if x_2 <0:
            go_right_2 = True


    if Intersect(x, x_2, y, y_2) == True:
        go_right_2 = False
        go_right = True




    screen.blit(myimage_2, (x_2, y_2))
    screen.blit(myimage, (x, y))

    window.blit(screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(5)
