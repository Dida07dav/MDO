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
# #
# n = [int(input("-> ")) for i in range(int(input("n = ")))]
# a = len(n)
# for i in range(0, a, 2):
#     print(n[i], end=" ")
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
# # Задание 9
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
# #
# w = int(input("Ширина треугольника: "))
# h = int(input("Высота треугольника: "))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i <= h + 1 or j == 0 or j == w + 1:
#             print("*", end="")
#     w += 2

# # Задание 10
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
# # Задание 11
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
# # Задание 12
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

# Задание 13


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

# Задание 14
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


# Задание 15


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

# Задание 16


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
#  № Задание 17
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

# № Задание 18

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
#
# pos1 = int(input('pos1 = '))
# pos2 = int(input('pos2 = '))
# f = open('text4.txt', 'r')
# L = f.readlines()
#
# s = L[pos1]
# L[pos1] = L[pos2]
# L[pos2] = s
#
# f = open('text4.txt', 'w')
# f.writelines(L)
# f.close()


# 1
# my_file = open("text4.txt", "w")
# my_file.write("Замена строки в текстовом документе;\nизменить строку в списке;\nзаписать список в файл;")
# my_file.close()
# my_file1 = int(input('pos1 = '))
# my_file2 = int(input('pos2 = '))
# f = open('text4.txt', 'r')
# L = f.readlines()
# s = L[len(L) - 1]
# k = len(s)
# if (k > 0) and (s[k - 1] != '\n'):
# 	L[len(L) - 1] += '\n'
# f.close()
# s = L[my_file1]
# L[my_file1] = L[my_file2]
# L[my_file2] = s
#
# f = open('text4.txt', 'w')
# f.writelines(L)
# f.close()

#2
# my_file = open("text5.txt", "w")
# my_file.write("Замена строки в текстовом документе;\nизменить строку в списке;\nзаписать список в файл;")
# my_file.close()
# f = open("text5.txt", 'r')
# read_file = f.readlines()
# print(read_file)
# s = read_file[len(read_file)- 1]
# k = len(s)
# if (k > 0) and (s[k - 1] != '\n'):
# 	read_file[len(read_file) - 1] += '\n'
# f.close()
# read_file2 =[]
# i = 0
# while i < len(read_file):
# 	s = read_file[len(read_file) - i -1]
# 	read_file2 = read_file2 + [s]
# 	i = i + 1
# f = open('text5.txt', 'w')
# f.writelines(read_file2)
# f.close()

#3
# my_file = open("python.txt", "w")
# my_file.write("Python поддерживает динамическую типизацию, то есть тип переменной определяется только во время исполнения. \nПоэтому вместо «присваивания значения переменной» лучше говорить о «связывании значения с некоторым именем.»")
# my_file.close()
#
# my_file1 = open("python1.txt", "w")
# my_file1.write("\nК примитивным типам в Python относятся булевый, целое число произвольной точности, число с плавающей запятой и комплексное число")
# my_file1.close()
# s = open('python.txt', 'rb')
# s1 = open('python1.txt', 'rb')
# F = s.readlines()
# F1 = s1.readlines()
# F2 = F + F1
# s.close()
# s1.close()
#
# s2 = open('python3.txt', 'wb')
# s2.writelines(F2)
# s2.close()

# Задание14
#
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
#
# # Задание 15
#
# print((lambda x, y: x * y * 5)(2, 5))
#
# # или
#
# summa = lambda a=2, b=5, c=5: a * b * c
# print(summa())
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
#

# Задание 17
# #### I am learning Python. hello, WORLD!
# # 1
# s = input("-> ")
# a = s.find("h")
# b = s.rfind("h")
# print(s[:a] + s[b + 1:])
#
#
# # 2
#
# #### I am learning Python. hello, WORLD!
# s = input("-> ")
# a = s[:s.find("h")]
# b = s[s.find("h"):s.rfind("h") + 1]
# c = s[s.rfind("h") + 1:]
# s = a + b[::-1] + c
# print(s)

# 3

# s = input("Строка: ")
# s_replace = input("Ее заменяемая строка: ")
# s_new = input("Новая подстрока: ")
#
# a = s.find(s_replace)
# while a != -1:
# 	b = len(s_replace)
# 	s = s[:a] + s_new + s[a+b:]
# 	a = s.find(s_replace)
# print(s)

# 4
#
# text = " Ежевику для ежат \n Принесли два ежа,\n Ежевику еле-еле \n Ежата возле ели съели."
# str = (' ' + text).lower().count(' е')
# print(text, "(", str, "слов", ")")
# print()
# print("Количество слов: ", str)

# Задание 18

# №1
import re
# email = "123456@i.ru," \
# 	" 123_456@ru.name.ru," \
# 	" login@i.ru, " \
# 	"логин-1@i.ru, " \
# 	"login.3@i.ru, " \
# 	"login.3-67@i.ru, " \
# 	"1login@ru.name.ru"
# print(re.findall("""
# [A-Za-zа-я0-9-._]+
# @
# [A-Za-zа-я0-9-._]+
# """, email, re.VERBOSE))

#

# 19 Занятие
# №1

#
# def validate_password(password):
# 	return re.findall(r'((?=.*\d)(?=.*[a-z])(?=.*@)(?=.*[A-Z]).{6,18})', password, re.IGNORECASE)
#
#
# print(validate_password('my-p@ssw0rd'))
#
# # №2
#
# test = "В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021," \
# 	" были зафиксированы максимумы ежемесячных осадков"
# # reg = '02/06/2021|05/06/2021|14/06/2021'
# # reg = r'([\d*/]+)'
# reg = r'(\d{1,2}\/\d{1,2}\/\d{4})'
# print(re.findall(reg, test, re.I))

# 20 Занятие

#
# def count_items(item_list):
# 	count = 0
# 	for item in item_list:
# 		if isinstance(item, list):
# 			count += count_items(item)
# 		else:
# 			count = count_items(item_list[1:])
# 			if item_list[0] < 0:
# 				count = count + 1
# 	return count
#
#
# lst = [-2, 3, 8, -11, -4, 6]
# n = count_items(lst)
# print("n =", n)
#
#
# # 2 Вариант
#
# def Negativ(res):
# 	if res == []:
# 		return 0
# 	else:
# 		count = Negativ(res[1:])
# 		if res[0] < 0:
# 			count = count + 1
# 		return count


# lst = [-2, 3, 8, -11, -4, 6]
# n = Negativ(lst)
# print("n =", n)


# 21 Задание
# 1
# my_file = open("text4.txt", "w")
# my_file.write("Замена строки в текстовом документе;\nизменить строку в списке;\nзаписать список в файл;")
# my_file.close()
# my_file1 = int(input('pos1 = '))
# my_file2 = int(input('pos2 = '))
# f = open('text4.txt', 'r')
# L = f.readlines()
# f.close()
# s = L[my_file1]
# L[my_file1] = L[my_file2] +'\n'
# L[my_file2] = s + '\n'
#
# f = open('text4.txt', 'w')
# f.writelines(L)
# f.close()

# 2
# my_file = open("text5.txt", "w")
# my_file.write("Замена строки в текстовом документе;\nизменить строку в списке;\nзаписать список в файл;")
# my_file.close()
# f = open("text5.txt", 'r')
# read_file = f.readlines()
# read_file[len(read_file) - 1] += '\n'
# f.close()
# read_file2 =[]
# i = 0
# while i < len(read_file):
# 	s = read_file[len(read_file) - (i + 1)]
# 	read_file2 += [s]
# 	i = i + 1
# f = open('text5.txt', 'w')
# f.writelines(read_file2)
# f.close()

# 3
# my_file = open("python.txt", "w")
# my_file.write("Python поддерживает динамическую типизацию, то есть тип переменной определяется только во время исполнения. \nПоэтому вместо «присваивания значения переменной» лучше говорить о «связывании значения с некоторым именем.»\n")
# my_file.close()
#
# my_file1 = open("python1.txt", "w")
# my_file1.write("К примитивным типам в Python относятся булевый, целое число произвольной точности, число с плавающей запятой и комплексное число\n")
# my_file1.close()
# s = open('python.txt', 'rb')
# s1 = open('python1.txt', 'rb')
# F = s.readlines() + s1.readlines()
# s.close()
# s1.close()
#
# s2 = open('python3.txt', 'wb')
# s2.writelines(F)
# s2.close()

# 22 Задание

# class Book:
# 	the_book = "name"
# 	release = "0000"
# 	publisher = "publisher"
# 	genre = "genre"
# 	author = "author"
# 	price = "price"
#
# 	def print_info(self):
# 		print(" Маркетинг ".center(40, "*"))
# 		print(f"Название книги: {self.the_book}\n"
# 			  f"год выпуска: {self.release}\n"
# 			  f"Издатель: {self.publisher}\n"
# 			  f"Жанр: {self.genre}\n"
# 			  f"Автор: {self.author}\n"
# 			  f"цена: {self.price}")
# 		print("=" * 40)
#
# 	def input_info(self, the_book, release, publisher, genre, author, price):
# 		self.the_book = the_book
# 		self.release = release
# 		self.publisher = publisher
# 		self.genre = genre
# 		self.author = author
# 		self.price = price
#
# 	def set_the_book(self, the_book):
# 		self.the_book = the_book
#
# 	def get_the_book(self):
# 		return self.the_book
#
# 	def set_release(self, release):
# 		self.release = release
#
# 	def get_release(self):
# 		return self.release
#
# 	def set_publisher(self, publisher):
# 		self.publisher = publisher
#
# 	def get_publisher(self):
# 		return self.publisher
#
# 	def set_genre(self, genre):
# 		self.genre = genre
#
# 	def get_genre(self):
# 		return self.genre
#
# 	def set_author(self, author):
# 		self.author = author
#
# 	def get_author(self):
# 		return self.author
#
# 	def set_price(self, price):
# 		self.price = price
#
# 	def get_price(self):
# 		return self.price
#
#
# h1 = Book()
# h1.input_info("Маркетинг. Курс лекций", "2018", "Инфра-М", "Маркетинг, PR, реклама", "Басовский Леонид Ефимович", "719р.")
# h1.print_info()
# h1.set_the_book("Ромео и Джульетта")
# print(h1.get_the_book())
# h1.set_release('2004')
# print(h1.get_release())
# h1.set_publisher("Библиотека драматургии Агентства ФТМ")
# print(h1.get_publisher())
# h1.set_genre('Зарубежная драматургия, Зарубежная классика')
# print(h1.get_genre())
# h1.set_author("Уильям Шекспир")
# print(h1.get_author())
# h1.set_price('815р.')
# print(h1.get_price())
# print("=" * 40)


# # 23 Задание
from math import sqrt

#
# class Rectangle:
#     def __init__(self, lg, wd):
#         self.__length = lg
#         self.__width = wd
#
#     def get_length(self):
#         return self.__length
#
#     def get_width(self):
#         return self.__width
#
#     def get_square(self):
#         s = self.__length * self.__width
#         print("Площадь прямоугольника: ", s)
#
#     def perimetr(self):
#         s1 = (self.__length + self.__width) * 2
#         print("Периметр прямоугольника: ", s1)
#
#     def hypotenuse(self):
#         s2 = sqrt(self.__length ** 2 + self.__width ** 2)
#         print("Гипотенуза прямоугольника: ", round(s2, 2))
#
#     def figur(self):
#         print(("*" * self.__width + "\n") * self.__length)
#
#
# p = Rectangle(3, 9)
# print("Длина прямоугольника: ", p.get_length())
# print("Ширина прямоугольника: ", p.get_width())
# p.get_square()
# p.perimetr()
# p.hypotenuse()
# p.figur()


# 24 Задание

# class Weight:
#     def __init__(self, k=0):
#         self.__kg = k
#
#     @property
#     def klm(self):
#         return self.__kg
#
#     @klm.setter
#     def klm(self, k):
#         if isinstance(k, (int, float)):
#             self.__kg = k
#         else:
#             print("Килограммы задаются только числами")
#
#     def to_lb(self):
#         return round(self.__kg * 2.205, 3)
#
#
# f = Weight(12)
# print(f.klm, "кг => ", end="")
# print(f.to_lb(), 'фунтов')
#
# f.klm = 41
# print(f.klm, "кг => ", end="")
# print(f.to_lb(), 'фунтов')


# 25 Задание
# 1
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, num, surname, percent, value=0):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#         print(f'Счет #{self.__num} принадлежит {self.__surname} был открыт.')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.__num} принадлежащий {self.__surname} был закрыт.')
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def set_name(self, name):
#         self.__num = name
#
#     def get_name(self):
#         return self.__num
#
#     def set_surname(self, surname):
#         self.__surname = surname
#
#     def get_surname(self):
#         return self.__surname
#
#     def set_percent(self, percent):
#         self.__percent = percent
#
#     def get_percent(self):
#         return self.__percent
#
#     def set_value(self, value):
#         self.__value = value
#
#     def get_value(self):
#         return self.__value
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.__value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}.')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.__value, Account.rate_eur)
#         print (f'Состояние счета: {eur_val} {Account.suffix_eur}.')
#
#     def print_balance(self):
#         print(f'Текущий баланс {self.__value} {Account.suffix}')
#
#     def print_info(self):
#         print(f'Информация о счете:')
#         print('-' * 20)
#         print(f'#{self.__num}')
#         print(f'Владелец: {self.__surname}')
#         self.print_balance()
#         print(f'Проценты: {self.__percent:.0%}')
#         print('-' * 20)
#
#     def add_percents(self):
#         self.__value += self.__value * self.__percent
#         print('Проценты были успешно начислены')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.__value:
#             print(f'К сожалению у вас нет {val} {Account.suffix}')
#         else:
#             self.__value -= val
#             print(f'{val} {Account.suffix} было успешно снято!')
#         self.print_balance()
#
#     def add_money(self, val):
#         self.__value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance()
#
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# Account.set_usd_rate(2)
# acc.convert_to_usd()
#
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
#
# acc.set_name("56789")
# acc.set_surname("Alla")
# acc.set_percent(0.5)
# acc.set_value(3000)
# acc.print_info()
#
# acc.add_percents()
# print()
#
# acc.withdraw_money(3000)
# print()
#
# acc.withdraw_money(100)
# print()
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)
# print()

# 2
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, num, surname, percent, value=0):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#         print(f'Счет #{self.__num} принадлежит {self.__surname} был открыт.')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.__num} принадлежащий {self.__surname} был закрыт.')
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @property
#     def num(self):
#         return self.__num
#
#     @num.setter
#     def num(self, num):
#         self.__num = num
#
#     @property
#     def surname(self):
#         return self.__surname
#
#     @surname.setter
#     def surname(self, surname):
#         self.__surname = surname
#
#     @property
#     def percent(self):
#         return self.__percent
#
#     @percent.setter
#     def percent(self, percent):
#         self.__percent = percent
#
#     @property
#     def value(self):
#         return self.__value
#
#     @value.setter
#     def value(self, value):
#         self.__value = value
#
#     def convert_to_usd(self):
#         usd_val = Account.convert (self.__value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}.')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert (self.__value, Account.rate_eur)
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}.')
#
#     def print_balance(self):
#         print(f'Текущий баланс {self.__value} {Account.suffix}')
#
#     def print_info(self):
#         print(f'Информация о счете:')
#         print('-' * 20)
#         print(f'#{self.__num}')
#         print(f'Владелец: {self.__surname}')
#         self.print_balance ()
#         print(f'Проценты: {self.__percent:.0%}')
#         print('-' * 20)
#
#     def add_percents(self):
#         self.__value += self.__value * self.__percent
#         print('Проценты были успешно начислены')
#         self.print_balance ()
#
#     def withdraw_money(self, val):
#         if val > self.__value:
#             print(f'К сожалению у вас нет {val} {Account.suffix}')
#         else:
#             self.__value -= val
#             print(f'{val} {Account.suffix} было успешно снято!')
#         self.print_balance ()
#
#     def add_money(self, val):
#         self.__value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance()
#
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# Account.set_usd_rate(2)
# acc.convert_to_usd()
#
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
#
# acc.num = "13579"
# acc.surname = "Vladimir"
# acc.percent = 0.04
# acc.value = 2000
# acc.print_info()
#
# acc.add_percents()
# print()
#
# acc.withdraw_money(3000)
# print()
#
# acc.withdraw_money(100)
# print()
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)
# print()

# 26 Задание

# class Point:
# 	def __init__(self, x=0, y=0):
# 		self.__x = x
# 		self.__y = y
#
# 	def __str__(self):
# 		return f'({self.__x}, {self.__y})'
#
# 	def is_digit(self):
# 		if not isinstance(self.__x, (int, float)) or not isinstance(self.__y, (int, float)):
# 			print("Координаты должны быть числами")
# 			return False
# 		return True
#
# 	def is_int(self):
# 		if not isinstance(self.__x, int) or not isinstance(self.__y, int):
# 			print("Координаты должны быть целочисленными")
# 			return False
# 		return True
#
#
# class Prop:
# 	def __init__(self, sp: Point, ep: Point, color='red', width: int = 1):
# 		self._sp = sp
# 		self._ep = ep
# 		self._color = color
# 		self._width = width
#
# 	def set_coords(self, sp, ep):
# 		if sp.is_digit() and ep.is_digit():
# 			self._sp = sp
# 			self._ep = ep
#
#
# class Line (Prop):
#
# 	def draw_line(self) -> None:
# 		print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
# 	def set_coords(self, sp, ep):
# 		if sp.is_int() and ep.is_int():
# 			self._sp = sp
# 			self._ep = ep
#
#
# class Rect (Prop):
#
# 	def draw_rect(self) -> None:
# 		print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# line = Line(Point (1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(10.9, 20), Point(100.8, 200))
# line.draw_line()
#
# rect = Rect(Point(7, 9), Point(12, 15))
# rect.draw_rect()
# rect.set_coords(Point(30.8, 40), Point(50, 60))
# rect.draw_rect()

# 27 Задание

# class Liquid:
#     def __init__(self, name, density):
#         self.name = name
#         self.density = density
#
#     def edit_density(self, val):
#         self.density = val
#
#     def calc_m(self, v):
#         m = v * self.density
#         print(f'Вес {v} m^3 of {self.name} составляет {m} кг.')
#
#     def calc_v(self, m):
#         v = m / self.density
#         print(f'Объем {m} кг {self.name} равен {v} m^3.')
#
#     def print_info(self):
#         print(f"Жидкость '{self.name}' (плотность = {self.density} kg/m^3).")
#
#
# class Alcohol(Liquid):
#     def __init__(self, name, density, strength):
#         super().__init__(name, density)
#         self.strength = strength
#
#     def edit_strength(self, val):
#         self.strength = val
#
#
# a = Alcohol('Wine', 1064.2, 14)
# a.print_info()
#
# a.edit_density(1000)
# a.print_info()
# print()
# a.calc_m(0.5)
# a.calc_v(300)
# print()
#
# print(a.strength)
# a.edit_strength(20)
# print(a.strength)

# 28 Задание


# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.md = self.Notebook()
#         self.nt = self.Notebook1()
#
#     def display(self):
#         print(f'{self.name} =>', end="")
#
#     class Notebook:
#         def __init__(self):
#             self.model = "HP"
#             self.processor = "i7"
#             self.memory = 16
#
#         def display(self):
#             print(f" {self.model}, {self.processor}, {self.memory}")
#
#     class Notebook1:
#         def __init__(self):
#             self.model = "HP"
#             self.processor = "i7"
#             self.memory = 16
#
#         def display(self):
#             print(f" {self.model}, {self.processor}, {self.memory}")
#
#
# outer = Student("Roman")
# outer.display()
# d1 = outer.md
# d1.display()
#
# outer = Student("Vladimir")
# outer.display()
# d2 = outer.nt
# d2.display()

# 29 Задание
# № 1
# class Clock:
# 	__DAY = 86400
#
# 	def __init__(self, sec: int):
# 		if not isinstance(sec, int):
# 			raise ValueError("Секунды должны быть целым числом")
#
# 		self.sec = sec % self.__DAY
#
# 	def __add__(self, other):
# 		if not isinstance(other, Clock):
# 			raise ArithmeticError("Правый операнд должен быть типом данных Clock")
# 		return Clock(self.sec + other.sec)
#
# 	def __sub__(self, other):
# 		if not isinstance(other, Clock):
# 			raise ArithmeticError("Правый операнд должен быть типом данных Clock")
# 		return Clock(self.sec - other.sec)
#
# 	def __mul__(self, other):
# 		if not isinstance(other, Clock):
# 			raise ArithmeticError()
# 		return Clock(self.sec * other.sec)
#
# 	def __floordiv__(self, other):
# 		if not isinstance(other, Clock):
# 			raise ArithmeticError()
# 		return Clock(self.sec // other.sec)
#
# 	def __mod__(self, other):
# 		if not isinstance(other, Clock):
# 			raise ArithmeticError()
# 		return Clock(self.sec % other.sec)
#
# 	def __eq__(self, other):
# 		return self.sec == other.sec
#
# 	def __ne__(self, other):
# 		return not self.__eq__(other)
#
# 	def __gt__(self, other):
# 		return self.sec > other.sec
#
# 	def get_format_time(self):
# 		s = self.sec % 60  # секунды
# 		m = (self.sec // 60) % 60  # минуты
# 		h = (self.sec // 3600) % 24  # часы
# 		return f'{Clock.__get_form (h)}:{Clock.__get_form (m)}:{Clock.__get_form (s)}'
#
# 	@staticmethod
# 	def __get_form(x):
# 		return str(x) if x > 9 else "0" + str(x)
#
# 	def __getitem__(self, item):
# 		if not isinstance(item, str):
# 			raise ValueError("Ключ должен быть строкой")
#
# 		if item == "hour":
# 			return (self.sec // 3600) % 24
# 		elif item == "min":
# 			return (self.sec // 60) % 60
# 		elif item == "sec":
# 			return self.sec % 60
#
# 		return "Неверный ключ"
#
# 	def __setitem__(self, key, value):
# 		if not isinstance(key, str):
# 			raise ValueError("Ключ должен быть строкой")
# 		if not isinstance(value, int):
# 			raise ValueError('Значение должно быть целым числом')
# 		h = (self.sec // 3600) % 24
# 		m = (self.sec // 60) % 60
# 		s = self.sec % 60
# 		if key == "hour":
# 			self.sec = s + 60 * m + value * 3600
# 		elif key == 'min':
# 			self.sec = s + 60 * value + h * 3600
# 		elif key == 'sec':
# 			self.sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(700)
# print(c1.get_format_time())
# c1["hour"] = 12
# print(c1.get_format_time())
# print(c1['hour'], c1['min'], c1['sec'])

# № 2

# class Point3D:
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return f"{self.x}, {self.y}, {self.z}"
#
#     @staticmethod
#     def __check_value(v):
#         return isinstance(v, int) or isinstance(v, float)
#
#     def __add__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError("Правый операнд должен быть типом Point3D")
#         else:
#             return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)
#
#     def __sub__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError("Правый операнд должен быть типом Point3D")
#         else:
#             return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)
#
#     def __mul__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError("Правый операнд должен быть типом Point3D")
#         else:
#             return Point3D(self.x * other.x, self.y * other.y, self.z * other.z)
#
#     def __truediv__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError("Правый операнд должен быть типом Point3D")
#         return self.x / other.x, self.y / other.y, self.z / other.z
#
#     def __eq__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError("Правый операнд должен быть типом Point3D")
#         return self.x == other.x and self.y == other.y and self.z == other.z
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#         elif item == 'x':
#             return self.x
#         elif item == 'y':
#             return self.y
#         elif item == 'z':
#             return self.z
#         else:
#             print("Неверно задан ключ!")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой!")
#         if self.__check_value(value):
#             if key == 'x':
#                 self.x = value
#             elif key == 'y':
#                 self.y = value
#             elif key == 'z':
#                 self.z = value
#         else:
#             print("Координаты должны быть числами!")
#
#
# pt1 = Point3D(12, 15, 18)
# pt2 = Point3D(6, 3, 9)
# print("Координаты 1-й точки: ", pt1)
# print("Координаты 2-й точки: ", pt2)
#
# pt3 = pt1 + pt2
# print(f"Сложение координат: ({pt3})")
#
# pt4 = pt1 - pt2
# print(f"Разность координат: ({pt4})")
#
# pt5 = pt1 * pt2
# print(f"Произведение координат: ({pt5})")
#
# pt6 = pt1 / pt2
# print(f"Частное координат: ({pt6})")
#
# print(f"Равенство координат: {pt1 == pt2}")
#
# print("x =", pt1['x'], "x1 =", pt2['x'])
# print("y =", pt1['y'], "y1 =", pt2['y'])
# print("z =", pt1['z'], "z1 =", pt2['z'])
#
# pt1['x'] = 24
# print("Запись значения в координату x:", pt1['x'])

# 30 Задание
#
import math
from abc import ABC, abstractmethod


class Shape:
	def __init__(self, name, color):
		self.name = name
		self.color = color
	
	def info(self):
		print (f'{self.name}')


class Square (Shape):
	def __init__(self, name, color, side):
		super ().__init__ (name, color)
		self.side = side
	
	def info(self):
		super ().info ()
		print (f'Сторона: {self.side}\nЦвет:{self.color}'
			   f'\nПлощадь: {self.side * self.side}'
			   f'\nПериметр:{self.side * 2 + self.side * 2}')
	
	def figur(self):
		print (("*" * self.side + "\n") * self.side)


class Rectangle (Shape):
	def __init__(self, name, color, w, lg):
		super ().__init__ (name, color)
		self.width = w
		self.length = lg
	
	def info(self):
		super ().info ()
		print (f'Длина:{self.length}'
			   f'\nШирина: {self.width}\nЦвет:{self.color}'
			   f'\nПлощадь:{self.width * self.length}'
			   f'\nПериметр:{self.width * 2 + self.length * 2}')
	
	def figur(self):
		print (("*" * self.width + "\n") * self.length)


class Triangle (Shape):
	def __init__(self, name, color, side1, side2, side3):
		super ().__init__ (name, color)
		self.side1 = side1
		self.side2 = side2
		self.side3 = side3
	
	def info(self):
		super ().info ()
		print (f'Сторона 1: {self.side1}'
			   f'\nСторона 2: {self.side2}'
			   f'\nСторона 2: {self.side3}\n'
			   f'Цвет:{self.color}'
			   f'\nПлощадь:{self.side1 / 4 * math.sqrt (4 * self.side2 ** 2 - self.side1 ** 2)}'
			   f'\nПериметр:{(self.side1 + self.side2 + self.side3) / 2}')
	
	# def figur(self):
	#     for i in range(1, self.side1 - 4):
	#         print(' ' * (self.side1 - i) + '*' * (2 * i - 1))
	
	def figur(self):
		rows = []
		for j in range (self.side2):
			rows.append (" " * j + "*" * (self.side1 - 2 * j) + " " * j)
		print ("\n".join (rows))


# shape1 = Square('===Квадрат===', 'red', 3)
# shape1.info()
# shape1.figur()
# print()
# shape2 = Rectangle('===Прямоугольник===', 'green', 7, 3)
# shape2.info()
# shape2.figur()
#
# shape3 = Triangle('===Треугольник===', 'yellow', 11, 6, 6)
# shape3.info()
# shape3.figur()

# shape = [
# 	Square ('===Квадрат===', 'red', 3),
# 	Rectangle ('===Прямоугольник===', 'green', 7, 3),
# 	Triangle ('===Треугольник===', 'yellow', 11, 6, 6)
# ]
#
# for i in shape:
# 	i.info ()
# 	i.figur ()
#
#
# # 31 Занятие
#
# class NonOrder:
# 	def __set_name__(self, owner, name):
# 		self.name = name
#
# 	def __get__(self, instance, owner):
# 		return instance.__dict__[self.name]
#
# 	def __set__(self, instance, value):
# 		if value < 0:
# 			raise ValueError("Число не может быть отрицательным.")
# 		instance.__dict__[self.name] = value
#
#
# class Order:
# 	price = NonOrder()
# 	amount = NonOrder()
#
# 	def __init__(self, name, price, amount):
# 		self.name = name
# 		self.price = price
# 		self.amount = amount
#
# 	def info(self):
# 		return self.price * self.amount
#
#
# apple_order = Order("apple", 5, 10)
# print(apple_order.info())


# 32 Занятие
#
#
# class Side:
# 	def __set_name__(self, owner, name):
# 		self.name = name
#
# 	def __get__(self, instance, owner):
# 		return instance.__dict__[self.name]
#
# 	def __set__(self, instance, value):
# 		if value < 0:
# 			raise ValueError ("Число не может быть отрицательным.")
# 		instance.__dict__[self.name] = value
#
#
# class Triangle:
# 	a = Side ()
# 	b = Side ()
# 	s = Side ()
#
# 	def __init__(self, a, b, c):
# 		self.a = a
# 		self.b = b
# 		self.c = c
#
# 	def examination(self):
# 		if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
# 			return "существует."
# 		else:
# 			return "не существует."
#
# 	def info(self):
# 		print (f"Треугольник со сторонами ({self.a}, {self.b}, {self.c}) {self.examination ()}")
#
#
# tr = [
# 	Triangle (2, 5, 6),
# 	Triangle (5, 2, 8),
# 	Triangle (7, 3, 6)]
# for i in tr:
# 	i.info ()

# 33 Занятие
#
# from sistem import employee, salary, statement

# class Statement:
# 	def check_info(self, employees):
# 		print('Расчет заработной платы')
# 		print('=' * 50)
# 		for employee in employees:
# 			print(f'Заработная плата:  {employee.cod} - {employee.name}')
# 			print(f'- Проверить сумму: {employee.check_info ()}')
# 			print('')
#
#
# class Employee:
# 	def __init__(self, cod, name):
# 		self.cod = cod
# 		self.name = name
#
#
# class SalaryEmp(Employee):
# 	def __init__(self, cod, name, salary):
# 		super().__init__(cod, name)
# 		self.salary = salary
#
# 	def check_info(self):
# 		return self.salary
#
#
# class HourlyEmp (Employee):
# 	def __init__(self, cod, name, hours_worked, hour_rate):
# 		super().__init__(cod, name)
# 		self.hours_worked = hours_worked
# 		self.hour_rate = hour_rate
#
# 	def check_info(self):
# 		return self.hours_worked * self.hour_rate
#
#
# class CommissionEmp (SalaryEmp):
# 	def __init__(self, cod, name, salary, commission):
# 		super().__init__(cod, name, salary)
# 		self.commission = commission
#
# 	def check_info(self):
# 		fixed = super().check_info()
# 		return fixed + self.commission


# salary_employee = employee.SalaryEmp (1, "Валерий Задорожный", 1500)
# hourly_employee = salary.HourlyEmp (2, "Илья Кромин", 300, 2)
# commission_employee = salary.CommissionEmp (3, "Николай Хорольский", 1000, 250)
# payroll = statement.Statement ()
# payroll.check_info ([
# 	salary_employee,
# 	hourly_employee,
# 	commission_employee
# ])