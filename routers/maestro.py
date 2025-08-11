from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
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


# Creamos el router de maestros
router = APIRouter(
    prefix="/maestro",
    tags=["maestro"],
    responses={404: {"description": "No encontrado"}},
)

# Modelo de datos para Orden
class Maestro(BaseModel):
    product_id: int
    quantity: int
    price: float


@router.get("/")
async def root():
    return {"message": "Estas en la seccion de maestros"}