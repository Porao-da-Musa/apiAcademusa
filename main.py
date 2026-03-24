from FastAPI import FastAPI
from app.routers import router

app = FastAPI(tittle="Academusa API", version="1.0.0")

app.include_router(router)

@app.get("/health")
def health_check():
    return {"status": "it's alive!"}