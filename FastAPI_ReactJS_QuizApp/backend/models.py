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
    #exams = relationship("Exam", back_populates = "ruler")

    def __repr__(self):
        return f"<Ruler {self.rulername}>"

"""
    class Uni:
        id: int primary key
        uniname:str
        is_active:boolean
"""

class Uni(Base):
    __tablename__ = "uni"
    id = Column(Integer(), primary_key = True)
    uniname = Column(String(80), unique = True)
    is_active = Column(Boolean(), default = True)

    def __repr__(self):
        return f"<Uni {self.uniname}>"

"""
    class Major:
        
"""

"""
    class User:
        id: int primary key
        fullname:str
        mssv:str
        major:str
        email:str
        phonenumb:str
        count:int
        score:int
"""

class User(Base):
    __tablename__ = "user"
    id = Column(Integer(), primary_key = True)
    fullname = Column(String(80), unique = False)
    mssv = Column(String(25), unique = True)
    major = Column(String(80))
    email = Column(String(80), unique = True)
    phonenumb = Column(String(25), unique = True)
    count = Column(Integer())
    score = Column(Integer())

    def __repr__(self):
        return f"<User {self.mssv}>"

"""
    class Exam:

"""

"""
    class Ques:

"""