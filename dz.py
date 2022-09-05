# Давыдова Лидия Викторовна
#  Python 225
# Задание №"1

# import random as r

# a = 1
# b = 2
# a = a + b
# b = a - b
# a = a - b
# print("a:", a)
# print("b:", b)
#
# a = 1
# b = 2
# a, b = b, a
# print("a:", a)
# print("b:", b)
#
# # Задание №"2
#
# a = 9
# b = 6
# c = 7
# d = 5
# r1 = a + b
# r2 = c + d
# print(r1 / r2)
#
# # a = int(input("Введите число:"))
# # print(type(a))
# # print(a + 6)
# # a = int(input("Введите число:"))
# # print(type(a))
# # print(a + 5)
# # a = int(input("Введите число:"))
# # print(type(a))
# # print(a / 12 )
#
#
# #  Задание №3
#
# a = int(input())
# b = (a // 10000) * ((a // 1000) % 10) * ((a // 100) % 10) * ((a // 10) % 10) * (a % 10)
# c = (a // 10000) * (a % 10) / 18
# print(str(b))
# print(str(c))
#
# # x = str(input())
# # A = 0
# # for i in x:
# #     A *= int(i)
# # print(a)
# # C = 0
# # for i in x:
# #     c += int(i)
# # print(c/len(x))
#
# # Задание 4
#
#
# n = int(input("Введите число от 1 до 99: "))
# if 1 <= n <= 99:
#
#     if 11 <= n <= 14:
#         print(n, "копеек")
#     else:
#         a = (n % 10)
#         if a == 1:
#             print(n, "копейка")
#         if 2 <= a <= 4:
#             print(n, "копейки")
#         if 5 <= a <= 9 or a == 0:
#             print(n, "копеек")
#
# else:
#     print("Ошибка")
#
# # другой вариант
# n = int(input("Введите число копеек:"))
# if 0 <= n <= 99:
#     if n <= 1 or n % 10 == 1 and n != 11:
#         print(n, "копейка")
#     elif 2 <= n <= 4 or 2 <= n % 10 <= 4 \
#             and n != 12 and n != 13 and n != 14:
#         print(n, "копейки")
#     # if 5 <= n <= 9:
#     #     print(n, "копеек")
#     else:
#         print(n, "копеек")
# else:
#     print("Ошибка")
#
# #  Задание 5
#
# user = input('1. "r"' '\n2. "+"'
#              '\n3. "-"' '\n4. "/"' '\n5. "*"'
#              '\n6. "%"' '\n7. "<"' '\n8. ">"'
#              "\nВведите знак: ")
# if user == 'r':
#     try:
#         operator = int(input("Введите цифру:"))
#         f_num = int(input("Введите первое число:"))
#         s_num = int(input("Введите второе число:"))
#         if operator == 2:
#             print(f_num + s_num)
#         if operator == 3:
#             print(f_num - s_num)
#         if operator == 4:
#             if s_num != 0:
#                 print(f_num / s_num)
#             else:
#                 print("На 0 делить нельзя")
#         if operator == 5:
#             print(f_num * s_num)
#         if operator == 6:
#             print(f_num % s_num)
#         if operator == 7:
#             print(f_num < s_num)
#         if operator == 8:
#             print(f_num < s_num)
#         f_num = -f_num
#         s_num = -s_num
#     except ValueError:
#         print("ввели не правильно")
# else:
#     print("Вы вели не верный знак")
#
# # operation = input('1)"r" - применяет унарный минус к операнду '
# #                   '\n2)"+" - сложение'
# #                   '\n3)"-" - вычитание'
# #                   '\n4)"/" - деление'
# #                   '\n5)"*" - умножение'
# #                   '\n6)"%" - деление по модулю (остаток то деление'
# #                   '\n7)"<" - минимальное из двух чисел'
# #                   '\n8)">" - максимальное из двух чисел'
# #                   '\nВведите знак:')
#
# #  Задание 6
#
# # from random import randint
# #
# # rnd = randint(1, 100)
# # print(rnd)
# # user_num = 0
# # while user_num < 10:
# #     user_num2 = int(input("Введите число от 1 до 100: "))
# #     user_num += 1
# #     if user_num2 == rnd:
# #         print("Вы угадали загаданное число c", user_num, end="-ой попытки")
# #         break
# #     if user_num2 <= rnd:
# #         print("Загаданное число больше!")
# #     if user_num2 >= rnd:
# #         print("Загаданное число меньше!")
# #     if user_num2 != rnd and user_num == 10:
# #         print("много было попыток, загаданное число:", rnd)
# #     if user_num2 == 0:
# #         print("прекратили пытаться, загаданное число:", rnd)
# #         break
#
# #  другой вариант
# # n = 12
# # i = 0
# # while True:
# #     a = int(input("Введите число:"))
# #     if a == 0:
# #         print("Вы прекратили пытаться")
# #         print("Количество попыток:", i)
# #         break
# #     if a < n:
# #         print("число меньше:")
# #     elif a == n:
# #         print("вы угадали!", "\nколичество попыток:", i)
# #         break
# #     else:
# #         print("число больше")
# #    i += 1
#
# # Задание 7
#
# # n = [int(input("-> ")) for i in range(int(input("n = ")))]
# # a = len(n)
# # for i in range(0, a, 2):
# #     print(n[i], end=" ")
#
# # Задание 8
#
# # n = [int(input("-> ")) for i in range(int(input("n = ")))]
# # a = len(n)
# # n.sort(reverse=True)
# # for i in range(a):
# #     print(n[i], end=" ")
#
# # n = [int(input("-> ")) for i in range(int(input("n = ")))]
# # for i in range(1, len(n)):
# #     if n[1] > n[i - 1]:
# #         print(n[i], end=" ")
#
#
# n = [int(input("-> ")) for i in range(int(input("n = ")))]
# a = len(n)
# for i in range(0, a, 2):
#     print(n[i], end=" ")
# # Задание 8
#
# w = [int(input("-> ")) for i in range(int(input("n = ")))]
# for i in range(1, len(w)):
#     if w[1] > w[i - 1]:
#         print(w[i], end=" ")
#
# # другой вариант
#
# w = [int(input("-> ")) for i in range(int(input("n = ")))]
# a = len(w)
# w.sort(reverse=True)
# for i in range(a):
#     print(w[i], end=" ")
#
# # Дополнительно
#
# w = int(input("Ширина треугольника: "))
# h = int(input("Высота треугольника: "))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i <= h + 1 or j == 0 or j == w + 1:
#             print("*", end="")
#     w += 2
#
# # 6 Урок
#
# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# for i in range(len(a)):
#     print(a)
#     break
# c = []
# for k in a:
#     b = 0
#     for j in a:
#         if k == j:
#             b += 1
#     if b == 1:
#         c.append(k)
# print(c)
#
# a = [1, 2, 3]
# b = [11, 22, 33, 4, 2]
# c = []
# i = 0
# while i < len(a):
#     c.append(a[i])
#     c.append(b[i])
#     i += 1
# print(c + b[3:5])
#
# # другой вариант
# a = [1, 2, 3]
# b = [11, 12, 13, 4, 2]
# c = []
# print("a =", a)
# print("b =", b)
#
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# print("c =", c)
#
# # 7 Урок
#
#
#
# n = [[r.randint(-20, 10) for a in range(3)]
#      for b in range(4)]
# m = 0
# for s in n:
#     for a in s:
#         if a < 0:
#             m += 1
#         print(a, end="\t\t")
#     print()
# print(f'Количество отрицательных элементов: {m}')
# # #2
#
# n = [[r.randint(0, 4) for i in range(3)]
#      for j in range(4)]
# m = 1
# for k in n:
#     for i in k:
#         if i > 0:
#             m *= i
#         print(i, end="\t\t")
#     print()
# print(f'Произведение ненулевых элементов: {m}')
# # 3
# main_list = [[r.randint(0, 10) for i in range(6)] for j in range(6)]
# sub_list = [r.randint(0, 10) for k in range(6)]
#
# # print(main_list)
# for row in range(len(main_list)):
#     for i in range(len(main_list[row])):
#         print(main_list[row][i], end='\t\t')
#     print()
# print(sub_list)
# for row in range(len(main_list)):
#     for i in range(len(main_list[row])):
#         if row % 2 == 0:
#             main_list[row] = sub_list
#         print(main_list[row][i], end='\t\t')
#     print()
# # 8 Урок
#
# # def change(lst):
# #     lst[0], lst[-1] = lst[-1], lst[0]
# #     return lst
# #
# #
# # print(change([1, 2, 3]))
# # print(change([9, 12, 33, 54, 105]))
# # print(change(["с", "л", "о", "н"]))
#
#
# def change(lst):
#     s = lst.pop()
#     k = lst.pop(0)
#     lst.append(k)
#     lst.insert(0, s)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))

# 9 урок
import math


# 10 Занятие
# Задание №"1

# s = ('ab', 'abcd', 'cde', 'abc', 'def')
# a = str(input('->'))
# print(s)
# print('s =', a)
# print('yes' if a in s else 'no')
#
#
# # №2
#
# # Введите по порядку, без пробелов, элементы кортежа: 253523651
# s = tuple(str(input("->")))
# print(s)
# print('Количество 2 =', s.count('2'))
# print('Количество 5 =', s.count('5'))
# print('Количество 3 =', s.count('3'))
# print('Количество 6 =', s.count('6'))
# print('Количество 1 =', s.count('1'))
#

# 12 занятие
# Даны два словаря: x = {'a': 1, 'b': 2} и y = {'b': 3, 'c': 4}.
# Объединить их в третий словарь.

#
# x = {
# 	'a': 1,
# 	'b': 2,
# }
# y = {
# 	'b': 3,
# 	'c': 4,
# }
# # c = {**x, **y}
# c = x | y
# print(c)


13


# №1
# a = {1: 10, 2: 20}
# b = {3: 30, 4: 40}
# c = {5: 50, 6: 60}
# d = {**a, **b, **c}
# print(d)


# № 2
# sales = {
# 	'emp1': {
# 		"name": 'Jhon',
# 		"salary": 7500,
# 	},
# 	'emp2': {
# 		"name": 'Emma',
# 		"salary": 8000,
# 	},
# 	'emp3': {
# 		"name": 'Brad',
# 		"salary": 6500,
# 	},
# }
# print(sales)
# person = input("Emp: ")
# print(sales[person][Name])
# sale = int(input("Зарплата : 0"))
# sales[person][Name] = sale
# print(sales[person])
# print(sale)
#
# for x in sales:
# 	print(x)
# 	for y in sales[x]:
# 		print('\t', y, " : ", sales[x][y], sep="")

#  Другой вариант

# sales = {
# 	'emp1': {
# 		"name": 'Jhon',
# 		"salary": 7500,
# 	},
# 	'emp2': {
# 		"name": 'Emma',
# 		"salary": 8000,
# 	},
# 	'emp3': {
# 		"name": 'Brad',
# 		"salary": 6500,
# 	},
# }
# print(sales)
#
#
# def create(sals):
# 	person = input ("Emp: ")
# 	Name = input ("Наименование: ")
# 	sales[person][Name] = input("Наименование: ")
# 	print(sales[person])
# 	return sales
#
#
# kol = int (input ("Количество изменений: "))
# a = 1
# while kol:
# 	create(sales)
# 	if a < kol:
# 		a += 1
# 	else:
# 		break
# for x in sales:
# 	print(x)
# 	for y in sales[x]:
# 		print('\t', y, " : ", sales[x][y], sep="")

# №3


# studs = {}
# k = int(input("Количество студентов: "))
# s = 0
# for i in range(k):
# 	name = input(str(i + 1) + "-й  студент: ")
# 	score = int(input("Балл: "))
# 	studs[name] = score
# 	s += score
# a = s / k
# print("\nСредний балл: %.0f. Студенты с баллом выше среднего: " % a)
# for i in studs:
# 	if studs[i] > a:
# 		print(i)

#2
# studs = {}
# k = int(input("Количество студентов: "))
#
#
# def student_people(i):
# 	people_name = str(input(str(i + 1) + "-й  студент: "))
# 	studs[people_name] = int(input("Балл: "))
# 	return studs
# s = 0
# for i in range(k):
# 	student_people(i)
# average_ball = sum(studs.values()) / k
# print("\nСредний балл: %.0f. Студенты с баллом выше среднего: " % average_ball)
# for i in studs:
# 	if studs[i] > average_ball:
# 		print(i)

# import builtins
#
# names = dir(builtins)
#
# for t in names:
# 	print(t)
#  №14
# from math import pi
#
#
# def square(figure_type, **kwargs):
# 	if figure_type == "rhombus":
# 		return kwargs["d1"] * kwargs["d2"] / 2
# 	if figure_type == "square":
# 		return kwargs["a"] ** 2
# 	if figure_type == "trapezoid":
# 		return (kwargs["a"] + kwargs["b"]) * (1 / 2) * kwargs["h"]
# 	if figure_type == "trapezoid":
# 		return 1 / 2 * (kwargs["a"] + kwargs["b"]) * kwargs["h"]
# 	if figure_type == "circle":
# 		return pi * kwargs["r"] ** 2
# 	return "invalid data"
#
#
# print(square(figure_type="rhombus", d1=10, d2=8))
# print(square(figure_type="square", a=5))
# print(square(figure_type="trapezoid", a=12, b=3, h=6))
# print(square(figure_type="circle", r=18))
# print(square(figure_type="unknown", a=1, b=2, c=3))

# № 15

#
# print((lambda x, y: x * y * 5)(2, 5))
#
# # или
#
# sum = lambda a=2, b=5, c=5: a * b * c
# print(sum())
#
# # №2
#
# students = [
# 	{'name': 'Jennifer', 'final': 95},
# 	{'name': 'David', 'final': 92},
# 	{'name': 'Nikolas', 'final': 98},
# ]
# res1 = sorted(students, key=lambda std: std['name'])
# print(res1)
# res2 = sorted(students, key=lambda std: std['final'], reverse=True)
# print(res2)
#
# # №3
#
# students = [
# 	{'name': 'Jennifer', 'final': 95},
# 	{'name': 'David', 'final': 92},
# 	{'name': 'Nikolas', 'final': 98},
# ]
# res1 = max(students, key=lambda std: std['name'])
# print(res1)
# res2 = min(students, key=lambda std: std['name'])
# print(res2)
#
# # №4
#
# nums = [3, 5, 7, 3, 9, 5, 7, 2]
# summa1 = list(map(lambda x: x**2, nums))
# summa2 = list(map(lambda x: x**3, nums))
# print(summa1)
# print(summa2)
