from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from school.database import Base


class Cool_room (Base):
	__tablename__ = 'cool_room'
	
	id = Column(Integer, primary_key=True)
	cool_name = Column(String(250), nullable=False)
	student = relationship('Student')
	
	def __repr__(self):
		return f"Класс (ID : {self.id}, Название: {self.cool_name})"