SELECT
    a.id,
    a.nombre,
    a.edificio,
    a.descripcion,
    a.capacidad,
    e.nombre AS escuela
FROM school.aulas a
JOIN school.escuela e ON e.id = a.escuela_id
ORDER BY a.nombre;
