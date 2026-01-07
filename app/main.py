from fastapi import FastAPI
from app.api import router

app = FastAPI(
    title="REST API Starter",
    description="Clean and minimal FastAPI boilerplate",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"status": "API is running"}
