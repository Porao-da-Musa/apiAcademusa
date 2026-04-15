# Academusa API

API FastAPI para receber e processar JSON do YOLO.

## Como rodar

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Endpoint principal

- `POST /api/v1/yolo/detections/process`

## Exemplo de payload

```json
{
  "frame_id": 123,
  "detections": [
    {
      "class": "person",
      "confidence": 0.98,
      "bbox": [120, 80, 60, 180]
    }
  ]
}
```

## O que a API faz

- valida a estrutura do JSON
- filtra deteccoes abaixo do limite configurado
- normaliza as bounding boxes
- retorna um resumo estruturado do frame

## Observacoes

- sem banco de dados
- sem autenticacao
- preparada para futura integracao com Supabase
