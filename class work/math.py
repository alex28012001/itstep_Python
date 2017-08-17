"""
#ex1
import math
x=int(input("Введите число: "))

x=x%10
print("Последния цифра этого числа: ",x)
"""



"""
#ex2
v=int(input("Введите скорость: "))
t=int(input("Введите ВРЕМЯ : "))

l=v*t

if(v>0):
    print("Проехано: ",l)

else:
    print("Вася едет назад...")
    
"""

"""
#ex3
import math

x=float(input("Введите положителное число: "))

z=math.modf(x)


print(z)
"""

"""
#ex5

import math

n=int(input("Введите n километры: "))
m=int(input("Введите m километры: "))

x=m/n

print("За ",x," дней")
"""


"""
#ex6

import math

a=int(input("Введите рубли: "))
b=int(input("Введите копейки: "))
c=int(input("Введите сколько хотите купить пирожков: "))

p=b*10
z=a*c
q=b*p

print("Стоимость в копейках: ",z)
print("Стоимость в рублях: ",q)
"""

"""


#ex7
import math

h=int(input("Введите высоту в метрах: "))
a=int(input("Введите сколько за день улитка поднимаеться: "))
b=int(input("Введите за сколько он спускаеться за ночь: "))

if(a>b):
    z=h/(a-b)

print("За ",z,"дней")
"""

#ex8
import math

n=int(input("Введите трехзначное число: "))


d1 = n % 10
n = n // 10
d2 = n % 10
n = n // 10
d3 = n % 10

sum1=d1+d2+d3

print("Сумма трехзначного числа: ",sum1)
