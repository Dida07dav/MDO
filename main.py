# coding=utf-8
# Функции преобразования типов
# int() - числовой тип
# str() - строковой тип
# float() - вещественный тип
# bool() - булевый тип


# name = "Dida"
# age = 20
# print("Hello " + name + ". I am " + str(age))
#
# print(type(name))
# print(type(age))
# print(id(name))
# print(id(age))

# a, b, c = 5, "Hello", 9.2
# print(a, b, c)
# import keyword
# print(keyword.kwlist)

# a = 5
# print(a)
# a = 6
# print(a)

# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# # c = a  # с = 1
# # a = b  # a = 2
# # b = c  # b = 1
# a, b = b, a
# print("a:", a)
# print("b:", b)

# print("строка \
# символов")
# print('строка \
#       символов')

# print("Документ \"script.py\" находится \rпо заданному пути: \n\tD:\\Python\\project")
#
# print(type(45550))
# print(type(4.45445465476))
# print(454757687678564346546768)
# print(4.4654534356467879790775456)


# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(5 / 2)
# print(5 // 2)
# print(5 ** 2)
# print(14 % 4)


# a = 5
# b = 7
# c = 3
# s = a + b + c
# print("Сумма:", s)
# print("Произведение:", a * b * c)
# print("Среднее арифметическое:", s / 3)

# number = 6 + 4 * 5 ** 2 + 7
# print(number)
# number = (6 + 4) * (5 ** 2 + 7)
# print(number)

# num = 10
# num += 5  # num = num + 5
# print(num)
# num = 4321  # 432
# print("Исходное число:", num)
# a = num % 10
# print(a)
# num = num // 10
# # print(num)
# b = num % 10
# print(b)
# num = num // 10
# # print(num)
# c = num % 10
# print(c)
# num = num // 10
# # print(num)
# d = num % 10
# print(d)
# print(a * 1000 + b * 100 + c * 10 + d)

# num = 9573  # 432
# print("Исходное число:", num)
# res = (num % 10) * 1000
# num = num // 10  # 432
# res += (num % 10) * 100
# num = num // 10
# res += (num % 10) * 10
# num = num // 10
# res += num % 10
# print(res)

# 2 Занятие
#
# a = int(input("Введите число: "))
# # a = int(a)
# print(type(a))
# print(a * 2)

# num1 = "2"
# num2 = 3
# res = int(num1) + num2
# #res = num1 + str(num2)
# print(res)
# print(type(res))

# print(int(3.8))
# print(round(3.8638675, 2))

# print(5 / 2)

# a = '5.2'
# b = 10
# c = float(a) + b
# print(c)
# print(type(c))

# name = "Виктор"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="---", end="\n")
# print("Я учу Python")

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# res = num ** power
# print("Число", num, "в степень", power, "равно:", res)

# b1 = True   # добавление
# # b2 = False   #
# # print(b1 + 5)
# # print(b2 + 5)
# print(type(b1))


# print(bool("Python"))
# print(bool(""))  # False
# print(bool(" "))  # True
# print(bool(-15))
# print(bool(0))  # False
# print(bool(False))  # False
# print(bool(None))  # False

# test = None
# print(test)
# print(type(test))
# test = 5
# print(test)
# print(type(test))

# print(7 == 7)
# print(7 + 2 == 7)
# print(7 + 2 != 7)
# print(8 >= 8)
# print(8 <= 5)
# print('привет' > 'Привет')

# print(2 < 14 < 9)
# print(2 * 5 > 7 >= 4 + 3)

# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# print(5 - 3 == 2 and 1 + 3 == 4)  # True ( True : True)
# print(5 - 3 == 2 and 1 + 3 < 4)  # False ( True : False)
# print(5 - 3 < 2 and 1 + 3 == 4)  # False ( False : True)
# print(5 - 3 > 2 and 1 + 3 < 4)  # False ( False : False)

# print(5 - 3 == 2 or 1 + 3 == 4)  # True ( True : True)
# print(5 - 3 == 2 or 1 + 3 < 4)  # True ( True : False)
# print(5 - 3 < 2 or 1 + 3 == 4)  # True ( False : True)
# print(5 - 3 > 2 or 1 + 3 < 4)  # False ( False : False)

# print(not 9 - 5)
# print(not 5 - 5)

# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("ВВедите свой вопрос:"))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     pass
#     print("Доступ запрещен")

# a = 15
# b = 7
# if a > b:
#     print("a > b")
# elif a < b:
#     print("b > a")
# else:
#     print("b == a")

# a = 10
# b = 20
# c = 20
# a = int(input("Введите первую сторону: "))
# b = int(input("Введите вторую сторону: "))
# c = int(input("Введите третью сторону:"))
# # if a == b and b == c and c == a:
# if a == b == c:
#     print('Треугольник равносторонний')
# elif a == b or c == a or b == c:
#     print('Треугольник равнобедренный')
# # elif a != b and b != c and c != a:
# else:
#     print('Треугольник разносторонний')

# num1 = 10
# num2 = 20
# num3 = 20
# if num1 == num2 == num3:
#     print("Треугольник равносторонний")
# elif num1 ==num2 or num1 == num3 or num2 ==num3:
#     print('Треугольник равнобедренный')
# else:
#     print('Треугольник разносторонний')

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:   #(day >= 1) and (day <= 5):
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует!")

# mouth = int(input("Введите номер месяца: "))
# if 1 <= mouth <= 12:
#     if 1 <= mouth <= 2 or mouth == 12:
#         print("зима")
#     if 3 <= mouth <= 5:
#         print("весна")
#     if 6 <= mouth <= 8:
#         print("лето")
#     if 9 <= mouth <= 11:
#         print("осень")
# else:
#     print("Ошибка ввода данных")

# mouth = int(input('ВВедите номер месяца:'))
# if mouth == 1 or mouth == 2 or mouth == 12:
#     print('Зима')
# elif mouth == 3 or mouth == 4 or mouth == 5:
#     print('Весна')
# elif mouth == 6 or mouth == 7 or mouth == 8:
#     print('Лето')
# elif mouth == 9 or mouth == 10 or mouth == 11:
#     print('Осень')
# else:
#     print('Ошибка ввода данных')


# n = int(input("Введите количество ворон:"))
# if 0 <= n <= 9:
#     if n == 1:
#         print("На ветке", n, "ворона")
#     if 2 <= n <= 4:
#         print("На ветке", n, "вороны")
#     # else:
#     if 5 <= n <= 9 or n == 0:
#         print("На ветке", n, "ворон")
# else:
#     print("Ошибка ввода данных")

# (условие ? True : False)

# a, b = 30, 20
#
# minim = a if a < b else b
# print(minim)

# 3 Занятие


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

# a = 5
# b = 0
# print(a / b)

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Неправильные данные")
# else:
#     print("все нормально. Вы вели числа", n, "и", m)
# finally:
#     print("Конец программы")
# # except ValueError:
# # print("Что-то пошло не так")
# # print("Нельзя водить строки")
# # except ZeroDivisionError:
# # print("Нельзя делить на ноль")
# print("ОК!!!")

# a = input("введите первое число: ")
# b = input("введите второе число: ")
# try:
#     a = int(a)  # a = 2
#     b = int(b)  # b = пять
# except ValueError:
#     a = str(a)
#     b = b
# finally:
#     print(a + b)

# while условие:
#    блок инструкций

# i = 10
# while i <= 20:
#     print("i =", i)
#     i += 1   # i = i + 1

# i = 1
# while i <= 20:
#     if i % 2:
#         print(i, end=" ")
#     i += 1

# i = 1
# while i <= 1000:
#     print(i, end=" ")
#     i *= 10

# i = 3
# while i > 0:
#     print("***\n***", end="")
#     i -= 1

# n = int(input("укажите количество символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# n = int(input("укажите количество символов: "))
# while n > 0:
#     print("*", end=" ")
#     n -= 1

# n = int(input("Введите начало диапазонов: "))
# m = int(input("Введите конец диапазона: "))
# # i = n
# res = 0
# while n <= m:
#     if n % 2:
#         res += n   # res = res + n
#         print(n, end=" ")
#     n += 1
# print("Сумма целых нечетных чисел: ", res)

# n = input("Введите целое число: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое")
#         n = input("Введите целое число: ")
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен!")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i +=

# while True:
#     n = int(input("Введите положительное целое число: "))
#     if not n > 0:
#         break
# print(n)

# res = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     res *= n
# print("Результат:", res)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)

# 4 Занятие


# n = int(input("Количество символов:"))
# sim = input("Тип символа:")
# orient = int(input("0 - горизонтальная"
#                    "\n1 - вертикальная"
#                    "\nориентация линии: "))
# i = 0
# while i < n:
#     if orient == 0:
#         print(sim, end=" ")
#     elif orient == 1:
#         print(sim)
#     else:
#         print("Такой ориентации не предусмотренно")
#         break
#     i += 1

# num = int(input("Введите количество чисел последовательности: "))  # 5
# i = 1
# n = float(input("Введите число: "))
# summa = n  # 4
# maxim = n  # 4
# minim = n  # 4
# while i < num:
#     n = float(input("Введите число: "))  # 2 3 6 1
#     summa += n  # summa = summa + n 4 + 2 = 6 + 3 = 9 + 6 = 15 + 1 16
#     if maxim < n:
#         maxim = n  # maxim = 6
#     if minim > n:
#         minim = n  # minim = 1
#     i += 1
# print(f"Среднее арифметическое равно: {summa / num}")
# print(f"Минимальное число равно: {minim}")
# print(f"Максимальное число равно: {maxim}")

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1


# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1
# for element in collection:
#     print(element)

# for i in 5, 6, 7, 8, 9:
#     print(i)
#
# for i in "Hello":
#     print(i)

# range(start, stop, step)
# print(range(4, 6))

# for i in range(6):
#     print(i)

# a = int(input("Введите целое число: "))  # 36
# for i in range(1, a):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):  # 10
#     if i % 10 == i // 10:  # 1 == 1
#         print(i, end=" ")  # 11

# for i in range(3):
#     print(i, end=" ")
#     if i == 1:
#         break
#
# else:
#     print("done")

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("------")

# w = int(input("Ширина прямоугольника: "))
# h = int(input("Высота прямоугольника:"))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# n = [i for i in range(6) if i % 2 == 0]
# print(n)

# n = [i * 2 for i in "Hello"]
# print(n)

# Список
# n = [5, 6, [7, 8, 9], "Hello", 5.6, True]
# # print(n)
# # print(type(n))
# # print(n[0])
# # print(n[1])
# # print(n[2][2])
# #
# # print(n[-3][2])
# n[1] = 256
# print(n)
# print(len(n))


# s = [1, 2, 3]
# print([5] * 6)
# # print(s)
# #
# # b = list("Hello")
# print(b)


# 5 урок

# n = list(range(2, 10, 2))
# n2 = [2, 4, 6, 8]
# print(n)
# print(id(n))
# print(n2)
# print(id(n2))
# if n == n2:
#     print('списки равны')
# else:
#     print('списки разные')

# [выражение for переменная is последовательность]
# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)
# n = 5
#
# for i in range(1, n + 1):
#     print(i ** 2, end=" ")

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)

# print([int(input("-> ")) for i in range(int(input("n = ")))])

# n = [2, 4, 6, 8]
#
# for i in range(len(n)):
#     print(n[i], end=" ")
#
# print()
# for elem in n:
#     print(elem, end=" ")

# n = [-3, 9, -5, -1]
# b = 0
# for i in n:
#     if i < 0:
#         b += i
# print(b)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# b = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         b += a[i]
# print(b)

# n = list(range(21, 41))
# print(n)
# s = k = 0
# # for i in range(len(n)):
# #     if n[i] % 2 == 0:
# #         k += 1
# #     else:
# #         s += n[i]
# # 2-ой вариант
# for i in range(len(n)):
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
# print("Количество: ", k)
# print("сумма: ", s)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# s = k = 0
# for i in range(len(a)):
#     if a[i] != 0:
#         s += a[i]
#         k += 1
#
# print(s / k)

# 6 Занятие

# a = [7, 9, 2, 1, 17]
# a[0], a[-1] = a[-1], a[0]
# print(a)

# Срез
# список(start: stop: step)

# s = [5, 9, 3, 7, 1, 8]
# print(s[1:4])
# print(s[2:])
# print(s[::-1])
# print(s[1:5])
# print(s[6:7:])

# s = [1, 2, 3, 4, 5, 6, 7]
# print(s[:])
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[-1:])
# print(s[3:4])
# print(s[4:])
# print(s[4:1:-1])
# print(s[-3:1:-1])
# print(s[2:5])

# s = [5, 9, 3, 7, 1, 8]
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:3] = [20]
# s[2] = 30
# s[38:] = [18, 11, 12, 13, 14]
# print(s)
# print(s[7])

# Методы списка

# s = [5, 9, 3, 7, 1, 8]
# s.append(99)  # добавляет один элемент в конец список
# print(s)
# s.extend([1, 2, 3])  # добавляет список в конец основного список
# print(s)
# s.extend('apple')
# print(s)
# s.insert(1, 100)  # добавляет элемент по индексу (первый параметр), с заданным значением (второй параметр)
# print(s)


# s = []
# n = int(input("n ="))
# for num in range(n):
#     x = int(input("-> "))
#     s.append(x)
# print(s)
#
# s = []
# n = int(input("Кол-во элемента списка: "))
# for num in range(n):
#     w = int(input("Введите число кратное 3: "))
#     if w % 3 == 0:
#         s.append(w)
#     else:
#         print("число", w, "не делится на 3")
# print(s)
#

# a = [5, 9, 1, 4, 3]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
# i = 0
# while i < len(a):
#     c.append(a[i])
#     c.append(b[i])
#     i += 1
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
# i = 0
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33, 4, 2]
# c = []
# i = 0
# while i < len(a):
#     c.append(a[i])
#     c.append(b[i])
#     i += 1
# print(c + b[3:5])

# s = [5, 9, 3, 7, 1, 8]
# # s[3:] = []
# print(s)
# # s.remove(9)  # удаляет первый искомый элемент из списка по значение
# # print(s)
# # last = s.pop(0)  # без параметров - удаляет последний элемент из списка,
# # # указанный параметр - это индекс удаляемого элемента
# # print(last)
# # print(s)
# # s.clear()  # удаляет из списка все элементы
# # print(s)
# del s[2]
# print(s)

# s = [int(input("-> ")) for i in range(int(input("n = ")))]
# k = int(input('Введите индекс:'))
# s.pop(k)
# print(s)


# s = [5, 9, 3, 7, 1, 8, 9, 9, 9, 3, 11, 7]
# num = s.count(9)  # количество заданных значений в списке
# print(num)
# print(s)
# ind = s.index(7, 9)
# print(ind)

# a = [1, 2, 3]
# b = a
# print("a =", a)
# print("b =", b)
# # a.append(20)
# a[0] = 5
# b[1] = 20
# print("a =", a)
# print("b =", b)


# a = [1, 2, 3]
# b = a.copy()
# print("a =", a)
# print("b =", b)
# # a.append(20)
# a[0] = 5
# b[1] = 20
# print("a =", a)
# print("b =", b)


# s = [5, 9, 3, 7, 1, 8, 9, 9, 9, 3, 11, 7]
# print(s)
# s.reverse()  # переворачивает список
# print(s)
# s.sort(reverse=True)  # сортирует в порядке возрастания, изменяет список, reverse=True -сортировка в порядке убывания
# print(s)
# a = sorted(s, reverse=True)   # сортирует в порядке возрастания, НЕ изменяет список
# print(a)
# print(s)

# s2 = ['Виталий', 'Сергей', 'Александр', 'Анна']
# s2.sort(key=len, reverse=True)
# print(s2)

# 7 Занятие

# a = [1, 2, 3]
# b = [11, 12, 13, 4, 2, 6, 8]
# c = []
# print("a =", a)
# print("b =", b)
#
# if len(b) > len(a):
#     for i in range(len(a)):  # от 0 до 3
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):  # от 3 до 5
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# print("c =", c)


# import random
#
# print(random.random())
# print(random.randint(10, 15))
# print(random.randrange(0, 10, 2))


# from random import randint, randrange
#
#
# print(randint(10, 15))
# print(randrange(0, 10, 2))

# import random as r
#
# print(r.randint(10, 15))
# print(r.randrange(10))
#
# city = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# print(r.choice(city))
#
# s = [55, 66, 77, 88, 99, 50, 20, 30, 40, 60, 70, 80]
# print(r.choice(s))
# print(r.choices(s, k=4))
# r.shuffle(s)
# print(s)
#
# print(r.uniform(10.5, 25.5))
# print(round(r.uniform(10.5, 25.5), 2))

# mas = [r.randint(0, 100) for i in range(10)]
# print(mas)

# Функции агрегирования

# lst = [5, 3, 2, 4, 1]
# print(len(lst))
# print(max(lst))
# print(min(lst))
# print(sum(lst))

# sum = [1, 2, 3]
# print(min(sum))

# x = [r.randint(0, 100) for i in range(0, 5)]
#
# print(x)
# m = max(x)
# print("Max:", m)
# x.remove(m)
# x.insert(0, m)
# print(x)

# x = [r.randint(-20, 20) for i in range(0, 10)]
# print(x)
# x.sort(reverse=True)
# # x.reverse()
# print(x)

# x = [r.randint(0, 40) for i in range(0, 10)]
# print(x)
# m = min(x)
# print("Min:", m)
# k = x.index(m)
# print("Index min:", k)
# del x[0:k]
# print(x)

# x = list('483hf983h83gy7')
# print(x)
# print('h' in x)
# print('e' in x)
# print('a' not in x)
# print('e' not in x)

# lst = []
# # if len(lst) == 0:
# #     print("Список пуст")
# if len(lst) == 0:
#     print("Список пуст")

# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [r.randint(0, 10) for i in range(n1)]
# b = [r.randint(0, 10) for j in range(n2)]
# print("a =", a)
# print("b =", b)
# c = a + b
# print("c =", c)

# c = []
# for i in a:
#     if i not in c:
#         c.append(i)
# for i in b:
#     if i not in c:
#         c.append(i)
# print("Элементы обоих списка без повторений =", c)

# c = []
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print("Элементы общие для двух списка: ", c)

# c = [min(a), min(b), max(a), max(b)]
# print("Минимальное и максимальное значение каждого из списка: ", c)
# n = [[r.randint(0, 4) for x in range(3)]
#      for b in range(4)]
# m = 1
# for row in n:
#     for x in row:
#         if x > 0:
#             m += x
#         print(x, end="\t\t")
#     print()
# print("Произведение: ", m)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# # print(len(m))
# # print(m[1][2])
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t\t")
#     print()
# print()
# for row in m:
#     for x in row:
#         print(x, end="\t\t")
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)
# a = [1, 2], [3, 4], [5, 6], [7, 8]
# print(a)
# for x, y in a:
#     print(x, "+", y, "=", x + y)

# m = [[r.randint(-10, 20) for x in range(6)]
#      for y in range(4)]
#
# for row in m:
#     for x in row:
#         print(x, end="\t\t")
#     print()
# print(row, end="\t\t")

# 8 Занятие

# num1 = math.sqrt(16)
# num2 = math.ceil(3.2)
# num3 = math.floor(3.8)
#
# print(num1)
# print(num2)
# print(num3)
#
# print(dir(math))
# print(math.pi)

# rd = int(input("Введите радиус окружности: "))
# print("Длина окружности:", round(2 * math.pi * rd, 2))

# seconds = time.time()
# print("Секунды с начало эпохи: ", seconds)
# locale_time = time.ctime(456877895.7)
# print("Местное время:", locale_time)
# res = time.localtime()
# # print("Localtime:", res)
# print(res.tm_mday, ".", res.tm_mon, ".", res.tm_year, sep="")
# print(time.strftime("Today is %B %d, %Y."))
# print(time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(41233445)))

# pause = 5
# print("Program started...")
# time.sleep(pause)
# print(pause, "seconds.")

# text = input("Название напоминания: ")
# locale_time = float(input("Через сколько минут: "))
# locale_time = locale_time * 60
# time.sleep(locale_time)
# print(text)

# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(res, "seconds.")

# start = time.monotonic()
# time.sleep(5)
# res = time.monotonic() - start
# print(res, "seconds. ")

# import locale
#
# locale.setlocale(locale.LC_ALL, "ru")  # Перевод на другой язык
#
# print(time.strftime("Сегодня: %B %d %Y."))

# Функция
# print()
#
#
# def hello(name):  # аргументы
#     print("Hello", name)
#
#
# hello("Irina")  # параметры
# hello("Igor")


# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# n = 6
# m = 4
# get_sum(n, m)
# get_sum("abc", "def")
# get_sum(2.5, 4.3)


# def symbol(a, b, c):
#     for i in range(a):
#         if i % 2 == 0:
#             print(b, end="")
#         else:
#             print(c, end="")
#     print()
#
#
# symbol(9, "+", "-")
# symbol(7, "x", "o")

# def get_summa(a, b):
#     print(a + b)
#     return a + b
#
#
# res = get_summa(1, 8)
# print(res)
# print(get_summa(2, 5))

# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two


# print(maximum(9, 6))

# x = int(input("a: "))
# y = int(input("b: "))
#
#
# def rs(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
#
#
# print(rs(x, y))


# def cube(a):
#     return a ** 3
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))

# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=" ")
#         # a, b = b, a + b
#
#         a = b
#         b = a + b


# fib(25)

# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))

# 9 Задание

# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(is_greater(10, 5))
# print(is_greater(5, 15))


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#
#     for has_upper and has_lower and has_num:
#         if len(password) >= 8 and has_upper and has_lower and has_num:
#             return True
#         else:
#             if len(password) < 8:
#                 print("Количество символов слишком маленькое")
#     else:
#         print("Недопустимые символы")
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это ненадежный пароль")


# def get_sum(a=4, b=3, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))
# s = 2
# print(get_sum(c=s))

# def symbol(elements=20, sign='-'):
#     for i in range(elements):
#         print(sign, end='')
#     print()
#
#
# symbol(10, "+")
# symbol(5, "*")
# symbol(15, "#")
# symbol(7)
# symbol()

# def digits_sum(n, event=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if event and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not event and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print("Сумма четных цифр:")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
# print("Сумма нечетных цифр:")
# print(digits_sum(9874023, False))
# print(digits_sum(38271, False))
# print(digits_sum(123456789, event=False))

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#     print("*" * 20)
#
#
# display_info("Ira", 20)
# display_info(20, "Ira")
# display_info(age=23, name="Igor")
# display_info("Ira", age=23, name="Igor")

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1 == lt2)  # True
# print(lt1 is lt2)  # False
# print(id(lt1))
# print(id(lt2))


# lt1 = 5
# lt2 = 5
# print(lt1 == lt2)  # True
# print(lt1 is lt2)  # True
# print(id(lt1))
# print(id(lt2))

# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(lt1)
# lt1.pop(1)
# print(lt1)
# print(id(lt1))

# s = "Hello "
# print(id(s))
# s += "World"  # s = s + "World"
# print(s)
# print(id(s))
# # s[1] = "a"
# # s[1:2] = "a"
# # s = s[:1] + s + s[2:]
# s = s[1:-1]
# print(s)
# print(id(s))

# a = "Hello"
# b = "Hello"
# print(a == b)
# print(a is b)

# a = 5
# b = 5
# print(a == b)
# print(a is b)

# a = True
# b = True
# print(a == b)
# print(a is b)

# def add_numbers(n):
#     print("Внутри функции:", n, "=", id(n))
#     n += 1
#     print("После изменения:", n, "=", id(n))
#     return n
#
#
# x = 1
# print(x, "=", id(x))
# x = add_numbers(x)
# print(x, "=", id(x))


# def add_numbers(n):
#     print("Внутри функции:", n, "=", id(n))
#     n += [4]
#     # n = n + [4]
#     print("После изменения:", n, "=", id(n))
#
#
# x = [1, 2, 3]
# print(x, "=", id(x))
# add_numbers(x)
# print(x, "=", id(x))

# типы данных:
# изменяемые: список (list)
# неизменяемые: число (int), строка (str), вещественное число (float), булевы значения (bool)

# 10 Занятие

# Картеж (tuple) - это неизменяумая структура данныч, которая по своему подобию очень похожа на список.
# Картеж -нетзменяемый список. Или списки доступные толькодля чтения. Состоит из элементов, разделенных запятыми
# заключенных в круглые скобки
#
# lst =(10, 20, 30)
# tpl = (10, 20, 30)
#
# print(lst.__sizeof__())
# print(tpl.__sizeof__())


# # a = (1, 5, 6, 7, 8)
# # print(a)
# # print(type(a))
# b = tuple((1, 5, 6, 7, 8))
# print(b)
# print(type(b))

# q = 1, 2, 3, "w"  # упаковка картежа
# t = (1, )
# print(type(q))
# print(type(t))
# t1 = tuple("hello")
# print(t1)
# print(t1[1])
# print(t1[1:3])
# t1[1] = "i"

# s1 = tuple(int(input("->")) for i in range(5))
# print(s1)

# s = input("-> ")
# print(tuple(s))

# mas = [r.randint(0, 100) for i in range(10)]
# tpl = tuple(mas)
# print(tpl)

# mas = tuple(r.randint(0, 100) for i in range(10))
# print(mas)

# s = tuple(2 ** i for i in range(1, 13))
# print(s)

# t1 = tuple("hello")
# t2 = tuple(" world")
# t3 = t1 + t2
# print(t3)
# # print(len(t3))
# # print(t3.count('l'))
# # print(t3.index('l', 4))
# # if 'a' in t3:
# #     print(t3.index('a'))
# # else:
# #     print("Такого символа нет")
# for i in t3:
#     print(i, end=" ")

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first+ 1) + 1
#             return tpl[first:second]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9,2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = 'new'
# t[4].append('hi')
# print(t, id(t))

# t = (1, 2, 3)
# # # x = t[0]
# # # y = t[1]
# # # z = t[3]
# # x, y, z = t  # распоковка картежа
# # print(x, y, z)
# # print(type(x))
# # print(type(t))

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
# user1, user2, user3 = get_user()
# print(user1)
# print(user2)
# print(user3)

# t = (1, 2, 3)
# del t
# print(t)

# lst = [1, 2, 3, 4, 5, 6]
# print(type(lst))
# print(lst)
# tpl = tuple(lst)
# print(type(tpl))
# print(tpl)
# print(list(tpl))

# countris = (
#     ("Германия", 20.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# # print(countris)
#
# for country in countris:
#     country_name, country_population, cities = country
#     print("\nСтрана:", country_name, "население =", country_population)
#     for city in cities:
#         city_name, city_popolation = city
#         print("\tГород", city_name, "население =", city_popolation)


# Множества  (set) - неупорядоченная коллекция, которая хранит только уникальное значения

# {}
# set()

# s = {4, 7, 8, 9, 4, 2, 4, 2, 4}
# print(type(s))
# print(len(s))
# print(s)

# s = set("hello")
# # print(s)

# c = [1, 5, 4, 2, 2, 6, 4]
# s = set(c)
# print(s)
# c = list(s)
# print(c)
# numbers = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
# s = list({x for x in numbers if x % 2 == 0})
# print(s)

# def to_set(el):
#     # st = set(el)
#     # return st, len(st)
#     return set(el), len(set(el))
#
#
# print(to_set('Я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))


# t = {'red', 'green', 'blue'}
# # print("green" not in t)
# for i in t:
#     print(i)

# {i for i in последовательность}
# {i for i in последовательность if условие}
# {i(True) if условие else (False) for i in последовательность}
# {i(True) if условие else (False) for i in последовательность if условие}

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = {i for i in r if 'a' not in i}
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r}
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c'}
# print(a)

# 11 Занятие

# print("Вносим изменения")
#
# print("Вносим изменения в склонированный проект")
#
# print("PyCharm")

# 12 Занятие

# a = {"Tom", "Bob", "Alice"}
# a.add("Ann")
# print(a)
# # b = "Tom"
# # if b in a:
# #     a.remove(b)
# # a.discard("Tom")
# # a.pop()
# a.clear()
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b)
# c = a | b
# # c = a & b
# # c = b - a
# c = a ^ b
# # a |= b
# # a &= b
# # print(c)
# print(c)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}


# s = s1.union(s2, s3, s4, s5, s6, s7)
# # s = s1 |s2 | s3 | s4 | s5 | s6| s7
# print(s)
# print(len(s))
# print(max(s))
# print(min(s))

# s1 = "Hello"
# s2 = "How are you"
# a = set(s1) & set(s2)
# for i in a:
# 	print(i, end=" ")

# drawing = {'Marina', 'Jenya', 'Sveta'}
# music = {'Kostya', 'Jenya', 'Ilya'}
# one = drawing ^ music
# print(one)
#
# two = drawing & music
# print(two)
#
# drawing = drawing - two
# print(drawing)

# Tun frozenset (замороженное множество)

# a = frozenset([1, 2, 3, 4, 5])
# print(a)
# s = frozenset({"hello", "world"})
# print(s)

# Словарь dict()

# lst = ["one", "two", "three"]
# print(lst)
# print(lst[0])
# d = {"a": "one", "b": "two", "c": "three"}
# print(d)
# print(d["b"])

# d = {}
# print(d)
# print(type(d))

# d = {'one': 1, 2: "two"}
# print(d)


# d = dict(short='dict', long='dictionary')
# print(d)

# users = (
# 	('igor@gmail.com', 'Igor'),
# 	('irina@gmail.com', 'Irina'),
# 	('ann@gmail.com', 'Ann'),
# )
# print(users)
# d_users = dict(users)
# print(d_users)

# d = {i: i ** 2 for i in range(7)}
# print(d)
# print(d[2])
# d[2] = 15
# d[9] = 4**2
# print(d)

# d = {0: 'text', 'one': 45, (1, 2.3): 'Кортеж', 42: [2, 3, 6, 7], True: 1}
# print(d)
# # print(d[42][2])
# # print(d[(1, 2.3)])
# #
# # print('one' in d)
# # print('two' in d)
# # key = 'two'
# # #
# # # if key in d:
# # # 	del d[key]
# #
# # try:
# # 	del d[key]
# # except KeyError:
# # 	print("Такого элемента нет")
# # print(d)
# for key in d:
# 	print(key, "->", d[key])

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for key in d:
# 	res *= d[key]
#
# print(res)

# d = dict()
# # d[1] = input("->")
# # d[2] = input("->")
# # d[3] = input("->")
# # d[4] = input("->")
# d ={i: input("->")for i in range(1, 5)}
# print(d)
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)
# print(len(d))

# goods = {
# 	"1": ['Core-i3-4330', 9, 4500],
# 	"2": ['Core-i5-4670k', 3, 8500],
# 	"3": ['AMD FX-6300', 6, 3700],
# 	"4": ['Pentium G3220', 8, 2100],
# 	"5": ['Core-i5-3450', 5, 4600],
# }
#
# for i in goods:
# 	print(i, ") ", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], "руб", sep="")
# while True:
# 	n = input("№: ")
# 	if n != "0":
# 		k = int(input("Количество: "))
# 		goods[n][1] = k
# 	else:
# 		break
#
#
# for i in goods:
# 	print(i, ") ", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], "руб", sep="")


# d = {'A': 1, 'B': 2, 'C': 3}
# v = d["B"]
# print("B =", v)
# value = d.get('E', "False")
# d.clear()
# d2 = d.copy()
#
# print("D =", d)
# print("D2 =", d2)
# print()
#
# d['E'] = 7
# d2['B'] = 5
#
# print("D =", d)
# print("D2 =", d2)


# d = {'A': 1, 'B': 2, 'C': 3}
# # a = d.items()
# # print(a)
# #
# # b = d.keys()
# # b = d.keys()
# # print(b)
# #
# # c = d.values()
# # print(c)
# #
# # for key, val in d.items():
# # 	print(key, ":", val)
# # item = d.pop("B", 5)
# # print(item)
# # print(d)
# # item = d.setdefault("E")
# # print(item)
# # print(d)
# d.update([('R', 7), ('q', 9)])
# print(d)


# x = {
# 	'a': 1,
# 	'b': 2,
# }
# y = {
# 	'b': 3,
# 	'c': 4,
# }
# # c = {**x, **y}
# # c = x | y
# c = x.copy()
# c.update(y)
# print(c)

# 13 Занятие

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
#
# new_d = dict()
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
# print(d)
# print(new_d)
#
# a = {
# 	'First': {
# 		1: 'one',
# 		2: 'two',
# 		3: 'three',
# 	},
# 	'Second': {
# 		4: 'four',
# 		5: 'five',
# 	},
# }
# print(a)
# for x in a:
# 	print(x)
# 	for y in a[x]:
# 		print('\t', y, ":", a[x][y], sep="")

# sales = {
# 	"John": {
# 		"N": 3056,
# 		"S": 8463,
# 		"E": 8441,
# 		"W": 2494,
#
# 	},
# 	"Tom":{
# 		"N": 4832,
# 		"S": 6786,
# 		"E": 4737,
# 		"W": 3612,
#
# 	},
# 	"Anne": {
# 		"N": 5239,
# 		"S": 4802,
# 		"E": 5820,
# 		"W": 1859,
#
# 	},
# 	"Fiona": {
# 		"N": 3984,
# 		"S": 3645,
# 		"E": 8821,
# 		"W": 2451,
#
# 	}
#
#
# }
# for x in sales:
# 	print(x)
# 	for y in sales[x]:
# 		print('\t', y, ":", sales[x][y], sep="")
# person = input("Имя: ")
# region = input("Регион: ")
# print(sales[person][region])
# data = int(input("Новое значение: 0"))
# sales[person][region] = data
# print(sales[person])

# data = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# d = {k: v for k, v in data.items() if v <= 2}
# print(d)

# s = "Hello"
# b = {i: i * 3 for i in s}
# print(b)
#
# a = list(b.items())
# print(a)

# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
#
# d = dict()
# s = None
#
# for i in a:
# 	if type(i) == str:
# 		d[i] = []  # d["one"] = []
# 		s = i  # s = "one
# 	else:
# 		d[s].append(i)
# print(d)

# zip()

# d = zip([12, 1, 2], ["Dec", "Jan", "Feb"])
# print(d)
# print(type(d))
# # print(dict(d))
# print(list(d))

# a = ["Dec", "Jan", "Feb"]
# b = [12, 1, 2]
# d = {k: v for k, v in zip(b, a)}
# print(d)

# a = ["a", "b", "c"]
# b = [12, 1, 2]
# c = [4.8, 5.0, 6.0]
# q = zip(a, b, c)
# # print(list(c))
# print(list(q))


# print(list(zip(range(5), range(100))))


# one = {"name": "Igor", "Last_name": "Smith", "Job": "Consultant"}
# two = {"name": "Olgar", "Last_name": "Doe", "Job": "Mangert"}
#
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
# 	print(k1, "->", v1)
# 	print(k2, "->", v2)

# Распоковка последовательнности

# pairs = [(1, 'a'), (2, 'b'), (3, "c"), (4, 'd')]
# a, b = zip(*pairs)
# print(a)
# print(b)

# # Таблица
# month = ['January', 'February', 'March']
# total_sales = [52000.00, 51000.00, 48000.00]
# prod_cost = [46800.00, 45900.00, 43200.00]
#
# for sales, costs, m in zip(total_sales, prod_cost, month):
# 	profit = sales - costs
# 	print("Общая прибыль в", m, "=", profit)

# one = {'apple': 20, 'orange': 35}
# two = {'pepper': 40, 'onion': 55}
# print([two, one])
# print({**two, **one})
#
# for i in range(6):
# 	print(i)
#
# colors = ["red", "yellow", "green"]
# j = 1
# for i in colors:
# 	print(j, i)
# 	j += 1


# colors = ["red", "yellow", "green"]
# for j, i in enumerate(colors, 1):
# 	print(j,"->", i)

# num_list = [1, 2, 3, 4, 5]
# i = iter(num_list)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i, "STOP"))

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)

# def func(*args):
# 	return args
#
#
# print(func(2))
# print(func(2, 1, 3))
# print(func())

# def summa(*params):
# 	res = 0
# 	for i in params:
# 		res += i
# 		return res
#
#
# print(summa(1, 2, 3, 4, 5))
# print(summa(7, 3))

# def to_dict(*args):
# 	return {i: i for i in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('grey'), (2, 17), 3.11, -4)


# def ch(*args):
# 	res = []
# 	sr_ar = sum(args) / len(args)
# 	print(sr_ar)
#
# 	for i in args:
# 		if i < sr_ar:
# 			res.append(i)
#
# 	return res
#
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))

# №1
# a = {1: 10, 2: 20}
# b = {3: 30, 4: 40}
# c = {5: 50, 6: 60}
# d = {**a, **b, **c}
# print(d)

# №2

# 14 Занятие

# def func(a, *args):
# 	return a, args
#
#
# print(func(1))
# print(func(1, 2, 3, "abc"))

# def print_scores(student, *scores):
# 	print("Student Name:" + student)
# 	for score in scores:
# 		print(score)
#
#
# print_scores("Irina", 100, 95, 88, 92, 99)
# print_scores("Igor", 96, 20, 33)


# def func(**kwargs):
# 	return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(a="python"))

# def intro(**data):
# 	for key, value in data.items():
# 		print(key, 'is', value)
# 	print()
#
#
# intro(first_name="Irina", last_name="Fokina", age=22)
# intro(first_name="Igor", last_name="WOOD", email="igor@gmail.com", age=25, phone="9587655470")


# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# my_dict = {'one': 'first'}
# db(k1=22, k2=11, k4=91)
# db(name='Bob', age='31', weight=61, eyes_color='gray')
# print('my_dict =', my_dict)

# def db(b, *args,name=None, **kwargs ):
# 	print(b, args, name, kwargs)
#
#
# db(6, 'q', 'w', 'e', name='Olga', a=5)

# name = 'Tom'  # глобальная область видимости
#
#
# def hi():
# 	global name
# 	name = 'Sam'  #локальная область видимости
# 	print("Hello", name)
#
#
# def bye():
#
# 	print("Good bye", name)
#
#
# hi()
# bye()
# print(name)
#
# i = 5
#
#
# def func(arg=i):
# 	print("i =", i)
# 	print("arg =", arg)
#
#
# i = 6
# func()    # 5 или 6
#
# x = 4
#
#
# def add_two(a):
# 	# x = 2
#
# 	def add_some():
# 		# x = 5
# 		print('x =', x)
# 		return a + x
# 	return add_some()
#
#
# print(add_two(3))

# import builtins
#
# names = dir(builtins)
#
# for t in names:
# 	print(t)

# min =[4, 5, 6]
# print(max(min))
# print(min(min))
#
# def outer_func(who):
# 	def inner_func():
# 		print("Hello", who)
#
# 	inner_func()
#
#
# outer_func("World!")


# def func1():
# 	a = 6
#
# 	def func2(b):
# 		a = 4
# 		print("Сумма:", a + b)
# 	print("Значение переменной а:", a)
# 	func2(4)
#
#
# func1()

# def fn1():
# 	x = 25  # 1
#
# 	def fn2():
# 		x = 33  # 3
#
# 		def fn3():
# 			nonlocal x
# 			x = 55  # 5
# 			print("fn3.x =", x)  # 6
#
# 		fn3()  # 4
# 		print("fn2.x =", x)  # 7
#
# 	fn2()  # 2
# 	print("fn1.x =", x)  # 8
#
# fn1()


# def outer(a1, b1, a2, b2):
# 	a = 0
# 	b = 0
#
# 	def inner():
# 		nonlocal a, b
# 		a = a1 + a2
# 		b = b1 + b2
#
# 	inner()
# 	return [a, b]
#
#
# res = outer(2, 3, -1, 4)
# print(res)

# def increment(number):
# 	def inner(x):
# 		return number + x
# 	return inner
#
#
# a = increment(10)
# print(a(5))
# print(a(4))
#
# b = increment(1)
# print(b(7))
#
# print(increment(5)(10))

# def func1():
# 	a = 1
# 	b = "line"
# 	c = [1, 2, 3]
#
# 	def func2():
# 		nonlocal a, b
# 		c.append(4)
# 		a = a + 1
# 		b = b + "_new"
# 		return a, b, c
#
# 	return func2
#
#
# func = func1()
# print(func())

# def func(city):
# 	s = 0
#
# 	def inner():
# 		nonlocal s
# 		s += 1
# 		print(city, s)
#
# 	return inner
#
#
# res1 = func('Москва')
# res1()
# res1()
#
# res2 = func('Сочи')
# res2()
# res2()
#
# res1()

# student = {
# 	'Alice': 98,
# 	'Bob': 67,
# 	'Chris': 85,
# 	'David': 75,
# 	'Elise': 54,
# 	'Fiona': 35,
# 	'Grace': 69
# }
#
#
# def make_classifier(lower, upper):
# 	def students(exem):
# 		return {k: v for k, v in exem.items() if lower <= v < upper}
#
# 	return students
#
#
# a = make_classifier(80, 100)
# b = make_classifier(70, 80)
# c = make_classifier(50, 70)
# d = make_classifier(0, 50)
#
# print(a(student))
# print(b(student))
# print(c(student))
# print(d(student))


# 15 Занитие

# def square(figure_type, **kwargs):
# 	if figure_type == 'rhombus':
# 		return kwargs['d1'] *
#
# print(square(figure_type='rhombus', ))


# lambda (окончание функции)

# def get_sum(x, y):
# 	return x + y
#
#
# print(get_sum(1, 2))
# print(get_sum(3, 4))
#
# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)(3, 4))
#
# func = lambda x, y: x + y
# print(func(1, 2))
# print(func(3, 4))


# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# sum = lambda a=1, b=2, c=3: a + b + c
#
# print(sum())  # 6
# print(sum(10))  # 15
# print(sum(10, 20))  # 33

# func1 = lambda *args: args
#
# print(func1(1, 2, 3, 4, 5, 6, 7))
# print(func1('a', 'b', 'c'))

# c = (
# 	lambda x: x * 2,
# 	lambda x: x * 3,
# 	lambda x: x * 4,
#
# )
#
# for t in c:
# 	print(t('abc_'))

# def inc(n):
# 	def inner(x):
# 		return n + x
# 	return inner
#
#
# f = inc(5)
# print(f(2))
#
#
# # def inc1(n):
# # 	return lambda x: n + x
# #
# #
# # f1 = inc(5)
# # print(f1(2))
# #
# # inc2 = lambda n: lambda x: n + x
# #
# # f2 = inc(5)
# # print(f2(2))
#
# print((lambda n: lambda x: n + x)(5)(2))

# print((lambda n: lambda x: lambda y: n + x + y)(2)(4)(6))

# d = {'b': 10, 'a': 15, 'c': 4}
# list_d = list(d.items())
# print(list_d)
# list_d.sort(key=lambda i: i[1], reverse=True)
# print(list_d)
# print(dict(list_d))


# players = [
# 	{'name': 'Антон', 'last_name': 'Бирюков', 'rating': 9},
# 	{'name': 'Алексей', 'last_name': 'Бодня', 'rating': 10},
# 	{'name': 'Федор', 'last_name': 'Сидоров', 'rating': 4},
# 	{'name': 'Михаил', 'last_name': 'Семенов', 'rating': 6}
# ]
#
# res1 = sorted(players, key=lambda item: item['last_name'])
# print(res1)
# res2 = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res2)
# res3 = sorted(players, key=lambda item: item['rating'])
# print(res3)

# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
#
# b = a[1](5, 3)
# print(b)

# a = {'one': lambda x: x - 1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 1]
#
# for i in b:
# 	if i < 0:
# 		print(a['two'](i))
# 	elif i > 0:
# 		print(a['one'](i))
# 	else:
# 		print(a['three'](i))

# d = {
# 	1: lambda: print('Понедельник'),
# 	2: lambda: print('Вторник'),
# 	3: lambda: print('Среда'),
# 	4: lambda: print('Четверг'),
# 	5: lambda: print('Пятница'),
# 	6: lambda: print('Суббота'),
# 	7: lambda: print('Воскресенье'),
# }
#
# print(d[3])
# d[3]()


# print((lambda a, b: a if a > b else b)(15, 4))

# map(func, *iterables)

# def mult(t):
# 	return t * 2
#
#
# lst = [2, 8, 12, -5, 10]
#
# a = list(map(mult, lst))
# print(a)
#
# print(list(map(lambda t: t * 2, lst)))

#
# b = ['1', '2', '3', '4', '5']
# c = list(map(int, b))
# print(c)
# print(type(c))


# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
# print(list(map(lambda x, y: (x, y), st, num)))


# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(list(map(lambda x, y: (x + y), l1, l2)))


# res = filter(func (true or false), *iterables)


# t = ('abcd', 'abc', 'cdefq', 'def', 'ghi')
#
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)


# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)

# import random
#
# lst = [random.randint(1, 40) for i in range(10)]
# print(lst)
# print(list(filter(lambda x: 10 <= x <= 20, lst)))

# Декораторы

# def hello():
# 	return 'Hello, I am func "hello"'
#
#
# def super_func(func):
# 	print('Hello, I am func "super_func"')
# 	print(func())
#
#
# super_func(hello)


# def hello():
# 	return 'Hello, I am func "hello"'
#
#
# test = hello
# print(test())

# def my_decorator(func):  # 2
#     def func_wrapper():  # 3
#         print('Code before')  # 4
#         func()  # 5
#         print('Code after')  # 8
#     return func_wrapper  # 3
#
#
# def func_test():  # 6
#     print('func_test')  # 7
#
#
# text = my_decorator(func_test)  # 1
# text()


# def my_decorator(func):  # декорирующая функция
# 	def func_wrapper():
# 		print('*' * 40)
# 		func()
# 		print('*' * 40)
# 	return func_wrapper
#
#
# @my_decorator   # декоратор
# def func_test():  # декорирующая функция
# 	print('func_test')
#
#
# @my_decorator
# def hello():
# 	print('hello')
#
#
# func_test()
# print()
# hello()

# text = my_decorator(func_test)
# text()


# 16 Занятие

# def bold(fn):
# 	def wrap():
# 		return "<b>" + fn () + "</b>"
#
# 	return wrap
#
#
# def italic(fn):
# 	def wrap():
# 		return "<i>" + fn () + "</i>"
#
# 	return wrap
#
#
# @bold
# @italic
# def hello():
# 	return "text"
#
#
# print(hello())

# def cnt(fn):
# 	count = 0
#
# 	def wrap():
# 		nonlocal count
# 		count = count + 1
# 		fn()
# 		print("Вызов функции: ", count)
# 	return wrap
#
# @cnt
# def hello():
# 	print("Hello")
#
#
# hello()
# hello()
# hello()


# def args_decorator(fn):
# 	def wrap(args1, args2):
# 		print("Данные:")
# 		fn(args1, args2)
#
# 	return wrap


# @args_decorator
# def print_full_name(first, last):
# 	print("Меня зовут:", first, last)
#
#
# print_full_name("Ирина", "Лаврова")

#
# def args_decorator(fn):
# 	def wrap(*args, **kwargs):
# 		print("args", args)
# 		print("kwargs", kwargs)
# 		fn(*args, **kwargs)
#
# 	return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study="Python"):
# 	print(a, b, c, "изучают", study, "\n")
#
# @args_decorator
# def new_func(q):
# 	print(q)
#
#
# print_full_name("Борис", "Елизавета", "Светлана", study="JavaScript")
# print_full_name("Владимир", "Екатерина", "Виктор")
#
# new_func("Новая функция")


# def decor(args1, args2):
# 	def args_dec(fn):
# 		def wrap(x, y):
# 			print(args1, x, args2, y, "=", end=" ")
# 			fn(x, y)
#
# 		return wrap
# 	return args_dec
#
#
# @decor("Сложение:", "+")
# def summa(a, b):
# 	print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
# 	print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)
#
# def myltiply(arg):
# 	def my_decorator(func):
# 		def wrap(*args, **kwargs):
# 			return arg * func(*args, **kwargs)
#
# 		return wrap
# 	return my_decorator
#
#
# @myltiply(3)
# def return_num(num):
# 	return num
#
#
# print("Результат:", return_num(5))

# print(int('10'))
# print(int('1010', 2))
# print(int('12', 8))
# print(int('A', 16))

#
# print(bin(18))  #0b10010
# print(oct(18))  #0o22
# print(hex(18))  #0x12
#
#
# print(0b10010)
# print(0o22)
# print(0x12)

# q = "Pyt"
# w = 'hon'
# e = q + w
# print(e)
#
# print(e * 3)
# print(e * -3)
#
# print(e in "i am learn Python")
# print(e in "i am learn Java")

# s = "Hello"
# print(s[1])
# print(s[-5])
# # print(s[5])
#
# print(s[-5:-2])


# s = 'python'
# s = s[:3] + 't' + s[4:]
# print(s)


# def changeCharToStr(s, c_old, c_new):
# 	i = 0
# 	s2 = ""
#
# 	while i < len(s):
# 		if s[i] == c_old:
# 			s2 = s2 + c_new
# 		else:
# 			s2 = s2 + s[i]
# 		i = i + 1
#
# 	return s2
#
#
# srt1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# str2 = changeCharToStr(srt1, 'N', 'P')
# print(srt1)
# print(str2)
#
# print(u"Hello")
# print("Hello")

# print('I\'m learning\nPython')
# print('C:\\file.txt')
# print(r'C:\file.txt')
# print(r'C:\file\\'[:-1])
# print(r'C:\file' + "\\")
# print('C:\\file\\')

# name = "Дмитрий"
# age = 25
# print(f"Меня зовут {name}. Мне {age} лет")

# import math
#
#
# print(f"Значение числа pi: {round(math.pi, 2)}")
# print(f"Значение числа pi: {math.pi:.2f}")

#
# x = 10
# y = 5
# print(f"{x} x {y} / 2 = {x * y / 2}")

# a = 74
# print(f"{{{{{{{a}}}}}}}")

# dir_name = "my_doc"
# file_name = 'date.txt'
# print(fr"home\{dir_name}\{file_name}")
# print(r"home\{dir_name}\{file_name}")
# print("home\\" + dir_name + "\\" +file_name)


# s = 'Hello'
# print(s)
#
# a = """aaaa"""
# print(a)
#
# s = '''<div
#     < a href="#">content</a>
# </div>'''
#
# print(s)

# def square(n):
# 	"""Принимает число n, возвращает квадрат числа n"""
# 	a = 2
# 	return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
#
# import math as m
#
#
# def cylinder(r, h):
# 	"""
# 	Вычисляет площадь цилиндра.
#
# 	Вычисляет площадь цилиндра на оснавонии заданной высоты и радиуса основания
# 	:param r:  положительное число, радиус основания цилиндра
# 	:param h: положительное число, высота цилиндра
# 	:return: положительное число, площадь цилиндра
# 	"""
# 	return 2 * m.pi * r * (r + h)
#
#
# print(cylinder(2, 4))

# 17 Занятие


# print(ord("a"))
# print(ord("#"))
# print(ord("к"))
#
# while True:
# 	n = input("->")
# 	if n != "-1":
# 		print(ord(n))
# 	else:
# 		break


# my_str = "Test string for me"
# arr = [ord(x) for x in my_str]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr += [x for x in [ord(x) for x in input("->")[:3]] if x not in arr]
# print(arr)
# if arr [-1] in arr[:-1]:
# 	print("Количество последних элементов:", arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)


# print(chr(97))
# print(chr(7897))
# print(chr(47))

# a = 122
# b = 97
#
# for i in range(b, a + 1):
# 	print(chr(i), end=" ")

# a = 122
# b = 97
#
# if a > b:
# 	for i in range(b, a + 1):
# 		print(chr(i), end=" ")
# else:
# 	for i in range(a, b + 1):
# 		print(chr(i), end=" ")


# print("apple" == "Apple")
# print("apple" > "Apple")  # 97 > 65


# from random import  randint
#
# short = 7
# longest = 12
# min_ascii = 33
# max_ascii = 126
#
#
# def random_password():
# 	random_length = randint(short, longest)
# 	res = ""
# 	for i in range(random_length):
# 		random_char = chr(randint(min_ascii, max_ascii))
# 		res += random_char
# 	return res
#
#
# print("Ваш случайный пароль:", random_password())

#
# s = "hello, WORLD! I am learn Python."
# print(s.capitalize())  # Hello, world! i am learn python.
# print(s.lower())   # hello, world! i am learn python.
# print(s.upper())  # HELLO, WORLD! I AM LEARN PYTHON.
# print(s.swapcase())  # HELLO, world! i AM LEARN pYTHON.
# print(s.title())  # Hello, World! I Am Learn Python.


# s = "hello, WORLD! I am learn Python."
# print(s.count("h", 1, -4))  # количество искомых символов
# print(s.find("Python"))   # возвращает индекс первого совпадения
# print(s.find("oPython"))  # если подстроки нет, возвращается -1


# string = "один два"
# one = string[:string.find(" ")]
# two = string[string.find(" ") + 1:]
# print(two + " " + one)


# s = 'ab12c59p7dq'
# digits = []
#
# for symbol in s:
#     if '0123456789'.find(symbol) != -1:
#         digits.append(int(symbol))
# print(digits)
#
# s = "hello, WORLD! I am learn Python."
# print(s.index("Python"))
# # print(s.index("oPython"))

# s = "Дана строка сим(волов, среди которых ес)ть одна окрывающаяся"
# ind1 = s.index("(")
# ind2 = s.index(")")
# print(ind1)
# print(ind2)
#
# print(s[ind1+1:ind2])

# s = "hello, WORLD! i am learn Python."
# print(s.find("l"))
# print(s.rfind("l"))
# print(s.index("l"))
# print(s.rindex("l"))
#
# s = "Some content in this message has been blocked because the sender isn`t in your Safe senders list"
# item = "o"
# if s.count(item) == 1:
# 	print(s.find(item))
# elif s.count(item) >= 2:
# 	print(s.find(item), s.rfind(item))

# s = "hello, WORLD! I am learn Python."
# print(s.endswith("on."))
# print(s.endswith("lo", 3, 5))
#
# print(s.startswith("hello"))
# print(s.startswith("I am", 14))

# print("aab123".isalnum())  # не пустая и состоит из букв и цифр
# print("45%6".isalnum())  #
#
# print("ABCabc".isalpha())  # не пустая и содержит только буквы
# print("123abc".isalpha())
#
# print("123".isdigit())  # не пустая и содержит только цифры
# print("ывав1".isdigit())
#
# print('abc'.islower())  # не пустая и содержит только буквенные символы в нижнем регистре,
# # также может содержать спецсиволв и цифры
# print('abc@98AS'.islower())
#
# print('ABC'.isupper())  # не пустая и содержит только буквенные символы в нижнем регистре,
# # также может содержать спецсиволв и цифры
# print('ABC1^q'.isupper())
#
# print(' \t \n'.isspace()) # строка состоит только из пробельных символов + табуляция и перенос на другую строку
# print(' a '.isspace())


# print('py'.center(10))
# print('py'.center(11, "-"))
# print('py'.center(24, ">"))


# print("   py".lstrip())  # py
# print("py   ".rstrip())  # py
# print("   py   ".strip())  # py
#
# print("https://www.python.org".lstrip("th/sp"))
# print('$py.$$$;'.rstrip(';$.'))
# print('$py.$$$;'.strip(';$.'))
#
# print("https://www.python.org/".lstrip("th/sp:").rstrip("/.org"))

# srt1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования. New"
# print(srt1.replace("Nython", "Python", 2))

# s = "-"
# seq = ('a', 'b', 'c')
# print(s.join(seq))  # a-b-c
#
# print("..".join(['1', '2']))
# print(":".join("Hello"))


# print('Строка разделенная пробелами'.split())
# print('www.python.org.ru'.split(".", 2))
# print('www.python.org.ru'.rsplit("."))
# print('www...python...org'.split("."))

# a = input("->").split()
# print(a)
# def name(name):
# 	  print(f"{name[0]} {name[1][0]}. {name[2][0]}.")
#
#
# a = input("Введите ФИО: ").split()
# name(a)

# s = "В строке заменить пробелы символом"
# # lst = s.split()
# # print(lst)
# # st = "*".join(lst)
# # print(st)
#
# print(s.replace(" ", "*"))

# 18 Занятие

# s = """Ежевику для ежат
# Принесли два ежа.
# Ежевику еле-еле
# Ежата возле ели съели."""
#
# up = s.count("Е")
# down = s.count(" е")
# # print(up)
# # print(down)
# e = up + down
# print("Количество слов:", e)

# Регулярные выражения

import re

# s = "Я ищу сов[паден]ия в 2021 го-да. И я их найду в 2 счёта. 45678"
# # reg = r'[201]'
# # print(s.find(reg))
# # print(re.findall(reg, s))  # возвращает список, содержащий все совпадение
# # print(re.search(reg, s))  # возвращает первый найденный элемент
# # print(re.search(reg, s).span())  # (15, 16)
# # print(re.search(reg, s).start())  # 15
# # print(re.search(reg, s).end())  # 16
# # print(re.search(reg, s).group())  # я
# #
# # print(re.match(reg, s))  # для поиска по заданному шаблону
#
#
# # print(re.split(reg, s))
# # print(re.split(reg, s, 1))
#
# # print(re.sub(reg, "!", s, 1))
#
# # [] - любой из символов
# # print(re.findall(reg, s))
# #
# reg = r'[А-яё.[\]-]'
# print(re.findall(reg, s))

# s = "Еда, беду, победа"
# reg = '[Ее]д[ау]'
# print(re.findall(reg, s))


# s = "Я ищу совпадения в 2021 го-да. И я их найду в 2 счёта. 45678"
# reg = r'[^0-9]'
# # [^abc] - вернет все, за исключением abc
# print(re.findall(reg, s))

# s = "Час в 24-часовом формате от 00 до 23. 2021-06-15Т21:40. Минуты, в диапозоне от 00 до 59ю 2021-06-15Т01:09."
# reg = "[0-2][0-9]:[0-5][0-9]"
# print(re.findall(reg, s))

# s = "Я ищу совпадения в 2021 го-да. И \t из найду в 2 счёта. \n 45678"
# reg = r'20*'
# # \d - одна цифра [0-5]
# # \w - цифра, буква, символ _ [0-9A-яА-z]
# # \s - пробельный символ (включая табуляция и перенос строки)
# # \D - все кроме цифр [0-5]
# # \W - все кроме цифр, букв, символа _ [0-9A-яА-z]
# # \S - все кроме пробельного символа (включая табуляция и перенос строки)
# print(re.findall(reg, s))
# + - от 1 до бесконечности повторений
# * - от 0 до бесконечности повторений
# ? - 0 или 1

#
# d = "Цифры: 7, +17, -42, 0.01.3, 0.3"
# reg1 = r'[+-]?[\d.]+'
# print(re.findall(reg1, d))

# s = "05-03-1987 # Дата рождения"
# print("Дата рождения:", re.sub("#.*", "", s))
#
# # 05-03-1987
#
# print("Дата рождения:", re.sub("-", ".",  re.sub("#.*", "", s)))
#
# s = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831"
# # reg = r"\w+\s*=\s*[^;]+"
# reg = r'[^;]+'
# print(re.findall(reg, s))


# s = "12 сентября 2021 года 789"
# reg = r"\d{2,4}"
# print(re.findall(reg, s))

# s = "+7 499 456-45-78, +74994564578, 7(499) 456 45 78, 74994564578"
# reg = r"\+?7\d{10}"
# print(re.findall(reg, s))

#
# s = "Я ищу совпадения в 2021 го-да. И я их найду в 2 счё_та"
# # reg = r'^\w+\s\w+'
# reg = r'\w+\s\w+$'
# print(re.findall(reg, s))

# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + q', flags=re.ASCII))  # только анг.символы
# print(re.findall(r'[0-9] +[^А-я]+', '12 + й'))
#
# text = 'hello world'
# print(re.findall(r'\w+', text, flags=re.DEBUG))

# s = "Я ищу совпадения в 2021 го-да. И \tя их найду в 2 счё_та"
# reg = r'Я'
# print(re.findall(reg, s, re.IGNORECASE))

# text = """
# one
# two
# """
# # print(re.findall(r'one.\w+', text))
# # print(re.findall(r'one.\w+', text, flags=re.DOTALL))
# print(re.findall(r'one$', text))
# print(re.findall(r'one$', text, flags=re.MULTILINE))

# print(re.findall("""[a-z.-]+@[a-z.-]+""", 'text@mail.ru'))

# print(re.findall("""
# [a-z.-]+ # part1
# @        #@
# [a-z.-]+ #past2
# """, 'text@mail.ru', re.VERBOSE))


# 19 занятие

# text = """Python,
# python,
# PYTHON"""
# reg = "(?im)^python"
# print(re.findall(reg, text))

# def validate_name(name):
#     return re.findall(r'^[\w-]{3,16}$', name, re.IGNORECASE)
#
#
# print(validate_name('Python_master'))
# print(validate_name('Python_ma5st#er'))


# greedy - захватывает максимально возможное число символов
# ? - lazy - захватывает минимально возможное число символов

# *?, +?, ??
# {m,n}?, {,n}?, {m,}?

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall('<.*?>', text))

# s = "<p>Изображение <img alt='картинка' src='bg.jpg' width='100'> - фон страницы</p>"
# # reg = '<img[^>]*>'
# reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'
# print(re.findall(reg, s))
#

# text = "Методы этой группы[16] выполняют[17] преобразование регистра[18][19] строки"
# print(re.findall(r'\[.*?]', text))


# s = "Петр и Виталий отлично учатся"
# reg = 'Петр|Ольга|Виталий'
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0, double = 8.0f"
# # reg = r"(?:int|float)\s*=\s*\d[.\w+]*"
# reg = r"(?:int|float)\s*=\s*(\d[.\w+]*)"
# print(re.findall(reg, s))

# (?:  ...) - обозначет, что эта группирующая скобка является не сохраняющей

# s = '127.0.0.1'
# #s = '192.255.255.255'
# # reg = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# # reg = r'(?:\d{1,3}.){3}(?:\d{1,3})'
# reg = r'(?:\d{1,3}.){3}\d{1,3}'
# print(re.findall(reg, s))

# s = "Word2016, PS6, AI5"
# reg = r'[a-z]+\d*'
# print(re.findall(reg, s, re.I))

# s = "5 + 7*2 - 4"
# reg = r'\s*([+*-])\s*'
# print(re.split(reg, s))


# a = "31-12-2000"
# reg = "(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])"
# print(re.findall(reg, a))


# s = "Я ищу совпадения в 2021 года. И я из найду в 2 счёта"
# reg = r'([0-9]+)\s(\D+)'
# print(re.search(reg, s).group())
# # m = re.search(reg, s)
# # print(m[0])
# # print(m[1])
# # print(m[2])
# # print(re.findall(reg, s))
# print(re.search(reg, s).group(1))
# print(re.search(reg, s).group(2))

# text = """
# Самара
# Москва
# Сочи
# Тверь
# Уфа
# Казань
# """
# count = 0
#
#
# def replace_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print("<select>")
# print(re.sub(r'\s*(\w+)\s*', replace_find, text))
# print("</select>")


# s = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
# # reg = r'<img\s+[^>]*src=([\'"])(.+)\1>'
# reg = r'<img\s+[^>]*(src=)(?P<q>[\'"])(.+)(?P=q)>'
# # (?P<name>)  (?P=name)
# print(re.findall(reg, s))


# s = "Самолет прилетает 10/23/2022. Будем рады вас видеть после 10/24/2022"
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# # print(re.findall(reg, s))
# print(re.sub(reg, r"\2.\1.\3", s))

# s = "google.com and google.ru"
# reg = r"(([a-z0-9-]{2,}\.)+[a-z]{2,4})"
# # print(re.findall(reg, s))
# print(re.sub(reg, r"http://\1", s))

def validate_phone(name):
    reg = r"^\+?7[ (]*\d+[ )]*[\d -]{8,10}$"
    return re.search(reg, name).group()


print(validate_phone('+7 499 456-45-78'))
print(validate_phone('+74994564578'))
print(validate_phone('7 (499) 456 45 78'))
print(validate_phone('7 (499) 456-45-78'))
