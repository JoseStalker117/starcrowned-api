SELECT 
    a.id,
    a.nombre,
    a.email,
    a.telefono,
    a.fecha_nacimiento,
    a.fecha_registro,
    g.nombre AS grupo,
    e.nombre AS escuela
FROM school.alumnos a
JOIN school.grupos g ON g.id = a.grupo_id
JOIN school.cursos c ON c.id = g.curso_id
JOIN school.escuela e ON e.id = c.escuela_id
WHERE a.id = %s;
