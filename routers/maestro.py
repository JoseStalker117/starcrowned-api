from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from . import fbcrowned as fb

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