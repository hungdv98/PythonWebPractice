from database import Base
from sqlalchemy import Column, Integer, Boolean, Text, String
from sqlalchemy.orm import relationship

"""
    class Ruler:
        id:int primary key
        username:str
        email:str
        password:str
        is_active:boolean
        exams:relationship
"""

class Ruler(Base):
    __tablename__ = "ruler"
    id = Column(Integer(), primary_key = True)
    rulername = Column(String(25), unique = True)
    email = Column(String(80), unique = True)
    password = Column(Text(), nullable = True)
    is_active = Column(Boolean(), default = False)
    exams = relationship("Exam", back_populates = "ruler")

    def __repr__(self):
        return f"<Ruler {self.rulername}>"

"""
    class User:

"""

"""
    class Exam:

"""

"""
    class Uni:

"""