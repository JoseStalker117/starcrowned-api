SELECT
    m.id,
    m.nombre,
    m.descripcion,
    c.nombre AS curso
FROM school.materias m
JOIN school.cursos c ON c.id = m.curso_id
ORDER BY m.nombre;
