class Criter(object):
    total = 0

    @staticmethod
    def status():
        print("На свет появилось: ",Criter.total, "зверюшек")


    def __init__(self, name):
        self.name = name
        print("На свет появилась новая зверюшки")
        Criter.total += 1

    def __str__(self):
        rep = ("Обьект класса Critter\n")
        rep += "Имя: " + self.name
        return rep

    def talk(self):
        print("Привет меня зовут", self.name,"\n")

crit = Criter("Бобик")
crit.talk()

crit2 = Criter("Мурзик")
crit2.talk()


print("\n\nВывод обьектов на экран")
print(crit)
print(crit2)

Criter.status()

--------------------------------------------------------------------------------------------------------------------------------------

class Criter(object):
    total = 0


    @staticmethod
    def status():
        print("Всего на свет появилось ", Criter.total, "зверюшек")

    def __init__(self, name, nastr):
        print("\n\nНа свет появилась новая зверюшка!")
        self.name = name
        self.__nastr = nastr
        Criter.total += 1

    def talk (self):
        print("Привет меня зовут ", self.name)
        print("У меня настроение ",self.__nastr,"\n")

    def __str__(self):
        rep = ("ОбЪект класса Criter\n")
        rep += "Имя: "+ self.name
        rep += "\nНастроение: "+ self.__nastr
        return rep

    def __private_method(self):
        print("Это закрытый метод")

    def publik_method(self):
        print("Это открытый метод")
        self.__private_method()



crit = Criter("Мурзик","хорошее")
crit.talk()
print(crit)

crit2 = Criter("Бобик", "Плохое")
crit2.talk()
print(crit2)

print("\n")
crit.status()
print("\n")



crit.publik_method()


--------------------------------------------------------------------------------------------------------------------------------------



class Criter(object):

    def __init__(self, name, hungry = 0, boredom = 0):
        self.name = name
        self.hungry = hungry
        self.boredom = boredom


    def __pasttime(self):
        self.hungry += 1
        self.boredom += 1


    @property
    def mood(self):
        unhappy = self.hungry + self.boredom
        if unhappy < 5:
            m = "Превосходно"
            print("\n\n")

        elif unhappy <= 10:
            m ="неплохо"
            print("\n\n")

        elif unhappy <= 15:
            m = "не сказать что хорошо"
            print("\n\n")

        else:
            m = "ужасно"
            print("\n\n")

        return m




    def talk(self):
        print("Привет меня зовут ",self.name, "чувствую я себя ", self.mood)
        print("\n\n")
        self.__pasttime()


    def eat(self, food = 4):
        food = int(input("\nСколько вы хотите скормить пачек вискаса?"))
        print("МРррррр\n\n")
        self.hungry += food
        if self.hungry > 0:
            self.hungry = 0

        self.__pasttime()


    def play(self, happy = 4):
        happy = int(input("\nСколько времени вы хотите поиграть с питомцем(в часах)?\n\n"))
        print("\nУраа\n\n")
        self.boredom += happy
        if self.boredom > 0:
            self.boredom = 0

        self.__pasttime()

def main():
    crit_name = input("Как вы назовете свою зверюшку? ")
    crit = Criter(crit_name)

    choice = None
    while choice!= 0:
        print("0. Выход\n1.Узнать самочувствие зверюшки\n2.Покормить зверюшку\n3.Поиграть со зверюшкой")
        choice = input("Ваш выбор: ")
        if choice == '0':
            print("Досвидание")

        elif choice == '1':
            crit.talk()

        elif choice == '2':
            crit.eat()

        elif choice =='3':
            crit.play()

        else:
            print("Введите коректный номер")

main()
input("\n Нажмите ентер чтобы выйти")



-------------------------------------------------------------------------------------------------------------------
Программа TV

class TV(object):
    def __init__(self,kanal = 0, gr = 0):
        self.kanal = kanal
        self.gr = gr

    def kan(self):
        self.kanal = int(input("Введите канал который хотите посмотреть: "))
        if self.kanal < 100:
            print("Готово\n\n")

        else:
            print("\nТокого канала нет\n\n")


    def grom(self):
        self.gr = int(input("Введите громкость: "))
        if self.gr < 100:
            print("Готово\n\n")

        else:
            print("\nМакс.звук 100\n\n")



    def talk(self):
        print("Вы сейчас находитесь на ",self.kanal," канале")
        print("Громкость : ",self.gr,"\n\n")



def main():
    choice = None
    print("Добро пожаловать в ZALA\n\n")
    while choice !='3':
        tv = TV()

        choice = input("1.Поменять канал\n2.Изменить громкость\n3.Выключить телевизор: ")
        if choice == '1':
            if tv.kan() == True:
                tv.talk()

        elif choice == '2':
            if tv.grom() == True:
                tv.talk()

        elif choice =='3':
            print("\nДосвидание")


        else:
            print("Введите коректный номер")


main()



