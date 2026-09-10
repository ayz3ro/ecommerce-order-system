from fastapi import APIRouter

from repositories.users import UserRepository
from schemas.auth import LoginRequest, LoginResponse
from services.auth import AuthService

router = APIRouter()


@router.post(path="/login", summary="User Authentication",
             description="Endpoint for logging in. User enters email and password, "
                         "if the data is correct, a successful answer is returned.", response_model=LoginResponse,
             responses={200: {"description": "Login successful",
                              "content": {"application/json": {"example": {"message": "Login successful"}}}},
                        400: {"description": "Incorrect credentials",
                              "content": {"application/json": {"example": {"detail": "Invalid email or password"}}}},
                        401: {"description": "Incorrect email or password",
                              "content": {"application/json": {"example": {"detail": "Unauthorized"}}}},
                        422: {"description": "Validation error (e.g. incorrect email)", "content": {
                            "application/json": {"example": {"detail": [
                                {"loc": ["body", "email"], "msg": "value is not a valid email address",
                                 "type": "value_error.email"}]}}}}, }, tags=["Authentication"])
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    service = AuthService(UserRepository(db))

    token = service.authenticate_user(request.email, request.password)

    return LoginResponse(access_token=token, token_type="bearer")
