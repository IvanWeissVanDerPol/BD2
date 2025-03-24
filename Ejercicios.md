# Enunciados completos de todos los archivos 📄

Este documento contiene todos los **enunciados completos** extraídos de los archivos y escaneos de exámenes de BD2.

---


## BD2_TAA_2022.pdf
- Explique en sus términos a qué corresponde un índice y a qué un archivo índice. Enumere al menos tres tipos de índices estudiados.
- Explique el porqué la organización basada en Árboles B y B+ resulta apropiada como estructura de datos para implementar índices ordenados.
- Indique para qué tipo de consultas resulta más apropiado: (a) un índice ordenado, (b) un índice hash, (c) un índice bitmap.
- Explique los tipos de índices estudiados conforme su organización física y cuándo conviene aplicarlos.
- Explique las formas de organización física de los archivos de datos en un SGBD.
- Explique resumidamente y en sus propios términos las posibles formas de organización de los registros en archivos.
- Explique las medidas de rendimiento que deben tener en cuenta para la elección de unidades de discos magnéticos. ¿Cuál sería la más determinante?
- Explique el algoritmo del Ascensor y mencione las principales métricas de rendimiento de discos.
- Explique los niveles de RAID 0, 1 y 5. ¿Cuál es la principal razón para la implementación de almacenamiento redundante?
- Explique brevemente las ventajas de RAID en cuanto a rendimiento y fiabilidad. Detalle los niveles RAID 0, 1 y 5.
- Explique el costo asintótico de: (a) Búsqueda lineal, (b) Búsqueda binaria, (c) Índice primario, (d) Índice secundario.
- Dada una operación de selección basada en condición de igualdad, indique las condiciones físicas para usar cada algoritmo.
- Grafique el Diagrama de Procesamiento de consultas y explique los pasos.
- Detalle los pasos lógicos para el Procesamiento de Consultas.
- Explique tablas de dimensiones, tablas de hechos y medidas. Dé ejemplos.
- Explique la diferencia entre OLTP y OLAP. Dé ejemplos.
- Explique la diferencia entre esquema estrella y cubos OLAP. Dé consideraciones.

## Primer Examen Parcial 18/03/2021

- Indique para qué tipo de consultas resulta más apropiado:  
  (a) un índice ordenado,  
  (b) un índice hash,  
  (c) un índice bitmap.

- Explique en sus términos las formas organización de archivos posibles para la implementación de archivos de tablas/datos.

- Grafique el Diagrama de Procesamiento de consultas y explique los pasos del mismo.

- Explique los niveles de RAID 0, 1 y 5. A su criterio, ¿cuál es la principal razón para la implementación de unidades de almacenamiento redundante?

- Explique las medidas de rendimiento que deben tener en cuenta para la elección de unidades de discos magnéticos. ¿A su criterio, cuál de las mismas sería la más determinante?

- Explique el costo asintótico espacial y temporal del Algoritmo de Programación Dinámica:  
  (a) sin la optimización de evaluación de árboles en profundidad por la izquierda,  
  (b) con la optimización de evaluación de árboles en profundidad por la izquierda.

- Dada una operación de selección cualquiera basada en una condición de igualdad, explique en qué casos un SGBD utilizará los siguientes algoritmos e indique cuál es el costo asintótico de los mismos:  
  (a) Búsqueda Lineal,  
  (b) Búsqueda Binaria,  
  (c) Búsqueda en índice primario para un atributo clave,  
  (d) Búsqueda en índice secundario para atributo no clave.

---

## Segundo Examen Parcial 20/05/2021

- (a) Explique qué es una Planificación Secuencial.  
  (b) Explique qué es una Planificación Secuenciable.  
  (c) Fundamente a su criterio la importancia de la Secuencialidad en SGBD.

- (a) Defina el concepto de Transacción en SGBDs.  
  (b) Indique y defina las fases del Ciclo de Vida de una Transacción.  
  (c) Indique y defina las propiedades que un SGBD debe asegurar para las Transacciones.

- (a) Describa la función del Componente de Gestión de Concurrencia en un SGDB.  
  (b) Describa la estructura de datos utilizada para la gestión y concesión de bloqueos.

- (a) Describa el protocolo de Bloqueo de 2 Fases.  
  (b) Indique cuáles son las variantes del mismo.

- (a) Detalle el protocolo de Control de Concurrencia de Quorum de Consenso.  
  (b) Explique las implicancias de la condición que debe tenerse en cuenta para la definición de los valores de Quorum.  
  (c) Indique los valores de Quorum que permiten emular el Protocolo de Mayoría y el Protocolo Sesgado.

- (a) Detalle los pasos de cada fase del protocolo C2F en Bases de Datos Distribuidas.  
  (b) Indique cómo proceden los participantes en caso de falla del coordinador.  
  (c) Indique cómo se procede en un sitio en caso de falla del mismo.

- Explique detalladamente las formas de almacenamiento distribuido en Bases de Datos Distribuidas Relacionales.

- Conforme la figura de abajo y la consulta `"select * from R join S"`, indique los pasos y el costo total de transmisión de realizar la Estrategia de la Semireunión si la consulta fue recibida:  
  (a) en el Sitio 1,  
  (b) en el Sitio 2.

- Explique en sus términos: ¿Cuál es la diferencia entre bases de datos OLTP y OLAP? Así mismo, cite al menos dos ejemplos de aplicación para cada tipo.

- Resuelva el siguiente planteamiento (consultas SQL LEFT JOIN relacionadas con `cliente` y `ventas`).

- Explique en sus términos en qué consisten las tablas de dimensiones, tablas de hechos y medidas en el modelado multidimensional. Así mismo, enumere al menos tres ejemplos para cada uno.



## 46994875_1959212391051398_5941978629998116864_n.jpg & 46882004_365635817346164_7869854359566155776_n.jpg
- Tema 1: Explique detalladamente las medidas de rendimiento que deben ser consideradas respecto a los discos magnéticos.
- Tema 2: Explique detalladamente las ventajas de configurar un esquema de almacenamiento basada en RAID. Ejemplifique además los niveles 1 y 5.
- Tema 3: Explique las propiedades de las transacciones que se deben garantizar por un SGBD conforme al estándar SQL.
- Tema 4: Dada la consulta: `SELECT e.LNAME FROM EMPLEADO e JOIN TRABAJA_EN te ON te.EMPLEADO = e.ID JOIN PROYECTO p ON (p.ID = te.PROYECTO) WHERE p.NOMBRE = 'AQUARIUS' AND e.FECHA_NAC >= '2000-01-01'` realice traducción inicial a álgebra relacional e ilustre dos casos de optimización.
- Tema 5: Explique en el contexto de los Protocolos del Control de Concurrencia qué se entiende por: (1) Planificación, (2) Planificación Secuenciable, (3) Secuencialidad en Cuanto a Conflicto y (4) Secuencialidad en Cuanto a Vistas.
- Tema 6: Ilustre la construcción de un índice Hash basado en la técnica de Asociación Extensible para la columna nombre-sucursal considerando para ello la tabla y los valores de hash indicados.
- Tema 7: Desarrolle el planteamiento hipotético de cuatro casos basados en una consulta de selección en la forma: `SELECT * FROM <tabla> WHERE <tabla>.<columna> = <valor>` y que deriven cada uno en una operación selección con coste o estimación de coste diferente.
- Tema 8: Dada la consulta `SELECT * FROM A JOIN B ON A.a = B.b`, teniendo en cuenta: A se encuentra en 20 bloques, B en 15, hay 10 bloques libres, se evalúa con algoritmo de Bucle Anidado por Bloques. Calcule el coste de evaluación si la estrategia de reemplazo de bloques es LRU o MRU.
- Tema 9: Detalle apropiadamente cómo se implementa la organización física de bloques denominada estructura de páginas por ranuras.
- Tema 10: La tabla corresponde a una relación Cliente con 1 fila por bloque. a) Construir un índice B+ con 4 punteros por nodo para clave primaria id. b) Índice hash estático con cajones de 4 elementos, usando función x mod 4 sobre saldo. c) Clasifique los índices como primarios o secundarios.

## par1a2019sem2.pdf
- Modelar el siguiente enunciado utilizando el modelo entidad-relación (MER): 'Una empresa tiene varios empleados. Cada empleado trabaja en un departamento. Cada departamento puede tener varios empleados y un jefe.'
- Transforme el modelo entidad-relación anterior a un modelo relacional.
- Considere la siguiente tabla: Empleado(CI, Nombre, Dirección, Cargo, Cod_Dep). Determinar las dependencias funcionales.
- Aplique la normalización correspondiente a la tabla anterior, hasta alcanzar la 3FN.
- Escriba consultas SQL para obtener: a) Lista de empleados por departamento. b) Nombre de empleados con cargo 'Analista'. c) Total de empleados por departamento.
- Redacte las mismas consultas del punto anterior utilizando Álgebra Relacional.
- Diseñe un esquema de base de datos para una biblioteca con las siguientes entidades: Libro, Autor, Editorial, Socio, Préstamo.


## par1a2016sem2.pdf / par1a2016sem2(1).pdf
- A partir del siguiente enunciado: 'Una universidad tiene carreras. Cada carrera tiene materias. Cada materia tiene un docente responsable. Los alumnos pueden inscribirse a varias materias y rendir exámenes.' Realizar el MER.
- Transforme el MER anterior al modelo relacional.
- Dadas las siguientes relaciones, identifique las dependencias funcionales: Carrera(CodCarrera, Nombre), Materia(CodMateria, Nombre, CodCarrera), Docente(CI, Nombre, CodMateria).
- Aplique las formas normales correspondientes a las relaciones del punto anterior.
- Escriba consultas SQL para: a) Listar materias por carrera. b) Buscar docentes de una materia específica. c) Mostrar alumnos que rindieron exámenes en más de una materia.
- Esquematice el diagrama conceptual generado por el modelo MER.
- Indique las claves primarias y foráneas en el modelo relacional obtenido.

