from fastapi import APIRouter

router = APIRouter()

@rotuer.get("/health")
def health_check():
    return {
        "status": "healthy"
    }