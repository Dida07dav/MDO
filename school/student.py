from sqlalchemy import Column, ForeignKey, Integer, String

from school.database import Base


class Student (Base):
	__tablename__ = 'student'
	
	id = Column(Integer, primary_key=True)
	surname = Column(String(250), nullable=False)
	name = Column(String(250), nullable=False)
	patronymic = Column(String(250), nullable=False)
	age = Column(Integer)
	cool_room = Column(Integer, ForeignKey('cool_room.id'))
	
	def __init__(self, full_name, age, id_group):
		self.surname = full_name[0]
		self.name = full_name[1]
		self.patronymic = full_name[2]
		self.age = age
		self.group = id_group
	
	def __repr__(self):
		return f"Ученик(ФИО: {self.surname} {self.name} {self.patronymic}," \
			   f"Возраст: {self.age}, ID группы: {self.cool_room})"