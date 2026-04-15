from fastapi import APIRouter, Depends, status

from app.api.deps import get_yolo_service
from app.schemas.yolo_schema import YoloFrameRequest, YoloFrameResponse
from app.services.yolo_service import YoloService

router = APIRouter(prefix="/yolo", tags=["yolo"])


@router.post(
    "/detections/process",
    response_model=YoloFrameResponse,
    status_code=status.HTTP_200_OK,
)
def process_yolo_detections(
    payload: YoloFrameRequest,
    service: YoloService = Depends(get_yolo_service),
) -> YoloFrameResponse:
    return service.process_frame(payload)
