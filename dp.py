# Давыдова Лидия Викторовна
#  Python 225
# Задание

# # №1

print((lambda x, y: x * y * 5)(2, 5))

# или

sum = lambda a=2, b=5, c=5: a * b * c
print(sum())

# №2

students = [
	{'name': 'Jennifer', 'final': 95},
	{'name': 'David', 'final': 92},
	{'name': 'Nikolas', 'final': 98},
]
res1 = sorted(students, key=lambda std: std['name'])
print(res1)
res2 = sorted(students, key=lambda std: std['final'], reverse=True)
print(res2)

# №3

students = [
	{'name': 'Jennifer', 'final': 95},
	{'name': 'David', 'final': 92},
	{'name': 'Nikolas', 'final': 98},
]
res1 = max(students, key=lambda std: std['name'])
print(res1)
res2 = min(students, key=lambda std: std['name'])
print(res2)

# №4

nums = [3, 5, 7, 3, 9, 5, 7, 2]
summa1 = list(map(lambda x: x**2, nums))
summa2 = list(map(lambda x: x**3, nums))
print(summa1)
print(summa2)


