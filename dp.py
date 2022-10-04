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
from math import sqrt


class Rectangle:
    def __init__(self, lg, wd):
        self.__length = lg
        self.__width = wd

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_square(self):
        s = self.__length * self.__width
        print("Площадь прямоугольника: ", s)

    def perimetr(self):
        s1 = (self.__length + self.__width) * 2
        print("Периметр прямоугольника: ", s1)

    def hypotenuse(self):
        s2 = sqrt(self.__length ** 2 + self.__width ** 2)
        print("Гипотенуза прямоугольника: ", round(s2, 2))

    def figur(self):
        print(("*" * self.__width + "\n") * self.__length)


p = Rectangle(3, 9)
print("Длина прямоугольника: ", p.get_length())
print("Ширина прямоугольника: ", p.get_width())
p.get_square()
p.perimetr()
p.hypotenuse()
p.figur()


# 24 Задание

