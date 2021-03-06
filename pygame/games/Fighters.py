import pygame
from pygame import mixer
from Bot import Bots
from tkinter import *
import sys






def main(root, canvas_fake, canvas):
    canvas.destroy()

    canvas1 = Canvas(root, width=600, height=700, bg='#A9A9A9')
    canvas_fake = Canvas(root, width=600, height=700, bg='#A9A9A9')

    label = Label(canvas_fake,
                  text="Fighters",
                  bg="#A9A9A9",
                  fg='black',
                  font="Aharoni 90")
    label.place(x=80, y=7)

    button_play = Button(canvas_fake, text='Play', fg='white', bg="#696969", width=30, height='3', font='Calibri')
    button_play.bind('<Button-1>', lambda event: fun(root))
    button_play.place(x=150, y=150)

    button_play = Button(canvas_fake, text='Control', fg='white', bg="#696969", width=30, height='3',
                         font='Calibri')
    button_play.bind('<Button-1>', lambda event:control(canvas_fake,canvas1, root))
    button_play.place(x=150, y=250)

    button_play = Button(canvas_fake, text='Volume', fg='white', bg="#696969", width=30, height='3', font='Calibri')
    button_play.bind('<Button-1>',lambda event: volume(canvas_fake,canvas1, root))
    button_play.place(x=150, y=350)

    button_play = Button(canvas_fake, text='Description', fg='white', bg="#696969", width=30, height='3',
                         font='Calibri')
    button_play.bind('<Button-1>', lambda event: description(canvas_fake,canvas1, root))
    button_play.place(x=150, y=450)

    button_play = Button(canvas_fake, text='Exit', fg='white', bg="#696969", width=30, height='3', font='Calibri')
    button_play.bind('<Button-1>', exit)
    button_play.place(x=150, y=550)

    canvas_fake.pack()
    canvas1.pack()
    root.mainloop()







def fun(root):
    root.destroy()

    SPEED_FIGHTER = 4
    SPEED_BIRD_X = 0.4
    SPEED_BIRD_Y = 0.1
    JUMP_SPEED = 0.2
    HEALTH_FIGHTER = 100
    DAMAGE_FIGHTER = 0.1
    HEALTH_BOT = 70
    DAMAGE_BOT_PROST = 0.09
    DAMAGE_BOT_SIL = 1
    GRAVITY = 0.08
    MANA = 100
    MANA_PLUS = 1

    """размер окна"""
    SIZE = (1450, 770)

    """создание окна"""
    window = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Fighters")

    """холст"""
    screen = pygame.image.load("images/fon.png").convert()
    screen = pygame.transform.scale(screen, (SIZE))
    screen_win = pygame.image.load("images/win.jpg").convert()
    screen_lose = pygame.image.load("images/lose.jpg").convert()
    clock = pygame.time.Clock()

    """холст фейк"""
    screen_fake = pygame.Surface(SIZE)











    """шрифты"""
    pygame.font.init()
    font = pygame.font.SysFont("Berlin Sans FB", 25)
    font2 = pygame.font.SysFont("Berlin Sans FB", 17)










    """создание обектов"""
    """Птицы"""
    bird = pygame.image.load("images/bird.png").convert_alpha()
    bird = pygame.transform.scale(bird, (70, 70))
    birdq = bird

    birdleft = pygame.image.load("images/birdleft.png").convert_alpha()
    birdleft = pygame.transform.scale(birdleft, (70, 70))
    birdw = birdleft

    birdnew1 = pygame.image.load("images/bird.png").convert_alpha()
    birdnew1 = pygame.transform.scale(birdnew1, (70, 70))
    birdt = birdnew1

    """Fighter (анимация)"""
    fighter = pygame.image.load("images/fighter.png").convert_alpha()
    fighter_copy = fighter

    fighter_down = pygame.image.load("images/fighter_down.png").convert_alpha()
    fighter_down_copy = fighter_down

    fighter_left = pygame.image.load("images/fighter_left.png").convert_alpha()
    fighter_left_copy = fighter_left

    fighter_right = pygame.image.load("images/fighter_right.png").convert_alpha()
    fighter_right_copy = fighter_right

    fighter_up = pygame.image.load("images/fighter_up.png").convert_alpha()
    fighter_up_copy = fighter_up

    """атаки Fighters"""
    fighter_atack_stay = pygame.image.load("images/fighter_atack_stay.png").convert_alpha()
    fighter_atack_stay_copy = fighter_atack_stay

    fighter_atack_stay_2 = pygame.image.load("images/fighter_atack_stay(2).png").convert_alpha()
    fighter_atack_stay_2_copy = fighter_atack_stay_2

    fighter_right_atack = pygame.image.load("images/fighter_right_atack.png").convert_alpha()
    fighter_right_atack_copy = fighter_right_atack

    fighter_left_atack = pygame.image.load("images/fighter_left_atack.png").convert_alpha()
    fighter_left_atack_copy = fighter_left_atack

    """БОТ"""
    bot = pygame.image.load("images/bot.png").convert_alpha()
    bot_copy = bot



    """Атаки Бота"""
    bot_atack_right = pygame.image.load("images/bot_atack_right.png").convert_alpha()
    bot_atack_right_copy = bot_atack_right

    bot_atack_left = pygame.image.load("images/bot_atack_left.png").convert_alpha()
    bot_atack_left_copy = bot_atack_left




    """Mana"""
    mana = pygame.image.load("images/Mana/1000%.png").convert()
    mana_copy = mana

    mana_950 = pygame.image.load("images/Mana/950%.png").convert()
    mana_900 = pygame.image.load("images/Mana/900%.png").convert()
    mana_850 = pygame.image.load("images/Mana/850%.png").convert()
    mana_800 = pygame.image.load("images/Mana/800%.png").convert()
    mana_750 = pygame.image.load("images/Mana/750%.png").convert()
    mana_700 = pygame.image.load("images/Mana/700%.png").convert()
    mana_650 = pygame.image.load("images/Mana/650%.png").convert()
    mana_600 = pygame.image.load("images/Mana/600%.png").convert()
    mana_550 = pygame.image.load("images/Mana/550%.png").convert()
    mana_500 = pygame.image.load("images/Mana/500%.png").convert()
    mana_450 = pygame.image.load("images/Mana/450%.png").convert()
    mana_400 = pygame.image.load("images/Mana/400%.png").convert()
    mana_350 = pygame.image.load("images/Mana/350%.png").convert()
    mana_300 = pygame.image.load("images/Mana/300%.png").convert()
    mana_250 = pygame.image.load("images/Mana/250%.png").convert()

    """Health fighter"""
    health = pygame.image.load("images/Health/100%.png").convert()
    health_copy = health

    health_95 = pygame.image.load("images/Health/95%.png").convert()
    health_90 = pygame.image.load("images/Health/90%.png").convert()
    health_85 = pygame.image.load("images/Health/85%.png").convert()
    health_80 = pygame.image.load("images/Health/80%.png").convert()
    health_75 = pygame.image.load("images/Health/75%.png").convert()
    health_70 = pygame.image.load("images/Health/70%.png").convert()
    health_65 = pygame.image.load("images/Health/65%.png").convert()
    health_60 = pygame.image.load("images/Health/60%.png").convert()
    health_55 = pygame.image.load("images/Health/55%.png").convert()
    health_50 = pygame.image.load("images/Health/50%.png").convert()
    health_45 = pygame.image.load("images/Health/45%.png").convert()
    health_40 = pygame.image.load("images/Health/40%.png").convert()
    health_35 = pygame.image.load("images/Health/35%.png").convert()
    health_30 = pygame.image.load("images/Health/30%.png").convert()
    health_25 = pygame.image.load("images/Health/25%.png").convert()
    health_20 = pygame.image.load("images/Health/20%.png").convert()
    health_15 = pygame.image.load("images/Health/15%.png").convert()
    health_10 = pygame.image.load("images/Health/10%.png").convert()
    health_5 = pygame.image.load("images/Health/5%.png").convert()
    health_0 = pygame.image.load("images/Health/0%.png").convert_alpha()


    """Health bot"""
    health_bot = pygame.image.load("images/Health_bot/70%.png").convert
    health_bot_copy = health_bot







    """координаты птиц"""
    bird_right = True
    bird_down = True
    bird_x = 0
    bird_y = 0

    birdnew1_right = True
    birdnew1_down = True
    birdnew1_x = -600
    birdnew1_y = 80

    """координаты бойца"""
    fighter_right = False
    fighter_left = False
    fighter_down = False
    fighter_up = False
    fighter_atack_1 = False
    fighter_atack_2 = False
    fighter_right_atacks = False
    fighter_left_atacks = False
    onGROUND = False
    fighter_yvel = 0
    fighter_x = 200
    fighter_y = 250
    vidimost_fighter = True

    """координаты бота"""
    bot_right = bot_left = False
    bot_atack1 = False
    bot_atack2 = False
    vidimost = True

    """1 БОТ"""
    bot1 = Bots(1000, 250, fighter_x, fighter_y, bot, bot_atack_right,
                bot_atack_left, HEALTH_BOT, HEALTH_FIGHTER)








    """функция для столкновения обьектов"""
    def Intersect(x1, x2, y1, y2):
        if (x1 > x2 - 135) and (x1 < x2 + 159) and (y1 > y2 - 140) and (y1 < y2 + 185):
            return 1
        else:
            return 0






    """Фоновая музыка"""
    mixer.pre_init(44100, -16, 1, 512)
    mixer.init()
    sound = mixer.Sound("sounds/metro_2033.ogg")
    sound.play(-1)

    sec = 0.50







    """обработчик событий"""
    done = True
    while done:
        timer = pygame.time.get_ticks() / 1000
        print(timer)

        if MANA != 100:
            if timer > sec:
                sec += 0.50
                MANA += MANA_PLUS








        """ЦИКЛ"""
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = False
                sys.exit()









            """событие нажатие на мыщку"""
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 3:
                    fighter_atack_1 = True

                if e.button == 1:
                    fighter_atack_2 = True






            """событие отжатие на мышку"""
            if e.type == pygame.MOUSEBUTTONUP:
                if e.button == 3:
                    fighter_atack_1 = False
                    fighter = fighter_copy

                if e.button == 1:
                    fighter_atack_2 = False
                    fighter = fighter_copy





            """событие нажатия на клавиатуру"""
            if e.type == pygame.KEYDOWN:

                if e.key == pygame.K_ESCAPE:
                    menu()

                if e.key == pygame.K_d:
                    fighter_right = True

                if e.key == pygame.K_a:
                    fighter_left = True

                if e.key == pygame.K_s:
                    fighter_down = True

                if e.key == pygame.K_e:
                    fighter_right_atacks = True

                if e.key == pygame.K_q:
                    fighter_left_atacks = True

                if fighter_y > 544:
                    if e.key == pygame.K_SPACE:
                        fighter_up = True





            """событие отжатие клавиатуры"""
            if e.type == pygame.KEYUP:

                if e.key == pygame.K_d:
                    fighter_right = False
                    fighter = fighter_copy

                if e.key == pygame.K_a:
                    fighter_left = False
                    fighter = fighter_copy

                if e.key == pygame.K_s:
                    fighter_down = False
                    fighter = fighter_copy

                if e.key == pygame.K_e:
                    fighter_right_atacks = False
                    fighter = fighter_copy

                if e.key == pygame.K_q:
                    fighter_left_atacks = False
                    fighter = fighter_copy



        """Условия передвежения Fighter"""
        if vidimost_fighter == True:

            if fighter_right == True:
                fighter = fighter_right_copy
                if fighter_x < 1330:
                    fighter_x += SPEED_FIGHTER

            if fighter_left == True:
                fighter = fighter_left_copy
                if fighter_x > 0:
                    fighter_x -= SPEED_FIGHTER

            if fighter_down == True:
                if fighter_y > 544:
                    onGROUND = True
                    fighter = fighter_down_copy




        """Прыжок"""
        if fighter_up == True:
            onGROUND = True
            fighter = fighter_up_copy
            if fighter_y > 200:
                for i in range(20):
                    fighter_y -= JUMP_SPEED

            else:
                fighter_up = False
                onGROUND = False

        if onGROUND == True:
            fighter_yvel = 0




        """Падение"""
        if onGROUND == False:
            fighter = fighter_copy
            if fighter_y < 545:
                fighter_yvel += GRAVITY
                fighter_y += fighter_yvel





        """атаки Fighters"""
        if vidimost_fighter == True:
            if fighter_atack_1 == True:
                fighter = fighter_atack_stay_copy

            if fighter_atack_2 == True:
                fighter = fighter_atack_stay_2_copy

            if MANA > 10:
                if fighter_right_atacks == True:
                    fighter = fighter_right_atack_copy
                    MANA -= MANA_PLUS






        if MANA > 10:
            if fighter_left_atacks == True:
                fighter = fighter_left_atack_copy
                MANA -= MANA_PLUS




        if HEALTH_FIGHTER < -1:
            vidimost_fighter = False





        """Мана fighter"""
        if MANA != -100:

            if MANA == 100:
                mana = mana_copy


            elif MANA >= 95:
                mana = mana_950

            elif MANA >= 90:
                mana = mana_900

            elif MANA >= 85:
                mana = mana_850

            elif MANA >= 80:
                mana = mana_800

            elif MANA >= 75:
                mana = mana_750

            elif MANA >= 70:
                mana = mana_700

            elif MANA >= 65:
                mana = mana_650

            elif MANA >= 60:
                mana = mana_600

            elif MANA >= 55:
                mana = mana_550

            elif MANA >= 50:
                mana = mana_500

            elif MANA >= 45:
                mana = mana_450

            elif MANA >= 40:
                mana = mana_400

            elif MANA >= 35:
                mana = mana_350

            elif MANA >= 30:
                mana = mana_300

            elif MANA >= 25:
                mana = mana_250


        """Health fighter"""
        if vidimost_fighter == True:

            if HEALTH_FIGHTER == 100:
                health = health_copy

            elif HEALTH_FIGHTER >= 95:
                health = health_95

            elif HEALTH_FIGHTER >= 90:
                health = health_90

            elif HEALTH_FIGHTER >= 85:
                health = health_85

            elif HEALTH_FIGHTER >= 80:
                health = health_80

            elif HEALTH_FIGHTER >= 75:
                health = health_75

            elif HEALTH_FIGHTER >= 70:
                health = health_70

            elif HEALTH_FIGHTER >= 65:
                health = health_65

            elif HEALTH_FIGHTER >= 60:
                health = health_60

            elif HEALTH_FIGHTER >= 55:
                health = health_55

            elif HEALTH_FIGHTER >= 45:
                health = health_45

            elif HEALTH_FIGHTER >= 40:
                health = health_40

            elif HEALTH_FIGHTER >= 35:
                health = health_35

            elif HEALTH_FIGHTER >= 30:
                health = health_30

            elif HEALTH_FIGHTER >= 25:
                health = health_25

            elif HEALTH_FIGHTER >= 20:
                health = health_20

            elif HEALTH_FIGHTER >= 15:
                health = health_15

            elif HEALTH_FIGHTER >= 10:
                health = health_10

            elif HEALTH_FIGHTER >= 5:
                health = health_5

            elif HEALTH_FIGHTER >= 0:
                health = health_0


        if vidimost == True:
            """Health bot"""
            bot1.health(HEALTH_BOT, HEALTH_FIGHTER)









        """Передвежение 1 птицы по оси X"""
        if bird_right == True:
            bird_x += SPEED_BIRD_X
            if bird_x > 1500:
                bird_right = False


        else:
            bird = birdw
            bird_x -= SPEED_BIRD_X
            if bird_x < -70:
                bird = birdq
                bird_right = True

        """Передвежение 1 птицы по оси y"""
        if bird_down == True:
            bird_y += SPEED_BIRD_Y
            if bird_y > 70:
                bird_down = False


        else:
            bird_y -= SPEED_BIRD_Y
            if bird_y < 20:
                bird_down = True









        """Передвежение 2 птицы по оси X"""
        if birdnew1_right == True:
            birdnew1_x += SPEED_BIRD_X
            if birdnew1_x > 1500:
                birdnew1_right = False


        else:
            birdnew1 = birdw
            birdnew1_x -= SPEED_BIRD_X
            if birdnew1_x < -70:
                birdnew1 = birdt
                birdnew1_right = True

        """Передвежение 2 птицы по оси y"""
        if birdnew1_down == True:
            birdnew1_y += SPEED_BIRD_Y
            if birdnew1_y > 150:
                birdnew1_down = False


        else:
            birdnew1_y -= SPEED_BIRD_Y
            if birdnew1_y < 80:
                birdnew1_down = True

        if vidimost == True:





            """Передвежение бота по оси x"""
            bot1.update(fighter_x, fighter_y, bot)

        if HEALTH_BOT <= 9:
            vidimost = False




        if HEALTH_BOT < 10:
            screen = screen_win

        if HEALTH_FIGHTER <-1:
            screen = screen_lose





        """заливка фейкового холста"""
        screen_fake.fill((50, 50, 50))

        if vidimost == True:
            """столкновение c ботом"""
            if Intersect(fighter_x, bot1.bot_x, fighter_y, bot1.bot_y) == True:

                """право(бот)"""
                if fighter_x > bot1.bot_x:
                    fighter_left = False
                    bot_atack1 = True
                    bot_atack2 = False

                    if vidimost_fighter == True:
                        """атака вправо от бота"""
                        if bot_atack1 == True:
                            bot = bot_atack_right
                            HEALTH_FIGHTER -= DAMAGE_FIGHTER

                        else:
                            bot = bot_copy

                    """простая атака влево от fighter"""
                    if fighter_atack_2:
                        HEALTH_BOT -= DAMAGE_BOT_PROST

                    """сильная атака от fighter"""
                    if MANA > 30:
                        if fighter_left_atacks == True:
                            HEALTH_BOT -= DAMAGE_BOT_SIL

                """лево(бот)"""
                if fighter_x < bot1.bot_x:
                    fighter_right = False
                    bot_atack2 = True
                    bot_atack1 = False

                    if vidimost_fighter == True:
                        """атака влево от бота"""
                        if bot_atack2 == True:
                            bot = bot_atack_left
                            HEALTH_FIGHTER -= DAMAGE_FIGHTER

                        else:
                            bot = bot_copy

                    """простая атака вправо от fighter"""
                    if fighter_atack_1:
                        HEALTH_BOT -= DAMAGE_BOT_PROST

                    """сильная атака от fighter"""
                    if MANA > 30:
                        if fighter_right_atacks == True:
                            HEALTH_BOT -= DAMAGE_BOT_SIL

            else:
                bot = bot_copy

        else:
            bot = pygame.image.load("images/Health_bot/0%.png").convert_alpha()














        """отоброжение обьектов"""
        screen_fake.blit(screen, (0, 0))
        screen_fake.blit(font.render('Health Fighter: ' + str(HEALTH_FIGHTER), 5, (117, 74, 103)), (45, 20))
        screen_fake.blit(font.render('Health Bot: ' + str(HEALTH_BOT), 5, (117, 74, 103)), (45, 50))
        screen_fake.blit(font.render('Mana: ' + str(MANA), 5, (117, 74, 103)), (45, 80))
        screen_fake.blit(font2.render('fps: ' + str(int(clock.get_fps())), 5, (117, 74, 103)), (1370, 20))

        screen_fake.blit(health, (fighter_x, fighter_y - 25))
        if vidimost_fighter == True:
            screen_fake.blit(mana, (fighter_x, fighter_y - 40))
        if vidimost == True:
            bot1.draw(screen_fake)
        if vidimost_fighter == True:
            screen_fake.blit(fighter, (fighter_x, fighter_y))
        screen_fake.blit(bird, (bird_x, bird_y))
        screen_fake.blit(birdnew1, (birdnew1_x, birdnew1_y))

        """отображение рабочей поверхности на экран"""

        window.blit(screen_fake, (0, 0))
        clock.tick(0)
        pygame.display.flip()






def exit(event):
    sys.exit()






def description(canvas_fake, canvas, root):
    canvas_fake.destroy()



    image = PhotoImage(file='images/description.gif')
    l = Label(canvas, image=image)
    l.pack()

    root.bind('<Escape>',lambda event:main(root, canvas_fake, canvas))


    root.mainloop()







def control(canvas_fake, canvas, root):

    def con_but(event):
        back = ent1.get()
        print(back)

        right = ent2.get()
        print(right)

        left = ent3.get()
        print(left)

        space = ent4.get()
        print(space)

        down = ent5.get()
        print(down)

        mouse1 = ent6.get()
        print(mouse1)

        mouse2 = ent7.get()
        print(mouse2)

        hard1 = ent8.get()
        print(hard1)

        hard2 = ent9.get()
        print(hard2)


    canvas_fake.destroy()
    image = PhotoImage(file='images/control.gif')
    l = Label(canvas, image=image)
    l.pack()




    ent1 = Entry(canvas, width=20, bd=7)
    ent1.insert(END, "Esc")
    ent1.place(x=400, y=25)


    ent2 = Entry(canvas, width=20, bd=7)
    ent2.insert(END,"D")
    ent2.place(x=400, y=95)

    ent3 = Entry(canvas, width=20, bd=7)
    ent3.insert(END, "A")
    ent3.place(x=400, y=165)

    ent4 = Entry(canvas, width=20, bd=7)
    ent4.insert(END, "Space")
    ent4.place(x=400, y=235)

    ent5 = Entry(canvas, width=20, bd=7)
    ent5.insert(END, "S")
    ent5.place(x=400, y=305)

    ent6 = Entry(canvas, width=20, bd=7)
    ent6.insert(END, "Mouse click 1")
    ent6.place(x=400, y=375)

    ent7 = Entry(canvas, width=20, bd=7)
    ent7.insert(END, "Mouse click 2")
    ent7.place(x=400, y=445)

    ent8 = Entry(canvas, width=20, bd=7)
    ent8.insert(END, "E")
    ent8.place(x=400, y=515)

    ent9 = Entry(canvas, width=20, bd=7)
    ent9.insert(END, "Q")
    ent9.place(x=400, y=585)



    button_play = Button(canvas, text='Enter', fg='white', bg="#696969", width=20, height='2', font='Calibri')
    button_play.bind('<Button-1>', con_but)
    button_play.place(x=330, y=630)


    root.bind('<Escape>', lambda event: main(root, canvas_fake, canvas))
    root.mainloop()






def volume(canvas_fake, canvas, root):
    canvas_fake.destroy()

    image = PhotoImage(file='images/volume.gif')
    l = Label(canvas, image=image)
    l.pack()


    def volume_but(event):
        ent = ent1.get()
        print(ent)




    ent1 = Entry(canvas, width=20, bd=8, font = "Calibri 20")
    ent1.insert(END, "100")
    ent1.place(x = 30, y=200)

    button_play = Button(canvas, text='Enter', fg='white', bg="#696969", width=23, height='2', font='Calibri')
    button_play.bind('<Button-1>', volume_but)
    button_play.place(x=350, y=200)



    root.bind('<Escape>', lambda event: main(root, canvas_fake, canvas))
    root.mainloop()







def menu ():
    root = Tk()
    root.geometry("600x700")
    root.title('menu')



    canvas_fake = Canvas(root, width = 600, height = 700, bg = '#A9A9A9')
    canvas = Canvas(root, width = 600, height = 700, bg = '#A9A9A9')



    label = Label(canvas_fake,
                text="Fighters",
                bg = "#A9A9A9",
                fg = 'black',
                font="Aharoni 90")
    label.place(x = 80, y = 7)







    button_play = Button(canvas_fake, text='Play', fg = 'white', bg = "#696969", width = 30, height = '3', font = 'Calibri')
    button_play.bind('<Button-1>',lambda event: fun(root))
    button_play.place(x = 150, y = 150)

    button_play = Button(canvas_fake, text='Control', fg = 'white', bg = "#696969", width = 30, height = '3',
                        font = 'Calibri')
    button_play.bind('<Button-1>', lambda event: control(canvas_fake,canvas, root))
    button_play.place(x = 150, y = 250)

    button_play = Button(canvas_fake, text='Volume', fg = 'white', bg = "#696969", width = 30, height = '3', font = 'Calibri')
    button_play.bind('<Button-1>',lambda event: volume(canvas_fake,canvas, root))
    button_play.place(x = 150, y = 350)

    button_play = Button(canvas_fake, text='Description', fg = 'white', bg = "#696969", width = 30, height = '3',
                        font = 'Calibri')
    button_play.bind('<Button-1>', lambda event: description(canvas_fake,canvas, root))
    button_play.place(x = 150, y = 450)

    button_play = Button(canvas_fake, text='Exit', fg = 'white', bg = "#696969", width = 30, height = '3', font = 'Calibri')
    button_play.bind('<Button-1>', exit)
    button_play.place(x = 150, y = 550)








    canvas_fake.pack()
    canvas.pack()
    root.mainloop()

menu()
