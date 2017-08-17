import pygame

"""окно"""
window = pygame.display.set_mode((1000, 660))
pygame.display.set_caption("Игра 1.0")

"""холст"""
screen = pygame.Surface((1000, 600))

"""строка состояния"""
info_string = pygame.Surface((1000, 60))
schet = 0

"""описание мяча"""
ball = pygame.image.load("ball.png").convert()
ball = pygame.transform.scale(ball, (70, 70))
ball_step = 1


"""координаты мяча"""
ball_x = 470
ball_y = 230
ball_right = True
ball_down = True


"""шрифты"""
pygame.font.init()
speed_font = pygame.font.SysFont("Buxton Sketch", 50)
inf_font = pygame.font.SysFont("Buxton Sketch", 50)


"""описание полосы сверху"""
poloca = pygame.Surface((1000, 20))
poloca.fill((105, 105, 105))


"""описание панели снизу"""
panel = pygame.Surface((200, 30))
panel.fill((128, 128, 128))


"""координаты панели"""
panel_x = 400
panel_y = 520


"""функция для столкновения обьектов"""
def Intersect(x1, x2, y1, y2):
    if (x1 > x2-70) and (x1 < x2 + 200) and (y1 > y2-70) and (y1 < y2+30):
        return 1
    else:
        return 0



"""событие закрытия окна"""
done = True
pygame.key.set_repeat(1, 1)
while done :
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False



        """передвижение панели клавишами"""
        if e.type == pygame.KEYDOWN:

            if e.key == pygame.K_LEFT:
                if panel_x > 0:
                    panel_x -= 2

            if e.key == pygame.K_RIGHT:
                if panel_x < 800:
                    panel_x += 2



    """передвежиние мяча по оси x и y"""
    if ball_right == True:
        ball_x += ball_step
        if ball_x > 930:
            ball_right = False

    else:
        ball_x -= ball_step
        if ball_x < 0:
            ball_right = True


    if ball_down == True:
        ball_y -= ball_step
        if ball_y < 40:
            ball_down = False

    else:
        ball_y += ball_step
        if ball_y > 800:
            schet -= 1
            ball_down = True

    """заливка"""
    screen.fill((0, 0, 0))
    info_string.fill((138, 43, 226))


    if Intersect(ball_x, panel_x, ball_y, panel_y) == True:
            ball_down = False
            ball_step += 0.01
            schet += 1

            ball_down = True



    """отрисовка объктов"""
    screen.blit(panel, (panel_x, panel_y))
    screen.blit(poloca, (0, 20))
    screen.blit(ball, (ball_x, ball_y))

    """отрисовка шрифтов"""
    info_string.blit(speed_font.render('Cкорость мяча: '+str(ball_step), 5, (255, 99, 71)), (5, 3))
    info_string.blit(inf_font.render('Счёт: '+str(schet), 5, (255, 99, 71)), (770, 3))


    """отображение холста на экран"""
    window.blit(info_string, (0, 0))
    window.blit(screen, (0, 60))
    pygame.display.flip()
    pygame.time.delay(-20)
    
    
    
    
    
    
 -----------------------------------------------------------------------------------------------------------------
 
 
 
 
 
 
 import random
import pygame

"""окно"""
window = pygame.display.set_mode((1000, 660))
pygame.display.set_caption("Игра 1.0")

"""холст"""
screen = pygame.Surface((1000, 600))

"""строка состояния"""
info_string = pygame.Surface((1000, 60))
schet = 0

"""описание мяча"""
ball = pygame.image.load("ball.png").convert()
ball = pygame.transform.scale(ball, (70, 70))
ball_step = 1


"""координаты мяча"""
a = random.randint(0, 1000)
b = random.randint(60, 400)

ball_x = a
ball_y = b
ball_right = True
ball_down = True


"""шрифты"""
pygame.font.init()
speed_font = pygame.font.SysFont("Buxton Sketch", 50)
inf_font = pygame.font.SysFont("Buxton Sketch", 50)


"""описание полосы сверху"""
poloca = pygame.Surface((1000, 20))
poloca.fill((105, 105, 105))


"""описание панели снизу"""
panel = pygame.Surface((200, 30))
panel.fill((128, 128, 128))


"""координаты панели"""
panel_x = 400
panel_y = 520


"""функция для столкновения обьектов"""
def Intersect(x1, x2, y1, y2):
    if (x1 > x2-70) and (x1 < x2 + 200) and (y1 > y2-70) and (y1 < y2+30):
        return 1
    else:
        return 0




"""событие закрытия окна"""
done = True
pygame.key.set_repeat(1, 1)
while done :
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False



        """передвижение панели клавишами"""
        if e.type == pygame.KEYDOWN:

            if e.key == pygame.K_LEFT:
                if panel_x > 0:
                    panel_x -= 4

            if e.key == pygame.K_RIGHT:
                if panel_x < 800:
                    panel_x += 4



    """передвежиние мяча по оси x и y"""
    if ball_right == True:
        ball_x += ball_step
        if ball_x > 930:
            ball_right = False

    else:
        ball_x -= ball_step
        if ball_x < 0:
            ball_right = True


    if ball_down == True:
        ball_y -= ball_step

        if ball_y < 40:
            ball_down = False

    else:
        ball_y += ball_step
        if ball_y > 800:
            schet -= 1
            ball_down = True




    """заливка"""
    screen.fill((0, 0, 0))
    info_string.fill((138, 43, 226))




    if Intersect(ball_x, panel_x, ball_y, panel_y) == True:

        if (ball_x < panel_x + 200):
            ball_down = True
            ball_right = True
            ball_step += 0.1
            schet += 1


        if(ball_x < panel_x +100):

            ball_down = True
            ball_right = False
            ball_step += 0.1
            schet += 1


        else:
            ball_down = True
            ball_right = True










    """отрисовка объктов"""
    screen.blit(panel, (panel_x, panel_y))
    screen.blit(poloca, (0, 20))
    screen.blit(ball, (ball_x, ball_y))

    """отрисовка шрифтов"""
    info_string.blit(speed_font.render('Cкорость мяча: '+str(ball_step), 5, (255, 99, 71)), (5, 3))
    info_string.blit(inf_font.render('Счёт: '+str(schet), 5, (255, 99, 71)), (770, 3))


    """отображение холста на экран"""
    window.blit(info_string, (0, 0))
    window.blit(screen, (0, 60))
    pygame.display.flip()
    pygame.time.delay(-20)
    
    
    
    ----------------------------------------------------------------------------------------------------------------------------------
    ping pong with menu
    
    
import random
import pygame
import sys

"""окно"""
window = pygame.display.set_mode((1200, 710))
pygame.display.set_caption("Игра 1.0")

"""холст"""
screen = pygame.Surface((1200, 640))

"""строка состояния"""
info_string = pygame.Surface((1200, 60))
schet = 0

"""описание мяча"""
ball = pygame.image.load("ball.png").convert_alpha()
ball = pygame.transform.scale(ball, (70, 70))
ball_step = 1


"""координаты мяча"""
a = random.randint(0, 1000)
b = random.randint(60, 400)

ball_x = a
ball_y = b
ball_right = True
ball_down = True


"""шрифты"""
pygame.font.init()
speed_font = pygame.font.SysFont("Buxton Sketch", 50)
inf_font = pygame.font.SysFont("Buxton Sketch", 50)


"""описание полосы сверху"""
poloca = pygame.Surface((1200, 20))
poloca.fill((105, 105, 105))


"""описание панели снизу"""
panel = pygame.Surface((200, 30))
panel.fill((128, 128, 128))


"""координаты панели"""
panel_x = 500
panel_y = 580



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
            info_string.fill((119, 136, 153))
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

            window.blit(info_string, (0, 0))
            window.blit(screen, (0, 60))
            pygame.display.flip()




"""функция для столкновения обьектов"""
def Intersect(x1, x2, y1, y2):
    if (x1 > x2-70) and (x1 < x2 + 200) and (y1 > y2-70) and (y1 < y2+30):
        return 1
    else:
        return 0


"""создаем меню"""
punkts = [(500, 160, 'Game', (250, 250, 30), (0, 0, 0), 0),
          (500, 260, 'Quit', (250, 250, 30), (0, 0, 0), 1),
          (500, 360, '2 game', (250, 250, 30), (0, 0, 0), 2)]



game = Menu(punkts)
game.menu()



"""подготовка к запуску игры"""
"""событие закрытия окна"""




done = True
pygame.key.set_repeat(1, 1)
pygame.mouse.set_visible(False)
while done :

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False



        """передвижение панели клавишами"""
        if e.type == pygame.KEYDOWN:

            if e.key == pygame.K_LEFT:
                if panel_x > 0:
                    panel_x -= 2

            if e.key == pygame.K_RIGHT:
                if panel_x < 1000:
                    panel_x += 2

            if e.key == pygame.K_ESCAPE:
                game.menu()


    """передвежиние мяча по оси x и y"""
    if ball_right == True:
        ball_x += ball_step
        if ball_x > 1130:
            ball_right = False

    else:
        ball_x -= ball_step
        if ball_x < 0:
            ball_right = True


    if ball_down == True:
        ball_y -= ball_step

        if ball_y < 40:
            ball_down = False

    else:
        ball_y += ball_step
        if ball_y > 800:
            schet -= 2
            ball_down = True




    """заливка"""
    screen.fill((50, 50, 50))
    info_string.fill((138, 43, 226))




    if Intersect(ball_x, panel_x, ball_y, panel_y) == True:

        if (ball_x < panel_x + 200):
            ball_down = True
            ball_right = True
            ball_step += 0.05
            schet += 1


        if (ball_x < panel_x +100):
            ball_down = True
            ball_right = False
            ball_step += 0.05
            schet += 1










    """отрисовка объктов"""
    screen.blit(panel, (panel_x, panel_y))
    screen.blit(poloca, (0, 20))
    screen.blit(ball, (ball_x, ball_y))

    """отрисовка шрифтов"""
    info_string.blit(speed_font.render('Cкорость мяча: '+str(ball_step), 5, (255, 99, 71)), (60, 3))
    info_string.blit(inf_font.render('Счёт: '+str(schet), 5, (255, 99, 71)), (900, 3))


    """отображение холста на экран"""
    window.blit(info_string, (0, 0))
    window.blit(screen, (0, 60))
    pygame.display.flip()
    pygame.time.delay(-20)




------------------------------------------------------------------------------------------------------------------------------------
игра пинг понг вместе в анимации шара(не работает) выдает ошибку TypeError: object() takes no parameters


import random
import pygame
import sys

"""окно"""
window = pygame.display.set_mode((1200, 710))
pygame.display.set_caption("Игра 1.0")

"""холст"""
screen = pygame.Surface((1200, 640))

"""строка состояния"""
info_string = pygame.Surface((1200, 60))
schet = 0

"""описание мяча"""
ball = pygame.image.load("ball.png").convert_alpha()
ball = pygame.transform.scale(ball, (70, 70))
ball_step = 1


"""координаты мяча"""
a = random.randint(0, 1000)
b = random.randint(60, 400)

ball_x = a
ball_y = b
ball_right = True
ball_down = True


"""шрифты"""
pygame.font.init()
speed_font = pygame.font.SysFont("Buxton Sketch", 50)
inf_font = pygame.font.SysFont("Buxton Sketch", 50)


"""описание полосы сверху"""
poloca = pygame.Surface((1200, 20))
poloca.fill((105, 105, 105))


"""описание панели снизу"""
panel = pygame.Surface((200, 30))
panel.fill((128, 128, 128))


"""координаты панели"""
panel_x = 500
panel_y = 580


"""Класс меню"""
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
            info_string.fill((119, 136, 153))
            screen.fill((119, 136, 153))

            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp [0]>i[0] and mp[0]<i[0]+200 and mp[1]>i[1] and mp[1]<i[1]+100:
                    punkt = i[5]
            self.render(screen, font_menu , punkt)

            """НАЖАТИЕ КНОПКАМ ВВЕРХ И ВНИЗ"""
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

                """нАЖАТИЕ КНОПКОЙ МЫШЬЮ НА ПУНКТ"""
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        done = False
                    elif punkt == 1:
                        sys.exit()

            window.blit(info_string, (0, 0))
            window.blit(screen, (0, 60))
            pygame.display.flip()

"""Класс для создания анимации"""
class Animation:
    def _init_(self, x, y, sprites=None, time=100):
        self.x = x
        self.y = y
        self.sprites = sprites
        self.time = time
        self.work_time = 0
        self.skip_frame = 0
        self.frame = 0

    def update(self, dt):
        self.work_time += dt
        self.skip_frame = self.work_time / self.time
        if self.skip_frame > 0:
            self.work_time = self.work_time % self.time
            self.frame += self.skip_frame
            if self.frame >= len(self.sprites):
                self.frame = 0

    def get_sprite(self):
        return self.sprites[self.frame]




"""загружаем анимирувонную картинку"""
sprite = pygame.image.load('ball1.png').convert_alpha()



''' вырезаем кадры ''' ####
anim = []
anim.append(sprite.subsurface((0, 0, 80, 80)))
anim.append(sprite.subsurface((40, 0, 40, 40)))
anim.append(sprite.subsurface((80, 0, 40, 40)))




"""создаем кадровую ленту"""
time = 180
target = Animation(anim, time)





"""функция для столкновения обьектов"""
def Intersect(x1, x2, y1, y2):
    if (x1 > x2-70) and (x1 < x2 + 200) and (y1 > y2-70) and (y1 < y2+30):
        return 1
    else:
        return 0


"""создаем меню"""
punkts = [(500, 160, 'Game', (250, 250, 30), (0, 0, 0), 0),
          (500, 260, 'Quit', (250, 250, 30), (0, 0, 0), 1)]




game = Menu(punkts)
game.menu()


"""Создаём таймер"""
clock = pygame.time.Clock()
dt = 0



"""подготовка к запуску игры"""
done = True
pygame.key.set_repeat(1, 1)
pygame.mouse.set_visible(False)
while done :
    """ОБРАБОТЧИК СОБЫТИЙ"""

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False



        """передвижение панели клавишами"""
        if e.type == pygame.KEYDOWN:

            if e.key == pygame.K_LEFT:
                if panel_x > 0:
                    panel_x -= 2

            if e.key == pygame.K_RIGHT:
                if panel_x < 1000:
                    panel_x += 2

            if e.key == pygame.K_ESCAPE:
                game.menu()


    """передвежиние мяча по оси x и y"""
    if ball_right == True:
        ball_x += ball_step
        if ball_x > 1130:
            ball_right = False

    else:
        ball_x -= ball_step
        if ball_x < 0:
            ball_right = True


    if ball_down == True:
        ball_y -= ball_step

        if ball_y < 40:
            ball_down = False

    else:
        ball_y += ball_step
        if ball_y > 800:
            schet -= 2
            ball_down = True


    """заливка"""
    screen.fill((50, 50, 50))
    info_string.fill((138, 43, 226))




    if Intersect(ball_x, panel_x, ball_y, panel_y) == True:

        if (ball_x < panel_x + 200):
            ball_down = True
            ball_right = True
            ball_step += 0.05
            schet += 1


        if (ball_x < panel_x +100):
            ball_down = True
            ball_right = False
            ball_step += 0.05
            schet += 1










    """отрисовка объктов"""
    target.update(dt)
    screen.blit(target.get_sprite(), (0, 0))
    screen.blit(panel, (panel_x, panel_y))
    screen.blit(poloca, (0, 20))
    screen.blit(ball, (ball_x, ball_y))

    """отрисовка шрифтов"""
    info_string.blit(speed_font.render('Cкорость мяча: '+str(ball_step), 5, (255, 99, 71)), (60, 3))
    info_string.blit(inf_font.render('Счёт: '+str(schet), 5, (255, 99, 71)), (900, 3))


    """отображение холста на экран"""
    window.blit(info_string, (0, 0))
    window.blit(screen, (0, 60))
    pygame.display.flip()
    dt = clock.tick(120)
