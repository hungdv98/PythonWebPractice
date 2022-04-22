from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from database import Session, engine
from schemas import SubmitAns
from models import Question, FinalResult, Exam, User
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder
from helpers import check_not_passed, get_numb_diff_pair, get_time_format, parsing_score
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
    # listQues = session.query(
    #         Question.id,
    #         Question.question_name,
    #         Question.opt1,
    #         Question.opt2,
    #         Question.opt3,
    #         Question.opt4
    #     ).filter(Question.exam_id == id).all()

    listQues = session.execute(
        f"""
            SELECT 
                q.id,
                q.question_name,
                q.opt1,
                q.opt2,
                q.opt3,
                q.opt4
            FROM 
                question q 
            WHERE
                q.exam_id = {id}
            ORDER BY RANDOM()
            LIMIT 26;
        """
    )


    response = []
    
    for r in listQues:
        response.append(dict(r))

    return jsonable_encoder(response)
    #return jsonable_encoder(listQues)
    # return json.dumps(jsonable_encoder(listQues))

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

    score = 26
    numQues = score

    user_keys = [k["id"] for k in submit_ans.ans]
    correct_ans = [e for e in listAns if e["id"] in user_keys]
    user_ans_sorted = sorted(submit_ans.ans, key=lambda d: d['id'])


    if check_not_passed(correct_ans, user_ans_sorted):
        score -= get_numb_diff_pair(correct_ans, user_ans_sorted)

    username = session.query(User.fullname).filter(User.id == submit_ans.user_id).first()

    finalScore = FinalResult(
        datetime = get_time_format(),
        user_id = submit_ans.user_id,
        exam_id = id,
        uni_id = uni_id,
        score = parsing_score(score)+"/"+str(numQues)
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
        return {"message":f"{finalScore.score}"}
    
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_204_NO_CONTENT,
            detail = f"Failed to create result for user {username} with error {e}"
        )