# Ejercicios de Transacciones y Control de Concurrencia

A continuación se desarrollan todos los ejercicios solicitados sobre transacciones y control de concurrencia, abordando cada pregunta con explicaciones profundas, estructuradas y detalladas, en base a principios de bases de datos distribuidas y conforme a los estándares de SQL.

---

## 1. Modelo Abstracto del Sistema de Transacciones en un SGBD Distribuido (ACID)

### Enunciado

Explique detalladamente el Modelo Abstracto del Sistema de Transacciones en un Sistema de Bases de Datos Distribuidas orientado a asegurar las propiedades ACID.

### Desarrollo

Un modelo abstracto de sistema de transacciones distribuido incluye múltiples nodos, cada uno ejecutando parte de una transacción. Para garantizar las propiedades ACID en este contexto complejo, el modelo incorpora los siguientes componentes:

#### Componentes del modelo abstracto

1. **Coordinador Global de la Transacción**
   - Controla la ejecución distribuida.
   - Coordina el protocolo de compromiso (como 2PC).
2. **Gestores de Recursos Locales**
   - Ejecutan operaciones sobre sus bases de datos locales.
   - Aplican control de concurrencia y recuperación local.
3. **Log de Transacciones**
   - Utilizado para asegurar la durabilidad (registro WAL).
   - Escribe antes de aplicar los cambios (write-ahead logging).
4. **Protocolo de Compromiso**
   - Más común: Two-Phase Commit (2PC).
   - Asegura atomicidad y consistencia global.
5. **Control de Concurrencia Distribuido**
   - Mediante protocolos como quorum consensus, bloqueo distribuido, timestamping, etc.
   - Asegura el aislamiento.

#### Aseguramiento de ACID

| Propiedad    | Mecanismo Distribuido                                            |
| ------------ | ---------------------------------------------------------------- |
| Atomicidad   | Coordinación con 2PC y logs en todos los nodos.                  |
| Consistencia | Reglas de integridad local + global; coordinación transaccional. |
| Aislamiento  | Control de concurrencia distribuido (ej. 2PL distribuido).       |
| Durabilidad  | Logs + almacenamiento persistente en cada nodo.                  |

---

## 2. Propiedades de Transacciones según el estándar SQL

### Enunciado

Explique detalladamente las propiedades de las transacciones que deben ser aseguradas por un SGBD conforme al estándar SQL.

### Desarrollo

El estándar SQL (SQL:1992, SQL:2003, etc.) define que todo SGBD debe asegurar las propiedades ACID para cada transacción. Estas propiedades son:

1. **Atomicidad**
   - Una transacción debe completarse completamente o no ejecutarse.
   - SQL lo logra con `ROLLBACK` y `COMMIT`.
2. **Consistencia**
   - Toda transacción debe llevar la BD de un estado válido a otro.
   - Se asegura mediante constraints, triggers y procedimientos.
3. **Aislamiento**
   - SQL define niveles de aislamiento:
     - `READ UNCOMMITTED`: puede haber lecturas sucias.
     - `READ COMMITTED`: sin lecturas sucias.
     - `REPEATABLE READ`: sin lecturas no repetibles.
     - `SERIALIZABLE`: máximo aislamiento (equivalente a ejecución secuencial).
4. **Durabilidad**
   - Una vez que se hace `COMMIT`, los cambios persisten incluso ante fallos.
   - Esto se logra con escritura a logs (WAL).

---

## 3. Gestor de Bloqueos en un SGBD con Control de Concurrencia

### Enunciado

Explique qué entiende por un Gestor de Bloqueos en un SGBD y cómo evitar inanición.

### Desarrollo

#### ¿Qué es un Gestor de Bloqueos?

Es el componente del SGBD encargado de administrar el acceso concurrente a los datos mediante bloqueos (locks).

#### Funciones

- Controlar exclusividad de escritura (locks exclusivos).
- Permitir lectura concurrente (locks compartidos).
- Llevar registro de qué transacciones tienen qué bloqueos.
- Detectar deadlocks (con grafos de espera).

#### Implementación

Estructura: tablas hash o árboles con entradas tipo:

```text
Objeto: Registro R
Estado del lock: Compartido / Exclusivo
Transacciones esperando: [T2, T3]
```

#### Evitar inanición

- Asignación FIFO de locks.
- Uso de protocolos de prioridad (wait-die, wound-wait).
- Límites de tiempo para espera (timeouts).
- Reintentos con backoff exponencial.

---

## 4. Planificación y Serializabilidad

### Enunciado

Explique los conceptos: Planificación, Planificación Secuenciable, Secuencialidad en Cuanto a Conflicto y Vistas.

### Desarrollo

| Concepto                                 | Definición                                                                                                                         |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Planificación                            | Es el orden en que las operaciones (lecturas/escrituras) de múltiples transacciones se intercalan.                                 |
| Planificación Secuenciable               | Aquella planificación que es equivalente a alguna secuencia serial (sin intercalación).                                            |
| Secuencialidad en cuanto a conflicto     | Dos planificaciones son equivalentes si mantienen el orden de operaciones conflictivas (lectura-escritura sobre los mismos datos). |
| Secuencialidad en cuanto a vistas        | Dos planificaciones son equivalentes si cada lectura accede a los mismos valores y el estado final de los datos es el mismo.       |

Nota: La secuencialidad por conflicto es más fácil de comprobar (mediante grafos de precedencia), pero más restrictiva que la de vistas.

---

## 5. Importancia de la Secuencialidad

### Enunciado

Explique qué es una Planificación Secuencial y Secuenciable. Fundamente su importancia.

### Desarrollo

- **Secuencial**: No hay intercalación de operaciones, es decir, T1 termina antes de comenzar T2.
- **Secuenciable**: Intercalación posible, pero equivalente a una secuencia serial.

**Importancia:**

- Garantiza correctitud del sistema.
- Permite concurrencia segura sin resultados erróneos.
- Base para pruebas de serializabilidad en SGBDs.

---

## 6. Definición y Ciclo de Vida de una Transacción

### Enunciado

Defina transacción. Indique fases del ciclo de vida y propiedades que deben asegurarse.

### Desarrollo

#### Definición

Una transacción es una unidad lógica de procesamiento que accede y modifica datos.

#### Fases

1. Inicio (`BEGIN`)
2. Ejecución (`SELECT`, `UPDATE`, etc.)
3. Validación (revisión de conflictos)
4. Compromiso o Aborto (`COMMIT` o `ROLLBACK`)

#### Propiedades

- ACID, como detallado previamente.

---

## 7. Función del Componente de Gestión de Concurrencia y Estructuras

### Enunciado

Describa la función del Componente de Gestión de Concurrencia.

### Desarrollo

#### Función

Evitar conflictos en accesos simultáneos a los datos, asegurando aislamiento y consistencia.

#### Estructura de datos

- Tabla de bloqueos: qué objetos están bloqueados, por quién, y en qué modo.
- Colas de espera: transacciones en espera por recursos.
- Grafo de espera: útil para detección de ciclos (deadlocks).

---

## 8. Protocolo de Bloqueo de 2 Fases

### Enunciado

Describa el protocolo de Bloqueo de 2 Fases y variantes.

### Desarrollo

#### Fases

1. Fase de crecimiento: solo se solicitan nuevos bloqueos.
2. Fase de decrecimiento: solo se liberan bloqueos.

#### Variantes

- 2PL Básico: cumple la regla base.
- 2PL Estricto: los locks se mantienen hasta commit/abort.
- 2PL Rígido: todos los locks (S y X) se liberan al final.

**Garantía:** serializabilidad por conflictos.

---

## 9. Protocolo de Quorum de Consenso

### Enunciado

Describa el protocolo de Quorum de Consenso y condiciones.

### Desarrollo

#### Fundamento

Un sistema replicado exige coordinación para asegurar consistencia. Se define:

- $Q_r$: número de réplicas necesarias para leer.
- $Q_w$: número para escribir.
- $N$: total de réplicas.

#### Condición esencial

- $Q_r + Q_w > N$
- $Q_w > N/2$

#### Protocolos emulados

- **Mayoría**: $Q_r = Q_w = \lceil N/2 \rceil$
- **Sesgado**: Ejemplo: $Q_r = 1$, $Q_w = N$ (óptimo para lectura frecuente).

---

## 10. Propiedades ACID (Repetido)

### Enunciado

Explique propiedades que deben garantizarse según el estándar SQL.

**Ya cubierto en el ejercicio 2.**

---

# Tema 10: Bases de Datos Distribuidas

A continuación se desarrollan las preguntas del Tema 10: Bases de Datos Distribuidas, con explicaciones técnicas detalladas, estructuradas y listas para estudio o examen.

---

## 1. Protocolo de Compromiso de 2 Fases (2PC/C2F)

### Enunciado

Explique detalladamente el Protocolo de Compromiso de 2 Fases aplicado en Sistemas de Bases de Datos Distribuidas y cómo procede:
- (a) Un sitio participante en caso de falla del mismo,
- (b) Los sitios participantes en caso de falla del sitio coordinador.
- Detalle los pasos de cada fase del protocolo C2F.

### Desarrollo

#### Introducción

El Protocolo de Compromiso de 2 Fases (2PC) asegura la atomicidad global de una transacción distribuida: todos los participantes deben comprometer (commit) o abortar la transacción, sin inconsistencias.

#### Fase 1: Fase de Preparación (Voting Phase)

1. El coordinador envía a todos los participantes un mensaje `PREPARE`.
2. Cada participante:
   - Verifica si puede comprometer.
   - Registra en su log local `VOTE-YES` o `VOTE-NO`.
   - Responde con `YES` (puede commit) o `NO` (debe abortar).

#### Fase 2: Fase de Decisión (Commit/Abort Phase)

- Si todos votaron `YES`, el coordinador:
  1. Registra `GLOBAL-COMMIT` en el log.
  2. Envía mensaje `COMMIT` a todos.
- Si algún `NO`, el coordinador:
  1. Registra `GLOBAL-ABORT`.
  2. Informa `ABORT` a todos.

Los participantes realizan el commit o rollback y registran la acción en su log.

#### Fallas y Recuperación

- (a) Si falla un sitio participante:
  - Al reiniciarse, lee su log local:
    - Si registró `VOTE-YES` pero no sabe la decisión final → bloqueado.
    - Debe esperar mensaje del coordinador o consultar a otros participantes.
    - Si no votó → puede abortar localmente.
- (b) Si falla el coordinador:
  - Participantes que votaron `YES` y no recibieron decisión:
    - Bloqueados, no pueden tomar decisión solos (problema del 2PC).
    - Esperan que el coordinador se recupere.
    - Opcional: ejecutan protocolo de recuperación para determinar decisión (consenso entre participantes).

---

## 2. Formas de Almacenamiento Distribuido en Bases de Datos Relacionales

### Enunciado

Explique detalladamente las formas de almacenamiento distribuido en Bases de Datos Distribuidas Relacionales.

### Desarrollo

#### Tipos de almacenamiento distribuido

1. **Fragmentación (Partitioning)**
   - Divide la base de datos en fragmentos y los distribuye.
   - a. Fragmentación Horizontal: Por filas, según predicados. Ejemplo: `Clientes_EEUU`, `Clientes_Europa`.
   - b. Fragmentación Vertical: Por columnas. Requiere incluir PK. Ejemplo: `Cliente_Básico (ID, Nombre)`, `Cliente_Contacto (ID, Email)`.
   - c. Fragmentación Híbrida: Combinación de horizontal + vertical.
2. **Replicación**
   - Copias de fragmentos completos o parciales.
   - a. Total: Todos los nodos tienen una copia.
   - b. Parcial: Solo algunos nodos.
   - Sincronización:
     - Síncrona: cambios reflejados en todas las copias al instante.
     - Asíncrona: cambios propagados posteriormente.
3. **Almacenamiento Combinado**
   - Fragmentación + Replicación.
   - Aumenta disponibilidad y rendimiento.

---

## 3. Estrategia de la Semireunión (Semijoin Strategy)

### Enunciado

Conforme la figura y la consulta `SELECT * FROM R JOIN S`, indique los pasos y el costo total de transmisión al aplicar la Estrategia de la Semireunión si la consulta fue recibida en:
- (a) Sitio 1
- (b) Sitio 2

### Desarrollo

#### Supuestos

- Semijoin reduce el volumen de datos transmitidos al evitar enviar la tabla completa.
- `R` está en Sitio 1, `S` en Sitio 2.

#### Estrategia Semijoin – Pasos

- Si la consulta es recibida en **Sitio 1**:
  1. Sitio 1 extrae los atributos de unión de `R` y proyecta `π_R.A`.
  2. Envía `π_R.A` al Sitio 2.
  3. Sitio 2 filtra solo lo necesario (`π_S.* σ_S.A ∈ π_R.A (S)`).
  4. Sitio 2 envía solo las filas relevantes de `S` al Sitio 1.
  5. Sitio 1 ejecuta el JOIN final.
- Si se recibe en **Sitio 2**:
  1. Proyecta `π_S.A`, la envía a Sitio 1.
  2. Sitio 1 devuelve `σ_R.A ∈ π_S.A (R)`.
  3. Sitio 2 ejecuta el JOIN.

#### Costo Total de Transmisión

Depende de:

- Tamaño de proyección.
- Cantidad de coincidencias.
- Tamaño del resultado del semijoin.

Generalmente, el semijoin reduce el tráfico comparado con enviar tablas completas. Se prefiere cuando hay alta selectividad.

---

# Tema 11: Data Warehousing y OLAP

A continuación se desarrollan las preguntas del Tema 11: Data Warehousing y OLAP, explicadas punto por punto, con ejemplos y esquemas conceptuales listos para usar como base teórica o práctica para exámenes.

---

## 1. Arquitectura de un Data Warehouse (DW) y Características

### Enunciado

Esquematizar la arquitectura de un DW y citar y describir 4 características del Datawarehouse.

### Desarrollo

#### Esquema Conceptual de Arquitectura DW

```text
      +--------------------+
      |  Fuentes de Datos  |
      +--------+-----------+
               ↓
         [ ETL / ELT ]
               ↓
      +--------------------+
      |   Data Warehouse   |
      +--------+-----------+
               ↓
  +------------+------------+
  |                         |
+-----------+         +------------------+
| Data Marts|         | Herramientas OLAP|
+-----------+         +------------------+
                         ↓
                    Reportes / Dashboards
```

#### 4 Características de un Data Warehouse

| Característica            | Descripción                                                      |
| ------------------------- | ---------------------------------------------------------------- |
| Orientado a temas         | Organizado por áreas de negocio (ventas, clientes, etc.).        |
| Integrado                 | Datos unificados de múltiples fuentes con formatos consistentes. |
| No volátil                | Una vez cargados, los datos no se modifican frecuentemente.      |
| Variable en el tiempo     | Mantiene datos históricos para análisis en el tiempo.            |

---

## 2. Tablas de Dimensiones, Hechos y Medidas

### Enunciado

Explique tablas de dimensiones, tablas de hechos y medidas. Dé ejemplos.

### Desarrollo

#### Tablas de Hechos

- Contienen los hechos medibles del negocio.
- Claves foráneas a las tablas de dimensión.
- Ejemplo:

```text
FACT_VENTAS (fecha_id, producto_id, tienda_id, cantidad, total_venta)
```

#### Tablas de Dimensiones

- Aportan contexto descriptivo a los hechos.
- No tienen medidas, sí atributos descriptivos.
- Ejemplo:

```text
DIM_FECHA (fecha_id, día, mes, año)
DIM_PRODUCTO (producto_id, nombre, categoría)
DIM_TIENDA (tienda_id, ciudad, país)
```

#### Medidas

- Valores numéricos agregables: SUM, COUNT, AVG, etc.
- Ejemplos: `cantidad`, `total_venta`, `descuento_aplicado`

---

## 3. Diferencia entre OLTP y OLAP (con ejemplos)

### Enunciado

Explique la diferencia entre bases de datos OLTP y OLAP. Dé ejemplos.

### Desarrollo

| Característica | OLTP                        | OLAP                                |
| -------------- | --------------------------- | ----------------------------------- |
| Propósito      | Transacciones diarias       | Análisis y toma de decisiones       |
| Tipo de datos  | Actualizados, operacionales | Históricos, agregados               |
| Esquema        | Normalizado                 | Desnormalizado (estrella/snowflake) |
| Consultas      | Simples, rápidas            | Complejas, multidimensionales       |
| Ejemplos       | Registro de compras, pagos  | Análisis de ventas por región       |

**Ejemplos OLTP:**

- Sistema bancario de retiros y depósitos
- Aplicación de punto de venta (POS)

**Ejemplos OLAP:**

- Reportes financieros anuales
- Dashboard de marketing por campaña

---

## 4. Esquema Estrella vs. Cubos OLAP

### Enunciado

Explique la diferencia entre esquema estrella y cubos OLAP. Dé consideraciones.

### Desarrollo

#### Esquema Estrella

- Arquitectura de base de datos relacional optimizada para OLAP.
- Una tabla de hechos central conectada a múltiples tablas de dimensiones.

```text
   DIM_FECHA
       |
DIM_PRODUCTO — FACT_VENTAS — DIM_CLIENTE
       |
    DIM_TIENDA
```

- Simplicidad y rapidez para consultas agregadas.

#### Cubo OLAP

- Estructura multidimensional que permite análisis rápido en varias dimensiones.
- Facilita operaciones como:
  - Roll-up (agregación)
  - Drill-down (detalle)
  - Slice / Dice (filtros)
  - Pivot (rotación de ejes)

**Consideraciones:**

- Esquema Estrella es modelo lógico implementado en BD.
- Cubo OLAP es una estructura lógica/visual generada por herramientas OLAP.
- Los cubos se construyen sobre esquemas estrella o snowflake.

---

# Tema 12: Big Data y NoSQL

A continuación se desarrollan las respuestas para el Tema 12: Big Data y NoSQL, con enfoque académico y práctico para el estudio o resolución de exámenes.

---

## 1. Arquitectura de una Base de Datos Big Data y Conceptos Erróneos

### Enunciado

Ilustre y describa la arquitectura de una BD Big Data. Comente además acerca de 3 conceptos equivocados de una BD Big Data.

### Desarrollo

#### Arquitectura de una BD Big Data

```text
      [ Fuentes de Datos ]
(Sensores, Logs, APIs, Web, RDBMS)
           ↓
 +------------------+
 |     Ingesta      | ← (Kafka, Flume, NiFi)
 +------------------+
           ↓
 +------------------+
 |    Almacenamiento| ← (HDFS, S3, Cassandra)
 +------------------+
           ↓
 +------------------+
 |     Procesamiento| ← (MapReduce, Spark)
 +------------------+
           ↓
 +------------------+
 |     Análisis     | ← (Hive, Pig, Presto)
 +------------------+
           ↓
 +------------------+
 |    Visualización | ← (Tableau, PowerBI)
 +------------------+
```

#### Componentes Clave

1. Ingesta: recolecta datos masivos en tiempo real o por lotes.
2. Almacenamiento distribuido: permite guardar volúmenes masivos con tolerancia a fallos.
3. Procesamiento paralelo: mediante modelos como MapReduce o Spark.
4. Consulta y análisis: permite ejecutar SQL o scripts sobre los datos.
5. Visualización: genera dashboards e informes.

#### 3 Conceptos Erróneos sobre Big Data

| Mito                                         | Realidad                                                                      |
| -------------------------------------------- | ----------------------------------------------------------------------------- |
| Big Data = datos grandes                     | No se trata solo de tamaño, también de velocidad y variedad.                  |
| Big Data reemplaza las BDs tradicionales     | Se complementan: OLTP y Big Data tienen fines distintos.                      |
| Solo las empresas grandes lo usan            | Muchas pymes lo aplican para análisis en la nube con herramientas asequibles. |

---

## 2. Escalabilidad Horizontal en NoSQL

### Enunciado

Una de las características de las BD NoSQL corresponde a la Escalabilidad Horizontal. Describir el concepto de la misma.

### Desarrollo

#### Definición de Escalabilidad Horizontal

La escalabilidad horizontal permite aumentar la capacidad de procesamiento o almacenamiento añadiendo más nodos al sistema, en lugar de mejorar un único servidor.

#### En el contexto NoSQL

- Las BD NoSQL como Cassandra, MongoDB y HBase están diseñadas para escalar horizontalmente.
- Se realiza mediante sharding, que divide los datos entre nodos.
- Cada nodo almacena una porción de los datos (y a veces copias para tolerancia a fallos).

**Ejemplo:**

```text
Usuario_ID 1–1000  → Nodo A
Usuario_ID 1001–2000 → Nodo B
Usuario_ID 2001–3000 → Nodo C
```

#### Ventajas

- Alta disponibilidad.
- Tolerancia a fallos.
- Bajo costo (servidores commodity).
- Incremento lineal del rendimiento.

---

## 3. Las 3 V's de Big Data

### Enunciado

Describa las 3 V's de BigData.

### Desarrollo

| V             | Descripción                                                                                                                    |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Volumen       | Cantidad masiva de datos generados (desde terabytes hasta exabytes). Ej.: redes sociales, sensores IoT.                        |
| Velocidad     | Ritmo con que los datos son generados, procesados y analizados (en tiempo real o lotes). Ej.: análisis de fraudes en segundos. |
| Variedad      | Diferentes tipos de datos: estructurados (SQL), semi-estructurados (JSON), no estructurados (videos, texto).                   |

---

# Tema 13: Modelado de Datos - Resoluciones completas

A continuación se desarrollan las resoluciones completas de ejercicios de modelado de datos.

---

## 1. MER - Empresa, empleados y departamentos

### Enunciado

'Una empresa tiene varios empleados. Cada empleado trabaja en un departamento. Cada departamento puede tener varios empleados y un jefe.'

### Modelo Entidad-Relación

Entidades:

- Empleado (CI, Nombre, Dirección, Cargo)
- Departamento (Cod_Dep, Nombre_Dep)

Relaciones:

- Trabaja_en entre Empleado y Departamento
  - Cardinalidad: N:1 (varios empleados por departamento)
  - Participación total de Empleado
- Jefe_de: Empleado es jefe de un Departamento
  - 1:1 (cada departamento tiene un solo jefe)
  - Participación total de Departamento, parcial de Empleado

## 2. Transformación al modelo relacional

Relaciones:

- EMPLEADO(CI PK, Nombre, Dirección, Cargo, Cod_Dep FK)
- DEPARTAMENTO(Cod_Dep PK, Nombre_Dep, CI_Jefe FK referencias EMPLEADO(CI))

Notas:

- Se usa clave foránea en EMPLEADO para relación "Trabaja_en"
- Clave foránea en DEPARTAMENTO para jefe (auto-relación)

## 3. Dependencias funcionales - Empleado(CI, Nombre, Dirección, Cargo, Cod_Dep)

- CI → Nombre, Dirección, Cargo, Cod_Dep
- Cod_Dep no determina nada

## 4. Normalización hasta 3FN

### 1NF

- Tabla ya está en 1NF (atributos atómicos)

### 2NF

- La clave primaria es CI (no compuesta)
- No hay dependencias parciales ⇒ está en 2NF

### 3NF

- No hay dependencias transitivas (Nombre, Dirección, Cargo dependen solo de CI)
- ⇒ Ya está en 3NF

## 5. MER - Universidad, carreras, materias, docentes, alumnos

### Enunciado

'Una universidad tiene carreras. Cada carrera tiene materias. Cada materia tiene un docente responsable. Los alumnos pueden inscribirse a varias materias y rendir exámenes.'

Entidades:

- Carrera (CodCarrera, Nombre)
- Materia (CodMateria, Nombre, CodCarrera)
- Docente (CI, Nombre)
- Alumno (CI_Alumno, Nombre)

Relaciones:

- Pertenece (Materia → Carrera) [N:1]
- Responsable (Docente → Materia) [1:1]
- Inscripcion (Alumno, Materia, FechaInscripcion)
- Examen (Alumno, Materia, FechaExamen, Nota)

## 6. Transformación al modelo relacional

- CARRERA(CodCarrera PK, Nombre)
- MATERIA(CodMateria PK, Nombre, CodCarrera FK)
- DOCENTE(CI PK, Nombre)
- MATERIA_DOCENTE(CodMateria PK/FK, CI_Docente FK)
- ALUMNO(CI_Alumno PK, Nombre)
- INSCRIPCION(CI_Alumno FK, CodMateria FK, FechaInscripcion, PK compuesta)
- EXAMEN(CI_Alumno FK, CodMateria FK, FechaExamen, Nota, PK compuesta)

## 7. Dependencias funcionales dadas

- Carrera(CodCarrera, Nombre): CodCarrera → Nombre
- Materia(CodMateria, Nombre, CodCarrera): CodMateria → Nombre, CodCarrera
- Docente(CI, Nombre, CodMateria): CI → Nombre, CodMateria

## 8. Normalización de relaciones

- Carrera: Ya está en 3NF
- Materia: CodMateria → CodCarrera, Nombre ⇒ está en 3NF
- Docente:
  - CI → CodMateria → CodCarrera → problema de dependencia transitiva
  - Solución: dividir en:
    - DOCENTE(CI, Nombre)
    - MATERIA_DOCENTE(CI, CodMateria)

## 9. Esquema de base de datos para biblioteca

Entidades:

- Libro (ISBN, Titulo, Año, CodEditorial FK)
- Autor (CodAutor, Nombre)
- Editorial (CodEditorial, Nombre)
- Socio (ID_Socio, Nombre, Direccion)
- Prestamo (ID_Prestamo, ID_Socio FK, ISBN FK, Fecha, Fecha_Devolucion)

Relaciones:

- Escrito_por: muchos a muchos entre Libro y Autor ⇒ tabla intermedia LIBRO_AUTOR(ISBN FK, CodAutor FK)

## 10. Esquema MER conceptual

- Se modela con entidades rectangulares, relaciones con rombos, atributos ovalados.
- Relaciones: Prestamo, Escrito_por
- Participación total de Socio en Prestamo

## 11. Claves primarias y foráneas en el modelo relacional

- LIBRO: ISBN (PK), CodEditorial (FK)
- AUTOR: CodAutor (PK)
- EDITORIAL: CodEditorial (PK)
- SOCIO: ID_Socio (PK)
- PRESTAMO: ID_Prestamo (PK), ID_Socio (FK), ISBN (FK)
- LIBRO_AUTOR: ISBN (FK), CodAutor (FK), PK compuesta

## 12. SQL y Consultas

### Consultas SQL

a) Lista de empleados por departamento:

```sql
SELECT d.Nombre_Dep, e.Nombre
FROM Empleado e
JOIN Departamento d ON e.Cod_Dep = d.Cod_Dep;
```

b) Nombre de empleados con cargo 'Analista':

```sql
SELECT Nombre
FROM Empleado
WHERE Cargo = 'Analista';
```

c) Total de empleados por departamento:

```sql
SELECT Cod_Dep, COUNT(*) AS Total_Empleados
FROM Empleado
GROUP BY Cod_Dep;
```

### Álgebra Relacional

a) Lista de empleados por departamento:

π_{d.Nombre_Dep, e.Nombre} (Empleado ⨝ Empleado.Cod_Dep = Departamento.Cod_Dep Departamento)

b) Empleados con cargo 'Analista':

π_{Nombre} (σ_{Cargo = 'Analista'} (Empleado))

c) Total de empleados por departamento:

No directamente expresable en álgebra relacional clásica sin extensiones agregadas (uso de álgebra relacional extendida con γ):

γ_{Cod_Dep, COUNT(*) → Total_Empleados} (Empleado)

### Consultas adicionales (Parcial 2016 Sem 2)

a) Listar materias por carrera:

```sql
SELECT c.Nombre AS Carrera, m.Nombre AS Materia
FROM Materia m
JOIN Carrera c ON m.CodCarrera = c.CodCarrera;
```

b) Buscar docentes de una materia específica:

```sql
SELECT d.Nombre
FROM Docente d
JOIN Materia_Docente md ON d.CI = md.CI
WHERE md.CodMateria = 'MAT123';
```

c) Alumnos que rindieron exámenes en más de una materia:

```sql
SELECT CI_Alumno
FROM Examen
GROUP BY CI_Alumno
HAVING COUNT(DISTINCT CodMateria) > 1;
```

### LEFT JOIN - Cliente y Ventas (enunciado hipotético)

```sql
SELECT c.Nombre, v.Fecha, v.Monto
FROM Cliente c
LEFT JOIN Venta v ON c.ID_Cliente = v.ID_Cliente;
```

Esto devuelve todos los clientes, incluso los que no han realizado ninguna venta (ventas nulas).

