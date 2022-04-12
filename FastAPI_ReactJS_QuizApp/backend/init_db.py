from database import engine, Base 
from models import Ruler, Uni, Exam, Question, User

Base.metadata.create_all(bind=engine)