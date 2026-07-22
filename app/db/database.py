from typing import List
from app.models.pedido import Pedido
from app.models.producto import Producto

pedidos_db: List[Pedido] = []
producto_db: List[Producto] = []
contador_pedido = 1
contador_producto = 1
