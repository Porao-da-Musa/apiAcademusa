from app.core.settings import Settings, get_settings
from app.services.yolo_service import YoloService


def get_yolo_service() -> YoloService:
    settings: Settings = get_settings()
    return YoloService(
        min_confidence=settings.min_confidence,
        target_class=settings.default_detection_class,
    )
