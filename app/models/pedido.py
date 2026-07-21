from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal, List
from app.models.item_pedido import Item_pedido

class PedidoCreate(BaseModel):
    cliente_nombre: str = Field(..., min_length=3, max_length=100)
    cliente_email: EmailStr
    estado: Optional[Literal["pendiente", "confirmado", "enviado", "entregado", "cancelado"]] = Field(default="pendiente")
    
class PedidoUpdate(BaseModel):
    pass

class Pedido(PedidoCreate):
    id: int
    fecha_creacion: str
    total: float
    productos: Optional[List[Item_pedido]] = []