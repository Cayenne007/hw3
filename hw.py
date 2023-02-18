
import os
import csv

os.system('clear')

#Задача 1

n = int(input('Введитче число n: '))
array = [i for i in range(1, n)]
x = int(input('Введите число х: '))
result = 0
for i in array:
    if i == x:
        result += 1
print(f'Число {x} встречается {result} раз')

#Задача 2
n = int(input('Введитче число n: '))
array = [i for i in range(1, n+1)]
x = int(input('Введите число х: '))
minimum = n
result = 0
for i in array:   
    print(f'i={i} x-i={x-i}') 
    if minimum > abs(x - i):
        minimum = abs(x -i)
        result = i
print(result)

#Задача 3
cost = {1: 'A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т',
2: 'D, G, Д, К, Л, М, П, У',
3: 'B, C, M, P, Б, Г, Ё, Ь, Я',
4: 'F, H, V, W, Y, Й, Ы',
5: 'K, Ж, З, Х, Ц, Ч',
8: 'J, X, Ш, Э , Ю',
10: 'Q, Z, Ф, Щ, Ъ'
}
text = str(input('Введите слово: ')).upper()
result = 0

for i in text:
    for (id, val) in cost.items():
        if i in val:
            result += id
        
print('Стоимость слова: ',result)

