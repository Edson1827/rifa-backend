from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Comissao
from datetime import datetime

router = APIRouter(prefix="/afiliado", tags=["Afiliado"])

@router.get("/comissoes")
def listar_comissoes(db: Session = Depends(get_db)):
    comissoes = db.query(Comissao).all()
    return [{"valor": c.valor, "data": c.data.strftime("%Y-%m-%d")} for c in comissoes]
