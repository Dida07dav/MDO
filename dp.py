# Давыдова Лидия Викторовна
#  Python 225
# 33 Занятие

# from sistem import employee, salary, dz
#
#
# salary_employee = employee.SalaryEmp(1, "Валерий Задорожный", 1500)
# hourly_employee = salary.HourlyEmp(2, "Илья Кромин", 300, 2)
# commission_employee = salary.CommissionEmp(3, "Николай Хорольский", 1000, 250)
# payroll = dz.Statement()
# payroll.check_info([
# 		salary_employee,
# 		hourly_employee,
# 		commission_employee
# ])

# 34 Занятие

# import json
# from random import choice

#
# def gen_person():
# 	name = ''
# 	tel = ''
#
# 	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# 	nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
# 	while len(name) != 7:
# 		name += choice(letters)
#
# 	while len(tel) != 10:
# 		tel += choice(nums)
#
# 	person = {
# 		'name': name,
# 		'tel': tel
# 	}
# 	return person, tel
#
#
# def write_json(person_dict, num):
# 	try:
# 		data = json.load(open('persons.json'))
# 	except FileNotFoundError:
# 		data = {}
#
# 	data[num] = person_dict
#
# 	with open('persons.json', 'w') as f:
# 		json.dump(data, f, indent=2)
#
#
# for i in range(5):
# 	write_json(gen_person ()[0], gen_person ()[1])
#
# def gen_person():
# 	name = ''
# 	tel = ''
# 	num = ''
#
# 	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# 	nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
# 	while len (name) != 7:
# 		name += choice (letters)
#
# 	while len (tel) != 10:
# 		tel += choice (nums)
#
# 	while len(num) != 12:
# 		num += choice(nums)
#
# 	person = {num: {
# 		'name': name,
# 		'tel': tel
# 	}}
# 	return person
#
#
# def write_json(person_dict):
# 	try:
# 		data = json.load(open('persons.json'))
# 	except FileNotFoundError:
# 		data = {}
#
# 	data.update(person_dict)
#
# 	with open('persons.json', 'w') as f:
# 		json.dump(data, f, indent=4)
#
#
# for i in range(5):
# 	write_json(gen_person())

# 35 Задание
# import json
#
# data = {}
#
#
# class CountryCapital:
#     def __init__(self, country, capital):
#         self.country = country
#         self.capital = capital
#         data[self.country] = self.capital
#
#     def __str__(self):
#         return f'{self.country}: {self.capital}'
#
#     @classmethod
#     def add_country(cls, new_country, new_capital, filename):
#
#         data[new_country] = new_capital
#
#         with open(filename, "w") as f:
#             json.dump(data, f, indent=2, ensure_ascii=False)
#
#     @classmethod
#     def delete_country(cls, del_country, filename):
#         if del_country in data:
#             del data[del_country]
#
#             with open(filename, "w") as f:
#                 json.dump(data, f, indent=2, ensure_ascii=False)
#         else:
#             print("Такой страны в базе нет")
#
#     @classmethod
#     def search_data(cls, country, filename):
#         if country in data:
#             print(f"Страна {country} столица {data[country]} есть в словаре!")
#         else:
#             print(f"Страна {country} отсутствует в словаре")
#
#     @classmethod
#     def change_capital(cls, country, new_value, filename):
#
#         if country in data:
#             data[country] = new_value
#
#             with open(filename, "w") as f:
#                 json.dump(data, f, indent=2, ensure_ascii=False)
#         else:
#             print("Такой страны в базе нет")
#
#     @classmethod
#     def load_from_file(cls, filename):
#         with open(filename, 'r') as f:
#             print(json.load(f))
#
#
# index = ''
# # filename1 = 'list_capital.json'
# # with open(filename1, "w") as fw:
# #     json.dump(data, fw, indent=2, ensure_ascii=False)
#
# while index != 6:
#     try:
#         print("*" * 40)
#         index = int(input('Выбор действия:\n1 - добавление данных\n2 - удаление данных\n'
#                           '3 - поиск данных\n4 - редактирование данных\n5 - просмотр данных\n'
#                           '6 - завершение работы\nВвод: '))
#         if index == 1:
#             country_name = input("Введите название страны (с заглавной буквы): ")
#             capital_name = input("Введите название столицы страны (с заглавной буквы): ")
#             CountryCapital.add_country(country_name, capital_name, filename='list_capital.json')
#             print("Файл сохранен!")
#         if index == 2:
#             country_name = input("Введите страну для удаления (с заглавной буквы): ")
#             CountryCapital.delete_country(country_name, filename='list_capital.json')
#         if index == 3:
#             country_name = input("Введите название страны (с заглавной буквы): ")
#             CountryCapital.search_data(country_name, filename='list_capital.json')
#         if index == 4:
#             country_name = input("Введите название страны столицу которой хотите изменить (с заглавной буквы): ")
#             new_capital = input("Введите новое название столицы: ")
#             CountryCapital.change_capital(country_name, new_capital, filename='list_capital.json')
#             print("Файл сохранен!")
#         if index == 5:
#             CountryCapital.load_from_file(filename='list_capital.json')
#     except IndexError:
#         break

# 36 Задание
# import csv
# with open("data2.csv") as r_file:
#     file_reader = csv.reader(r_file, delimiter=";")
#     for row in file_reader:
#         print(row)
       
# 2 вариант


# data2 = [['hostname', 'vendor', 'model', 'location'],
#          ['sw1', 'Cisco', '3750', 'London'],
#          ['sw2', 'Cisco', '3850', 'Liverpool'],
#          ['sw3', 'Cisco', '3650', 'Liverpool'],
#          ['sw4', 'Cisco', '3650', 'London']]
#
# with open('data1_new.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=";", lineterminator='\r', quoting=csv.QUOTE_NONNUMERIC)
#     writer.writerows(data2)
#
# with open('data1_new.csv') as f:
#     print(f.read())

# 37 Задание

# from bs4 import BeautifulSoup
# import requests
# import re
# import csv
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def write_csv(data):
#     with open('supply.csv', 'a') as f:
#         writer = csv.writer(f, lineterminator="\r", delimiter=";")
#         writer.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find_all('section', class_="ms-blog-section-inner")[0]
#     supply = p1.find_all('article')
#
#     for supply1 in supply:
#         name = supply1.find("h3").text
#         url = supply1.find("h3").find("a").get('href')
#         rating = supply1.find("span", class_="ms-blog-item-date").text
#
#         data = {'name': name, 'url': url, 'rating': rating}
#         write_csv(data)
#
#
# def main():
#     url = "https://www.moysklad.ru/poleznoe/marketplejsy/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

# 38 Задание

# import json
#
# data = {"Россия": "Москва"}
#
#
# def load_data(func):
#     def wrap(*args, filename):
#         try:
#             data = json.load(open(filename))
#         except FileNotFoundError:
#             data = {}
#         func(*args, filename)
#         print("Файл сохранен")
#     return wrap
#
#
# class CountryCapital:
#     def __init__(self, country, capital):
#         self.country = country
#         self.capital = capital
#         data[self.country] = self.capital
#
#     def __str__(self):
#         return f'{self.country}: {self.capital}'
#
#     @classmethod
#     @load_data
#     def add_country(cls, new_country, new_capital, filename):
#
#         data[new_country] = new_capital
#
#         with open(filename, "w") as f:
#             json.dump(data, f, indent=2, ensure_ascii=False)
#
#     @classmethod
#     @load_data
#     def delete_country(cls, del_country, filename):
#
#         if del_country in data:
#             del data[del_country]
#
#             with open(filename, "w") as f:
#                 json.dump(data, f, indent=2, ensure_ascii=False)
#         else:
#             print("Такой страны в базе нет")
#
#     @classmethod
#     @load_data
#     def search_data(cls, country, filename):
#
#         if country in data:
#             print(f"Страна {country} столица {data[country]} есть в словаре!")
#         else:
#             print(f"Страна {country} отсутствует в словаре")
#
#     @classmethod
#     @load_data
#     def change_capital(cls, country, new_value, filename):
#
#         if country in data:
#             data[country] = new_value
#
#             with open(filename, "w") as f:
#                 json.dump(data, f, indent=2, ensure_ascii=False)
#         else:
#             print("Такой страны в базе нет")
#
#     @classmethod
#     def load_from_file(cls, filename):
#         with open(filename, 'r') as f:
#             print(json.load(f))
#
#
# index = ''
# filename1 = 'list_capital.json'
# with open(filename1, "w") as fw:
#     json.dump(data, fw, indent=2, ensure_ascii=False)
#
# while index != 6:
#     try:
#         print("*" * 40)
#         index = int(input('Выбор действия:\n1 - добавление данных\n2 - удаление данных\n'
#                           '3 - поиск данных\n4 - редактирование данных\n5 - просмотр данных\n'
#                           '6 - завершение работы\nВвод: '))
#         if index == 1:
#             country_name = input("Введите название страны (с заглавной буквы): ")
#             capital_name = input("Введите название столицы страны (с заглавной буквы): ")
#             CountryCapital.add_country(country_name, capital_name, filename='list_capital.json')
#         if index == 2:
#             country_name = input("Введите страну для удаления (с заглавной буквы): ")
#             CountryCapital.delete_country(country_name, filename='list_capital.json')
#         if index == 3:
#             country_name = input("Введите название страны (с заглавной буквы): ")
#             CountryCapital.search_data(country_name, filename='list_capital.json')
#         if index == 4:
#             country_name = input("Введите название страны столицу которой хотите изменить (с заглавной буквы): ")
#             new_capital = input("Введите новое название столицы: ")
#             CountryCapital.change_capital(country_name, new_capital, filename='list_capital.json')
#         if index == 5:
#             CountryCapital.load_from_file(filename='list_capital.json')
#     except IndexError:
#         break

# 39 Задание


