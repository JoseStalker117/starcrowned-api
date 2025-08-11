-- school.escuela
INSERT INTO school.escuela (nombre, direccion, telefono, tipo, nivel) VALUES
('Instituto Científico del Norte', 'Av. Reforma 123, Monterrey, NL', '8181234567', 'Privada', 'Secundaria'),
('Colegio Nacional', 'Calle Juárez 55, Saltillo, COAH', '8447654321', 'Pública', 'Preparatoria'),
('Centro Educativo del Sur', 'Blvd. Independencia 231, Torreón, COAH', '8711122334', 'Privada', 'Primaria'),
('Escuela Técnica 14', 'Prolongación Hidalgo 451, Monterrey, NL', '8187654321', 'Pública', 'Secundaria'),
('Instituto Patria', 'Camino Real 98, San Pedro, NL', '8189988776', 'Privada', 'Preparatoria');

-- school.estadoasistencia
INSERT INTO school.estadoasistencia (estatus) VALUES
('Presente'),
('Ausente'),
('Tarde'),
('Justificado'),
('Retardo');

-- school.cursos
INSERT INTO school.cursos (nombre, descripcion, escuela_id, anio_lectivo, grado) VALUES
('1er Año', 'Primer año de secundaria', 1, '2025-08-01', '1'),
('2do Año', 'Segundo año de secundaria', 1, '2025-08-01', '2'),
('3er Año', 'Tercer año de secundaria', 1, '2025-08-01', '3'),
('1er Año Prepa', 'Primer año de preparatoria', 2, '2025-08-01', '4'),
('2do Año Prepa', 'Segundo año de preparatoria', 2, '2025-08-01', '5');

-- school.materias
INSERT INTO school.materias (nombre, curso_id, descripcion) VALUES
('Matemáticas I', 1, 'Álgebra básica y aritmética'),
('Ciencias Naturales', 1, 'Biología y medio ambiente'),
('Historia de México', 2, 'Desde la colonia hasta la independencia'),
('Física I', 4, 'Movimiento y leyes de Newton'),
('Literatura Universal', 5, 'Análisis de obras clásicas');

-- school.docentes
INSERT INTO school.docentes (nombre, email, telefono, escuela_id, especialidad, fecha_ingreso, activo) VALUES
('Carlos Mendoza', 'cmendoza@escuela.edu.mx', '8182345671', 1, 'Matemáticas', '2020-08-15', true),
('Laura García', 'lgarcia@escuela.edu.mx', '8189988776', 1, 'Ciencias Naturales', '2019-08-15', true),
('Ricardo Pérez', 'rperez@escuela.edu.mx', '8441234567', 2, 'Historia', '2018-08-15', true),
('Ana Torres', 'atorres@escuela.edu.mx', '8447654321', 2, 'Física', '2021-01-10', true),
('Julieta Salas', 'jsalas@escuela.edu.mx', '8719988776', 2, 'Literatura', '2022-09-01', true);

-- school.aulas
INSERT INTO school.aulas (nombre, edificio, descripcion, capacidad, escuela_id) VALUES
('Aula 101', 'Edificio A', 'Salón de matemáticas', 30, 1),
('Aula 102', 'Edificio A', 'Salón de ciencias', 28, 1),
('Aula 201', 'Edificio B', 'Salón de historia', 32, 2),
('Laboratorio 1', 'Edificio C', 'Laboratorio de física', 25, 2),
('Aula 301', 'Edificio D', 'Literatura y lectura', 30, 2);

-- school.grupos
INSERT INTO school.grupos (nombre, curso_id, anio_lectivo, turno) VALUES
('1A', 1, '2025-08-01', 'Matutino'),
('1B', 1, '2025-08-01', 'Vespertino'),
('2A', 2, '2025-08-01', 'Matutino'),
('3A', 3, '2025-08-01', 'Matutino'),
('4A', 4, '2025-08-01', 'Matutino');

-- school.alumnos
INSERT INTO school.alumnos (nombre, email, telefono, grupo_id, fecha_nacimiento, fecha_registro) VALUES
('Luis Fernández', 'luis.fernandez@example.com', '8181122233', 1, '2011-04-10', '2025-08-01'),
('María López', 'maria.lopez@example.com', '8183344556', 1, '2011-06-25', '2025-08-01'),
('Juan Hernández', 'juan.hernandez@example.com', '8185566778', 2, '2011-08-15', '2025-08-01'),
('Ana Martínez', 'ana.martinez@example.com', '8187788990', 3, '2010-12-01', '2025-08-01'),
('Pedro Gómez', 'pedro.gomez@example.com', '8189900112', 4, '2009-09-20', '2025-08-01');

-- school.horariosgrupo
INSERT INTO school.horariosgrupo (grupo_id, materia_id, docente_id, dia_semana, hora_inicio, hora_fin, aulas_id) VALUES
(1, 1, 1, 'Lunes', '08:00', '09:00', 1),
(1, 2, 2, 'Martes', '08:00', '09:00', 2),
(3, 3, 3, 'Miércoles', '09:00', '10:00', 3),
(4, 4, 4, 'Jueves', '10:00', '11:00', 4),
(5, 5, 5, 'Viernes', '11:00', '12:00', 5);

-- school.asistencias
INSERT INTO school.asistencias (alumno_id, fecha, estado_id, hora, horarios_id) VALUES
(1, '2025-08-04', 1, '08:00', 1),
(2, '2025-08-04', 1, '08:00', 1),
(3, '2025-08-04', 2, '09:00', 2),
(4, '2025-08-04', 3, '10:00', 3),
(5, '2025-08-04', 1, '11:00', 4);

-- school.calificaciones
INSERT INTO school.calificaciones (alumno_id, materia_id, parcial, a1, a2, a3, pm, examen, asistencia, participacion) VALUES
(1, 1, 1, 9, 8, 10, 9, 8, 10, 9),
(2, 1, 1, 8, 8, 7, 8, 9, 9, 8),
(3, 2, 1, 7, 7, 8, 7, 7, 8, 7),
(4, 3, 1, 6, 7, 7, 7, 6, 8, 8),
(5, 4, 1, 10, 10, 10, 10, 10, 10, 10);

-- school.cuotas
INSERT INTO school.cuotas (alumno_id, descripcion, monto, pagado, fecha_vencimiento, fecha_pago) VALUES
(1, 'Inscripción anual', 1500.00, true, '2025-07-31', '2025-07-15'),
(2, 'Mensualidad agosto', 500.00, false, '2025-08-10', NULL),
(3, 'Mensualidad agosto', 500.00, true, '2025-08-10', '2025-08-02'),
(4, 'Inscripción anual', 1500.00, true, '2025-07-31', '2025-07-20'),
(5, 'Mensualidad agosto', 500.00, false, '2025-08-10', NULL);

-- school.inscripciones
INSERT INTO school.inscripciones (alumno_id, fecha_inscripcion, activo) VALUES
(1, '2025-07-15', true),
(2, '2025-07-16', true),
(3, '2025-07-17', true),
(4, '2025-07-18', true),
(5, '2025-07-19', true);
