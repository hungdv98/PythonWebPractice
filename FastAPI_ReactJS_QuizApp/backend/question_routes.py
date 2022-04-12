from fastapi import APIRouter, status, Depends, Response
from fastapi.exceptions import HTTPException
from database import Session, engine
from schemas import QuestionModel
from models import Question, Ruler
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder

question_router = APIRouter(
    prefix = "/question",
    tags = ["question"]
)

session = Session(bind = engine)

@question_router.get("/hello")
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

@question_router.post("/", 
    status_code = status.HTTP_201_CREATED
)
async def create_a_question(ques:QuestionModel, Authorize:AuthJWT = Depends()):
    """
        ## Create a question
        This requires the following
        - question_name : str
        - opt1 : str
        - opt2 : str
        - opt3 : str
        - opt4 : str
        - correct : int
        - exam_id : int
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
        new_ques = Question(
            question_name = ques.question_name,
            opt1 = ques.opt1,
            opt2 = ques.opt2,
            opt3 = ques.opt3,
            opt4 = ques.opt4,
            correct = ques.correct,
            exam_id = ques.exam_id
        )
      
        session.add(new_ques)
        session.commit()

        response = {
            "question_name": new_ques.question_name,
            "opt1": new_ques.opt1,
            "opt2": new_ques.opt2,
            "opt3": new_ques.opt3,
            "opt4": new_ques.opt4,
            "correct": new_ques.correct,
            "exam_id": new_ques.exam_id
        }
      
        return jsonable_encoder(response)

    raise HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "User not allowed to carry out request"
    )

@question_router.get("/")
async def list_all_questions(Authorize:AuthJWT = Depends()):
    """
        ## List all questions
        This lists all questions made. It can be accessed by superusers
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
        questions = session.query(Question).all()
        return jsonable_encoder(questions)
    raise HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "You are not superuser"
    )

@question_router.get("/{id}")
async def get_question_by_id(id:int, Authorize:AuthJWT = Depends()):
    """
        ## Get a question by its ID
        This gets a question by its ID and is only accessed by superuser
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
        question = session.query(Question).filter(Question.id == id).first()
        return jsonable_encoder(question)
    raise HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "User not allowed to carry out request"
    )

@question_router.put("/update/{id}")
async def update_a_question(id:int, ques:QuestionModel, Authorize:AuthJWT = Depends()):
    """
        ## Updating a question
        This updates a question and requires the following fields
        - question_name : str
        - opt1 : str
        - opt2 : str
        - opt3 : str
        - opt4 : str
        - correct : int
        - exam_id : int
    """
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid Token"
        )
    
    ques_to_update = session.query(Question).filter(Question.id == id).first()

    ques_to_update.question_name = ques.question_name
    ques_to_update.opt1 = ques.opt1
    ques_to_update.opt2 = ques.opt2
    ques_to_update.opt3 = ques.opt3
    ques_to_update.opt4 = ques.opt4
    ques_to_update.correct = ques.correct
    ques_to_update.exam_id = ques.exam_id

    session.commit()

    response = {
        "question_name": ques_to_update.question_name,
        "opt1": ques_to_update.opt1,
        "opt2": ques_to_update.opt2,
        "opt3": ques_to_update.opt3,
        "opt4": ques_to_update.opt4,
        "correct": ques_to_update.correct,
        "exam_id": ques_to_update.exam_id
    }

    return jsonable_encoder(response)

@question_router.delete("/delete/{id}",
    status_code = status.HTTP_204_NO_CONTENT
)
async def delete_a_question(id:int, Authorize:AuthJWT = Depends()):
    """
        ## Delete a question
        This deletes a question by its id
    """
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid Token"
        )
    
    ques_to_delete = session.query(Question).filter(Question.id == id).first()
    quesName = ques_to_delete.question_name

    try:        
        session.delete(ques_to_delete)
        session.commit()
        return Response(status_code = status.HTTP_204_NO_CONTENT)
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_204_NO_CONTENT,
            detail = f"Failed to delete {quesName} with error {e}"
        )