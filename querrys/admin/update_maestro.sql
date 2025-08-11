UPDATE school.docentes
SET
    nombre = %s,
    email = %s,
    telefono = %s,
    escuela_id = %s,
    especialidad = %s,
    activo = %s
WHERE id = %s;
