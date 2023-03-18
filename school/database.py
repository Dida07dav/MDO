from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_SCHOOL = 'school.db'

passage = create_engine(f'sqlite:///{DATABASE_SCHOOL}')
Session = sessionmaker(bind=passage)

Base = declarative_base()


def create_db():
	Base.metadata.create_all(passage)