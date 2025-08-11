UPDATE school.escuela
SET
    nombre = %s,
    direccion = %s,
    telefono = %s,
    tipo = %s,
    nivel = %s
WHERE id = %s;
