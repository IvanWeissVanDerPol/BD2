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
