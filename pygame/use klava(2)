import pygame

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Игра 2.0")
screen = pygame.Surface((800, 600))

hero = pygame.image.load("hero.png").convert()
hero = pygame.transform.scale(hero, (70, 70))

hero_x = 0
hero_y = 0

hero_right = False
hero_left = False
hero_up = False
hero_down = False



done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

        if e.type == pygame.KEYDOWN:

            if e.key == pygame.K_LEFT:
                hero_left = True

            if e.key == pygame.K_RIGHT:
                hero_right = True

            if e.key == pygame.K_UP:
                hero_up = True

            if e.key == pygame.K_DOWN:
                hero_down = True


        if e.type == pygame.KEYUP:

            if e.key == pygame.K_LEFT:
                hero_left = False

            if e.key == pygame.K_RIGHT:
                hero_right = False

            if e.key == pygame.K_UP:
                hero_up = False

            if e.key == pygame.K_DOWN:
                hero_down = False


    if hero_left == True:
        if hero_x > 0:
            hero_x -= 1

    if hero_right == True:
        if hero_x <730:
            hero_x += 1

    if hero_up == True:
        if hero_y > 0:
            hero_y -= 1

    if hero_down == True:
        if hero_y < 530:
            hero_y += 1





    screen.fill((50, 50, 50))

    screen.blit(hero, (hero_x, hero_y))
    window.blit(screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(1)
