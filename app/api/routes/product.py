# app/api/routes/product.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from app.schemas.product_schema import Product, ProductCreate
from app.services.product_service import ProductService
from app.api.dependencies import get_db
import logging

router = APIRouter()

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.post("/cadastrar", response_model=Product)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    try:
        product_service = ProductService(db)
        created_product = product_service.create_product(product)
        return created_product  # Retorna o objeto Pydantic que é serializável
    except Exception as e:
        logger.error(f"Erro ao cadastrar produto: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/listagem", response_model=List[Product])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        product_service = ProductService(db)
        products = product_service.get_products(skip=skip, limit=limit)
        return products  # Retorna a lista de objetos Pydantic
    except Exception as e:
        logger.error(f"Erro ao listar produtos: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{product_id}", response_model=Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product_service = ProductService(db)
    product = product_service.get_product(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return product

@router.put("/editar/{product_id}", response_model=Product)
def update_product(product_id: int, product_data: ProductCreate, db: Session = Depends(get_db)):
    product_service = ProductService(db)
    updated_product = product_service.update_product(product_id, product_data)
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return updated_product

@router.delete("/delete/{product_id}", status_code=204)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product_service = ProductService(db)
    if not product_service.delete_product(product_id):
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return {"detail": "Produto deletado com sucesso"}
