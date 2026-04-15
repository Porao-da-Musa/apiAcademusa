from app.schemas.yolo_schema import (
    NormalizedBBox,
    YoloDetectionInput,
    YoloDetectionOutput,
    YoloFrameRequest,
    YoloFrameResponse,
    YoloSummary,
)


class YoloService:
    def __init__(self, min_confidence: float, target_class: str) -> None:
        self.min_confidence = min_confidence
        self.target_class = target_class

    def process_frame(self, payload: YoloFrameRequest) -> YoloFrameResponse:
        processed_detections = [
            self._process_detection(detection) for detection in payload.detections
        ]
        accepted_detections = [
            detection for detection in processed_detections if detection.accepted
        ]

        people_detected = sum(
            1
            for detection in accepted_detections
            if detection.class_name == self.target_class
        )

        average_confidence = 0.0
        if accepted_detections:
            average_confidence = round(
                sum(detection.confidence for detection in accepted_detections)
                / len(accepted_detections),
                4,
            )

        summary = YoloSummary(
            total_detections=len(processed_detections),
            accepted_detections=len(accepted_detections),
            rejected_detections=len(processed_detections) - len(accepted_detections),
            people_detected=people_detected,
            average_confidence=average_confidence,
            target_class=self.target_class,
        )

        return YoloFrameResponse(
            status="success",
            frame_id=payload.frame_id,
            summary=summary,
            detections=processed_detections,
        )

    def _process_detection(self, detection: YoloDetectionInput) -> YoloDetectionOutput:
        x, y, width, height = detection.bbox
        normalized_bbox = NormalizedBBox(
            x=round(x, 4),
            y=round(y, 4),
            width=round(width, 4),
            height=round(height, 4),
            area=round(width * height, 4),
        )

        class_name = detection.class_name.strip().lower()
        is_target_class = class_name == self.target_class.lower()
        meets_confidence = detection.confidence >= self.min_confidence

        return YoloDetectionOutput(
            class_name=class_name,
            confidence=round(detection.confidence, 4),
            bbox=normalized_bbox,
            accepted=is_target_class and meets_confidence,
        )
