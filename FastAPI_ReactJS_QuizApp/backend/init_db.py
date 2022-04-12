from database import engine, Base 
from models import Ruler

Base.metadata.create_all(bind=engine)