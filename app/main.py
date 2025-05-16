from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import pagamentos, afiliado

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pagamentos.router)
app.include_router(afiliado.router)

@app.get("/")
def root():
    return {"message": "API de Rifas Online Ativa"}
