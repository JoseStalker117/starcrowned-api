from typing import List, Optional
from pydantic import BaseModel
from datetime import date, time, datetime

#DEFAULT MODELS
class Usuario(BaseModel):
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


# ALUMNO MODELS
class Alumno(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    active: bool = True
    
# MAESTRO MODELS
class Asistencia(BaseModel):
    alumno_id: int
    fecha: date
    estado_id: int
    hora: time
    horarios_id: int

class Calificacion(BaseModel):
    alumno_id: int
    materia_id: int
    parcial: int
    a1: int
    a2: int
    a3: int
    pm: int
    examen: int
    asistencia: int
    participacion: int
    
# ADMIN MODELS
class Admin(BaseModel):
    id: Optional[int] = None
    name: str
    price: float
    stock: int = 0
    description: Optional[str] = None
