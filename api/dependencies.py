from fastapi import Depends
from sqlalchemy.orm import Session

from db.session import get_db
from repositories.users import UserRepository
from services.auth import AuthService


def get_auth_service(db: Session = Depends(get_db), ) -> AuthService:
    user_repository = UserRepository(db)

    return AuthService(user_repository=user_repository, )
