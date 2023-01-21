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
import json

data = {}


class CountryCapital:
    def __init__(self, country, capital):
        self.country = country
        self.capital = capital
        data[self.country] = self.capital

    def __str__(self):
        return f'{self.country}: {self.capital}'

    @classmethod
    def add_country(cls, new_country, new_capital, filename):

        data[new_country] = new_capital

        with open(filename, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    @classmethod
    def delete_country(cls, del_country, filename):
        if del_country in data:
            del data[del_country]

            with open(filename, "w") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        else:
            print("Такой страны в базе нет")

    @classmethod
    def search_data(cls, country, filename):
        if country in data:
            print(f"Страна {country} столица {data[country]} есть в словаре!")
        else:
            print(f"Страна {country} отсутствует в словаре")

    @classmethod
    def change_capital(cls, country, new_value, filename):

        if country in data:
            data[country] = new_value

            with open(filename, "w") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        else:
            print("Такой страны в базе нет")

    @classmethod
    def load_from_file(cls, filename):
        with open(filename, 'r') as f:
            print(json.load(f))


index = ''
# filename1 = 'list_capital.json'
# with open(filename1, "w") as fw:
#     json.dump(data, fw, indent=2, ensure_ascii=False)

while index != 6:
    try:
        print("*" * 40)
        index = int(input('Выбор действия:\n1 - добавление данных\n2 - удаление данных\n'
                          '3 - поиск данных\n4 - редактирование данных\n5 - просмотр данных\n'
                          '6 - завершение работы\nВвод: '))
        if index == 1:
            country_name = input("Введите название страны (с заглавной буквы): ")
            capital_name = input("Введите название столицы страны (с заглавной буквы): ")
            CountryCapital.add_country(country_name, capital_name, filename='list_capital.json')
            print("Файл сохранен!")
        if index == 2:
            country_name = input("Введите страну для удаления (с заглавной буквы): ")
            CountryCapital.delete_country(country_name, filename='list_capital.json')
        if index == 3:
            country_name = input("Введите название страны (с заглавной буквы): ")
            CountryCapital.search_data(country_name, filename='list_capital.json')
        if index == 4:
            country_name = input("Введите название страны столицу которой хотите изменить (с заглавной буквы): ")
            new_capital = input("Введите новое название столицы: ")
            CountryCapital.change_capital(country_name, new_capital, filename='list_capital.json')
            print("Файл сохранен!")
        if index == 5:
            CountryCapital.load_from_file(filename='list_capital.json')
    except IndexError:
        break
