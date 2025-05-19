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