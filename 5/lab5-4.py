#задача с треугольником
a = int(input('Введите сторону a '))
b = int(input('Введите сторону b '))
c = int(input('Введите сторону c '))
 
def F():
    global a
    global b
    global c
    if (a==0) and (b==0) and (c==0):
        print('Треугольник несуществует')
    elif a == b == c:
        print('Треугольник равносторонний')
    elif a == b or b == c:
        print('Треугольник несуществует')
    elif a < 0 or b < 0 or c < 0:
        print('Треугольник несуществует')        
    else:
        return()
print(F())