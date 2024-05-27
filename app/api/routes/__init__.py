from fastapi import APIRouter
from . import category, supplier, product, auth

router = APIRouter()
router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(category.router, prefix="/categories", tags=["categories"])
router.include_router(supplier.router, prefix="/suppliers", tags=["suppliers"])
router.include_router(product.router, prefix="/products", tags=["products"])
