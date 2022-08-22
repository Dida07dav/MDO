# Давыдова Лидия Викторовна
#  Python 225
# Задание

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

# 2 вариант
studs = {}
student_people = int(input("Количество студентов: "))
s = 0
for i in range(student_people):
	people_name = input(str(i + 1) + "-й  студент: ")
	score = int(input("Балл: "))
	studs[people_name] = score
	s += score
a = s / student_people
print("\nСредний балл: %.0f. Студенты с баллом выше среднего: " % a)
for i in studs:
	if studs[i] > a:
		print(i)
