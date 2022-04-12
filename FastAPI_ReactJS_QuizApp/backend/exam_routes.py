from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from database import Session, engine
from schemas import ExamModel
from models import Uni, Ruler, Exam
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder

exam_router = APIRouter(
    prefix = "/exam",
    tags = ["exam"]
)

session = Session(bind = engine)

@exam_router.get("/hello")
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

@exam_router.post("/", 
    status_code = status.HTTP_201_CREATED
)
async def create_an_exam(exam:ExamModel, Authorize:AuthJWT = Depends()):
    """
        ## Create an exam
        This requires the following
        - exam_name:str
        - uni_id:int
    """
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid Token"
        )
    
    current_ruler = Authorize.get_jwt_subject()
    ruler = session.query(Ruler).filter(Ruler.rulername == current_ruler).first()
    print("[DEBUG] ruler id = ", ruler.id)
    if ruler:
        new_exam = Exam(
            exam_name = exam.exam_name,
            ruler_id = ruler.id,
            uni_id = exam.uni_id
        )
      
        session.add(new_exam)
        session.commit()

        response = {
            "exam_name": new_exam.exam_name,
            "ruler_id": new_exam.ruler_id,
            "uni_id": new_exam.uni_id
        }
      
        return jsonable_encoder(response)

    raise HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "User not allowed to carry out request"
    )