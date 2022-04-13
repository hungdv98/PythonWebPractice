from email.policy import default
from database import Base
from sqlalchemy import Column, Integer, Boolean, Text, String, ForeignKey
from sqlalchemy.orm import relationship

"""
    class Ruler:
        id:int primary key
        username:str
        email:str
        password:str
        is_active:boolean
"""

class Ruler(Base):
    __tablename__ = "ruler"
    id = Column(Integer(), primary_key = True)
    rulername = Column(String(25), unique = True)
    email = Column(String(80), unique = True)
    password = Column(Text(), nullable = False)
    is_active = Column(Boolean(), default = False)

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
        uni_id:relationship
"""

class User(Base):
    __tablename__ = "userbot"
    id = Column(Integer(), primary_key = True)
    fullname = Column(String(80), unique = False)
    mssv = Column(String(25), unique = True)
    major = Column(String(80))
    email = Column(String(80), unique = True)
    phonenumb = Column(String(25), unique = True)
    uni_id = Column(Integer(), ForeignKey("uni.id"))

    def __repr__(self):
        return f"<User {self.mssv}>"

"""
    class FinalResult:
        id: int primary key
        datetime: str (format: yyyymmdd)
        user_id: relationship
        exam_id: relationship
        uni_id: relationship
        score: str
"""
class FinalResult(Base):
    __tablename__ = "finalresult"
    id = Column(Integer(), primary_key = True)
    datetime = Column(String(20), nullable = False)
    user_id = Column(Integer(), ForeignKey("userbot.id"))
    exam_id = Column(Integer(), ForeignKey("exam.id"))
    uni_id = Column(Integer(), ForeignKey("uni.id"))
    score = Column(String(), default = "0")

    def __repr__(self):
        return f"<FinalResult {self.id}>"

"""
    class Exam:
        id: int primary key
        exam_name: str
        ruler_id: relationship
        uni_id: relationship

"""
class Exam(Base):
    __tablename__ = "exam"
    id = Column(Integer(), primary_key = True)
    exam_name = Column(String(25), unique = True, nullable = False)
    ruler_id = Column(Integer(), ForeignKey("ruler.id"))
    uni_id = Column(Integer(), ForeignKey("uni.id"))

    def __repr__(self):
        return f"<Exam {self.exam_name}>"

"""
    class Question:
        id: int primary key
        question_name: str
        opt1: str
        opt2: str
        opt3: str
        opt4: str
        correct: int
        exam_id: int
        exams: relationship

"""
class Question(Base):
    __tablename__ = "question"
    id = Column(Integer(), primary_key = True)
    question_name = Column(String(80), unique = True, nullable = False)
    opt1 = Column(String(80), nullable = False)
    opt2 = Column(String(80), nullable = False)
    opt3 = Column(String(80), nullable = False)
    opt4 = Column(String(80), nullable = False)
    correct = Column(Integer(), nullable = False) 
    exam_id = Column(Integer(), ForeignKey("exam.id"))
    exam = relationship("Exam", backref= "question")

    def __repr__(self):
        return f"<Question {self.question_name}>"