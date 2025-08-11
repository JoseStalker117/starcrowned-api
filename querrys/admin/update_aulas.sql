UPDATE school.aulas
SET
    nombre = %s,
    edificio = %s,
    descripcion = %s,
    capacidad = %s,
    escuela_id = %s
WHERE id = %s;
