# Давыдова Лидия Викторовна
#  Python 225
# 33 Занятие
#
from sistem import employee, salary, dz


salary_employee = employee.SalaryEmp(1, "Валерий Задорожный", 1500)
hourly_employee = salary.HourlyEmp(2, "Илья Кромин", 300, 2)
commission_employee = salary.CommissionEmp(3, "Николай Хорольский", 1000, 250)
payroll = dz.Statement()
payroll.check_info([
		salary_employee,
		hourly_employee,
		commission_employee
])
