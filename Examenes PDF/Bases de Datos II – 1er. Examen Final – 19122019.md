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
