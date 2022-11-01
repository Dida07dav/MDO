class Statement:
	def check_info(self, employees):
		print('Расчет заработной платы')
		print('=' * 50)
		for employee in employees:
			print(f'Заработная плата:  {employee.cod} - {employee.name}')
			print(f'- Проверить сумму: {employee.check_info ()}')
			print('')

