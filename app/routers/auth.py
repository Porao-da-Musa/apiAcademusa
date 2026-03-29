from fastapi import APIRouter

from app.schemas.auth import AuthResponse, LoginRequest, SignupRequest, UserResponse
from app.services.auth_service import get_user_by_id, login_user, signup_user

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup", response_model=AuthResponse, status_code=201)
def signup(payload: SignupRequest):
    return signup_user(payload)


@router.post("/login", response_model=AuthResponse)
def login(payload: LoginRequest):
    return login_user(payload)


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: str):
    return get_user_by_id(user_id)
