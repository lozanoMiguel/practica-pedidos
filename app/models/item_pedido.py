from pydantic import BaseModel, Field
from typing import Optional

class ItemPedidoCreate(BaseModel):
    cantidad: int = Field(..., gt=0)
    precio_unitario: float 
    subtotal: float
    
class ItempedidoUpdate(BaseModel):
    cantidad: Optional[int] = Field(None, gt=0)
    precio_unitario: Optional[float]
    subtotal: Optional[float]
    
class ItemPedido(ItemPedidoCreate):
    id: int
