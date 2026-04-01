from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.src.models.user import User
from app.src.schemas.user import UserCreate


def create_user(db: Session, user_data: UserCreate) -> User:
    user = User(
        name=user_data.name,
        email=user_data.email,
    )

    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        print("SERVICE: user created successfully")
        return user

    except IntegrityError as exc:
        print("SERVICE: IntegrityError caught")
        db.rollback()
        raise ValueError("Email already exists") from exc


def list_users(db: Session) -> list[User]:
    return db.query(User).all()