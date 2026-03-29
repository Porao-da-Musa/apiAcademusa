from pydantic import BaseModel, Field


class SignupRequest(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: str = Field(min_length=5, max_length=100)
    password: str = Field(min_length=6, max_length=50)


class LoginRequest(BaseModel):
    email: str = Field(min_length=5, max_length=100)
    password: str = Field(min_length=6, max_length=50)


class UserResponse(BaseModel):
    id: str
    name: str
    email: str


class AuthResponse(BaseModel):
    message: str
    user: UserResponse
