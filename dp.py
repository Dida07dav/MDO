# Давыдова Лидия Викторовна
#  Python 225
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

#2
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

#3
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
# from math import sqrt
#
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

#27 Задание

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


class Student:
    def __init__(self, name):
        self.name = name
        self.md = self.Notebook()
        self.nt = self.Notebook1()
        
    def display(self):
        print(f'{self.name} =>', end="")

    class Notebook:
        def __init__(self):
            self.model = "HP"
            self.processor = "i7"
            self.memory = 16

        def display(self):
            print(f" {self.model}, {self.processor}, {self.memory}")

    class Notebook1:
        def __init__(self):
            self.model = "HP"
            self.processor = "i7"
            self.memory = 16

        def display(self):
            print(f" {self.model}, {self.processor}, {self.memory}")


outer = Student("Roman")
outer.display()
d1 = outer.md
d1.display()

outer = Student("Vladimir")
outer.display()
d2 = outer.nt
d2.display()


        
