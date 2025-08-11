SELECT h.id, m.nombre AS materia, h.dia_semana, h.hora_inicio, h.hora_fin, a.nombre AS aula
FROM school.horariosgrupo h
JOIN school.materias m ON m.id = h.materia_id
JOIN school.aulas a ON a.id = h.aulas_id
JOIN school.grupos g ON g.id = h.grupo_id
JOIN school.alumnos al ON al.grupo_id = g.id
WHERE al.id = %s
ORDER BY h.dia_semana, h.hora_inicio;
