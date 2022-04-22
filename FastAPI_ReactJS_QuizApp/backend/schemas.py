from pydantic import BaseModel
from typing import Optional, List

class SignUpModel(BaseModel):
    id:Optional[int]
    rulername:str
    email:str
    password:str
    is_active:Optional[bool]

    class Config:
        orm_mode = True 
        schema_extra = {
            "example": {
                "rulername":"rulername",
                "email":"email@gmail.com",
                "password":"abcabc123",
                "is_active":True
            }
        }

class Settings(BaseModel):
    authjwt_secret_key:str = '87b9b87947910d7165d85188b23ac363b3ab31c3d7f9a3b98db700555d562cb0'

class LoginModel(BaseModel):
    email:str
    password:str

class UniModel(BaseModel):
    uniname:str

class UserModel(BaseModel):
    id:Optional[int]
    fullname:str
    mssv:str
    major:str
    email:str
    phonenumb:str
    jobpos:str
    uni_id:Optional[int]

class QuestionModel(BaseModel):
    id:Optional[int]
    question_name:str
    opt1:str
    opt2:str
    opt3:str
    opt4:str
    correct:int
    exam_id:int

    class Config:
        orm_mode = True 

class ExamModel(BaseModel):
    id:Optional[int]
    exam_name:str
    uni_id:int

    class Config:
        orm_mode = True 

class FinalResult(BaseModel):
    id:Optional[int]
    user_id:int 
    exam_id:int
    uni_id:int
    datetime:str 
    score:str

    class Config:
        orm_mode = True

class SubmitAns(BaseModel):
    user_id:int
    ans: List[dict] = []

    class Config:
        orm_mode = True