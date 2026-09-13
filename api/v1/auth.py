from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.dependencies import get_db
from repositories.users import UserRepository
from schemas.auth import LoginRequest, LoginResponse, RegisterRequest, RegisterResponse
from services.auth import AuthService

router = APIRouter()


@router.post("/login", response_model=LoginResponse, summary="User Authentication", tags=["Authentication"], )
def login(request: LoginRequest, db: Session = Depends(get_db), ) -> LoginResponse:
    user_repository = UserRepository(db)

    auth_service = AuthService(user_repository=user_repository, )

    access_token = auth_service.authenticate_user(email=request.email, password=request.password, )

    return LoginResponse(access_token=access_token, token_type="bearer", )


@router.post("/register", response_model=RegisterResponse, summary="User Registration", tags=["Authentication"], )
def register(request: RegisterRequest, auth_service: AuthService = Depends(get_auth_service), ):
    return auth_service.register_user(email=request.email, password=request.password, )
