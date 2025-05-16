# Backend Rifa - FastAPI

Este é um backend mínimo funcional para rodar na Render com rotas de Pix (Pay2M) e Afiliado.

## Instruções

1. Crie seu ambiente:
```bash
pip install -r requirements.txt
```

2. Suba para o GitHub

3. Na Render:
- Start Command: uvicorn app.main:app --host 0.0.0.0 --port 10000
- Build Command: pip install -r requirements.txt
- Environment: `PAY2M_TOKEN=xxxxxxx`
