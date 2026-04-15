from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator


class YoloDetectionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    class_name: str = Field(alias="class", min_length=1, max_length=100)
    confidence: float = Field(ge=0.0, le=1.0)
    bbox: list[float] = Field(min_length=4, max_length=4)

    @field_validator("bbox")
    @classmethod
    def validate_bbox(cls, value: list[float]) -> list[float]:
        if len(value) != 4:
            raise ValueError("bbox deve ter exatamente 4 valores.")
        if any(item < 0 for item in value):
            raise ValueError("bbox nao pode conter valores negativos.")
        return value


class YoloFrameRequest(BaseModel):
    frame_id: int = Field(ge=0)
    detections: list[YoloDetectionInput] = Field(default_factory=list)


class NormalizedBBox(BaseModel):
    x: float
    y: float
    width: float
    height: float
    area: float


class YoloDetectionOutput(BaseModel):
    class_name: str
    confidence: float
    bbox: NormalizedBBox
    accepted: bool


class YoloSummary(BaseModel):
    total_detections: int
    accepted_detections: int
    rejected_detections: int
    people_detected: int
    average_confidence: float
    target_class: str


class YoloFrameResponse(BaseModel):
    status: Literal["success"]
    frame_id: int
    summary: YoloSummary
    detections: list[YoloDetectionOutput]
