from venv import create
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("postgresql://postgres:Abcd%401234@localhost:5432/pizza_order", echo = True)

Base = declarative_base()

Session = sessionmaker()