from fastapi import APIRouter
import requests
import os
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/pagamentos", tags=["Pagamentos"])

@router.post("/pix")
def criar_pagamento_pix(payload: dict):
    valor = payload.get("valor", 0)
    try:
        resposta = requests.post(
            "https://api.pay2m.com.br/pagamento",
            headers={"Authorization": f"Bearer {os.getenv('PAY2M_TOKEN')}"},
            json={
                "valor": valor,
                "chave_pix": "seu_pix@dominio.com",
                "descricao": "Compra de rifa"
            }
        )
        return resposta.json()
    except Exception as e:
        return JSONResponse(status_code=500, content={"erro": str(e)})
