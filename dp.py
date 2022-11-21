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

import json
from random import choice


def gen_person():
	name = ''
	tel = ''
	
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
	nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	
	while len(name) != 7:
		name += choice(letters)
	
	while len(tel) != 10:
		tel += choice(nums)
	
	person = {
		'name': name,
		'tel': tel
	}
	return person, tel


def write_json(person_dict, num):
	try:
		data = json.load(open('persons.json'))
	except FileNotFoundError:
		data = {}

	data[num] = person_dict

	with open('persons.json', 'w') as f:
		json.dump(data, f, indent=2)


for i in range(5):
	write_json(gen_person ()[0], gen_person ()[1])

