from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from . import cryptfernet as crypt
from . import fbcrowned as fb
from . import sbpostgre as sb


# Instancia de los objetos de firebase y postgres
class default():
    def __init__(self):
        self.fb = fb.fbCrowned()
        self.sb = sb.sbPostgre()
        self.crypt = crypt.CryptFernet()
client = default()

# Creamos el router para los productos
router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    responses={404: {"description": "No encontrado"}},
)

# Modelo de datos para Producto
class Admin(BaseModel):
    id: Optional[int] = None
    name: str
    price: float
    stock: int = 0
    description: Optional[str] = None


@router.get("/")
async def root():
    return {"message": "Estas en la seccion de admin"}

@router.get("/postgre")
async def root():
    return client.sb.test()
    