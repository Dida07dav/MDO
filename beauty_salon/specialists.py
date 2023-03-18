from sqlalchemy import Column, ForeignKey, Integer, String

from beauty_salon.database import Base


class Specialists (Base):
	__tablename__ = 'specialists'
	
	id = Column(Integer, primary_key=True)
	hairdresser = Column(String(250), nullable=False)
	manicure = Column(String(250), nullable=False)
	beautician = Column(String(250), nullable=False)
	age = Column(Integer)
	price = Column(Integer, ForeignKey('price.id'))
	
	def __init__(self, special_name, age, id_price):
		self.hairdresser = special_name[0]
		self.manicure = special_name[1]
		self.beautician = special_name[2]
		self.age = age
		self.price = id_price
		
	def __repr__(self):
		return f"Специалисты({self.hairdresser} {self.manicure} {self.beautician}," \
			   f"Возраст: {self.age}, ID группы: {self.price})"