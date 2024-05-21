# app/schemas/supplier_schema.py
from pydantic import BaseModel

class SupplierBase(BaseModel):
    name: str

class SupplierCreate(SupplierBase):
    pass

class Supplier(SupplierBase):
    id: int

    class Config:
        from_attributes = True
