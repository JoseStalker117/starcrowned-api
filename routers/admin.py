from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from . import fbcrowned as fb
from . import sbpostgre as sb

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
    sbconnect = sb.sbPostgre()
    return sbconnect.test()
    