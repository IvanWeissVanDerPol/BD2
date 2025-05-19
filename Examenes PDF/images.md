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
