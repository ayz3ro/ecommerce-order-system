from core.security import verify_password
from core.exceptions import InvalidCredentials
from core.security import create_access_token


class AuthService:

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def authenticate_user(
        self,
        email: str,
        password: str,
    ):
        user = self.user_repository.get_by_email(email)

        if user is None:
            raise InvalidCredentials()

        if not verify_password(
            password,
            user.password_hash,
        ):
            raise InvalidCredentials()

        return create_access_token(user.id)