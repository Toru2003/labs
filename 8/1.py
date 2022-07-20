import sorts
import random
import time
from prettytable import PrettyTable

f = open("output.txt", 'w')
n = int(input("введите количество чисел в последовательности: "))
ui_time = time.time()
a = []
for i in range(n):
    a.append(random.randint(1, 100))
b = a[:]
sorts.quick_sort(b)
tb = ['Обменная сортировка']

c = a[:]
start_time = time.time()
sorts.bubble(b)
tb.append(str(time.time() - start_time))
start_time = time.time()
sorts.bubble(c)
tb.append(str(time.time() - start_time))
c = a[:]
start_time = time.time()
sorts.bubble_reverse(c)
tb.append(str(time.time() - start_time))

tb.append('Сортировка слиянием')
c = a[:]
start_time = time.time()
sorts.confluence_sort(b)
tb.append(str(time.time() - start_time))
start_time = time.time()
sorts.confluence_sort(c)
tb.append(str(time.time() - start_time))
c.reverse()
tb.append(str(time.time() - start_time))

tb.append('Быстрая сортировка ')
c = a[:]
start_time = time.time()
sorts.quick_sort(b)
tb.append(str(time.time() - start_time))
start_time = time.time()
sorts.quick_sort(c)
tb.append(str(time.time() - start_time))
c.reverse()
tb.append(str(time.time() - start_time))

tb.append('Встроенная сортировка')
c = a[:]
start_time = time.time()
sorted(b)
tb.append(str(time.time() - start_time))
start_time = time.time()
sorted(c)
tb.append(str(time.time() - start_time))
c = a[:]
start_time = time.time()
sorted(c, reverse=1)
tb.append(str(time.time() - start_time))

th = ['Метод', 'отсортированная', 'случайная', 'отсортированная в обратном порядке']
table = PrettyTable(th)
while tb:
    table.add_row(tb[:4])
    tb = tb[4:]
f.write(str(table))
print('время работы всей программы:', time.time() - ui_time)
