from fastapi import APIRouter, HTTPException

from app.api.v1.models.auth import LoginResponse, LoginRequest

router = APIRouter(prefix="/auth")


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
def login(request: LoginRequest):
    if not request.email or not request.password:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    if (request.email == "user1@gmail.com" and request.password == "user_1111") or (
            request.email == "user2@gmail.com" and request.password == "user_2222"):
        return {"message": "Login successful"}

    raise HTTPException(status_code=401, detail="Unauthorized")