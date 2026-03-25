# Academusa API

Feito com FastAPI

## Setup

\```bash
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
\```