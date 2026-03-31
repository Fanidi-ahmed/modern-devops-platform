from app.src.schemas.user import UserCreate, UserResponse

users_db: list[UserResponse] = []
current_id = 1


def create_user(user_data: UserCreate) -> UserResponse:
    global current_id

    user = UserResponse(
        id=current_id,
        name=user_data.name,
        email=user_data.email,
    )

    users_db.append(user)
    current_id += 1

    return user


def list_users() -> list[UserResponse]:
    return users_db