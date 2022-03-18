from pydantic import BaseModel
from typing import Optional

class SignUpModel(BaseModel):
    id:Optional[int]
    username:str
    email:str
    password:str
    is_staff:Optional[bool]
    is_active:Optional[bool]

    class Config:
        orm_mode = True 
        schema_extra = {
            "example": {
                "username":"username",
                "email":"email@gmail.com",
                "password":"abcabc123",
                "is_staff":False,
                "is_active":True
            }
        }

class Settings(BaseModel):
    authjwt_secret_key:str = '87b9b87947910d7165d85188b23ac363b3ab31c3d7f9a3b98db700555d562cb0'

class LoginModel(BaseModel):
    username:str
    password:str