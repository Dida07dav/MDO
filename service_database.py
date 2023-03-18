from faker import Faker

from beauty_salon.database import create_db, Name_of_service
from beauty_salon.price import Price
from beauty_salon.services import Services
from beauty_salon.specialists import Specialists


def service_database(load_fake_data=True):
	create_db()
	if load_fake_data:
		_load_fake_data(Name_of_service())


def _load_fake_data(name_of_service):
	price_names = ['укладка - 1200', 'сушка - 500', 'мытье головы - 200',
					 'восстановление - 1500', 'покраска - 2700']
	
	price1 = Price(price_list="KM-1")
	price2 = Price(price_list="КM-2")
	name_of_service.add(price1)
	name_of_service.add(price2)
	
	for key, it in enumerate(price_names):
		services = Services(service_title=it)
		services.price.append(price1)
		if key % 2 == 0:
			services.price.append(price2)
		name_of_service.add(services)
	
	faker = Faker('ru_RU')
	price_list = [price1, price2]
	name_of_service.commit()
	
	for _ in range (50):
		special_name = faker.name().split()
		age = faker.random.randint(21, 45)
		price = faker.random.choice(price_list)
		specialists = Specialists(special_name, age, price.id)
		name_of_service.add(specialists)
	
	name_of_service.commit()
	name_of_service.close()
	