'''Домашнее задание от 19.02.2023'''

import random    ### Для последней задачи, №9

'''
Задача №1
Напишите программу, которая выводит все числа от 1 до 100 включительно, которые делятся на 3, но не делятся на 2.
'''

# for number in range(1, 101):
#     if number % 3 == 0 and number % 2 != 0:
#         print(number, end=' ')

'''
Задача №2
Напишите программу, которая запрашивает у пользователя число и выводит таблицу умножения этого числа до 10.
'''

# number = int(input('Введите число и я выведу вам таблицу умножения: '))

# for num in range(2, 9+1):
#     print(num * number)

'''
Задача №3
Напишите программу, которая запрашивает у пользователя строку и выводит все буквы этой строки, которые находятся на нечетных позициях.
'''
# word = ' '.join(input('Введите строку, а я выведу все символы на нечетных позициях: ')).split()
# for char in range(0, len(word), 2):
#     print(word[char])


'''
Задача №4
Напишите программу, которая выводит следующую последовательность чисел: 1, 2, 4, 7, 11, 16, 22, 29, 37, 46. Каждое число в последовательности получается путем прибавления к предыдущему числу значения, которое равно порядковому номеру этого числа в последовательности.
'''
# numbers = []
# a = 1
# print(a, end=' ')
# for num in range(1, 10):
#     a += num
#     numbers.append(a)
#     print(a, end=' ')
'''
Задача №5
Напишите программу, которая запрашивает у пользователя число и выводит на экран все числа от 1 до введенного числа включительно.
'''
#### Путаюсь при запуске while, а именно, как установить условие на while. Мне проще сделать переменную булево и управлять окончанием работы, но правильно ли это?
### Не всегда понимаю, когда использовать  break - очевидно, что когда дальнейший код не имеет смысла при каком либо условии, но всё равно путаница)
### например, если проверка возраста не пройдена, то дальнейший алгоритм не должен обрабатывать инфу о юзере. Тогда break уместно?
# active = True
# numbers_list = []
# while active: ## while num != number  ???? можно ли было так написать ? - ошибка, цикл не знает он таких переменных.
#     number = int(input('Please, enter a number > '))
#     for num in range(1, number+1):
#         numbers_list.append(num)
#         if num == number:
#             active = False
# for number_list in numbers_list:
#     print(number_list, end=' ')

'''
Задача №6
Напишите программу, которая запрашивает у пользователя число и выводит на экран сумму всех чисел от 1 до введенного числа включительно.
'''
### на уроке ты просил все данные хранить в списках, по идее, я могла бы тут сплитовать инпут, и уже бы работать со списком, но чё-то не догнала, как дальше работать
# active = True
# max_number_list = []
# summ = 0
# while active:
#     number = int(input('Please, enter a number > ')) ##нельзя применить int(input()), если сплитуем input()
#     for num in range(1, number+1):
#         summ += num
#         if num == number:
#             active = False
#     max_number_list.append(summ) ### - здесь сбивают с толку пробелы. Как правильнее? добавление в список и print() вынести из while или оставить в while?
#     print(max_number_list[0])    ### - Ибо, оба варианта работают.


'''
Задача №7
Напишите программу, которая запрашивает у пользователя число и выводит на экран все четные числа от 1 до введенного числа включительно.
'''
###  Опять же, в голове каша, когда я хочу ввод сохранить сразу в список и в цикле работать со списоком
### Вариант №1
# active = True
# even_numbers = []
# while active:
#     number = int(input('Please, enter a number> '))
#     for num in range(1, number+1):
#         if num % 2 == 0:
#             even_numbers.append(num)
#         else:
#             continue
#         if num == number:
#             active = False
#     for even_number in even_numbers:
#         print(even_number)

### Вариант №1
''''
В этом варианте хотела реализовать работу изначально со списком. Т.к, все инпуты со сплитами должны быть.
не получилось решить. Из-за работы continue? Мы берем число 1, получаем остаток от деления и он не равен 0, условие с континью, становится
истыным и снова идёт перебор чисел от 1 до введённого. И так бесконечно. 
реализовать эту задачу без continue - получается, а с  - нет.
'''
###
# active = True
# even_numbers = []
# number = input('Please, enter a number> ').split() ### сохраняем в список число !!!!! Когда используем continue - input должен быть ВНЕ while.
#                                                     ### иначе каждый раз при возврате на начало цикла, просит ввести число.
# number[0] = int(number[0]) ### - преобразовываем число под индексом 0 в инт. Вроде так работает, но так можно?
# while active:
#     for num in range(1, number[0]+1): ### Перебираем от 1 до введённого числа.
#         if num % 2 == 0:
#             even_numbers.append(num)
#         else:
#             continue
#         if num == number:
#             active = False
# for even_number in even_numbers:
#     print(even_number)


'''
Задача № 8
Напишите программу, которая запрашивает у пользователя слово и выводит на экран все буквы этого слова в обратном порядке.
'''
### Вариант № 1
# active = True
#
# while active:
#     s = ' '.join(input('Please, enter the word> ')).split()
#     for x in s[::-1]:
#         print(x, end=' ')
#     break

### Вариант № 2
## Почему None ?
# s = ' '.join(input('Please, enter the word> ')).split()
# print(s.reverse())

'''
Задача №9
Напишите программу, которая генерирует случайное число от 1 до 100 и предлагает пользователю угадать это число. Если пользователь вводит число, которое больше загаданного, программа выводит "Слишком много!", если меньше - "Слишком мало!", если угадал - "Поздравляю, вы угадали!".
'''
# active = True
# random_number = random.randint(1, 100)
# print(random_number)
# while active:
#     number = int(input('Please, enter a number> '))
#     if number == random_number:
#         print('Congratulations, you guessed the number!')
#         break
#     elif number < random_number:
#         print('Too little!')
#         answer = input("You didn't guess! Do you want to continue the game? Enter y or n> ")
#         if answer == 'y':
#             continue
#         else:
#             print('Goodbye')
#             active = False
#     elif number > random_number:
#         print('Too much!')
#         answer = input("You didn't guess! Do you want to continue the game? Enter y or n> ")
#         if answer == 'y':
#             continue
#         else:
#             print('Goodbye')
#             active = False


