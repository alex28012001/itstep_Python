class Car(object):
    pedal_dvish = False
    pedal_tormoz = False
    dvig_off = True
    fari_on = False
    fari_off = True
    dveri_on = False
    dveru_off = True
    dvigatel = False



    def __init__(self, name):
        self.name = name
        print("Добро пожаловать в ", self.name)




    def zajiganie(self):
        if self.dveri_on == True:
            print("\nВы завели свою машину(", self.name, ")")
            self.dvigatel = True

        else:
            print("Вы еще не зашли в машину ,чтобы завести ее")
            self.dvigatel = False







    def ezda(self):
        if self.dveri_on == True and self.dvigatel == True:
            self.pedal_dvish = True
            print("\nВы едете")

        else:
            if self.dveri_on == False:
                print("Вы не можете ехать из - за того что вы не вошли в машину")
                self.pedal_dvish = False

            elif self.dvigatel == False:
                print("Вы не можете ехать из - за того что вы не завели машину")
                self.pedal_dvish = False

            elif self.dveri_on == False and self.dvigatel == False:
                print("Вы не можете ехать из - за того что вы не вошли в машину и не завели ее")
                self.pedal_dvish = False





    def tormoz(self):
        if self.dveri_on == True and self.dvigatel == True and self.pedal_dvish == True:
            self.pedal_tormoz = True
            print("\nВы затормозили")

        else:


            if self.dvigatel == False and self.pedal_dvish == False:
                print("Вы не можете затормозить из - за того что вы не завели машину и вы не едете")
                self.pedal_tormoz = False


            elif self.dveri_on == False and self.dvigatel == False and self.pedal_dvish == False:
                print("Вы не можете затормозить из - за того что вы не вошли в машину ,не завели ее и вы не едете")
                self.pedal_tormoz = False








    def ostanovka_dvigately(self):
        if self.dvigatel == True and self.dveri_on == True:
            self.dvig_off = False
            print("\nДвигатель остановлен")

        else:
            if self.dvigatel == False:
                print("Вы не можете остановить двигатель из - за того что двигатель не включен")
                self.dvig_off = True

            elif self.dvigatel == False and self.dveri_on == False:
                print("Вы не можете остановить двигатель из - за того что вы не вошли в машину и двигатель не включен")
                self.dvig_off = False





    def fari(self):
        if self.dveri_on == True and self.dvigatel == True:
            self.fari_on = True
            print("\nФары включены")

        else:
            if self.dvigatel == False:
                print("Вы не можете включить фары из - за того что двигатель не включен")
                self.fari_on = False

            elif self.dvigatel == False and self.dveri_on == False:
                print("Вы не можете включить фары из - за того что вы не вошли в машину и не включили двигатель")
                self.fari_on = False


            elif self.fari_on == True:
                print("Фары уже включены")
                self.fari_on = False








    def fari2(self):
        if self.dveri_on == True and self.dvigatel == True:
            self.fari_off = False
            print("\nФары отключены")

        else:
            if self.dvigatel == False:
                print("Вы не можете отключить  фары из - за того что двигатель не включен")
                self.fari_off = True

            elif self.dvigatel == False and self.fari_on == False:
                print("Вы не можете отключить  фары из - за того что двигатель не включен и а фары не горят")
                self.fari_off = True



            elif self.dvigatel == False and self.dveri_on == False and self.fari_on == False:
                print("Вы не можете отключить фары из - за того что вы не вошли в машину , не включили двигатель и фары не горят")
                self.fari_off = True


            elif self.fari_off == False:
                print("Фары уже отключены")





    def dveri(self):
        if self.dveri_on == False:
            self.dveri_on = True
            print("\nДвери открыты")

        else:
            if self.dveri_on == True:
                print("Двери уже открыты")
                self.dveri_on = False







    def dveri2(self):
        if self.dveri_on == True:
            self.dveri_off = False
            print("\nДвери закрыты")

        else:
            if self.dveri_off == False :
                print("Двери уже закрыты")
                self.dveri_off = True







def main():
    car_name = input("Введите марку вашего автомобиля: ")
    car = Car(car_name)

    choice = None
    while choice != 9:
        print("\nФункционал машины:"
              + "\n\t1.Зажигание"
              + "\n\t2.Езда"
              + "\n\t3.Тормоз"
              + "\n\t4.Остановка двигателя"
              + "\n\t5.Включение фар"
              + "\n\t6.Выключение фар"
              + "\n\t7.Открытие дверей"
              + "\n\t8.Закрытие дверей"
              + "\n\t9.Выход\n\n")

        choice = input("Ваш выбор:")

        if choice == '9':
            print("Досвидание")

        elif choice == '1':
            car.zajiganie()

        elif choice == '2':
            car.ezda()

        elif choice == '3':
            car.tormoz()

        elif choice == '4':
            car.ostanovka_dvigately()

        elif choice == '5':
            car.fari()

        elif choice == '6':
            car.fari2()

        elif choice == '7':
            car.dveri()

        elif choice == '8':
            car.dveri2()



main()
