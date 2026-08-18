from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/users")

USERS = {
    1: {
        "id": 1,
        "username": "alice",
        "email": "alice@example.com",
        "activate": True,
    },
    2: {
        "id": 2,
        "username": "bob",
        "email": "bob@example.com",
        "activate": True,
    }
}

@router.get("/{user_id}")
def get_user(user_id: int):
    user = USERS.get(user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user