INSERT INTO school.asistencias (
    alumno_id,
    fecha,
    estado_id,
    hora,
    horarios_id
) VALUES (
    %s,  -- alumno_id
    %s,  -- fecha
    %s,  -- estado_id (referencia a estadoasistencia)
    %s,  -- hora
    %s   -- horarios_id
);
