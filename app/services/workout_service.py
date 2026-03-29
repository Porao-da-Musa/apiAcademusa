from fastapi import HTTPException, status

from app.models.data import WORKOUTS_BY_USER
from app.services.auth_service import get_user_by_id


def list_workout_by_user(user_id: str):
    get_user_by_id(user_id)
    exercises = WORKOUTS_BY_USER.get(user_id, [])

    return {
        "user_id": user_id,
        "has_occupied": any(exercise["status"] == "Ocupado" for exercise in exercises),
        "exercises": exercises,
    }


def create_workout_exercise(user_id: str, payload):
    get_user_by_id(user_id)
    exercises = WORKOUTS_BY_USER.setdefault(user_id, [])

    new_exercise = {
        "id": str(len(exercises) + 1),
        "order": len(exercises) + 1,
        "name": payload.name.strip(),
        "equipment": payload.equipment.strip(),
        "status": payload.status,
        "sets": payload.sets,
        "reps": payload.reps,
        "alternatives": payload.alternatives,
    }
    exercises.append(new_exercise)
    return new_exercise


def delete_workout_exercise(user_id: str, exercise_id: str):
    get_user_by_id(user_id)
    exercises = WORKOUTS_BY_USER.get(user_id, [])
    exercise = next((item for item in exercises if item["id"] == exercise_id), None)

    if not exercise:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Exercicio nao encontrado no treino.",
        )

    updated_exercises = [item for item in exercises if item["id"] != exercise_id]
    for index, item in enumerate(updated_exercises, start=1):
        item["order"] = index

    WORKOUTS_BY_USER[user_id] = updated_exercises
    return {"message": "Exercicio removido com sucesso."}
