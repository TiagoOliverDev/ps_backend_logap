from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError  # Para capturar erros específicos de SQLAlchemy
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
def create_product(product: ProductCreate, db: Session = Depends(get_db)) -> Product:
    """
    Create a new product with the given product data.

    Args:
        product (ProductCreate): The product data used for creating a new product.
        db (Session): Dependency injection of the database session.

    Returns:
        Product: The created product object.

    Raises:
        HTTPException: 500 error if there is a problem creating the product.
    """
    try:
        product_service = ProductService(db)
        created_product = product_service.create_product(product)
        return created_product
    except SQLAlchemyError as e:
        logger.error(f"Database error while creating product: {e}")
        raise HTTPException(status_code=500, detail="Failed to create product due to a database error.")
    except Exception as e:
        logger.error(f"Error creating product: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/produtos/listagem", response_model=List[Product])
def read_products(db: Session = Depends(get_db)) -> List[Product]:
    """
    Retrieve a list of products.

    Args:
        db (Session): Dependency injection of the database session.

    Returns:
        List[Product]: A list of products.

    Raises:
        HTTPException: 500 error if there is a problem retrieving the products.
    """
    try:
        product_service = ProductService(db)
        products = product_service.get_products()
        return products
    except SQLAlchemyError as e:
        logger.error(f"Database error while retrieving products: {e}")
        raise HTTPException(status_code=500, detail="Failed to retrieve products due to a database error.")
    except Exception as e:
        logger.error(f"Error retrieving products: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")

@router.get("/{product_id}", response_model=Product)
def read_product(product_id: int, db: Session = Depends(get_db)) -> Product:
    """
    Retrieve a specific product by its ID.

    Args:
        product_id (int): The unique identifier for the product.
        db (Session): Dependency injection of the database session.

    Returns:
        Product: The retrieved product object.

    Raises:
        HTTPException: 404 error if no product is found.
    """
    try:
        product_service = ProductService(db)
        product = product_service.get_product(product_id)
        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        return product
    except SQLAlchemyError as e:
        logger.error(f"Database error while retrieving product: {e}")
        raise HTTPException(status_code=500, detail="Failed to retrieve product due to a database error.")
    except Exception as e:
        logger.error(f"Error retrieving product: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")

@router.put("/editar/{product_id}", response_model=Product)
def update_product(product_id: int, product_data: ProductCreate, db: Session = Depends(get_db)) -> Product:
    """
    Update an existing product with new data.

    Args:
        product_id (int): The unique identifier for the product.
        product_data (ProductCreate): New data for updating the product.
        db (Session): Dependency injection of the database session.

    Returns:
        Product: The updated product object.

    Raises:
        HTTPException: 404 error if the product is not found.
        HTTPException: 500 error if there is a problem updating the product.
    """
    try:
        product_service = ProductService(db)
        updated_product = product_service.update_product(product_id, product_data)
        if updated_product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        return updated_product
    except SQLAlchemyError as e:
        logger.error(f"Database error while updating product: {e}")
        raise HTTPException(status_code=500, detail="Failed to update product due to a database error.")
    except Exception as e:
        logger.error(f"Error updating product: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")

@router.delete("/delete/{product_id}", status_code=204)
def delete_product(product_id: int, db: Session = Depends(get_db)) -> None:
    """
    Delete a product by its ID.

    Args:
        product_id (int): The unique identifier for the product.
        db (Session): Dependency injection of the database session.

    Returns:
        dict: A confirmation message of deletion.

    Raises:
        HTTPException: 404 error if the product is not found.
        HTTPException: 500 error if there is a problem deleting the product.
    """
    try:
        product_service = ProductService(db)
        if not product_service.delete_product(product_id):
            raise HTTPException(status_code=404, detail="Product not found")
        return {"detail": "Product successfully deleted"}
    except SQLAlchemyError as e:
        logger.error(f"Database error while deleting product: {e}")
        raise HTTPException(status_code=500, detail="Failed to delete product due to a database error.")
    except Exception as e:
        logger.error(f"Error deleting product: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
