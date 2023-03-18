from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from school.database import Base

association_table = Table('association', Base.metadata, Column('item_id', Integer, ForeignKey('items.id')),
						   Column ('cool_room_id', Integer, ForeignKey ('cool_room.id')))


class Items(Base):
	__tablename__ = 'items'
	
	id = Column(Integer, primary_key=True)
	item_title = Column(String(250), nullable=False)
	cool_room = relationship('Cool_room', secondary=association_table, backref='cool_room_lesson')
	
	def __repr__(self):
		return f"Предмет (ID: {self.id}, Название: {self.item_title})"