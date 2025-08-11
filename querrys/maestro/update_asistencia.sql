UPDATE school.asistencias
SET 
    estado_id = %s
WHERE id = %s;  -- id del registro de asistencia
