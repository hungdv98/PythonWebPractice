from fastapi import APIRouter, status, Depends, Response
from fastapi.exceptions import HTTPException
from database import Session, engine
from schemas import ExamModel
from models import Question, Uni, Ruler, Exam
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder

gexam_router = APIRouter(
    prefix = "/gexam",
    tags = ["gexam"]
)

session = Session(bind = engine)

@gexam_router.get("/hello")
async def hello(Authorize:AuthJWT = Depends()):
    """
        ## Hello World route
        This returns Hello World
    """
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid Token"
        )
    return {"message":"Hello World"}

@gexam_router.get("/{id}")
async def get_exam(id:int):
    """
        ## Generate an exam for user
        This returns an exam, json format
    """
    exam = session.query(Exam).filter(Exam.id == id).first()

    listQues = session.query(Question).filter(Question.exam_id == id).all()
    #handler1 = jsonable_encoder(listQues)
    
    return jsonable_encoder(listQues)


