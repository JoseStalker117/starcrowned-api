SELECT DISTINCT
    al.id AS alumno_id,
    al.nombre,
    al.email,
    al.telefono,
    al.fecha_nacimiento,
    al.fecha_registro,
    g.nombre AS grupo
FROM school.alumnos al
JOIN school.grupos g ON g.id = al.grupo_id
JOIN school.horariosgrupo hg ON hg.grupo_id = g.id
WHERE hg.docente_id = %s
ORDER BY al.nombre;
