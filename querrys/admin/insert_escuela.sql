INSERT INTO school.escuela (
    nombre,
    direccion,
    telefono,
    tipo,
    nivel
) VALUES (
    %s,  -- nombre
    %s,  -- direccion
    %s,  -- telefono
    %s,  -- tipo
    %s   -- nivel
);
