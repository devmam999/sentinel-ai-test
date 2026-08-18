from fastapi import FastAPI

from app.health import router as health_router

app = FastAPI(title="SentinelAI Test Service")

app.include_router(health_router)

@app.get("/")
def root():
    return {
        "service": "senteinelai-test-service"
    }