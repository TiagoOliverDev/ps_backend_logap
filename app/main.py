from fastapi import FastAPI
from app.api.routes import router as api_router
from app.db.database import Base, engine

app = FastAPI()

app.include_router(api_router)

# Cria todas as tabelas definidas nos modelos
# Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Hello World"}
