from fastapi import APIRouter
from app.src.core.logging import logger
from app.src.schemas.user import UserCreate, UserResponse
from app.src.services.user_service import create_user, list_users

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", response_model=UserResponse)
def create_user_endpoint(user_data: UserCreate) -> UserResponse:
    logger.info("Create user endpoint called")
    return create_user(user_data)


@router.get("", response_model=list[UserResponse])
def list_users_endpoint() -> list[UserResponse]:
    logger.info("List users endpoint called")
    return list_users()