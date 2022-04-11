from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from database import Session, engine
from schemas import SignUpModel, LoginModel
from models import Ruler
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder

auth_router = APIRouter(
    prefix = "/auth",
    tags = ["auth"]
)

session = Session(bind = engine)

@auth_router.get("/")
async def hello(Authorize:AuthJWT = Depends()):
    """
        ## Hello World route
    """
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid Token"
        )
    
    return {"message":"Hello World"}

#SignUp route
@auth_router.post("/signup",
    status_code = status.HTTP_201_CREATED
)
async def signup(Ruler:SignUpModel):
    """
        ## Create a Ruler
        This requires the following 
        ```
            rulername:str
            email:str
            password:str
            is_staff:bool
            is_active:bool
        ```
    """
    db_email = session.query(Ruler).filter(Ruler.email == Ruler.email).first()

    if db_email is not None:
        return HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Ruler with the email already exists"
        )
    
    db_rulername = session.query(Ruler).filter(Ruler.rulername == Ruler.rulername).first()

    if db_rulername is not None:
        return HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Ruler with the rulername already exists"
        )
    
    new_Ruler = Ruler(
        rulername = Ruler.rulername,
        email = Ruler.email,
        password = generate_password_hash(Ruler.password),
        is_active = Ruler.is_active,
        is_staff = Ruler.is_staff
    )

    session.add(new_Ruler)
    session.commit()

    return new_Ruler

#Login route
@auth_router.post("/login", status_code = 200)
async def login(Ruler:LoginModel, Authorize:AuthJWT=Depends()):
    """
        ## Login a Ruler
        This requires
            ```
                rulername:str
                password:str
            ```
        and returns a token pair `access` and `refresh`
    """
    db_ruler = session.query(Ruler).filter(Ruler.rulername == Ruler.rulername).first()

    if db_ruler and check_password_hash(db_ruler.password, Ruler.password):
        access_token = Authorize.create_access_token(subject = db_ruler.rulername)
        refresh_token = Authorize.create_refresh_token(subject = db_ruler.rulername)

        response = {
            "access": access_token,
            "refresh": refresh_token 
        }

        return jsonable_encoder(response)
    
    raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
        detail = "Invalid Rulername or Password"
    )

#Refresh token
@auth_router.get("/refresh")
async def refresh_token(Authorize:AuthJWT = Depends()):
    """
        ## Create a refresh token
        This creates a fresh token. It requires a refresh token.
    """
    try:
        Authorize.jwt_refresh_token_required()
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Please provide a valid refresh token"
        )
    
    current_ruler = Authorize.get_jwt_subject()
    
    access_token = Authorize.create_access_token(subject = current_ruler)

    return jsonable_encoder({
        "access": access_token
    })