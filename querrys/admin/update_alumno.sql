UPDATE school.alumnos
SET
    nombre = %s,
    email = %s,
    telefono = %s,
    grupo_id = %s,
    fecha_nacimiento = %s,
    fecha_registro = %s
WHERE id = %s;
