SELECT 
    a.id AS asistencia_id,
    m.nombre AS materia,
    g.nombre AS grupo,
    au.nombre AS aula,
    ea.estatus AS estado_asistencia,
    a.fecha,
    a.hora
FROM school.asistencias a
JOIN school.estadoasistencia ea ON ea.id = a.estado_id
JOIN school.horariosgrupo hg ON hg.id = a.horarios_id
JOIN school.materias m ON m.id = hg.materia_id
JOIN school.grupos g ON g.id = hg.grupo_id
JOIN school.aulas au ON au.id = hg.aulas_id
WHERE a.alumno_id = %s
ORDER BY a.fecha DESC, a.hora;
