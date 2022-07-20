#2 Задача из пдф
import os


namedir = 'C:\\Users\\4734368\\OneDrive\\Рабочий стол\\юургу\\основы программ\\6'
files = os.listdir(namedir)
k = 0
for i in files:
    if i[-3] == 'txt':
        k += 1
print(k)

try:
    f = open('input.txt')
    c = open('output.txt', 'w')

except:
    print('Файл с входными данными не обнаружен')
from functools import *
f=open(r"input.txt")
n=open(r"output.txt","w")
a=(f.readline())
if " " in a :
  a=int(a.split(" ")[0])
else:
    a = int(a)
k=1
n.write("Число: "+str(a)+'\n' +"количество цифр:  "+str(len(str(a)))+'\n'+"сумма цифр: "+ str((sum(map(int,list(str(a))))))+"\n"+"произведение цифр: "+str(reduce(lambda x,y :x*y,map(int,list(str(a))))))
f.close()
n.close()