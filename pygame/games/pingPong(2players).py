import pygame
import random
import sys

window = pygame.display.set_mode((1200, 710))
pygame.display.set_caption("Игра  2 0")
screen = pygame.Surface((1200, 710))

"""обьекты"""
panel = pygame.Surface((20, 150))
panel_2 = pygame.Surface((20, 150))
poloca = pygame.Surface((10, 660))
poloca_2 = pygame.Surface((1200, 10))
ball = pygame.image.load("ball11.png").convert()
ball = pygame.transform.scale(ball, (80, 80))

"""шрифты"""
pygame.font.init()
inf_font = pygame.font.SysFont("Buxton Sketch", 50)


"""координаты обьектов"""
poloca_x = 600
poloca_y = 0
poloca_2_x = 0
poloca_2_y = 650

panel_x = 50
panel_y = 300
panel_down = False
panel_up = False


panel_2_x = 1130
panel_2_y = 300
panel_2_down = False
panel_2_up = False

ball_x = 0
ball_y = 0
ball_right = True
ball_down = True
ball_step = 1
schet = 0
schet_2 = 0




def Intersect(x1, x2, y1, y2):
    if (x1 > x2-80) and (x1 < x2 + 20) and (y1 > y2-70) and (y1 < y2+150):
        return 1
    else:
        return 0

def Intersect2(x1, x2, y1, y2):
    if (x1 > x2-80) and (x1 < x2 + 20) and (y1 > y2-70) and (y1 < y2+150):
        return 1
    else:
        return 0


"""закрытие окна"""
done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
        """Передвижение 2 панелей"""
        if e.type == pygame.KEYDOWN:

            if e.key == pygame.K_UP:
                panel_2_up = True

            if e.key == pygame.K_DOWN:
                panel_2_down = True

            if e.key == pygame.K_w:
                panel_up = True

            if e.key == pygame.K_s:
                panel_down = True

        if e.type == pygame.KEYUP:
            if e.key == pygame.K_UP:
                panel_2_up = False

            if e.key == pygame.K_DOWN:
                panel_2_down = False

            if e.key == pygame.K_w:
                panel_up = False

            if e.key == pygame.K_s:
                panel_down = False



    if panel_2_up == True:
        if panel_2_y > 0:
            panel_2_y -= 1.5

    if panel_2_down == True:
        if panel_2_y < 500:
            panel_2_y += 1.5

    if panel_up == True:
        if panel_y > 0:
            panel_y -= 1.5

    if panel_down == True:
        if panel_y <500:
            panel_y += 1.5

        """ПЕРЕДВИЖЕНИЕ МЯЧА"""
    if ball_right == True:
        ball_x += ball_step
        if ball_x > 1280:
            schet_2 -= ball_step
            ball_right = False


    else:
        ball_x -= ball_step
        if ball_x < -90:
            schet -= 1
            ball_right = True

    if ball_down == True:
        ball_y -= ball_step
        if ball_y < 40:
            ball_down = False

    else:
        ball_y += ball_step
        if ball_y > 590:
            ball_down = True



    screen.fill((50, 50, 50))


    if Intersect(ball_x, panel_x, ball_y, panel_y) == True:
        ball_right = True
        ball_down = True
        schet += 1
        ball_step += 0.25

    if Intersect2(ball_x, panel_2_x, ball_y, panel_2_y) == True:
        ball_right = False
        ball_down = True
        schet_2 += 1
        ball_step += 0.25



    screen.blit(inf_font.render('Счёт: ' + str(schet_2), 5, (255, 99, 71)), (655, 3))
    screen.blit(inf_font.render('Счёт: ' + str(schet), 5, (255, 99, 71)), (400, 3))
    screen.blit(inf_font.render('Скорость мяча: ' + str(ball_step), 5, (255, 99, 71)), (440, 650))

    """отрисовка обьектов"""
    screen.blit(ball, (ball_x, ball_y))
    screen.blit(poloca_2, (poloca_2_x, poloca_2_y))
    screen.blit(poloca, ((poloca_x, poloca_y)))
    screen.blit(panel, (panel_x, panel_y))
    screen.blit(panel_2, (panel_2_x, panel_2_y))
    window.blit(screen, (0, 0))
    pygame.display.flip()




----------------------------------------------------------------------------------------------------------------------
ping pong 2 with menu



import pygame
import random
import sys

window = pygame.display.set_mode((1200, 710))
pygame.display.set_caption("Игра  2 0")
screen = pygame.Surface((1200, 710))

"""обьекты"""
panel = pygame.Surface((20, 150))
panel_2 = pygame.Surface((20, 150))
poloca = pygame.Surface((10, 660))
poloca_2 = pygame.Surface((1200, 10))
ball = pygame.image.load("ball11.png").convert()
ball = pygame.transform.scale(ball, (80, 80))

"""шрифты"""
pygame.font.init()
inf_font = pygame.font.SysFont("Buxton Sketch", 50)


"""координаты обьектов"""
poloca_x = 600
poloca_y = 0
poloca_2_x = 0
poloca_2_y = 650

panel_x = 50
panel_y = 300
panel_down = False
panel_up = False


panel_2_x = 1130
panel_2_y = 300
panel_2_down = False
panel_2_up = False


a = random.randint(0, 1000)
b = random.randint(60, 400)
ball_x = a
ball_y = b
ball_right = True
ball_down = True
ball_step = 1
schet = 0
schet_2 = 0




class Menu:
    def __init__(self, punkts = [120, 140, 'Punkt', (250, 250, 30), (50, 30, 50)]):
        self.punkts = punkts
    def render (self, poverhnost, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                poverhnost.blit(font.render(i[2], 1, i[4]), (i[0], i[1]-60))

            else:
                poverhnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1]-60))

    def menu (self):
        done = True
        font_menu = pygame.font.SysFont("Buxton Sketch", 100)

        pygame.key.set_repeat(0, 0)
        pygame.mouse.set_visible(True)

        punkt = 0
        while done:
            screen.fill((119, 136, 153))

            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp [0]>i[0] and mp[0]<i[0]+200 and mp[1]>i[1] and mp[1]<i[1]+100:
                    punkt = i[5]
            self.render(screen, font_menu , punkt)


            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()

                    if e.key == pygame.K_UP:
                        if punkt >0:
                            punkt -=1

                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts)-1:
                            punkt +=1

                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        done = False
                    elif punkt == 1:
                        sys.exit()

            window.blit(screen, (0, 0))
            pygame.display.flip()



"""создаем меню"""
punkts = [(500, 160, 'Game', (250, 250, 30), (0, 0, 0), 0),
          (500, 260, 'Quit', (250, 250, 30), (0, 0, 0), 1)]




game = Menu(punkts)
game.menu()


def Intersect(x1, x2, y1, y2):
    if (x1 > x2-80) and (x1 < x2 + 20) and (y1 > y2-70) and (y1 < y2+150):
        return 1
    else:
        return 0

def Intersect2(x1, x2, y1, y2):
    if (x1 > x2-80) and (x1 < x2 + 20) and (y1 > y2-70) and (y1 < y2+150):
        return 1
    else:
        return 0


"""закрытие окна"""
done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
        """Передвижение 2 панелей"""
        if e.type == pygame.KEYDOWN:

            if e.key == pygame.K_UP:
                panel_2_up = True

            if e.key == pygame.K_DOWN:
                panel_2_down = True

            if e.key == pygame.K_w:
                panel_up = True

            if e.key == pygame.K_s:
                panel_down = True

            if e.key == pygame.K_ESCAPE:
                game.menu()

        if e.type == pygame.KEYUP:
            if e.key == pygame.K_UP:
                panel_2_up = False

            if e.key == pygame.K_DOWN:
                panel_2_down = False

            if e.key == pygame.K_w:
                panel_up = False

            if e.key == pygame.K_s:
                panel_down = False



    if panel_2_up == True:
        if panel_2_y > 0:
            panel_2_y -= 1.5

    if panel_2_down == True:
        if panel_2_y < 500:
            panel_2_y += 1.5

    if panel_up == True:
        if panel_y > 0:
            panel_y -= 1.5

    if panel_down == True:
        if panel_y <500:
            panel_y += 1.5

        """ПЕРЕДВИЖЕНИЕ МЯЧА"""
    if ball_right == True:
        ball_x += ball_step
        if ball_x > 1280:
            schet_2 -= ball_step
            ball_right = False


    else:
        ball_x -= ball_step
        if ball_x < -90:
            schet -= 1
            ball_right = True

    if ball_down == True:
        ball_y -= ball_step
        if ball_y < 40:
            ball_down = False

    else:
        ball_y += ball_step
        if ball_y > 590:
            ball_down = True



    screen.fill((50, 50, 50))


    if Intersect(ball_x, panel_x, ball_y, panel_y) == True:
        ball_right = True
        ball_down = True
        schet += 1
        ball_step += 0.25

    if Intersect2(ball_x, panel_2_x, ball_y, panel_2_y) == True:
        ball_right = False
        ball_down = True
        schet_2 += 1
        ball_step += 0.25



    screen.blit(inf_font.render('Счёт: ' + str(schet_2), 5, (255, 99, 71)), (655, 3))
    screen.blit(inf_font.render('Счёт: ' + str(schet), 5, (255, 99, 71)), (400, 3))
    screen.blit(inf_font.render('Скорость мяча: ' + str(ball_step), 5, (255, 99, 71)), (440, 650))

    """отрисовка обьектов"""
    screen.blit(ball, (ball_x, ball_y))
    screen.blit(poloca_2, (poloca_2_x, poloca_2_y))
    screen.blit(poloca, ((poloca_x, poloca_y)))
    screen.blit(panel, (panel_x, panel_y))
    screen.blit(panel_2, (panel_2_x, panel_2_y))
    window.blit(screen, (0, 0))
    pygame.display.flip()
