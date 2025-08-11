SELECT 
    hg.id AS horario_id,
    m.nombre AS materia,
    g.nombre AS grupo,
    a.nombre AS aula,
    hg.dia_semana,
    hg.hora_inicio,
    hg.hora_fin
FROM school.horariosgrupo hg
JOIN school.materias m ON m.id = hg.materia_id
JOIN school.grupos g ON g.id = hg.grupo_id
JOIN school.aulas a ON a.id = hg.aulas_id
WHERE hg.docente_id = %s
ORDER BY 
    CASE 
        WHEN hg.dia_semana = 'Lunes' THEN 1
        WHEN hg.dia_semana = 'Martes' THEN 2
        WHEN hg.dia_semana = 'Miércoles' THEN 3
        WHEN hg.dia_semana = 'Jueves' THEN 4
        WHEN hg.dia_semana = 'Viernes' THEN 5
        WHEN hg.dia_semana = 'Sábado' THEN 6
        WHEN hg.dia_semana = 'Domingo' THEN 7
        ELSE 8
    END,
    hg.hora_inicio;
