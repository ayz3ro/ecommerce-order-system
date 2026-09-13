from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.dependencies import get_auth_service
from schemas.auth import LoginRequest, LoginResponse, RegisterRequest, RegisterResponse
from services.auth import AuthService

router = APIRouter()


@router.post("/login", response_model=LoginResponse, summary="User Authentication", tags=["Authentication"], )
def login(request: LoginRequest, auth_service: Session = Depends(get_auth_service), ) -> LoginResponse:
    return auth_service.authenticate_user(email=request.email, password=request.password, )


@router.post("/register", response_model=RegisterResponse, summary="User Registration", tags=["Authentication"], )
def register(request: RegisterRequest, auth_service: AuthService = Depends(get_auth_service), ):
    return auth_service.register_user(email=request.email, password=request.password, )
