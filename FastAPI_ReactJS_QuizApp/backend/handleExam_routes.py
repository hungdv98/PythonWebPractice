from fastapi import APIRouter, status, Depends, Response
from fastapi.exceptions import HTTPException
from database import Session, engine
from schemas import SubmitAns
from models import Question, FinalResult, Exam, User
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder
from helpers import check_not_passed, get_numb_diff_pair, get_time_format
import json

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
    listQues = session.query(
            Question.id,
            Question.question_name,
            Question.opt1,
            Question.opt2,
            Question.opt3,
            Question.opt4
        ).filter(Question.exam_id == id).all()

    return jsonable_encoder(listQues)
    #return json.dumps(jsonable_encoder(listQues))

@gexam_router.post("/{id}",
    status_code = status.HTTP_201_CREATED
)
async def submit_exam(id:int, submit_ans:SubmitAns):
    """
        ## Submit exam from user
        This returns result, required fields:
        - user_id:int
        - correct: List[dict] = []
    """
    listAns = session.query(
            Question.id,
            Question.correct
        ).filter(Question.exam_id == id).all()
    listAns = jsonable_encoder(listAns)

    uni_id = session.query(
        Exam.uni_id
    ).filter(Exam.id == id).first()
    uni_id = jsonable_encoder(uni_id)["uni_id"]

    score = len(listAns)
    numQues = score

    if check_not_passed(listAns, submit_ans.ans):
        score -= get_numb_diff_pair(listAns, submit_ans.ans)

    username = session.query(User.fullname).filter(User.id == submit_ans.user_id).first()

    finalScore = FinalResult(
        datetime = get_time_format(),
        user_id = submit_ans.user_id,
        exam_id = id,
        uni_id = uni_id,
        score = str(score)+"/"+str(numQues)
    )
    try:
        session.add(finalScore)
        session.commit()

        # response = {
        #     "datetime": finalScore.datetime,
        #     "user_id": finalScore.user_id,
        #     "exam_id": finalScore.exam_id,
        #     "uni_id": finalScore.uni_id,
        #     "score": finalScore.score
        # }
      
        # return jsonable_encoder(response)
        return {"message":"Congratulation!"}
    
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_204_NO_CONTENT,
            detail = f"Failed to create result for user {username} with error {e}"
        )