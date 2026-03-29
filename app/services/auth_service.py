from fastapi import HTTPException, status

from app.models.data import USERS


def _sanitize_user(user):
    return {
        "id": user["id"],
        "name": user["name"],
        "email": user["email"],
    }


def signup_user(payload):
    user_exists = next((user for user in USERS if user["email"] == payload.email), None)
    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Usuario ja cadastrado.",
        )

    new_user = {
        "id": f"user-{len(USERS) + 1}",
        "name": payload.name.strip(),
        "email": payload.email,
        "password": payload.password,
    }
    USERS.append(new_user)

    return {
        "message": "Conta criada com sucesso.",
        "user": _sanitize_user(new_user),
    }


def login_user(payload):
    user = next(
        (
            user
            for user in USERS
            if user["email"] == payload.email and user["password"] == payload.password
        ),
        None,
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha invalidos.",
        )

    return {
        "message": "Login realizado com sucesso.",
        "user": _sanitize_user(user),
    }


def get_user_by_id(user_id: str):
    user = next((user for user in USERS if user["id"] == user_id), None)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario nao encontrado.",
        )

    return _sanitize_user(user)
