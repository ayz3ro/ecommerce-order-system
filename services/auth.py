from core.exceptions import InvalidCredentials
from core.security import create_access_token
from core.security import verify_password


class AuthService:

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def authenticate_user(self, email: str, password: str, ):
        user = self.user_repository.get_by_email(email.lower())

        if user is None:
            raise InvalidCredentials()

        if not verify_password(password, user.password_hash, ):
            raise InvalidCredentials()

        return create_access_token(user.id)
