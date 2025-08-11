UPDATE school.grupos
SET
    nombre = %s,
    curso_id = %s,
    anio_lectivo = %s,
    turno = %s
WHERE id = %s;
