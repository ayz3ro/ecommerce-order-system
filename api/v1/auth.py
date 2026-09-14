from typing import Annotated

from fastapi import APIRouter, Depends, status

from api.dependencies import get_auth_service
from schemas.auth import (LoginRequest, LoginResponse, RegisterRequest, RegisterResponse, )
from services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["Authentication"], )

AuthServiceDependency = Annotated[AuthService, Depends(get_auth_service),]


@router.post("/login", response_model=LoginResponse, summary="User Authentication", )
def login(request: LoginRequest, auth_service: AuthServiceDependency, ) -> LoginResponse:
    return auth_service.authenticate_user(email=request.email, password=request.password, )


@router.post("/register", response_model=RegisterResponse, status_code=status.HTTP_201_CREATED,
    summary="User Registration", )
def register(request: RegisterRequest, auth_service: AuthServiceDependency, ) -> RegisterResponse:
    return auth_service.register_user(email=request.email, password=request.password, )
