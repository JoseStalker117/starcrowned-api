INSERT INTO school.cursos (
    nombre,
    descripcion,
    escuela_id,
    anio_lectivo,
    grado
) VALUES (
    %s,  -- nombre
    %s,  -- descripcion
    %s,  -- escuela_id
    %s,  -- anio_lectivo (date)
    %s   -- grado
);
