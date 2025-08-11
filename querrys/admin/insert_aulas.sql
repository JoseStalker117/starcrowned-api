INSERT INTO school.aulas (
    nombre,
    edificio,
    descripcion,
    capacidad,
    escuela_id
) VALUES (
    %s,  -- nombre
    %s,  -- edificio
    %s,  -- descripcion
    %s,  -- capacidad (entero > 0)
    %s   -- escuela_id
);
