SELECT
    c.id AS cuota_id,
    a.nombre AS alumno,
    g.nombre AS grupo,
    c.descripcion,
    c.monto,
    c.pagado,
    c.fecha_vencimiento,
    c.fecha_pago
FROM school.cuotas c
JOIN school.alumnos a ON a.id = c.alumno_id
JOIN school.grupos g ON g.id = a.grupo_id
WHERE c.alumno_id = %s
ORDER BY c.fecha_vencimiento DESC;
