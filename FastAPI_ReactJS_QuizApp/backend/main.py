from fastapi import FastAPI
from auth_routes import auth_router
from uni_routes import uni_router
from user_routes import user_router
from exam_routes import exam_router
from question_routes import question_router
from handleExam_routes import gexam_router
from leaderboard_routes import leaderboard_router
from fastapi_jwt_auth import AuthJWT
from schemas import Settings
import inspect, re
from fastapi.routing import APIRoute 
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title = "Quiz App API",
        version = "1.0",
        description = "API for Uni Quiz",
        routes = app.routes
    )

    openapi_schema["components"]["securitySchemes"] = {
        "Bearer Auth": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": "Enter: **'Bearer &lt;JWT&gt;'**, where JWT is the access token"
        }
    }

    api_router = [route for route in app.routes if isinstance(route, APIRoute)]

    for route in api_router:
        path = getattr(route, "path")
        endpoint = getattr(route, "endpoint")
        methods = [method.lower() for method in getattr(route, "methods")]

        for method in methods:
            if (
                re.search("jwt_required", inspect.getsource(endpoint)) or
                re.search("fresh_jwt_required", inspect.getsource(endpoint)) or
                re.search("jwt_optional", inspect.getsource(endpoint))
            ):
                openapi_schema["paths"][path][method]["security"] = [
                    {
                        "Bearer Auth": []
                    }
                ]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

@AuthJWT.load_config
def get_config():
    return Settings()

app.include_router(auth_router)
app.include_router(uni_router)
app.include_router(exam_router)
app.include_router(question_router)
app.include_router(user_router)
app.include_router(gexam_router)
app.include_router(leaderboard_router)