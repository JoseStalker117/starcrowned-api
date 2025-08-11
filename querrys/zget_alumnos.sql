SELECT
    a.id AS alumno_id,
    a.nombre,
    a.email,
    a.telefono,
    a.fecha_nacimiento,
    a.fecha_registro,
    g.nombre AS grupo
FROM school.alumnos a
LEFT JOIN school.grupos g ON g.id = a.grupo_id
ORDER BY a.nombre;
