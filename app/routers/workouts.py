from fastapi import APIRouter, status

from app.schemas.workout import (
    WorkoutCreateRequest,
    WorkoutExerciseResponse,
    WorkoutListResponse,
)
from app.services.workout_service import (
    create_workout_exercise,
    delete_workout_exercise,
    list_workout_by_user,
)

router = APIRouter(prefix="/workouts", tags=["workouts"])


@router.get("/{user_id}", response_model=WorkoutListResponse)
def get_workout(user_id: str):
    return list_workout_by_user(user_id)


@router.post("/{user_id}/exercises", response_model=WorkoutExerciseResponse, status_code=201)
def create_exercise(user_id: str, payload: WorkoutCreateRequest):
    return create_workout_exercise(user_id, payload)


@router.delete("/{user_id}/exercises/{exercise_id}", status_code=status.HTTP_200_OK)
def delete_exercise(user_id: str, exercise_id: str):
    return delete_workout_exercise(user_id, exercise_id)
