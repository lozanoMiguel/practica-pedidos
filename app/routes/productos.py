from fastapi import HTTPException, APIRouter
from typing import Optional, List
from app.models.producto import Producto, ProductoCreate
from app.db.database import producto_db, contador_producto
router = APIRouter()

@router.get("/", response_model=List[Producto])
def obtener_todos_los_productos(categoria: Optional[str]=None, stock_minimo: Optional[int]=None, activo: Optional[bool]=None, precio_maximo: Optional[float]=None):
    resultado = producto_db.copy()
    
    if not resultado:
        raise HTTPException(404, "No hay productos disponibles")
    
    if categoria:
        resultado = [p for p in resultado if p.categoria == categoria]
        
    if stock_minimo:
        resultado = [p for p in resultado if p.stock >= stock_minimo]
        
    if activo is not None:
        resultado = [p for p in resultado if p.activo]
    
    if precio_maximo:
        resultado = [p for p in resultado if p.precio < precio_maximo]
        
    return resultado

@router.post("/", response_model=Producto, status_code=201)
def agregar_producto(producto_nuevo: ProductoCreate):
    global producto_db
    global contador_producto
    nuevo = Producto(**producto_nuevo.model_dump(),id=contador_producto)
    contador_producto += 1
    producto_db.append(nuevo)
    return nuevo

@router.get("/{id}", response_model=Producto, status_code=201)
def obtener_producto(id: int):
    global producto_db
    resultado = next((p for p in producto_db if p.id == id), None)
    if resultado is None:
        raise HTTPException(404, "No existe un producto con ese ID")
    return resultado