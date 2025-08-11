INSERT INTO school.calificaciones (
    alumno_id,
    materia_id,
    parcial,
    a1,
    a2,
    a3,
    pm,
    examen,
    asistencia,
    participacion
) VALUES (
    %s,  -- alumno_id
    %s,  -- materia_id
    %s,  -- parcial (1, 2 o 3)
    %s,  -- a1
    %s,  -- a2
    %s,  -- a3
    %s,  -- pm
    %s,  -- examen
    %s,  -- asistencia
    %s   -- participacion
);
