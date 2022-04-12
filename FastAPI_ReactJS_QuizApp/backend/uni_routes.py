from fastapi import APIRouter, status, Depends, Response
from fastapi.exceptions import HTTPException
from database import Session, engine
from schemas import UniModel
from models import Uni, Ruler
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder

uni_router = APIRouter(
    prefix = "/uni",
    tags = ["uni"]
)

session = Session(bind = engine)

@uni_router.get("/hello")
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

@uni_router.post("/", 
    status_code = status.HTTP_201_CREATED
)
async def create_a_university(uni:UniModel, Authorize:AuthJWT = Depends()):
    """
        ## Create a university
        This requires the following
        - uniname : str
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
        new_uni = Uni(
            uniname = uni.uniname
        )
      
        session.add(new_uni)
        session.commit()

        response = {
            "uniname": new_uni.uniname,
        }
      
        return jsonable_encoder(response)

    raise HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "User not allowed to carry out request"
    )


@uni_router.get("/")
async def list_all_universities(Authorize:AuthJWT = Depends()):
    """
        ## List all universities
        This lists all universities made. It can be accessed by superusers
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
        unis = session.query(Uni).all()
        return jsonable_encoder(unis)
    raise HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "You are not superuser"
    )

@uni_router.get("/{id}")
async def get_university_by_id(id:int, Authorize:AuthJWT = Depends()):
    """
        ## Get a university by its ID
        This gets a university by its ID and is only accessed by superuser
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
        uni = session.query(Uni).filter(Uni.id == id).first()
        return jsonable_encoder(uni)
    raise HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "User not allowed to carry out request"
    )

@uni_router.put("/update/{id}")
async def update_a_university(id:int, uni:UniModel, Authorize:AuthJWT = Depends()):
    """
        ## Updating a university
        This updates a university and requires the following fields
        - uniname : str
    """
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid Token"
        )
    
    uni_to_update = session.query(Uni).filter(Uni.id == id).first()

    uni_to_update.uniname = uni.uniname

    session.commit()

    response = {
        "uniname": uni_to_update.uniname,
    }

    return jsonable_encoder(response)

@uni_router.delete("/delete/{id}",
    status_code = status.HTTP_204_NO_CONTENT
)
async def delete_a_university(id:int, Authorize:AuthJWT = Depends()):
    """
        ## Delete a university
        This deletes a university by its id
    """
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid Token"
        )
    
    uni_to_delete = session.query(Uni).filter(Uni.id == id).first()
    uniName = uni_to_delete.uniname

    try:        
        session.delete(uni_to_delete)
        session.commit()
        return Response(status_code = status.HTTP_204_NO_CONTENT)
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_204_NO_CONTENT,
            detail = f"Failed to delete {uniName} with error {e}"
        )