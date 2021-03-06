import pygame

SPEED_BOT = 0.7
OTSTUP = 80
bot_right = bot_left = False




class Bots(object):
    def __init__(self, bot_x, bot_y, fighter_x, fighter_y, image, bot_atack_right, bot_atack_left,
                 HEALTH_BOT, HEALTH_FIGHTER):
        self.fighter_x = fighter_x
        self.fighter_y = fighter_y
        self.bot_x = bot_x
        self.bot_y = bot_y
        self.image = image
        self.copy = image
        self.bot_atack_right = bot_atack_right
        self.bot_atack_left = bot_atack_left
        self.SPEED_BOT = SPEED_BOT
        self.OTSTUP = OTSTUP
        self.HEALTH_BOT = HEALTH_BOT
        self.HEALTH_FIGHTER = HEALTH_FIGHTER
        self.yvel = 0
        self.onGROUND = False
        self.GRAVITY = 0.04




    #Передвежиние бота
    def update(self, fighter_x, fighter_y, image):
        self.image = image
        self.fighter_x = fighter_x
        self.fighter_y = fighter_y

        """Передвежение бота по оси x"""
        if self.fighter_x < self.bot_x:
            if self.bot_x > self.fighter_x + OTSTUP:
                self.bot_x -= SPEED_BOT

        if fighter_x > self.bot_x:
            if self.bot_x < self.fighter_x - (OTSTUP + 10):
                self.bot_x += SPEED_BOT



        """Падение"""
        if self.bot_y > 520:
            self.onGROUND = True

        if self.onGROUND == False:
            if self.bot_x > 520:
                self.yvel += self.GRAVITY
                self.bot_y += self.yvel














    def health(self,HEALTH_BOT,HEALTH_FIGHTER):
        """Health bot"""
        self.health_bot = pygame.image.load("images/Health_bot/70%.png").convert()
        health_bot_copy = self.health_bot

        health_60_bot = pygame.image.load("images/Health_bot/60%.png").convert()
        health_50_bot = pygame.image.load("images/Health_bot/50%.png").convert()
        health_40_bot = pygame.image.load("images/Health_bot/40%.png").convert()
        health_30_bot = pygame.image.load("images/Health_bot/30%.png").convert()
        health_20_bot = pygame.image.load("images/Health_bot/20%.png").convert()
        health_10_bot = pygame.image.load("images/Health_bot/10%.png").convert()
        health_0_bot = pygame.image.load("images/Health_bot/0%.png").convert_alpha()


        self.HEALTH_BOT = HEALTH_BOT
        self.HEALTH_FIGHTER = HEALTH_FIGHTER


        if self.HEALTH_BOT == 70:
            self.health_bot = health_bot_copy

        elif self.HEALTH_BOT >= 60:
            self.health_bot = health_60_bot

        elif self.HEALTH_BOT >= 50:
            self.health_bot = health_50_bot

        elif self.HEALTH_BOT >= 40:
            self.health_bot = health_40_bot

        elif self.HEALTH_BOT >= 30:
            self.health_bot = health_30_bot

        elif self.HEALTH_BOT >= 20:
            self.health_bot = health_20_bot

        elif self.HEALTH_BOT >= 10:
            self.health_bot = health_10_bot

        elif self.HEALTH_BOT >= 9:
            self.health_bot = health_0_bot

        elif self.HEALTH_BOT < 9:
            self.health_bot = health_0_bot








    #отрисовка бота
    def draw(self, surf):

        surf.blit(self.image, (self.bot_x, self.bot_y))
        surf.blit(self.health_bot, (self.bot_x + 36, self.bot_y - 40))






