import pygame

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Игра 2.0")
screen = pygame.Surface((800, 600))


myimage = pygame.image.load("krest.png").convert()
myimage = pygame.transform.scale(myimage, (100, 100))

x = 0
y = 0
go_right = True
go_down = True


done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

    screen.fill((50, 50, 50))




    if go_right == True:
        x += 1
        if x > 700:
            go_right = False

    else:
        x -= 1
        if x < 0:
            go_right = True



    if go_down == True:
        y += 1
        if y > 500:
            go_down = False

    else:
        y -= 1
        if y < 0:
            go_down = True



    screen.blit(myimage, (x, y))
    window.blit(screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(1)
