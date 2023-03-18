from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_NAME = 'service.db'

promotion = create_engine(f'sqlite:///{DATABASE_NAME}')
Name_of_service = sessionmaker(bind=promotion)

Base = declarative_base()


def create_db():
	Base.metadata.create_all(promotion)