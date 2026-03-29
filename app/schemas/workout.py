from typing import List, Literal

from pydantic import BaseModel, Field

WorkoutStatus = Literal["Ocupado", "Disponivel"]


class WorkoutExerciseResponse(BaseModel):
    id: str
    order: int
    name: str
    equipment: str
    status: WorkoutStatus
    sets: int
    reps: int
    alternatives: List[str] = []


class WorkoutListResponse(BaseModel):
    user_id: str
    has_occupied: bool
    exercises: List[WorkoutExerciseResponse]


class WorkoutCreateRequest(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    equipment: str = Field(min_length=2, max_length=100)
    sets: int = Field(ge=1, le=10)
    reps: int = Field(ge=1, le=30)
    status: WorkoutStatus
    alternatives: List[str] = []
