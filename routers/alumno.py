from fastapi import APIRouter, HTTPException, status
from . import cryptfernet as crypt
from . import fbcrowned as fb
from . import sbpostgre as sb
from . import modelos


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



@router.get("/asistencias")
async def get_asistencias(uid: str):
    sbid = client.fb.fkey(uid)
    client.sb.connect()
    querry = load_sql('./querrys/alumno/get_asistencia.sql')
    with client.sb.connection.cursor() as cursor:
        try:
            cursor.execute(querry, (sbid,))
            result = cursor.fetchall()
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error executing query: {e}")
        finally:
            client.sb.disconnect()

@router.get("/calificaciones")
async def get_calificaciones(uid: str):
    sbid = client.fb.fkey(uid)
    client.sb.connect()
    querry = load_sql('./querrys/alumno/get_calificacion.sql')
    with client.sb.connection.cursor() as cursor:
        try:
            cursor.execute(querry, (sbid,))
            result = cursor.fetchall()
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error executing query: {e}")
        finally:
            client.sb.disconnect()

@router.get("/cuotas")
async def get_cuotas(uid: str):
    sbid = client.fb.fkey(uid)
    client.sb.connect()
    querry = load_sql('./querrys/alumno/get_cuotas.sql')
    with client.sb.connection.cursor() as cursor:
        try:
            cursor.execute(querry, (sbid,))
            result = cursor.fetchall()
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error executing query: {e}")
        finally:
            client.sb.disconnect()

@router.get("/horarios")
async def root(uid: str):
    sbid = client.fb.fkey(uid)
    client.sb.connect()
    querry = load_sql('./querrys/alumno/get_horario.sql')
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

@router.get("/perfil")
async def get_perfil(uid: str):
    sbid = client.fb.fkey(uid)
    client.sb.connect()
    querry = load_sql('./querrys/alumno/get_perfil.sql')
    with client.sb.connection.cursor() as cursor:
        try:
            cursor.execute(querry, (sbid,))
            result = cursor.fetchone()
            if result:
                return result
            else:
                raise HTTPException(status_code=404, detail="Perfil no encontrado")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error executing query: {e}")
        finally:
            client.sb.disconnect()