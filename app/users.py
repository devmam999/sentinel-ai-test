from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.database import get_user_by_id, is_user_active
from app.database import create_user as create_user_in_database

class UserCreate(BaseModel):
    username: str
    email: str

router = APIRouter(prefix="/api/users")


@router.get("/{user_id}")
def get_user(user_id: int):
    user = get_user_by_id(user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    if not is_user_active(user_id):
        raise HTTPException(
            status_code=403,
            detail="User account is inactive"
        )
    return user

@router.post("")
def create_user(user: UserCreate):
    return create_user_in_database(
        user.username,
        user.email,
    )