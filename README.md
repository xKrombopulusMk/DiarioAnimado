# Diário Animado

Projeto MVP de um diário multimídia automático.

## Executando localmente

Requisitos: Python 3.11, Node 18+.

```bash
# Backend
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

# Frontend
cd frontend
npm install
npm run dev
```

Ou via Docker:

```bash
docker-compose up --build
```

## Variáveis de ambiente
- `SECRET_KEY` – chave JWT
- `DATABASE_URL` – URL do banco (padrão sqlite:///./data.db)
- `RETENTION_DAYS` – dias de retenção dos dados (padrão 30)

## Exemplos de requisições

Registrar usuário:
```bash
curl -X POST http://localhost:8000/auth/register -H 'Content-Type: application/json' -d '{"email":"user@example.com","password":"123"}'
```

Login:
```bash
curl -X POST http://localhost:8000/auth/login -d 'username=user@example.com&password=123'
```

Enviar evento:
```bash
curl -X POST http://localhost:8000/data/upload -H 'Authorization: Bearer TOKEN' -H 'Content-Type: application/json' -d '{"type":"note","content":"Hoje foi incrível"}'
```

Criar episódio:
```bash
curl -X POST http://localhost:8000/episodes/create -H 'Authorization: Bearer TOKEN' -H 'Content-Type: application/json' -d '{"period":"day","style":"poetic"}'
```
