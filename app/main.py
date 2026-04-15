from fastapi import FastAPI

from app.api.routers.yolo import router as yolo_router
from app.core.settings import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="API para receber e processar YOLO.",
)

app.include_router(yolo_router, prefix=settings.api_prefix)


@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}
