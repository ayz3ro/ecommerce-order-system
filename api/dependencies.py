from fastapi import Depends
from sqlalchemy.orm import Session

from db.session import get_db
from modules.customers.repository import CustomerRepository
from modules.auth.service import AuthService


def get_auth_service(db: Session = Depends(get_db), ) -> AuthService:
    user_repository = CustomerRepository(db)

    return AuthService(user_repository=user_repository, )
