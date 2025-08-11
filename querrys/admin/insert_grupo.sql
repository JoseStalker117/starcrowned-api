INSERT INTO school.grupos (
    nombre,
    curso_id,
    anio_lectivo,
    turno
) VALUES (
    %s,  -- nombre
    %s,  -- curso_id
    %s,  -- anio_lectivo (date)
    %s   -- turno
);
