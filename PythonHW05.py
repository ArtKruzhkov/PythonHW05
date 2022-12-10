# Создайте программу для игры с конфетами человек против компьютера.
# Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# from random import randint

# def input_candy(name):
#     x = int(input(f'{name}, сколько конфет берете от 1 до 28: '))
#     while x < 1 or x > 28:
#         x = int(input(f'{name}, введите корректное количество конфет: '))
#     return x

# def p_print(name, amount, counter, value):
#     print(f'Ходил {name}, он взял {amount}, теперь у него {counter}. Осталось на столе {value} конфет')

# player1 = input('Введите имя первого игрока: ')
# player2 = input('Введите имя второго игрока: ')
# value = int(input('Введите количество конфет на столе: '))

# flag = randint(0,2)                            # флаг очередности
# if flag:
#     print(f'Первый ходит {player1}')
# else:
#     print(f'Первый ходит {player2}')

# counter1 = 0                                  # счетчик конфет каждого игрока
# counter2 = 0

# while value > 28:
#     if flag:
#         k = input_candy(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = randint(1, 29)                    # сколько возьмет компьютер
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")



# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# def coding(txt):
#     count = 1
#     res = ''
#     for i in range(len(txt)-1):
#         if txt[i] == txt[i+1]:
#             count += 1
#         else:
#             res = res + str(count) + txt[i]
#             count = 1
#     if count > 1 or (txt[len(txt)-2] != txt[-1]):
#         res = res + str(count) + txt[-1]
#     return res

# def decoding(txt):
#     number = ''
#     res = ''
#     for i in range(len(txt)):
#         if not txt[i].isalpha():
#             number += txt[i]
#         else:
#             res = res + txt[i] * int(number)
#             number = ''
#     return res

# s = input('Input text for coding: ')
# data = open('file.txt', 'w')
# data.write(s)
# data.close()
# print(f'Coded text: {coding(s)}')
# data = open('file2.txt', 'w')
# data.write(coding(s))
# print(f'Text after decoding: {decoding(coding(s))}')
# data = open('file2.txt', 'a')
# data.write(f'\n{decoding(coding(s))}')


