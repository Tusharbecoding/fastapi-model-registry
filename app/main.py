from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


app = FastAPI(
    title = "FastAPI Model Registry",
    description = "Manage AI Models",
    version = "1.0.0",
    docs_url = "/docs"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

@app.get("/")
async def root():
    return{
        "message": "You are in the FastAPI Models Registry",
        "status": "active"
    }

@app.get("/health")
async def health_check():
    return{
        "status": "healthy",
        "service": "ai-model-registry"
    }


