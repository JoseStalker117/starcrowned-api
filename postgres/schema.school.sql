CREATE TABLE school.escuela (
  id bigint GENERATED ALWAYS AS IDENTITY NOT NULL,
  nombre character varying NOT NULL,
  direccion text,
  telefono character varying,
  tipo text,
  nivel text,
  CONSTRAINT escuela_pkey PRIMARY KEY (id)
);
CREATE TABLE school.aulas (
  id bigint GENERATED ALWAYS AS IDENTITY NOT NULL,
  nombre character varying NOT NULL,
  edificio text NOT NULL,
  descripcion text,
  capacidad integer CHECK (capacidad > 0),
  escuela_id bigint NOT NULL,
  CONSTRAINT aulas_pkey PRIMARY KEY (id),
  CONSTRAINT aulas_escuela_id_fkey FOREIGN KEY (escuela_id) REFERENCES school.escuela(id)
);
CREATE TABLE school.cursos (
  id bigint GENERATED ALWAYS AS IDENTITY NOT NULL,
  nombre character varying NOT NULL,
  descripcion text,
  escuela_id bigint NOT NULL,
  anio_lectivo date,
  grado character varying,
  CONSTRAINT cursos_pkey PRIMARY KEY (id),
  CONSTRAINT cursos_escuela_id_fkey FOREIGN KEY (escuela_id) REFERENCES school.escuela(id)
);
CREATE TABLE school.docentes (
  id bigint GENERATED ALWAYS AS IDENTITY NOT NULL,
  nombre character varying NOT NULL,
  email character varying UNIQUE,
  telefono character varying,
  escuela_id bigint NOT NULL,
  especialidad text,
  fecha_ingreso date,
  activo boolean,
  CONSTRAINT docentes_pkey PRIMARY KEY (id),
  CONSTRAINT docentes_escuela_id_fkey FOREIGN KEY (escuela_id) REFERENCES school.escuela(id)
);
CREATE TABLE school.grupos (
  id bigint GENERATED ALWAYS AS IDENTITY NOT NULL,
  nombre character varying NOT NULL,
  curso_id bigint NOT NULL,
  anio_lectivo date,
  turno text,
  CONSTRAINT grupos_pkey PRIMARY KEY (id),
  CONSTRAINT grupos_curso_id_fkey FOREIGN KEY (curso_id) REFERENCES school.cursos(id)
);
CREATE TABLE school.materias (
  id bigint GENERATED ALWAYS AS IDENTITY NOT NULL,
  nombre character varying NOT NULL,
  curso_id bigint NOT NULL,
  descripcion text,
  CONSTRAINT materias_pkey PRIMARY KEY (id),
  CONSTRAINT materias_curso_id_fkey FOREIGN KEY (curso_id) REFERENCES school.cursos(id)
);
CREATE TABLE school.alumnos (
  id bigint GENERATED ALWAYS AS IDENTITY NOT NULL,
  nombre character varying NOT NULL,
  email character varying UNIQUE,
  telefono character varying,
  grupo_id bigint NOT NULL,
  fecha_nacimiento date,
  fecha_registro date,
  CONSTRAINT alumnos_pkey PRIMARY KEY (id),
  CONSTRAINT alumnos_grupo_id_fkey FOREIGN KEY (grupo_id) REFERENCES school.grupos(id)
);
CREATE TABLE school.estadoasistencia (
  id bigint GENERATED ALWAYS AS IDENTITY NOT NULL,
  estatus text NOT NULL,
  CONSTRAINT estadoasistencia_pkey PRIMARY KEY (id)
);
CREATE TABLE school.horariosgrupo (
  id bigint GENERATED ALWAYS AS IDENTITY NOT NULL,
  grupo_id bigint,
  materia_id bigint NOT NULL,
  docente_id bigint NOT NULL,
  dia_semana text,
  hora_inicio time without time zone,
  hora_fin time without time zone,
  aulas_id bigint NOT NULL,
  CONSTRAINT horariosgrupo_pkey PRIMARY KEY (id),
  CONSTRAINT horariosgrupo_grupo_id_fkey FOREIGN KEY (grupo_id) REFERENCES school.grupos(id),
  CONSTRAINT horariosgrupo_docente_id_fkey FOREIGN KEY (docente_id) REFERENCES school.docentes(id),
  CONSTRAINT horariosgrupo_materia_id_fkey FOREIGN KEY (materia_id) REFERENCES school.materias(id),
  CONSTRAINT horariosgrupo_aulas_id_fkey FOREIGN KEY (aulas_id) REFERENCES school.aulas(id)
);
CREATE TABLE school.asistencias (
  id bigint GENERATED ALWAYS AS IDENTITY NOT NULL,
  alumno_id bigint NOT NULL,
  fecha date NOT NULL,
  estado_id bigint NOT NULL,
  hora time without time zone,
  horarios_id bigint NOT NULL,
  CONSTRAINT asistencias_pkey PRIMARY KEY (id),
  CONSTRAINT asistencias_alumno_id_fkey FOREIGN KEY (alumno_id) REFERENCES school.alumnos(id),
  CONSTRAINT asistencias_estadoasistencia_id_fkey FOREIGN KEY (estado_id) REFERENCES school.estadoasistencia(id),
  CONSTRAINT asistencias_horarios_fkey FOREIGN KEY (horarios_id) REFERENCES school.horariosgrupo(id)
);
CREATE TABLE school.calificaciones (
  id bigint GENERATED ALWAYS AS IDENTITY NOT NULL,
  alumno_id bigint NOT NULL,
  materia_id bigint NOT NULL,
  parcial integer NOT NULL CHECK (parcial >= 1 AND parcial <= 3),
  a1 integer CHECK (a1 >= 0 AND a1 <= 10),
  a2 integer CHECK (a2 >= 0 AND a2 <= 10),
  a3 integer CHECK (a3 >= 0 AND a3 <= 10),
  pm integer CHECK (pm >= 0 AND pm <= 10),
  examen integer CHECK (examen >= 0 AND examen <= 10),
  asistencia integer CHECK (asistencia >= 0 AND asistencia <= 10),
  participacion integer CHECK (participacion >= 0 AND participacion <= 10),
  CONSTRAINT calificaciones_pkey PRIMARY KEY (id),
  CONSTRAINT calificaciones_alumno_id_fkey FOREIGN KEY (alumno_id) REFERENCES school.alumnos(id),
  CONSTRAINT calificaciones_materia_id_fkey FOREIGN KEY (materia_id) REFERENCES school.materias(id)
);
CREATE TABLE school.cuotas (
  id bigint GENERATED ALWAYS AS IDENTITY NOT NULL,
  alumno_id bigint NOT NULL,
  descripcion text,
  monto numeric,
  pagado boolean,
  fecha_vencimiento date,
  fecha_pago date,
  CONSTRAINT cuotas_pkey PRIMARY KEY (id),
  CONSTRAINT cuotas_alumno_id_fkey FOREIGN KEY (alumno_id) REFERENCES school.alumnos(id)
);
CREATE TABLE school.inscripciones (
  id bigint GENERATED ALWAYS AS IDENTITY NOT NULL,
  alumno_id bigint NOT NULL,
  fecha_inscripcion date,
  activo boolean DEFAULT true,
  CONSTRAINT inscripciones_pkey PRIMARY KEY (id),
  CONSTRAINT inscripciones_alumno_id_fkey FOREIGN KEY (alumno_id) REFERENCES school.alumnos(id)
);