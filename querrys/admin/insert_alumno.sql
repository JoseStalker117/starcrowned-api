INSERT INTO school.alumnos (
    nombre,
    email,
    telefono,
    grupo_id,
    fecha_nacimiento,
    fecha_registro
) VALUES (
    %s,  -- nombre
    %s,  -- email
    %s,  -- telefono
    %s,  -- grupo_id
    %s,  -- fecha_nacimiento
    %s   -- fecha_registro
);
