from fastapi import APIRouter, HTTPException

from app.database import get_user_by_id

router = APIRouter(prefix="/api/users")


@router.get("/{user_id}")
def get_user(user_id: int):
    user = get_user_by_id(user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return user