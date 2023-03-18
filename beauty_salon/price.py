from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from beauty_salon.database import Base


class Price(Base):
	__tablename__ = 'price'
	
	id = Column(Integer, primary_key=True)
	price_list = Column(String(250), nullable=False)
	specialists = relationship('Specialists')
	
	def __repr__(self):
		return f"Прайс (ID : {self.id}, Цена: {self.price_list})"