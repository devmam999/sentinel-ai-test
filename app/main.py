from fastapi import FastAPI

from app.health import router as health_router
from app.users import router as users_router
from app.auth import router as auth_router

app = FastAPI(title="SentinelAI Test Service")

app.include_router(health_router)
app.include_router(users_router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {
        "service": "sentinelai-test-service"
    }