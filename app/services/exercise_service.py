from app.models.data import EXERCISES


def list_exercises(category: str | None = None, level: str | None = None):
    exercises = EXERCISES

    if category:
        exercises = [
            exercise
            for exercise in exercises
            if exercise["category"].lower() == category.lower()
        ]

    if level:
        exercises = [
            exercise
            for exercise in exercises
            if exercise["level"].lower() == level.lower()
        ]

    return exercises
