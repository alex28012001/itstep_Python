import pygame

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Игра 2.0")
screen = pygame.Surface((800, 600))

hero = pygame.image.load("hero.png").convert()
hero = pygame.transform.scale(hero, (70, 70))
hero_x = 0
hero_y = 0


done = True
pygame.key.set_repeat(1, 1)
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

        if e.type == pygame.KEYDOWN:

            if e.key == pygame.K_LEFT:
                if hero_x > 0:
                    hero_x -= 1

            if e.key == pygame.K_RIGHT:
                if hero_x < 730:
                    hero_x += 1

            if e.key == pygame.K_UP:
                if hero_y > 0:
                    hero_y -= 1

            if e.key == pygame.K_DOWN:
                if hero_y < 530:
                    hero_y += 1






    screen.fill((50, 50, 50))

    screen.blit(hero, (hero_x, hero_y))
    window.blit(screen, (0, 0))
    pygame.display.flip()
