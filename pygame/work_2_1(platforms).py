import pygame

SIZE = (800, 600)

window = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Платформер")
screen = pygame.Surface(SIZE)

stena = pygame.image.load("stena.jpg").convert()
stena = pygame.transform.scale(stena, (40, 40))


class Platform:
    def __init__(self):
        self.img = stena


def make_level(level, platforma):
    x = 0
    y = 0
    for row in level:
        for col in row:
            if col == '-':
                screen.blit(platforma.img, (x, y))
            x +=40
        y += 40
        x = 0


level = [
    '--------------------',
    '-                  -',
    '-                  -',
    '-                  -',
    '-    --            -',
    '-                  -',
    '-                  -',
    '-        --        -',
    '-                  -',
    '-   -     -        -',
    '-                  -',
    '-                  -',
    '-                  -',
    '-                  -',
    '--------------------']

pl = Platform()



done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False



    screen.fill((50, 50, 50))
    make_level(level, pl)


    window.blit(screen, (0, 0))
    pygame.display.flip()
