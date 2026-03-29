from typing import List

from pydantic import BaseModel


class MetricResponse(BaseModel):
    title: str
    value: str
    description: str
    trend: str | None = None


class QuickActionResponse(BaseModel):
    title: str
    description: str
    path: str


class TodayWorkoutResponse(BaseModel):
    exercise: str
    equipment: str
    sets: int
    reps: int


class DashboardResponse(BaseModel):
    user_name: str
    occupancy_rate: int
    occupancy_message: str
    metrics: List[MetricResponse]
    quick_actions: List[QuickActionResponse]
    today_workout: List[TodayWorkoutResponse]
