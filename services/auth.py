from core.security import verify_password


class AuthService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def authenticate_user(self, email: str, password: str):

        user = self.user_repository.get_by_email(email)

        if not user:
            raise InvalidCredentials()

        if not verify_password(password, user.password_hash):
            raise InvalidCredentials()

        token = create_access_token(user.id)

        return token
