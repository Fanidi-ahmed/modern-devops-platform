from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.src.core.logging import logger
from app.src.database import get_db
from app.src.schemas.user import UserCreate, UserResponse
from app.src.services.user_service import create_user, list_users

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", response_model=UserResponse)
def create_user_endpoint(
    user_data: UserCreate,
    db: Session = Depends(get_db),
) -> UserResponse:
    logger.info("Create user endpoint called")
    print("ROUTE: entered create_user_endpoint")

    try:
        result = create_user(db, user_data)
        print("ROUTE: service returned successfully")
        return result

    except ValueError as exc:
        print("ROUTE: ValueError caught:", exc)
        logger.warning(f"User creation failed: {exc}")
        raise HTTPException(status_code=409, detail=str(exc)) from exc


@router.get("", response_model=list[UserResponse])
def list_users_endpoint(
    db: Session = Depends(get_db),
) -> list[UserResponse]:
    logger.info("List users endpoint called")
    return list_users(db)