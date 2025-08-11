SELECT 
    c.id AS calificacion_id,
    m.nombre AS materia,
    cu.nombre AS curso,
    g.nombre AS grupo,
    c.parcial,
    c.a1,
    c.a2,
    c.a3,
    c.pm,
    c.examen,
    c.asistencia,
    c.participacion
FROM school.calificaciones c
JOIN school.materias m ON m.id = c.materia_id
JOIN school.cursos cu ON cu.id = m.curso_id
JOIN school.grupos g ON g.curso_id = cu.id
JOIN school.alumnos a ON a.grupo_id = g.id
WHERE c.alumno_id = %s
ORDER BY m.nombre, c.parcial;