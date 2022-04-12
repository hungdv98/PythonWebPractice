from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from database import Session, engine
#from schemas import UserModel
#from models import Uni, Ruler, User
from fastapi_jwt_auth import AuthJWT
#from fastapi.encoders import jsonable_encoder

user_router = APIRouter(
    prefix = "/user",
    tags = ["user"]
)

session = Session(bind = engine)

@user_router.get("/hello")
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

# @uni_router.post("/", 
#     status_code = status.HTTP_201_CREATED
# )
# async def create_a_university(uni:UniModel, Authorize:AuthJWT = Depends()):
#     """
#         ## Create a university
#         This requires the following
#         - uniname : str
#     """
#     try:
#         Authorize.jwt_required()
#     except Exception as e:
#         raise HTTPException(
#             status_code = status.HTTP_401_UNAUTHORIZED,
#             detail = "Invalid Token"
#         )
    
#     current_ruler = Authorize.get_jwt_subject()
#     ruler = session.query(Ruler).filter(Ruler.rulername == current_ruler).first()

#     if ruler:
#         new_uni = Uni(
#             uniname = uni.uniname
#         )
      
#         session.add(new_uni)
#         session.commit()

#         response = {
#             "uniname": new_uni.uniname,
#         }
      
#         return jsonable_encoder(response)

#     raise HTTPException(
#         status_code = status.HTTP_401_UNAUTHORIZED,
#         detail = "User not allowed to carry out request"
#     )