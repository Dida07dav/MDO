# Давыдова Лидия Викторовна
#  Python 225
# 32 Занятие
#

class Side:
	def __set_name__(self, owner, name):
		self.name = name
	
	def __get__(self, instance, owner):
		return instance.__dict__[self.name]
	
	def __set__(self, instance, value):
		if value < 0:
			raise ValueError("Число не может быть отрицательным.")
		instance.__dict__[self.name] = value


class Triangle:
	a = Side()
	b = Side()
	s = Side()
	
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
	
	def existence(self):
		if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
			return "существует"
		else:
			return "не существует"
	
	def info(self):
		print(f"Треугольник со сторонами ({self.a}, {self.b}, {self.c}) {self.existence ()}")


t1 = [
	Triangle(2, 5, 6),
	Triangle(5, 2, 8),
	Triangle(7, 3, 6)]
for i in t1:
	i.info()

