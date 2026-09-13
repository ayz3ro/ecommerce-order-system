from sqlalchemy.exc import IntegrityError

from core.exceptions import InvalidCredentials, NotFound, EmailAlreadyInUse
from core.security import create_access_token, hash_password
from core.security import verify_password
from schemas.auth import RegisterResponse


class AuthService:

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def authenticate_user(self, email: str, password: str, ):
        user = self.user_repository.get_by_email(email.lower())

        if user is None:
            raise NotFound()

        if not verify_password(password, user.password_hash, ):
            raise InvalidCredentials()

        return create_access_token(user.id)

    def register_user(
        self,
        email: str,
        password: str,
    ) -> RegisterResponse:

        user = self.user_repository.create(
            email=email,
            password=password,
        )

        access_token = create_access_token(
            user_id=user.id,
        )

        return RegisterResponse(
            access_token=access_token,
            token_type="bearer",
        )