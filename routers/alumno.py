from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from . import fbcrowned as fb
from . import sbpostgre as sb

# Creamos el router para los usuarios
router = APIRouter(
    prefix="/alumno",
    tags=["alumno"],
    responses={404: {"description": "No encontrado"}},
)

# Modelo de datos para Usuario
class Alumno(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    active: bool = True

@router.get("/")
async def root():
    return {"message": "Estas en la seccion de alumno"}