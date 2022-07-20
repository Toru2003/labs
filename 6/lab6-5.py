#3 Задача
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
f=open(r"input.txt")
n=open(r"output.txt","w")
nums=[]
a=int(f.readline())
for i in range (2,a):
    fl=0
    for r in range (2,i//2+1):
        if i%r==0:
            fl=1
            break
    if fl==0:
        nums.append(i)
nums=str(nums)
nums=nums.replace("[",'')
nums=nums.replace("]",'')
nums=nums.replace(",",' ')
n.write(nums)