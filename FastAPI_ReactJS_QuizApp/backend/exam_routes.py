from fastapi import APIRouter, status, Depends, Response
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

@exam_router.get("/")
async def list_all_exams(Authorize:AuthJWT = Depends()):
    """
        ## List all exams
        This lists all exams made. It can be accessed by superusers
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

    if ruler:
        exams = session.query(Exam).all()
        return jsonable_encoder(exams)
    raise HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "You are not superuser"
    )

@exam_router.get("/{id}")
async def get_exam_by_id(id:int, Authorize:AuthJWT = Depends()):
    """
        ## Get an exam by its ID
        This gets an exam by its ID and is only accessed by superuser
    """
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid Token"
        )
    
    ruler = Authorize.get_jwt_subject()

    current_ruler = session.query(Ruler).filter(Ruler.rulername == ruler).first()

    if current_ruler:
        exam = session.query(Exam).filter(Exam.id == id).first()
        return jsonable_encoder(exam)
    raise HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "User not allowed to carry out request"
    )

@exam_router.put("/update/{id}")
async def update_an_exam(id:int, exam:ExamModel, Authorize:AuthJWT = Depends()):
    """
        ## Updating an exam
        This updates an exam and requires the following fields
        - exam_name : str
        - uni_id : int
    """
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid Token"
        )
    
    exam_to_update = session.query(Exam).filter(Exam.id == id).first()

    exam_to_update.exam_name = exam.exam_name
    exam_to_update.uni_id = exam.uni_id

    session.commit()

    response = {
        "exam_name": exam_to_update.exam_name,
        "uni_id": exam_to_update.uni_id
    }

    return jsonable_encoder(response)

@exam_router.delete("/delete/{id}",
    status_code = status.HTTP_204_NO_CONTENT
)
async def delete_an_exam(id:int, Authorize:AuthJWT = Depends()):
    """
        ## Delete an exam
        This deletes an exam by its id
    """
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid Token"
        )
    
    exam_to_delete = session.query(Exam).filter(Exam.id == id).first()
    examName = exam_to_delete.exam_name

    try:        
        session.delete(exam_to_delete)
        session.commit()
        return Response(status_code = status.HTTP_204_NO_CONTENT)
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_204_NO_CONTENT,
            detail = f"Failed to delete {examName} with error {e}"
        )