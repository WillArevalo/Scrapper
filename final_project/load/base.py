from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base ## Importamos propiedades como un ORM
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///newspaper.db')

Session = sessionmaker(bind=engine)

Base = declarative_base()