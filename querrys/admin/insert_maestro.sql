INSERT INTO school.docentes (
    nombre,
    email,
    telefono,
    escuela_id,
    especialidad,
    fecha_ingreso,
    activo
) VALUES (
    %s,  -- nombre
    %s,  -- email
    %s,  -- telefono
    %s,  -- escuela_id
    %s,  -- especialidad
    %s,  -- fecha_ingreso
    %s   -- activo (true/false)
);
