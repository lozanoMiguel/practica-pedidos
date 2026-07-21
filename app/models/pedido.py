from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal, List
from app.models.item_pedido import ItemPedido

class PedidoCreate(BaseModel):
    cliente_nombre: str = Field(..., min_length=3, max_length=100)
    cliente_email: EmailStr
    estado: Optional[Literal["pendiente", "confirmado", "enviado", "entregado", "cancelado"]] = Field(default="pendiente")
    
class PedidoUpdate(BaseModel):
    cliente_nombre: Optional[str] = Field(None, min_length=3, max_length=100)
    cliente_email: Optional[EmailStr]
    estado: Optional[Literal["pendiente", "confirmado", "enviado", "entregado", "cancelado"]] = Field(default=None)

class Pedido(PedidoCreate):
    id: int
    fecha_creacion: str
    total: float
    productos: Optional[List[ItemPedido]] = []