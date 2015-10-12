from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

#TABLE INFORMATION ARE PLACED HERE.
class contact (base):
	__tablename__ = 'contact'
	id = Column(Integer, primary_key=True)
	name = Column(String(60))
	email = Column(String(60))
	messege = Column(String(120))
