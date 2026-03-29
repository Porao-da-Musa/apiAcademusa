from fastapi import APIRouter

from app.schemas.dashboard import DashboardResponse
from app.services.dashboard_service import get_dashboard_data

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/{user_id}", response_model=DashboardResponse)
def get_dashboard(user_id: str):
    return get_dashboard_data(user_id)
