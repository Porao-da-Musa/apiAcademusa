from functools import lru_cache
from os import getenv

from pydantic import BaseModel, Field


class Settings(BaseModel):
    app_name: str = "Academusa YOLO API"
    app_version: str = "2.0.0"
    api_prefix: str = "/api/v1"
    min_confidence: float = Field(default=0.25, ge=0.0, le=1.0)
    default_detection_class: str = "person"


@lru_cache
def get_settings() -> Settings:
    return Settings(
        app_name=getenv("APP_NAME", "Academusa YOLO API"),
        app_version=getenv("APP_VERSION", "2.0.0"),
        api_prefix=getenv("API_PREFIX", "/api/v1"),
        min_confidence=float(getenv("MIN_CONFIDENCE", "0.25")),
        default_detection_class=getenv("DEFAULT_DETECTION_CLASS", "person"),
    )
