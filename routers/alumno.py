from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from . import cryptfernet as crypt
from . import fbcrowned as fb
from . import sbpostgre as sb


def load_sql(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
# Instancia de los objetos de firebase y postgres
class default():
    def __init__(self):
        self.fb = fb.fbCrowned()
        self.sb = sb.sbPostgre()
        self.crypt = crypt.CryptFernet()
client = default()


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

@router.get("/horarios")
async def root(uid: str):
    sbid = client.fb.fkey(uid)
    client.sb.connect()
    querry = load_sql('./querrys/get_horario_alumno.sql')
    with client.sb.connection.cursor() as cursor:
        try:
            cursor.execute(querry, (sbid,))
            result = cursor.fetchall()
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error executing query: {e}")
        finally:
            client.sb.disconnect()

    return {"message": "Estas en la seccion de alumno"} 