from fastapi import FastAPI

from app.health import router as health_router
from app.users import router as users_router
from app.auth import router as auth_router

app = FastAPI(
    title="SentinelAI Test Service",
    description="Internal API service used for incident testing",
    version="1.0.0",
)

app.include_router(health_router)
app.include_router(users_router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {
        "service": "sentinelai-test-service"
    }