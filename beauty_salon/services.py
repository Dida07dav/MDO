from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from beauty_salon.database import Base


class Services(Base):
	__tablename__ = 'services'
	
	id = Column(Integer, primary_key=True)
	service_title = Column(String(250), nullable=False)
	price = relationship('Price')
	
	def __repr__(self):
		return f"Сервис (ID: {self.id}, Название: {self.service_title})"