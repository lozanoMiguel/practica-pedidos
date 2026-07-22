from fastapi import FastAPI
from app.routes import pedidos, productos

app = FastAPI(title="API de Proyectos", version="1.0.0")

#app.include_router(pedidos.router, prefix="/pedidos", tags=["Pedidos"])
app.include_router(productos.router, prefix="/productos", tags=["Productos"])

@app.get("/")
def root():
    return {"message": "API de Proyectos funcionando"}