from fastapi import APIRouter, HTTPException, status
from typing import List
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


# Creamos el router de maestros
router = APIRouter(
    prefix="/maestro",
    tags=["maestro"],
    responses={404: {"description": "No encontrado"}},
)


@router.get("/alumnos")
async def root(uid: str):
    if client.fb.roles(uid) != 'maestro':
        raise HTTPException(status_code=403, detail="No tienes permiso para realizar esta acción")
    sbid = client.fb.fkey(uid)
    client.sb.connect()
    querry = load_sql('./querrys/maestro/get_alumnos.sql')
    with client.sb.connection.cursor() as cursor:
        try:
            cursor.execute(querry, (sbid,))
            result = cursor.fetchall()
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error executing query: {e}")
        finally:
            client.sb.disconnect()
            
@router.get("/horario")
async def get_horario(uid: str):
    if client.fb.roles(uid) != 'maestro':
        raise HTTPException(status_code=403, detail="No tienes permiso para realizar esta acción")
    sbid = client.fb.fkey(uid)
    client.sb.connect()
    querry = load_sql('./querrys/maestro/get_horario.sql')
    with client.sb.connection.cursor() as cursor:
        try:
            cursor.execute(querry, (sbid,))
            result = cursor.fetchall()
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error executing query: {e}")
        finally:
            client.sb.disconnect()
            
@router.get("/perfil")
async def get_perfil(uid: str):
    if client.fb.roles(uid) != 'maestro':
        raise HTTPException(status_code=403, detail="No tienes permiso para realizar esta acción")
    sbid = client.fb.fkey(uid)
    client.sb.connect()
    querry = load_sql('./querrys/maestro/get_perfil.sql')
    with client.sb.connection.cursor() as cursor:
        try:
            cursor.execute(querry, (sbid,))
            result = cursor.fetchall()
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error executing query: {e}")
        finally:
            client.sb.disconnect()
            
@router.post("/asistencias")
async def post_asistencia(uid: str, asistencia: List[modelos.Asistencia]):
    if client.fb.roles(uid) != 'maestro':
        raise HTTPException(status_code=403, detail="No tienes permiso para realizar esta acción")
    client.sb.connect()
    querry = load_sql('./querrys/maestro/insert_asistencia.sql')
    with client.sb.connection.cursor() as cursor:
        try:
            params = [
                (item.alumno_id, 
                 item.fecha, 
                 item.estado_id, 
                 item.hora, 
                 item.horarios_id)
                for item in asistencia
                ]
            cursor.executemany(querry, params)
            client.sb.connection.commit()
            return {"message": "Asistencia registrada correctamente"}
        except Exception as e:
            client.sb.connection.rollback()
            raise HTTPException(status_code=500, detail=f"Error executing query: {e}")
        finally:
            client.sb.disconnect()
            
@router.get("/calificaciones")
async def get_calificaciones(uid: str, calificacion: List[modelos.Calificacion]):
    if client.fb.roles(uid) != 'maestro':
        raise HTTPException(status_code=403, detail="No tienes permiso para realizar esta acción")
    client.sb.connect()
    querry = load_sql('./querrys/maestro/insert_calificaciones.sql')
    with client.sb.connection.cursor() as cursor:
        params = [
            (item.alumno_id, 
             item.materia_id, 
             item.parcial, 
             item.a1, 
             item.a2, 
             item.a3, 
             item.pm, 
             item.examen, 
             item.asistencia, 
             item.participacion)
            for item in calificacion
        ]
        try:
            cursor.executemany(querry, params)
            client.sb.connection.commit()
            return {"message": "Calificaciones registradas correctamente"}
        except Exception as e:
            client.sb.connection.rollback()
            raise HTTPException(status_code=500, detail=f"Error executing query: {e}")
        finally:
            client.sb.disconnect()
            
@router.get("/update_asistencia")
async def update_asistencia(uid: str, id_asistencia: int, status: int):
    if client.fb.roles(uid) != 'maestro':
        raise HTTPException(status_code=403, detail="No tienes permiso para realizar esta acción")
    client.sb.connect()
    querry = load_sql('./querrys/maestro/update_asistencia.sql')
    with client.sb.connection.cursor() as cursor:
        try:
            cursor.execute(querry, (status, id_asistencia))
            client.sb.connection.commit()
            return {"message": "Asistencia actualizada correctamente"}
        except Exception as e:
            client.sb.connection.rollback()
            raise HTTPException(status_code=500, detail=f"Error executing query: {e}")
        finally:
            client.sb.disconnect()
            
@router.get("/update_calificacion")
async def update_calificacion(uid: str, calificacion: List[modelos.Calificacion]):
    if client.fb.roles(uid) != 'maestro':
        raise HTTPException(status_code=403, detail="No tienes permiso para realizar esta acción")
    client.sb.connect()
    querry = load_sql('./querrys/maestro/update_calificaciones.sql')
    with client.sb.connection.cursor() as cursor:
        params = [
            (item.a1, 
             item.a2, 
             item.a3, 
             item.pm, 
             item.examen, 
             item.asistencia, 
             item.participacion, 
             item.alumno_id, 
             item.materia_id, 
             item.parcial)
            for item in calificacion
        ]
        try:
            cursor.executemany(querry, params)
            client.sb.connection.commit()
            return {"message": "Calificaciones actualizadas correctamente"}
        except Exception as e:
            client.sb.connection.rollback()
            raise HTTPException(status_code=500, detail=f"Error executing query: {e}")
        finally:
            client.sb.disconnect()