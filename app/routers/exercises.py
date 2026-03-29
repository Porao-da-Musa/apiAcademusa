from typing import List

from fastapi import APIRouter, Query

from app.schemas.exercise import ExerciseResponse
from app.services.exercise_service import list_exercises

router = APIRouter(prefix="/exercises", tags=["exercises"])


@router.get("", response_model=List[ExerciseResponse])
def get_exercises(
    category: str | None = Query(default=None),
    level: str | None = Query(default=None),
):
    return list_exercises(category=category, level=level)
