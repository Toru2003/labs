from math import sin 

""" 8 задание """

data = int(input('введите день рождения '))
data2 = int(input('введите месяц рождения '))

print(((data+data2)%4)+1)




""" 9 задание 1"""
x=int(input('введите число x  '))
y=(x+(x+x**1/2)**1/2)**1/2
print(y)


""" 9 задание 2"""
r=int(input('введите  радиус  '))
a=int(input('введите угол в градусах '))
s=(4*r*2)/sin(a)
print(s)







