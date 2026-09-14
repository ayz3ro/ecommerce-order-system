from core.exceptions import InvalidCredentials, EmailAlreadyInUse
from core.security import create_access_token, verify_password, hash_password
from schemas.auth import LoginResponse, RegisterResponse


class AuthService:
    def __init__(self, user_repository) -> None:
        self.user_repository = user_repository

    def authenticate_user(self, email: str, password: str, ) -> LoginResponse:
        normalized_email = email.strip().lower()

        user = self.user_repository.get_by_email(normalized_email)

        if user is None or not verify_password(password, user.password_hash, ):
            raise InvalidCredentials()

        access_token = create_access_token(user.id)

        return LoginResponse(access_token=access_token, token_type="bearer", )

    def register_user(self, email: str, password: str, ) -> RegisterResponse:
        normalized_email = email.strip().lower()

        if self.user_repository.get_by_email(normalized_email) is not None:
            raise EmailAlreadyInUse()

        password_hash = hash_password(password)

        user = self.user_repository.create(email=normalized_email, password_hash=password_hash, )

        access_token = create_access_token(user.id)

        return RegisterResponse(access_token=access_token, token_type="bearer", )
