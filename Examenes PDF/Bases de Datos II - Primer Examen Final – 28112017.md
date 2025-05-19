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
