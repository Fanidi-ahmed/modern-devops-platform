import json
from app.src.cache.redis_client import redis_client
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
        redis_client.delete("users")
        db.refresh(user)
        print("SERVICE: user created successfully")
        return user

    except IntegrityError as exc:
        print("SERVICE: IntegrityError caught")
        db.rollback()
        raise ValueError("Email already exists") from exc


def list_users(db):
    cached_users = redis_client.get("users")

    if cached_users:
        print("CACHE HIT")
        return json.loads(cached_users)

    print("CACHE MISS")

    users = db.query(User).all()

    users_data = [
        {"id": u.id, "name": u.name, "email": u.email}
        for u in users
    ]

    redis_client.set("users", json.dumps(users_data), ex=60)

    return users_data