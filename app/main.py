from fastapi import FastAPI
from app.api.routes import router as api_router
from app.db.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.services.questao_one import encontrar_vogal_especial

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

### Endpoint para resolução da questão 1
class InputString(BaseModel):
    input_string: str

@app.post("/teste/")
def read_vowel(input_string: str):
    return encontrar_vogal_especial(input_string)