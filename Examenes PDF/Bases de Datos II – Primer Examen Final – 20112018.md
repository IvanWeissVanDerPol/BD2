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
