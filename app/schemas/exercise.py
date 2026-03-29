from typing import List, Literal

from pydantic import BaseModel

LevelType = Literal["Iniciante", "Intermediario", "Avancado"]


class ExerciseResponse(BaseModel):
    id: str
    name: str
    category: str
    equipment: str
    level: LevelType
    muscles: List[str]
