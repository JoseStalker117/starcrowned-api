UPDATE school.calificaciones
SET 
    a1 = %s,
    a2 = %s,
    a3 = %s,
    pm = %s,
    examen = %s,
    asistencia = %s,
    participacion = %s
WHERE 
    alumno_id = %s AND
    materia_id = %s AND
    parcial = %s;
