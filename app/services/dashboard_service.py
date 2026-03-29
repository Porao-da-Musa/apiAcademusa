from app.services.auth_service import get_user_by_id


def _get_occupancy_message(rate: int):
    if rate < 40:
        return "Baixa - otimo momento!"
    if rate < 70:
        return "Media"
    return "Alta"


def get_dashboard_data(user_id: str):
    user = get_user_by_id(user_id)
    occupancy_rate = 50

    return {
        "user_name": user["name"],
        "occupancy_rate": occupancy_rate,
        "occupancy_message": _get_occupancy_message(occupancy_rate),
        "metrics": [
            {
                "title": "Treinos esta semana",
                "value": "5/4",
                "description": "20% em relacao a semana passada",
                "trend": "up",
            },
            {
                "title": "Tempo medio",
                "value": "45min",
                "description": "Meta atual: 60 min",
                "trend": None,
            },
            {
                "title": "Recordes pessoais",
                "value": "3",
                "description": "Novos recordes neste mes",
                "trend": "up",
            },
            {
                "title": "Lotacao da academia",
                "value": f"{occupancy_rate}%",
                "description": _get_occupancy_message(occupancy_rate),
                "trend": None,
            },
        ],
        "quick_actions": [
            {
                "title": "Ver mapa da academia",
                "description": "Veja equipamentos e lotacao em tempo real",
                "path": "/home/map",
            },
            {
                "title": "Gerenciar treino",
                "description": "Crie e personalize sua rotina",
                "path": "/home/my-workout",
            },
            {
                "title": "Explorar exercicios",
                "description": "Encontre alternativas para equipamentos ocupados",
                "path": "/home/exercises",
            },
        ],
        "today_workout": [
            {
                "exercise": "Supino Reto",
                "equipment": "Barra Livre",
                "sets": 4,
                "reps": 12,
            },
            {
                "exercise": "Crucifixo Inclinado",
                "equipment": "Halteres",
                "sets": 3,
                "reps": 15,
            },
            {
                "exercise": "Triceps Testa",
                "equipment": "Barra W",
                "sets": 3,
                "reps": 12,
            },
            {
                "exercise": "Triceps Corda",
                "equipment": "Polia Alta",
                "sets": 3,
                "reps": 15,
            },
            {
                "exercise": "Rosca Direta",
                "equipment": "Barra EZ",
                "sets": 4,
                "reps": 10,
            },
        ],
    }
