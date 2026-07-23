from pydantic import BaseModel, Field
from typing import Optional

class ItemPedidoCreate(BaseModel):
    producto_id: int
    cantidad: int = Field(..., gt=0)
    precio_unitario: float 
    subtotal: float
    

class ItemPedido(ItemPedidoCreate):
    producto_id: int
    cantidad: int 
    precio_unitario: float 
    subtotal: float
