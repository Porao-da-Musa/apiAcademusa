from fastapi import APIRouter

from app.routers.auth import router as auth_router
from app.routers.dashboard import router as dashboard_router
from app.routers.exercises import router as exercises_router
from app.routers.workouts import router as workouts_router

api_router = APIRouter(prefix="/api")
api_router.include_router(auth_router)
api_router.include_router(dashboard_router)
api_router.include_router(exercises_router)
api_router.include_router(workouts_router)
