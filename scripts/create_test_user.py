from core.security import hash_password
from db.session import SessionLocal
from models.user import User


def main() -> None:
    db = SessionLocal()

    try:
        email = "test@example.com"

        existing_user = (db.query(User).filter(User.email == email).first())

        if existing_user:
            print(f"User already exists with id={existing_user.id}")
            return

        user = User(email=email, password_hash=hash_password("password123"), )

        db.add(user)
        db.commit()
        db.refresh(user)

        print(f"Created user with id={user.id}")
        print(f"Email: {user.email}")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    main()
