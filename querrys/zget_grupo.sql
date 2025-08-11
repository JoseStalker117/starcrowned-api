SELECT
    g.id,
    g.nombre,
    c.nombre AS curso,
    g.anio_lectivo,
    g.turno
FROM school.grupos g
JOIN school.cursos c ON c.id = g.curso_id
ORDER BY g.nombre;
