'''
Задача №1
====> if else
Дано натуральное число N. Если число N двузначное,
то найти сумму цифр числа. Если число N трехзначное,
то найти произведение ненулевых цифр числа,
иначе написать, что число неподходящее.
In: 400
Out: 4
'''

# n = input('Введите натуральное число: ').split(' ')
# попытка №1
# if len(n) == 2:
#     n[0] = len(n) - 1
#     n[1] = len(n)
#     result = n[0]+n[1]
#     print(n[0], n[1])
#     print(result)
#print(n)

# попытка №2
# if len(n) == 2:
#     summ = n[0] + n[1]
# elif len(n) == 3:
#     if n[0] != 0:
#
# else:
#     print(f"Число {n} неподходящее")




"""
Дана строка из двух слов. Поменяйте эти слова местами.
Пример:
In: 'Hello Python'
Out: 'Python Hello'
"""
# №1
# s = input('Введите строку из двух слов: ')
# a = s.split()
# b = a[::-1]
# ' '.join(b)
# print(b)

# №2
# s = ' '.join(input('Введите строку из двух слов: ').split(' ')[::-1])
# print(s)

"""
Задача №3
========> while
Строка из нескольких слов, не более 10.
Определите, сколько букв содержит самое длинное слово в строке.
Пример:
In: Как дела в учебе
Out: 5
"""
# active = True
# while active:
#     msg = input('Введите слова из нескольких букв: ').split(' ')
#     print(msg)
#     for x in msg:
#         print (len(x))

    # for x in msg:
    #     a = len(x[0])
    #     if msg[x] > a:
    #         a = msg[x]
    #         print(a)
    # pass



"""
Задача №4
=====> while
Дано слово из символов(латинские буквы + цифры), других символов нет.
Нужно вывести новой строкой только цифры, если они есть или
написать, что их нет.
Пример: 
In: 'antuh1ouou21au3'
Out: 1213

In: 'sauhsauhasnhuasnhu'
Out: 'no digits'
"""
# active = True
# while active:
#     s = input('Введите строку: ')
#     for x in s:
#         if x.isdigit():
#             print(x)


