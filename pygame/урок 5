import pygame

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Игра 2.0")
screen = pygame.Surface((800, 600))

hero = pygame.image.load("hero.png").convert()
hero = pygame.transform.scale(hero, (60, 60))

krest = pygame.image.load("krest.png").convert()
krest = pygame.transform.scale(krest, (60, 60))

strela = pygame.image.load("strela.png").convert()
strela = pygame.transform.scale(strela, (60, 60))

strela_push = False

strela_x = -10
strela_y = 540



hero_x = 400
hero_y = 540


krest_x = 0
krest_y = 0
go_right_krest = True




def Intersect(x1, x2, y1, y2):
    if (x1 > x2-60) and (x1 < x2+60) and (y1 < y2+60):
        return 1
    else:
        return 0





done = True
pygame.key.set_repeat(1, 1)
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                if hero_x > 0:
                    hero_x -= 5

            if e.key == pygame.K_RIGHT:
                if hero_x <740:
                    hero_x +=5

            if e.key == pygame.K_UP:
                if hero_y >80:
                    hero_y -= 5

            if e.key == pygame.K_DOWN:
                if hero_y < 540 :
                    hero_y += 5


            if e.key == pygame.K_SPACE:
                if strela_push == False:
                    strela_x = hero_x +15
                    strela_push = True



    screen.fill((50, 50, 50))


    if go_right_krest== True:
        krest_x += 1
        if krest_x >740:
            go_right_krest = False

    else :
        krest_x -= 1
        if krest_x <0:
            go_right_krest = True


    if strela_y < 0:
        strela_push = False

    if strela_push == False:
        strela_y = 540
        strela_x = -10

    else:
        strela_y -= 1

