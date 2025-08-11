from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from . import cryptfernet as crypt
from . import fbcrowned as fb
from . import sbpostgre as sb

# Creamos el router para los usuarios
router = APIRouter(
    prefix="/default",
    tags=["default"],
    responses={404: {"description": "No encontrado"}},
)

# Instancia de los objetos de firebase y postgres
class default():
    def __init__(self):
        self.fb = fb.fbCrowned()
        self.sb = sb.sbPostgre()
        self.crypt = crypt.CryptFernet()
client = default()

# Modelo de datos para todos los usuarios registrados
class User(BaseModel):
    uid: str
    nombre: str
    apellidopaterno: str
    apellidomaterno: str    
    email: str
    telefono: str
    rol: str
    activo: bool = True
    fecha_creacion: datetime
    ultimo_login: datetime
    fkey: int


@router.get("/")
async def root():
    return {"message": "Estas en la seccion default"}

@router.get("/user")
async def root(uid: str):
    try:
        return client.fb.obtener_usuario(uid)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving user data: {e}")

@router.post("/registrar")
async def root(request: User):
    res = client.fb.registrar(request)
    return {"message": res}

