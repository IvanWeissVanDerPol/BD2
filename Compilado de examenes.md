# Enunciados completos de todos los archivos 📄

Este documento contiene todos los **enunciados completos** extraídos de los archivos y escaneos de exámenes de BD2.

---
# Bases de Datos II - Primer Examen Final – 28/11/2017

---

### **Tema 1 (10 p.)**  
Explique detalladamente **las formas de Almacenamiento Distribuido en Sistemas de Bases de Datos Distribuidas**.

---

### **Tema 2 (10 p.)**  
Explique detalladamente el **Protocolo de Compromiso de 2 Fases** aplicado en Sistemas de Bases de Datos Distribuidas y cómo procede:

a. Un sitio participante en caso de falla del mismo.  
b. Los sitios participantes en caso de falla del sitio coordinador.

---

### **Tema 3 (10 p.)**  
Explique detalladamente el **Modelo Abstracto del Sistema de Transacciones** en un Sistema de Bases de Datos Distribuidas orientado a asegurar las propiedades **ACID**.

---

### **Tema 4 (10 p.)**  
Explique detalladamente **las propiedades de las transacciones** que deben ser aseguradas por un SGBD conforme al estándar **SQL**.

---

### **Tema 5 (10 p.)**  
Explique qué entiende por un **Gestor de Bloqueos en un SGBD** que implementa un **Control de Concurrencia basado en Bloqueos**.  
Indique además cómo el mismo podría estar implementado y qué pasos debería tener en cuenta para evitar la inanicción de las transacciones.

---

### **Tema 6 (10 p.)**  
Explique en el contexto de los **Protocolos del Control de Concurrencia** qué se entiende por:  
1. Planificación  
2. Planificación Secuenciable  
3. Secuencialidad en Cuanto a Conflicto  
4. Secuencialidad en Cuanto a Vistas
```

### **Tema 7 (10 p.)**

Desarrolle el planteamiento hipotético de cuatro casos basados en una consulta de selección en la forma:

```sql
SELECT * FROM <tabla> WHERE <tabla>.<columna> = <valor>;
```

y que deriven cada uno en una operación de selección con costo o estimación de costo diferente.

---

### **Tema 8 (10 p.)**

Dada la consulta:

```sql
SELECT * FROM A A JOIN B B ON A.a = B.b
```

Teniendo en cuenta que:

* La tabla A se encuentra almacenada en 20 bloques.
* La tabla B se encuentra almacenada en 15 bloques.
* La memoria cuenta actualmente con 10 bloques libres para evaluar la consulta.
* La consulta está planificada para ser evaluada conforme al algoritmo de Bucle Anidado por Bloques.

**Calcule cuál será el coste de evaluación de la consulta si:**

1. La estrategia de reemplazo de bloques en la memoria es **LRU**.
2. La estrategia de reemplazo de bloques en la memoria es **MRU**.

---

### **Tema 9 (10 p.)**

Detalle apropiadamente cómo se implementa la organización física de bloques denominada **estructura de páginas por ranuras** para el almacenamiento de registros.

---

### **Tema 10 (10 p.)**

La siguiente tabla corresponde al estado actual del archivo de la relación **Cliente**, en el que cada bloque del archivo corresponde a 1 fila. Se pide:

**a.** Construir un índice en forma de árbol **B+** con nodos de 4 punteros para la clave primaria `id`, suponiendo que los registros/filas fueron insertados según el orden alfabético de la columna `nombre`.

**b.** Construir un índice hash estático cerrado con **cajones de 4 elementos**, cuya función de asociación es `"x mod 4"` sobre la columna `saldo`, siendo `x` el valor de cada fila en dicha columna.

**c.** Explique detalladamente en cada caso si el índice es **primario o secundario**.

---

### 📋 Tabla: relación Cliente

| id | nombre           | saldo |
| -- | ---------------- | ----- |
| 1  | Preston Schwartz | 282   |
| 2  | Cathleen Steele  | 159   |
| 3  | Tatyana Russo    | 367   |
| 4  | Libby Madden     | 431   |
| 5  | Orla Reid        | 317   |
| 6  | Vivian Cherry    | 367   |
| 7  | Kirk Jensen      | 337   |
| 8  | Amanda Macias    | 319   |
| 9  | Barry Morris     | 338   |
| 10 | Lee Lopez        | 437   |
| 11 | Elliott Fowler   | 367   |
| 12 | Paula Johns      | 190   |

---
# Bases de Datos II - Segundo Examen Final – 06/12/2016

---

### **Tema 1 – 20 p.**  
Explique concisa y ordenadamente:  
- Las medidas de rendimiento a tener en cuenta sobre los discos magnéticos. (6p)  
- Los tipos de organización de archivos que puede implementar un SGBD. (6p)  
- Las formas de almacenamiento distribuido en un SGBD y su definición en álgebra relacional. (5p)  
- Tipos de índices ordenados, asociativos y bitmap, y cite un caso en los que no conviene aplicarlos. (5p)  
- Etapas lógicas para el Procesamiento de Consultas. Explique cada una. (5p)

---

### **Tema 2 – 15 p.**  
La siguiente tabla corresponde al estado actual del archivo de la relación **cliente**, en el que cada bloque del archivo corresponde a 1 fila. Se pide:

a. Construir un índice en forma de árbol B+ con nodos de 4 punteros para la clave primaria `id`, suponiendo que los registros/fila fueron insertados según el orden alfabético de la columna `nombre`.  
b. Construir un índice hash estático cerrado con cajones de 3 elementos cuya función de asociación es `x mod 5` sobre la columna `saldo`, siendo x el valor de cada fila en dicha columna.  
c. Explique a dónde apuntan los registros índices para cada caso anterior.

| id  | nombre            | saldo |
|-----|-------------------|-------|
| 1   | Preston Schwartz  | 282   |
| 2   | Cathleen Steele   | 159   |
| 3   | Tatyana Russo     | 367   |
| 4   | Libby Madden      | 431   |
| 5   | Orla Reid         | 317   |
| 6   | Vivian Cherry     | 361   |
| 7   | Kirk Jensen       | 317   |
| 8   | Amanda Macias     | 190   |
| 9   | Barry Morris      | 338   |
| 10  | Lee Lopez         | 437   |
| 11  | Elliott Fowler    | 367   |
| 12  | Paula Johns       | 190   |

---

### **Tema 3 – 10 p.**  
Dadas las relaciones r1(A, B), r2(C, D), r3(E, F) con las siguientes propiedades:  
- r1 tiene 35.000 tuplas,  
- r2 tiene 75.000 tuplas,  
- 50 tuplas de r1 caben en un bloque y 100 tuplas de r2 caben en un bloque.

Estime el número de bloques de disco requeridos utilizando las siguientes estrategias para la reunión `r1 ⨝ r2 on r1.C = r2.C`:

a. Reunión en bucle anidado por bloques.  
b. Reunión por mezcla, suponiendo además que la relación r2 debe ser ordenada externamente disponiéndose de 3 bloques de memoria intermedia.  
c. Reunión en base de búsqueda indexada, suponiendo que existe un índice primario de árbol B+ en la columna C de relación r2 con nodos de 60 punteros.  
d. Reunión por Hash. Suponiendo el tamaño de M = 20. Recuerde que si N > M se debe aplicar particionamiento recursivo.

---

### **Tema 4 – 10 p.**  
Indique en qué casos aplicarían y cuál el costo asintótico en bloques de disco para cada una de las siguientes operaciones:

a. Búsqueda Lineal.  
b. Búsqueda Binaria.  
c. Búsqueda en índice primario para un atributo clave.  
d. Búsqueda en índice primario para un atributo no clave.  
e. Búsqueda en índice secundario para un atributo no clave.

---

### **Tema 5 – 10 p.**  
Esquematizar la arquitectura de un DW y citar y describir 4 características del Dataware.

---

### **Tema 6 – 5 p.**  
Ilustre y describa la arquitectura de una BD BigData.  
Comente además acerca de 3 conceptos equivocados de una BD Big
Aquí tienes los **temas 7 a 10** extraídos y redactados en formato **Markdown**, complementando la imagen proporcionada:

### Tema 7 – 5 p.  
Una de las características de las BD NoSQL corresponde a la **Escalabilidad Horizontal**.  
Describir el concepto de la misma.

---

### Tema 8 – 5 p.  
Describa las **3 V’s de BigData**.

---

### Tema 9 – 10 p.  
Muestre los pasos para la **reunión de las siguientes relaciones mediante la estrategia de la semireunión**.  
Indique además el **ahorro** que conlleva la misma respecto a la **transmisión de datos entre sitios** en relación a la estrategia más simple.  
Suponga además que la consulta ha sido recibida en el Sitio 1.

**Consulta:**  
R JOIN S ON (R.A2 = S.A2)

**Relación R en Sitio 1 (R@S1):**

| A1 | A2 |
| -- | -- |
| 1  | 3  |
| 1  | 4  |
| 1  | 6  |
| 2  | 6  |
| 2  | 7  |
| 3  | 7  |
| 3  | 8  |
| 3  | 9  |

**Relación S en Sitio 2 (S@S2):**

| A2 | A3 | A4 |
| -- | -- | -- |
| 3  | 13 | 16 |
| 4  | 13 | 16 |
| 6  | 14 | 17 |
| 7  | 14 | 17 |
| 8  | 15 | 16 |
| 9  | 15 | 16 |
| 10 | 13 | 16 |
| 11 | 14 | 16 |
| 12 | 15 | 16 |

---

### Tema 10 – 10 p.

**Esquematice el protocolo de compromiso de 2 fases** e indique cómo se procede en caso de **falla de un sitio participante**.

---

# Bases de Datos II – 1er. Examen Final – 19/12/2019 – Duración 90 min. – 18.00hs

---

### Tema 1 (10 p.)
Explique en qué consisten los problemas que deben evitarse en la detección de Interbloqueos en un Sistema de Base de Datos Distribuida.

---

### Tema 2 (10 p.)
**a.** Desarrolle los pasos correspondientes para la semi-reunión de las relaciones ilustradas abajo.  
Suponga que la consulta ha sido recibida en el Sitio 2.  
**b.** Explique o fundamente al menos dos (2) ventajas de este enfoque.

#### Consulta:  
R JOIN S ON (R.A2 = S.A2)

#### Relaciones:

**R@S1**

| A1 | A2 |
| -- | -- |
| 1  | 3  |
| 1  | 4  |
| 1  | 7  |
| 2  | 3  |
| 2  | 6  |
| 3  | 7  |
| 3  | 8  |
| 3  | 9  |

**S@S2**

| A2 | A3 | A4 |
| -- | -- | -- |
| 3  | 13 | 16 |
| 4  | 13 | 16 |
| 7  | 14 | 17 |
| 10 | 14 | 16 |
| 11 | 15 | 16 |
| 12 | 15 | 16 |

---

### Tema 3 (10 p.)

Explique los tipos de índices estudiados conforme su organización/implementación física y para qué tipo de consultas resultan apropiados.

---

### Tema 4 (10 p.)

Explique:
**(i)** El protocolo de control de bloqueo distribuido de **Quórum de Consenso**,
**(ii)** qué implica el que se cumpla la(s) condición(es) del protocolo y
**(iii)** la configuración de parámetros que deben aplicarse para emular los protocolos de Mayoría y Sesgado.

---

### Tema 5 (10 p.)

El ciclo para el Procesamiento de Consultas en un SGBD. Haga el diagrama y explique cada paso.

---

### Tema 6 (10 p.)

Dadas las relaciones `A(a1, a2, ..., a20)`, `B(b1, b2, ..., b12)` y `C(c1, c2, ..., c15)`, y la siguiente consulta:

```sql
select distinct A.a1, C.c1 
from A join B on (A.a2 = B.b3) 
join C on (C.c2 = B.b4) 
where A.a1 > 10 and B.b1 = 50;
```

Muestre:

1. Su traducción directa al álgebra relacional.
2. Detalle al menos 3 optimizaciones basadas en expresiones equivalentes que pueden aplicarse. Debe indicar la regla de equivalencia aplicada.
3. El árbol de evaluación de la expresión final, conforme el punto anterior.

---

### Tema 7 (10 p.)

**a.** Ilustre y describa la arquitectura de implementación de un Dataware.
**b.** Explique las 3 V’s que caracterizan a las iniciativas de Big Data.

---

### Tema 8 (10 p.)

Detalle apropiadamente cómo se implementa la organización física de bloques denominada **estructura de páginas por ranuras** para el almacenamiento de registros.
---
# Bases de Datos II – 2do. Examen Final – 16/01/2020 – Duración 90 min. – 18:00hs

---

### Tema 1 (10 p.)
Explique las formas de Almacenamiento Distribuido que pueden ser implementadas por SGBDD.

---

### Tema 2 (10 p.)
a. Desarrolle los pasos correspondientes para la semi-reunión de las relaciones ilustradas abajo.  
   Suponga que la consulta ha sido recibida en el Sitio 2.  
b. Explique o fundamente al menos dos (2) ventajas de este enfoque que no tengan que ver con la  
   reducción de costos de transmisión de datos.


R join S on (R.A2 = S.A2)

R\@S1           S\@S2
A1  A2         A2  A3  A4
1   3          3   13  16
1   4          4   14  16
1   6          7   17  17
2   3          10  14  16
2   6          11  15  16
3   7          12  15  16
3   8
3   9


---

### Tema 3 (10 p.)
Explique los tres (3) tipos de índices estudiados de acuerdo a su organización e implementación física  
e indique para cada uno para qué tipo de consultas resultan apropiados.

---

### Tema 4 (10 p.)
Explique:  
(i) el protocolo de control de bloqueo distribuido de Quórum de Consenso,  
(ii) qué implica el que se cumpla la(s) condición(es) del protocolo y  
(iii) la configuración de parámetros que deben aplicarse para emular los protocolos de Mayoría y Sesgado.

---

### Tema 5 (10 p.)
Explique las cuatro (4) formas de organización física de Archivos de Datos.

---

### Tema 6 (10 p.)
Dadas las relaciones A(a1, a2, ..., a20), B(b1, b2, ..., b12) y C(c1, c2, ..., c15), y la siguiente consulta:

select distinct A.a1, C.c1 from A join B on (A.a2 = B.b3)
join C on (C.c2 = B.b4) where A.a1 > 10 and B.b1 = 50;

Muestre:

1. Su traducción directa al álgebra relacional.
2. Detalle al menos 3 optimizaciones basadas en expresiones equivalentes que pueden aplicarse.
   Indicar la regla de equivalencia aplicada.
3. El árbol de evaluación de la expresión final, conforme el punto anterior.

---

### Tema 7 (10 p.)

a. Ilustre y describa la arquitectura de implementación de un Dataware.
b. Explique las 3 V’s que caracterizan a las iniciativas de Big Data.

---

### Tema 8 (10 p.)

Explique el algoritmo del Ascensor implementado para el acceso a la información en
Unidades de Discos Magnéticos.
---
# Bases de Datos II – Primer Examen Final – 20/11/2018 – Duración 100 min. – 18.00hs

---

### Tema 1 (10 p.)
Explique detalladamente las formas de Almacenamiento Distribuido en Sistemas de Bases de Datos Distribuidas.

---

### Tema 2 (10 p.)
En el Protocolo de Compromiso de 2 Fases en Sistemas de Bases de Datos Distribuidas, indique como se procede:

a. Un sitio participante en caso de falla del mismo, y  
b. Los sitios participantes en caso de falla del sitio coordinador.

---

### Tema 3 (10 p.)
Explique detalladamente el Modelo Abstracto del (Sub) Sistema de Transacciones implementado en un Sistema de Bases de Datos Distribuidas orientado a asegurar las propiedades ACID.

---

### Tema 4 (10 p.)
Explique qué entiende por un Gestor de Bloqueos en un SGBD que implementa un Control de Concurrencia basado en Bloqueos. Indique además cómo el mismo podría estar implementado y qué pasos debería de tener en cuenta para evitar la iniciación de las transacciones.

---

### Tema 5 (10 p.)
Explique en el contexto de los Protocolos del Control de Concurrencia que se entiende por:  
(1) Planificación,  
(2) Planificación Secuenciable,  
(3) Secuencialidad en Cuanto a Conflicto y  
(4) Secuencialidad en Cuanto a Vistas.  

Proporcione ejemplos positivos y negativos para los últimos dos casos.

---

### Tema 6 (10 p.)
Desarrolle el planteamiento hipotético de cuatro casos basados en una consulta de selección en la forma:  
`select * from <tabla> where <tabla>.<columna> = <valor>`  
y que deriven cada uno en una operación selección con coste o estimación de coste diferente.

---

### Tema 7 (10 p.)
Dada la consulta:  
`select * from A a join B b on A.a = B.b`,  
teniendo en cuenta que:

- La tabla A se encuentra almacenada en 20 bloques,  
- La tabla B se encuentra almacenada en 15 bloques,  
- La memoria cuenta con actualmente con 10 bloques libres para evaluar la consulta, y  
- Que la consulta está planificada para ser evaluada conforme el algoritmo de Bucle Anidado por Bloques,

Calcule cuál será el coste de evaluación de la consulta si:

1. La estrategia de reemplazo de bloques en la memoria es LRU.  
2. La estrategia de reemplazo de bloques en la memoria es MRU.

---

### Tema 8 (10 p.)
Detalle apropiadamente como se implementa la organización física de bloques denominada **estructura de páginas por ranuras** para el almacenamiento de registros.
---
# Bases de Datos II – Primer Examen Final – 22/11/2016 – Duración 120 minutos

---

### Tema 1 – 20 p.
**Explique concisa y ordenadamente:**
a. ¿Qué entiende por Disponibilidad y Reconfiguración en un SGBDD? (5p)  
b. Las formas de almacenamiento distribuido en un SGBDD. Proporcione ejemplos. (5p)  
c. Los tipos de índices ordenados, asociativos y bitmap, y cite un caso en los que no conviene aplicarlos. (5p)  
d. Los pasos para el Procesamiento de Consultas. Explique el diagrama. (5p)

---

### Tema 2 – 10 p.
La siguiente tabla corresponde al archivo de la relación cliente, en el que cada bloque del archivo corresponde a 1 fila, se pide:

a. Construir un índice ordenado en forma de árbol B+ con nodos de 4 punteros para la clave primaria id, suponiendo que los registros fueron insertados según el orden de los valores de la columna nombre.  
b. Construir un índice hash estático cerrado con cajones de 3 elementos cuya función de asociación es “x mod 4” sobre la columna saldo, siendo x el valor de cada fila en dicha columna.  
c. Explique a dónde apuntan los registros índices para cada caso anterior.


| ID | Nombre          | Saldo |
| -- | --------------- | ----- |
| 1  | Griffith Berger | 256   |
| 2  | Philip Cherry   | 456   |
| 3  | Kevin Conley    | 166   |
| 4  | Tad Bird        | 164   |
| 5  | Derek Bentley   | 226   |
| 6  | Upton Lane      | 935   |
| 7  | Brandon Ortiz   | 214   |
| 8  | Axel Shaw       | 213   |
| 9  | Wayne Soto      | 544   |
| 10 | Fuller Knowles  | 590   |
| 11 | Merrill Bishop  | 559   |
| 12 | Chadwick Hayden | 657   |
| 13 | David Jarvis    | 205   |
| 14 | Jakeem Vélez    | 203   |
| 15 | Andrew Wolfe    | 953   |

---

### Tema 3 – 10 p.
Dadas las relaciones r1(A, B, G) y r2(C, D, E) con las siguientes propiedades:  
r1 tiene 35.000 tuplas, r2 tiene 75.000 tuplas, 50 tuplas de r1 caben en un bloque y 100 tuplas de r2 caben en un bloque.  
Estime el número de accesos a bloques requeridos utilizando las siguientes estrategias para la reunión "r1 join r2 on (r1.C = r2.C)":

a. Reunión en bucle anidado por bloques.  
b. Reunión por mezcla, suponiendo además que la relación r2 debe ser ordenada externamente disponiéndose de 3 bloques de memoria intermedia.  
c. Reunión con índice anidada indexada, suponiendo que existe un índice primario de árbol B+ en la columna C de la relación r2 con nodos de 60 punteros.  
d. Reunión por Hash. Suponiendo el tamaño de M = 20. Recuerde que si N > M se debe aplicar particionamiento.

---

### Tema 4 – 10 p.
Dada una operación de selección cualquiera basada en una **condición de igualdad**, explique en qué situación el SGBD utilizaría cada uno de los siguientes algoritmos y el costo asintótico asociado en bloques de disco:

a. Búsqueda Lineal  
b. Búsqueda Binaria  
c. Búsqueda en índice primario para un atributo clave  
d. Búsqueda en índice secundario para un atributo no clave

---

### Tema 5 – 10 p.
Cite y explique brevemente 4 características del Dataware.

---

### Tema 6 – 10 p.
Ilustre el Proceso de Extracción, Transformación y Carga (ETL) de datos en DW.

---

### Tema 7 – 5 p.
Cite las ventajas y las desventajas de una BD NoSQL.

---

### Tema 8 – 5 p.
Describa las 3 V’s de BigData.

---

# Bases de Datos II – Primer Examen Final – 28/11/2017 – Duración 100 min. – 18.00hs

---

### Tema 1 (10 p.)
Explique detalladamente las formas de Almacenamiento Distribuido en Sistemas de Bases de Datos Distribuidas.

---

### Tema 2 (10 p.)
Explique detalladamente el Protocolo de Compromiso de 2 Fases aplicado en Sistemas de Bases de Datos Distribuidas y cómo procede:
- a. Un sitio participante en caso de falla del mismo, y  
- b. Todos los participantes en caso de falla del sitio coordinador.

---

### Tema 3 (10 p.)
Explique detalladamente el Modelo Abstracto del Sistema de Transacciones en un Sistema de Bases de Datos Distribuidas orientados a asegurar las propiedades ACID.

---

### Tema 4 (10 p.)
Explique detalladamente las propiedades de las transacciones que deben ser aseguradas por un SGBD conforme el estándar SQL.

---

### Tema 5 (10 p.)
Explique qué entiende por un Gestor de Bloqueos en un SGBD que implementa un Control de Concurrencia basado en Bloqueos. Indique además cómo el mismo podría estar implementado y qué pasos deben cumplirse para evitar la inanición de las transacciones.

---

### Tema 6 (10 p.)
Explique en el contexto de los Protocolos del Control de Concurrencia qué se entiende por:  
(1) Planificación,  
(2) Planificación Secuenciable,  
(3) Secuencialidad en Cuanto a Conflicto,  
(4) Secuencialidad en Cuanto a Vistas.

---

Aquí tienes las preguntas en **Markdown**, ahora incluyendo una nota con el nombre del archivo de imagen del que proviene cada una:

---

## Pregunta 11

**Dadas las relaciones** `"A (a1, a2, ..., a20)"`, `"B (b1, b2, ..., b12)"`, y `"C (c1, c2, ..., c15)"`, y la siguiente consulta:

```sql
SELECT DISTINCT A.a1, C.c1 
FROM A 
JOIN B ON A.a2 = B.b3 
JOIN C ON C.c2 = B.b4 
WHERE A.a1 > 10 AND B.b1 = 50;
```

**Muestre:**

1. Su traducción directa al álgebra relacional.
2. Los pasos para llegar a la expresión equivalente tal que se minimice la cantidad de datos procesados por cada operación.
3. El árbol de evaluación de la expresión final. Debe levantar una imagen del desarrollo realizado a mano alzada.

---

## Pregunta 12

**Describa el protocolo de compromiso de 2 fases. Asimismo indique cómo se procede: (a) en caso de falla del coordinador y (b) en caso de falla de un sitio participante.**

### Fase 1:

Esta fase comienza luego de la última sentencia de T.
CI añade el mensaje *"Preparar T"* a la bitácora y fuerza a guardar la bitácora en almacenamiento persistente.
CI envía el mensaje *"Preparar T"* a todos los participantes SKi.

En cada sitio participante SKi:

* El gestor SKi determina si se puede comprometer esta parte de T.
* Si no es posible comprometer T en SKi, SKi añade a la bitácora *"No"* y fuerza escritura del mensaje *"Abortar T"*.
* Si es posible comprometer T en SKi, SKi añade *"Preparado T"* a su bitácora y fuerza su grabación.
* En ambos casos, SKi envía el mensaje correspondiente a CI.

### Fase 2:

Comienza cuando CI recibe todas las respuestas `"Preparado T"` de los SKi,
o cuando ha transcurrido cierto tiempo desde que se ha enviado el mensaje *"Preparar T"* y no se han recibido todas las respuestas.

* Si se han recibido todas las respuestas y todas son *"Preparado T"*,
  CI añade a su bitácora *"Comprometido T"* y envía ese mensaje a los SKi.
* Cuando un SKi recibe el mensaje *"Comprometer T"*, compromete su parte y escribe *"Comprometido T"* en su bitácora.
* Si algún SKi no ha enviado *"Preparado T"*, CI envía *"Abortar T"* a todos y escribe *"Abortado T"*.

---

### En caso de falla:

#### a) Falla del coordinador:

Durante la recuperación del protocolo de confirmación de escritura:

* Si un sitio contiene *"Comprometido T"*, entonces T debe ser completado.
* Si contiene *"Abortar T"*, debe ser abortado.
* Si solo hay *"Preparado T"*, los sitios deben coordinarse entre sí y CI debe ser reelegido.

#### b) Falla de un sitio participante:

Al recuperarse, el sitio lee su bitácora:

* Si encuentra *"Comprometido T"*, realiza el *commit*.
* Si encuentra *"Abortar T"*, realiza el *rollback*.
* Si encuentra *"Preparado T"*, consulta a otros sitios.
* Si nadie tiene registros, se decide por aborto.

> **Nota:** Este protocolo resuelve el *problema del bloqueo* y depende del correcto manejo de bitácoras y comunicación.

---

Perfecto. Aquí tienes las preguntas en **Markdown**, ahora todas con su respectivo nombre de archivo de imagen:

---

## Pregunta 1

📷 *Archivo: `WhatsApp Image 2021-06-29 at 23.38.52 (2).jpeg`*

**Explique en forma precisa las formas de Almacenamiento Distribuido que pueden ser implementadas por SGBDD.**

* **Replicación de Datos:** El sistema conserva varias réplicas (copias) idénticas de la relación y guarda cada réplica en un sitio diferente.
  La alternativa es almacenar solo una copia de la relación r. Si la relación r se replica, se guarda una copia de esa relación en dos o más sitios.
  En el caso más extremo se tiene una réplica completa, en la que se guarda una copia en cada sitio del sistema.

* **Fragmentación de Datos:** El sistema divide la relación en varios fragmentos y guarda cada fragmento en un sitio diferente.
  Existen dos esquemas:

  * Fragmentación horizontal: asigna cada tupla de r a uno o más fragmentos.
  * Fragmentación vertical: divide el esquema r en subconjuntos de atributos.

**Comentarios:**
Faltó detallar cómo se definen y reconstruyen los fragmentos, así como indicar ventajas y desventajas de cada uno.

---

## Pregunta 2

📷 *Archivo: `WhatsApp Image 2021-06-29 at 23.38.52.jpeg`*

**Explique las formas de organización física de los archivos de datos en un SGBD.**

* **Heaps:** Registros guardados donde haya espacio; no se ordenan.
* **Secuencial:** Registros guardados en orden según una clave de búsqueda.
* **Hash:** Registros almacenados en bloques según una función hash sobre algún campo.
* **Organización en agrupación:** Datos de varias relaciones se guardan en un mismo archivo.

---

## Pregunta 3

📷 *Archivo: `WhatsApp Image 2021-06-29 at 23.38.53 (1).jpeg`*

**Explique:**

1. El protocolo de control de bloqueo distribuido de Quórum de Consenso.
2. Qué implica que se cumpla cada una de las condiciones del protocolo.
3. Configuración de parámetros para emular los protocolos de Mayoría y Sesgado.

---

## Pregunta 4

📷 *Archivo: `WhatsApp Image 2021-06-29 at 23.38.53 (2).jpeg`*

**Respuesta a la Pregunta 3 (continuación)**

* **Condiciones del Protocolo de Quórum:**
  Qr + Qw > S
  2 \* Qw > S
  Donde S es la suma de los pesos de todos los sitios.

* **Lectura:** Se bloquean suficientes réplicas que sumen ≥ Qr.

* **Escritura:** Se bloquean suficientes réplicas que sumen ≥ Qw.

* **Condición:** Impide bloqueos exclusivos simultáneos.

* **Emulación:**

  * *Mayoría:* Qr = Qw = n/2 + 1
  * *Sesgado:* Qr = 1, Qw = n

**Comentarios:**
(ii) Incompleto. Faltó indicar que también previene bloqueos exclusivos simultáneos.

---

## Pregunta 5

📷 *Archivo: `WhatsApp Image 2021-06-29 at 23.38.53 (3).jpeg`*

**Describa el Algoritmo del Luchador. Explique su aplicabilidad en SGBDD.**

* El sitio Si asume la falla del coordinador si no recibe respuesta en un tiempo T.
* Inicia elecciones entre sitios con mayor ID.
* Si no hay respuesta, se autodeclara coordinador.
* Si hay respuesta, espera confirmación.
* El algoritmo reinicia si el nuevo coordinador no responde.

**Disponibilidad:**
Se asegura continuidad en presencia de fallos.

**Reconfiguración:**
Permite adaptar el sistema abortando transacciones de sitios fallidos y eligiendo nuevos sitios.

---

## Pregunta 6

📷 *Archivo: `WhatsApp Image 2021-06-29 at 23.38.51 (1).jpeg`*

**Detalle los pasos lógicos para el procesamiento de consultas.**

1. **Análisis y Traducción:** Verifica sintaxis y convierte a álgebra relacional.
2. **Optimización:** Minimiza el costo de evaluación usando estadísticas.
3. **Evaluación:** Ejecuta el plan de consulta generado.

**Comentario:**
El motor de evaluación no decide ni analiza, solo ejecuta el plan indicado por el optimizador.

---

## Pregunta 7

📷 *Archivo: `WhatsApp Image 2021-06-29 at 23.38.51 (2).jpeg`*

**Dada una operación de selección con igualdad simple, indique qué condiciones obligan a usar:**

1. **Búsqueda Lineal:** Sin índice ni orden.
2. **Búsqueda Binaria:** Tabla ordenada, sin índice.
3. **Índice Primario:** Con clave índice.
4. **Índice Secundario:** Sin clave única, puede recuperar varios registros.

---

## Pregunta 8

📷 *Archivo: `WhatsApp Image 2021-06-29 at 23.38.51 (3).jpeg`*

**Explique por qué la organización con Árboles B y B+ es adecuada para implementar índices ordenados.**

* Eficientes para búsquedas en rango.
* Son auto-balanceados.
* Ordenan automáticamente por clave índice.

**Comentario:**
La respuesta es dispersa, pero aceptable.

---

## Pregunta 9

📷 *Archivo: `WhatsApp Image 2021-06-29 at 23.38.51.jpeg`*

**Explique los tipos de índices según su organización física y cuándo aplicarlos.**

* **Ordenados:** Basados en clave; útiles para igualdad/desigualdad.
* **Asociativos:** Usan hash; aplicables en igualdad.
* **Bitmaps:** Usan bits por valor de atributo; útiles para múltiples claves.

**Comentario:**
No se explicó el propósito y forma de aplicación del array de bits.

---

## Pregunta 10

📷 *Archivo: `WhatsApp Image 2021-06-29 at 23.38.52 (1).jpeg`*

**Ejercicio a mano alzada sobre planificación de transacciones.**

A y B: Determinar si las planificaciones son serializables/conflictivas.

* Se evalúa si los planes cumplen con las condiciones de serialización.
* Plan 3 en ambos casos parece ser serializable.



Aquí tienes el texto extraído de la imagen `6e73e01c-9467-42bf-a0be-b893b62c6887.png` (procesado por OCR). El resultado contiene errores por la baja calidad o alineación del texto, pero se puede reconstruir una versión bastante fiel:

---

### **Texto Extraído (y reconstruido parcialmente)**

**Tema 1 (10 p.):**
Explique detalladamente las medidas de rendimiento que deben ser consideradas respecto a los discos magnéticos.

**Tema 2 (10 p.):**
Explique detalladamente las ventajas de configurar un esquema de almacenamiento basado en RAID.
Ejemplifique además los niveles 1 y 5.

**Tema 4 (10 p.):**
Dada la consulta de abajo, proporcione una traducción inicial de la misma en álgebra relacional y luego
proceda a ilustrar con la misma al menos dos casos de optimización conforme las reglas de equivalencias estudiadas:

```sql
select e.LNAME from EMPLEADO e
join TRABAJA_EN te on (te.EMPLEADO = e.ID)
join PROYECTO p on (p.ID = te.PROYECTO)
where p.NOMBRE = "AQUARIUS" and e.FECHA_NAC >= '2000-01-01'
```

**Tema 5 (10 p.):**
Explique en el contexto de los Protocolos del Control de Concurrencia qué se entiende por:
(1) Planificación,
(2) Planificación Secuenciable,
(3) Secuencialidad en Cuanto a Conflicto,
(4) Secuencialidad en Cuanto a Vistas.

**Tema 6 (10 p.):**
Ilustre la construcción de un índice Hash basado en la técnica de Asociación Extensible para la columna `nombre-sucursal` considerando para ello la tabla y los valores de hash indicados a continuación:


---

### 📊 Tabla de la relación con nombre-sucursal y saldo

| Código | Nombre Sucursal | Saldo |
| ------ | --------------- | ----- |
| C-217  | Barcelona       | 750   |
| C-218  | Daimiel         | 500   |
| C-219  | Daimiel         | 600   |
| C-213  | Madrid          | 400   |
| C-214  | Pamplona        | 650   |
| C-215  | Pamplona        | 700   |
| C-216  | Pamplona        | 300   |
| C-273  | Madrid          | 400   |
| C-219  | Ronda           | 350   |

---

### 🧮 Valores de hash binarios por nombre-sucursal

![alt text](<Screenshot 2025-05-05 152219.png>)

| Nombre Sucursal | Hash Binario                       |
| --------------- | ---------------------------------- |
| Barcelona       | 0010, 1101, 1111, 0011, 0110, 0001 |
| Daimiel         | 1010, 0101, 0111, 1000             |
| Madrid          | 0110, 0111, 1011                   |
| Pamplona        | 0000, 0100, 1101                   |
| Ronda           | 0000, 0001, 0101, 0110, 0000       |

---

### Tema 7 (10 p.)

Ejemplifique cuatro planteamientos hipotéticos que ilustren cada uno la aplicación de un algoritmo de selección diferente, indicando además el coste o estimación de coste del mismo.

---

### Tema 8 (10 p.)

Dada la consulta:

```sql
SELECT * FROM A A JOIN B B ON A.a = B.b
```

Teniendo en cuenta que:

* La tabla A se encuentra almacenada en 12 bloques de disco.
* La tabla B se encuentra almacenada en 25 bloques de disco.
* La memoria cuenta actualmente con 10 bloques libres para evaluar la consulta.
* Que la consulta está planificada para ser evaluada conforme al algoritmo de Bucle Anidado por Bloques.

**Calcule cuál será el coste de evaluación de la consulta si:**

1. La estrategia de reemplazo de bloques en la memoria es **LRU**.
2. La estrategia de reemplazo de bloques en la memoria es **MRU**.


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
- Tema 7: zb .
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

