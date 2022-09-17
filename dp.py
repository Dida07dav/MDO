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


def count_items(item_list):
	count = 0
	for item in item_list:
		if isinstance(item, list):
			count += count_items(item)
		else:
			count = count_items(item_list[1:])
			if item_list[0] < 0:
				count = count + 1
	return count


lst = [-2, 3, 8, -11, -4, 6]
n = count_items(lst)
print("n =", n)


# 2 Вариант

def Negativ(res):
	if res == []:
		return 0
	else:
		count = Negativ(res[1:])
		if res[0] < 0:
			count = count + 1
		return count


lst = [-2, 3, 8, -11, -4, 6]
n = Negativ(lst)
print("n =", n)
