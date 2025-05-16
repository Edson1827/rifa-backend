from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from app.database import Base
from datetime import date

class Comissao(Base):
    __tablename__ = "comissoes"
    id = Column(Integer, primary_key=True, index=True)
    valor = Column(Integer)
    data = Column(Date, default=date.today)
    afiliado_id = Column(Integer, ForeignKey("afiliados.id"))

class Afiliado(Base):
    __tablename__ = "afiliados"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    codigo = Column(String, unique=True)
