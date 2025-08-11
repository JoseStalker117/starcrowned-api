SELECT 
    d.id,
    d.nombre,
    d.email,
    d.telefono,
    d.especialidad,
    d.fecha_ingreso,
    d.activo,
    e.nombre AS escuela
FROM school.docentes d
JOIN school.escuela e ON e.id = d.escuela_id
WHERE d.id = %s;
