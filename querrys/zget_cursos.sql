SELECT
    c.id,
    c.nombre,
    c.descripcion,
    e.nombre AS escuela,
    c.anio_lectivo,
    c.grado
FROM school.cursos c
JOIN school.escuela e ON e.id = c.escuela_id
ORDER BY c.nombre;
