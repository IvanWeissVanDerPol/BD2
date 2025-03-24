Aquí tienes los enunciados agrupados según los temas que proporcionaste:

---

## 1. Índices
- Explique en sus términos a qué corresponde un índice y a qué un archivo índice. Enumere al menos tres tipos de índices estudiados.
- Indique para qué tipo de consultas resulta más apropiado: (a) un índice ordenado, (b) un índice hash, (c) un índice bitmap.
- Explique los tipos de índices estudiados conforme su organización física y cuándo conviene aplicarlos.
- Explique el costo asintótico de: (a) Búsqueda lineal, (b) Búsqueda binaria, (c) Índice primario, (d) Índice secundario.
- Dada una operación de selección basada en condición de igualdad, indique las condiciones físicas para usar cada algoritmo.
- Tema 6: Ilustre la construcción de un índice Hash basado en Asociación Extensible.
- Tema 10: Construir un índice B+ e índice hash estático, y clasifique los índices como primarios o secundarios.

---

## 2. Organización Física de Archivos
- Explique las formas de organización física de los archivos de datos en un SGBD.
- Explique resumidamente y en sus propios términos las posibles formas de organización de los registros en archivos.
- Explique en sus términos las formas de organización de archivos posibles para la implementación de archivos de tablas/datos.
- Tema 9: Detalle apropiadamente cómo se implementa la organización física de bloques denominada estructura de páginas por ranuras.

---

## 3. Medidas de Rendimiento de Discos
- Explique las medidas de rendimiento que deben tener en cuenta para la elección de unidades de discos magnéticos. ¿Cuál sería la más determinante?
- Explique el algoritmo del Ascensor y mencione las principales métricas de rendimiento de discos.
- Tema 1: Explique detalladamente las medidas de rendimiento que deben ser consideradas respecto a los discos magnéticos.

---

## 4. Niveles RAID
- Explique los niveles de RAID 0, 1 y 5. ¿Cuál es la principal razón para la implementación de almacenamiento redundante?
- Explique brevemente las ventajas de RAID en cuanto a rendimiento y fiabilidad. Detalle los niveles RAID 0, 1 y 5.
- Tema 2: Explique detalladamente las ventajas de configurar un esquema de almacenamiento basado en RAID, ejemplificando niveles 1 y 5.

---

## 5. Árboles B y B+
- Explique el porqué la organización basada en Árboles B y B+ resulta apropiada como estructura de datos para implementar índices ordenados.

---

## 6. Algoritmos de Búsqueda
- Explique el costo asintótico espacial y temporal del Algoritmo de Programación Dinámica:
  - (a) sin la optimización de evaluación de árboles en profundidad por la izquierda,
  - (b) con la optimización de evaluación de árboles en profundidad por la izquierda.
- Dada una operación de selección cualquiera basada en una condición de igualdad, explique en qué casos un SGBD utilizará los siguientes algoritmos e indique el costo asintótico:
  - (a) Búsqueda Lineal,
  - (b) Búsqueda Binaria,
  - (c) Búsqueda en índice primario para un atributo clave,
  - (d) Búsqueda en índice secundario para atributo no clave.
- Tema 7: Desarrolle cuatro casos hipotéticos para una consulta de selección que generen diferentes costes.

---

## 7. Procesamiento de Consultas
- Grafique el Diagrama de Procesamiento de consultas y explique los pasos.
- Detalle los pasos lógicos para el Procesamiento de Consultas.
- Grafique el Diagrama de Procesamiento de consultas y explique los pasos del mismo (Primer Parcial 2021).
- Tema 4: Traducción inicial a álgebra relacional de consulta JOIN y optimización (2 casos).
- Tema 8: Evaluación con algoritmo de Bucle Anidado por Bloques para consulta JOIN. Calcule costes (LRU o MRU).

---

## 8. Modelado Multidimensional
- Explique tablas de dimensiones, tablas de hechos y medidas. Dé ejemplos.
- Explique la diferencia entre OLTP y OLAP. Dé ejemplos.
- Explique la diferencia entre esquema estrella y cubos OLAP. Dé consideraciones.
- Explique en sus términos qué son tablas de dimensiones, tablas de hechos y medidas en el modelado multidimensional. Enumere ejemplos.
- Explique en sus términos cuál es la diferencia entre bases de datos OLTP y OLAP, citando ejemplos.

---

## 9. Transacciones (ACID)
- (a) Defina el concepto de Transacción en SGBDs.
- (b) Indique y defina las fases del Ciclo de Vida de una Transacción.
- (c) Indique y defina las propiedades ACID que un SGBD debe asegurar.
- Tema 3: Explique las propiedades de las transacciones que se deben garantizar por un SGBD conforme al estándar SQL.

---

## 10. Concurrencia
- (a) Describa la función del Componente de Gestión de Concurrencia en un SGBD.
- (b) Describa la estructura de datos utilizada para la gestión y concesión de bloqueos.
- (a) Describa el protocolo de Bloqueo de 2 Fases.
- (b) Indique las variantes del protocolo de Bloqueo de 2 Fases.
- Tema 5: Explique en Control de Concurrencia qué significa: planificación, planificación secuenciable, secuencialidad en cuanto a conflicto y secuencialidad en cuanto a vistas.
- (a) Explique qué es una Planificación Secuencial.
- (b) Explique qué es una Planificación Secuenciable.
- (c) Fundamente la importancia de la Secuencialidad en SGBD.

---

## 11. Protocolos Distribuidos
- (a) Detalle el protocolo de Control de Concurrencia de Quorum de Consenso.
- (b) Explique implicancias para definir valores de Quorum.
- (c) Indique valores para emular protocolos de Mayoría y Sesgado.
- (a) Detalle pasos del protocolo C2F (commit en 2 fases) en Bases de Datos Distribuidas.
- (b) Cómo proceden participantes si falla coordinador.
- (c) Cómo procede un sitio si falla.

---

## 12. Almacenamiento Distribuido
- Explique detalladamente las formas de almacenamiento distribuido en Bases de Datos Distribuidas Relacionales.
- Indique pasos y coste de transmisión para Estrategia de Semireunión según el sitio que recibe la consulta.

---

## 13. Optimización de Consultas
- Tema 4: Traducción inicial a álgebra relacional y optimización de consultas JOIN (2 casos).
- Tema 7: Planteamiento hipotético de consultas SELECT que deriven en diferentes costes.

---

## 14. Normalización y Dependencias Funcionales
- Determinar dependencias funcionales en la tabla Empleado (CI, Nombre, Dirección, Cargo, Cod_Dep) y aplique hasta la 3FN.
- A partir de relaciones Carrera, Materia, Docente identifique dependencias funcionales y aplique normalización correspondiente.
- Indique las claves primarias y foráneas en el modelo relacional obtenido.

---

## Otros (Modelado ER y SQL)
- Modelar empresa-empleados-departamento en MER y transformar a modelo relacional.
- Modelar universidad-carreras-materias-docentes-alumnos en MER, transformar a modelo relacional y realizar consultas SQL relacionadas.
- Diseñar esquema de base de datos para una biblioteca (Libro, Autor, Editorial, Socio, Préstamo).
- Escribir consultas SQL y álgebra relacional para obtener empleados por departamento, analistas y totales.
- Escribir consultas SQL para materias por carrera, docentes y alumnos que rindieron exámenes.

---

Esta organización permite repasar claramente cada tema por separado y prepararte adecuadamente para cada uno.