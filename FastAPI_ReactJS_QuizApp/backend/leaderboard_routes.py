from typing import Final
from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from database import Session, engine
from models import Ruler, FinalResult, User
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder

leaderboard_router = APIRouter(
    prefix = "/leaderboard",
    tags = ["leaderboard"]
)

session = Session(bind = engine)

@leaderboard_router.get("/hello")
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

@leaderboard_router.get("/{id}")
async def get_leaderboard_by_exam_id(id:int, Authorize:AuthJWT = Depends()):
    """
        ## Get leaderboard by university ID (uni_id)
        This returns final result by university ID and is only accessed by superuser
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
        res = session.execute(
            f"""
                select 
                    distinct(usr.email), 
                    usr.fullname, 
                    usr.phonenumb, 
                    usr.mssv, 
                    fr.datetime, 
                    fr.score 
                from finalresult fr, userbot usr, uni u 
                where fr.user_id = usr.id and u.id = fr.uni_id and u.id = {id}
                order by fr.score desc;
            """
        )

        response = []
        
        for r in res:
            response.append(dict(r))

        return jsonable_encoder(response)


    raise HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "User not allowed to carry out request"
    )
