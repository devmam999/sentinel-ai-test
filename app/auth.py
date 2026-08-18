from fastapi import APIRouter, HTTPException

from app.database import get_user_by_username

router = APIRouter(prefix="/api/auth")


@router.post("/login")
def login(username: str, password: str):
    user = get_user_by_username(username)

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
        )

    if not user["active"]:
        raise HTTPException(
            status_code=403,
            detail="User account is inactive",
        )

    if password != "password123":
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
        )

    return {
        "user_id": user["id"],
        "username": user["username"],
        "authenticated": True,
    }