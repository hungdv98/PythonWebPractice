from fastapi import APIRouter, status, Depends, Response
from fastapi.exceptions import HTTPException
from database import Session, engine
from schemas import UserModel
from models import Ruler, User
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder

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

@user_router.post("/", 
    status_code = status.HTTP_201_CREATED
)
async def create_new_user(user:UserModel):
    """
        ## Create new user
        This requires the following
        - fullname:str
        - mssv:str
        - major:str
        - email:str
        - phonenumb:str
        - uni_id:int
    """

    try:
        new_user = User(
            fullname = user.fullname,
            mssv = user.mssv,
            major = user.major,
            email = user.email,
            phonenumb = user.phonenumb,
            uni_id = user.uni_id
        )
      
        session.add(new_user)
        session.commit()

        response = {
            "fullname": new_user.fullname,
            "mssv": new_user.mssv,
            "major": new_user.major,
            "email": new_user.email,
            "phonenumb": new_user.phonenumb,
            "uni_id": new_user.uni_id,
            "id": new_user.id
        }
      
        return jsonable_encoder(response)

    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_204_NO_CONTENT,
            detail = f"Failed to create new user, error: {e}"
        )

@user_router.get("/")
async def list_all_users(Authorize:AuthJWT = Depends()):
    """
        ## List all users
        This lists all users made. It can be accessed by superusers
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
        users = session.query(User).all()
        return jsonable_encoder(users)
    raise HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "You are not superuser"
    )

@user_router.get("/{id}")
async def get_a_user_by_id(id:int, Authorize:AuthJWT = Depends()):
    """
        ## Get a user by its ID
        This gets a user by its ID and is only accessed by superuser
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
        user = session.query(User).filter(User.id == id).first()
        return jsonable_encoder(user)
    raise HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "User not allowed to carry out request"
    )

@user_router.put("/update/{id}")
async def update_a_user(id:int, user:UserModel, Authorize:AuthJWT = Depends()):
    """
        ## Updating a user
        This updates a user and requires the following fields
        - fullname:str
        - mssv:str
        - major:str
        - email:str
        - phonenumb:str
        - uni_id:int
    """
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid Token"
        )
    
    user_to_update = session.query(User).filter(User.id == id).first()

    user_to_update.uniname = user.fullname

    session.commit()

    response = {
        "fullname": user_to_update.fullname,
        "mssv": user_to_update.mssv,
        "major": user_to_update.major,
        "email": user_to_update.email,
        "phonenumb": user_to_update.phonenumb,
        "uni_id": user_to_update.uni_id
    }

    return jsonable_encoder(response)

@user_router.delete("/delete/{id}",
    status_code = status.HTTP_204_NO_CONTENT
)
async def delete_a_user(id:int, Authorize:AuthJWT = Depends()):
    """
        ## Delete a user
        This deletes a user by its id
    """
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid Token"
        )
    
    user_to_delete = session.query(User).filter(User.id == id).first()
    userName = user_to_delete.fullname

    try:        
        session.delete(user_to_delete)
        session.commit()
        return Response(status_code = status.HTTP_204_NO_CONTENT)
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_204_NO_CONTENT,
            detail = f"Failed to delete {userName} with error {e}"
        )