class Employee:
	def __init__(self, cod, name):
		self.cod = cod
		self.name = name


class SalaryEmp(Employee):
	def __init__(self, cod, name, salary):
		super().__init__(cod, name)
		self.salary = salary

	def check_info(self):
		return self.salary