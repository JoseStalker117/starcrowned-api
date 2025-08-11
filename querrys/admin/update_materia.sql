UPDATE school.materias
SET
    nombre = %s,
    curso_id = %s,
    descripcion = %s
WHERE id = %s;
