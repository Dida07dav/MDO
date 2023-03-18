from faker import Faker

from school.database import create_db, Session
from school.items import Items
from school.student import Student
from school.cool_room import Cool_room


def create_database(load_fake_data=True):
	create_db()
	if load_fake_data:
		_load_fake_data(Session())


def _load_fake_data(session):
	lessons_names = ['Математика', 'Программирование', 'Линейная алгебра', 'Статистика', 'Физика']
	
	room1 = Cool_room(cool_name="ШК-7")
	room2 = Cool_room(cool_name="ШК-9")
	session.add(room1)
	session.add(room2)
	
	for key, it in enumerate(lessons_names):
		item = Items(item_title=it)
		item.cool_room.append(room1)
		if key % 2 == 0:
			item.cool_room.append(room2)
		session.add(item)
	
	faker = Faker('ru_RU')
	room_list = [room1, room2]
	session.commit()
	
	for _ in range(50):
		full_name = faker.name().split()
		age = faker.random.randint(7, 17)
		cool_room = faker.random.choice(room_list)
		student = Student (full_name, age, cool_room.id)
		session.add(student)
	
	session.commit()
	session.close()
	