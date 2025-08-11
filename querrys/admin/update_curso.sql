UPDATE school.cursos
SET
    nombre = %s,
    descripcion = %s,
    escuela_id = %s,
    anio_lectivo = %s,
    grado = %s
WHERE id = %s;
