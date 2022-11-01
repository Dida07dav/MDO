from sistem import employee


class SalaryEmp(employee.Employee):
	def __init__(self, cod, name, salary):
		super().__init__(cod, name)
		self.salary = salary

	def check_info(self):
		return self.salary
	

class HourlyEmp(employee.Employee):
	def __init__(self, cod, name, hours_worked, hour_rate):
		super().__init__(cod, name)
		self.hours_worked = hours_worked
		self.hour_rate = hour_rate

	def check_info(self):
		return self.hours_worked * self.hour_rate


class CommissionEmp(employee.SalaryEmp):
	def __init__(self, cod, name, salary, commission):
		super().__init__(cod, name, salary)
		self.commission = commission

	def check_info(self):
		fixed = super().check_info()
		return fixed + self.commission
