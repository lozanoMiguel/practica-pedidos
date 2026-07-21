from pydantic import BaseModel, Field
from typing import Optional

class ProductoCreate(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=100)
    descripcion: str = Field(..., min_length=10, max_length=500)
    precio: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    categoria: Optional[str] = Field(None, max_length=50)
    activo: bool = Field(default=True)
    
class ProductoUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=3, max_length=100)
    descripcion: Optional[str] = Field(None, min_length=10, max_length=500)
    precio: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)
    categoria: Optional[str] = Field(None, max_length=50)
    activo: Optional[bool] = Field(default=True)
    
class Producto(ProductoCreate):
    id: int