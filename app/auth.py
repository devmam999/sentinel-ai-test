from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/auth")


USERS = {
    "alice": "password123",
    "bob": "password456",
}


@router.post("/login")
def login(username: str, password: str):
    if USERS.get(username) != password:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
        )

    return {
        "username": username,
        "authenticated": True,
    }