# Academusa API

Feito com FastAPI

## Setup

```bash
# Clone o repo
git clone https://github.com/Porao-da-Musa/apiAcademusa.git
cd apiAcademusa

# Crie o venv
python -m venv venv
venv\Scripts\activate

# Dependências
pip install -r requirements.txt

# Variáveis de ambiente
cp .env.example .env

# Rode a API
uvicorn main:app --reload
```

## Rotas principais

- `GET /health`
- `POST /api/auth/signup`
- `POST /api/auth/login`
- `GET /api/auth/users/{user_id}`
- `GET /api/dashboard/{user_id}`
- `GET /api/exercises`
- `GET /api/exercises?category=Peito`
- `GET /api/exercises?level=Iniciante`
- `GET /api/workouts/{user_id}`
- `POST /api/workouts/{user_id}/exercises`
- `DELETE /api/workouts/{user_id}/exercises/{exercise_id}`

## Usuario inicial

- `teste@teste.com`
- `123456`

## Observacoes

- Os dados estão em memoria.
