Perfecto. A continuación, te presento una **explicación profunda y fundamentada** de cada ítem del **Tema 1**, integrando el contenido del libro *Fundamentos de Bases de Datos 18-19*, las presentaciones que compartiste, y el conocimiento contextual de sistemas distribuidos modernos.

---

## 🧩 **Tema 1 – 10 puntos: Explicación Integral**

---

### **a) Las formas de Almacenamiento Distribuido en BDD y sus Ventajas**

Los **Sistemas de Bases de Datos Distribuidos (BDD)** almacenan los datos a través de múltiples sitios físicos interconectados mediante una red. Esta arquitectura está pensada para **acercar los datos al usuario**, mejorar el rendimiento y garantizar tolerancia a fallos.

Existen **dos técnicas fundamentales de almacenamiento distribuido**:

---

#### ✅ 1. **Fragmentación**

La **fragmentación** consiste en **dividir una relación (tabla)** de una base de datos en partes llamadas **fragmentos**, que pueden ser distribuidos a diferentes sitios.

##### a) **Fragmentación Horizontal**

* Cada fragmento contiene un subconjunto de filas (tuplas).
* Se define por condiciones lógicas sobre atributos.
* Ejemplo: La relación `Cliente` se fragmenta en `Clientes_América`, `Clientes_Europa`, etc.

**Ventajas**:

* Procesamiento localizado: se consulta el fragmento local, reduciendo el tráfico de red.
* Mejora del tiempo de respuesta.
* Paralelismo en consultas distribuidas.

##### b) **Fragmentación Vertical**

* Cada fragmento contiene un subconjunto de columnas (atributos).
* Todos los fragmentos contienen una clave común (ej. `ID`) para reconstrucción mediante *join*.

**Ventajas**:

* Mejora la seguridad y privacidad (separación de datos sensibles).
* Optimiza acceso a campos específicos sin cargar toda la fila.

##### c) **Fragmentación Mixta**

* Aplica ambas estrategias (ej. fragmentar horizontalmente primero y luego verticalmente).

---

#### ✅ 2. **Replicación**

La **replicación** es la creación de **copias redundantes de datos o fragmentos** en múltiples nodos.

##### a) **Replicación completa**

* Todos los nodos contienen copias idénticas de las relaciones.
* Se maximiza disponibilidad, pero se incrementa el costo de actualización.

##### b) **Replicación parcial**

* Solo ciertos fragmentos están replicados.
* Ej. replicar solo clientes activos en varias regiones.

---

#### 📌 **Ventajas del Almacenamiento Distribuido**

* **Alta disponibilidad**: en caso de fallo de un sitio, otros sitios tienen los datos.
* **Reducción de latencia**: se accede a los datos localmente.
* **Escalabilidad horizontal**: se pueden añadir nodos sin rediseñar el sistema.
* **Paralelismo**: múltiples nodos procesan consultas simultáneamente.
* **Aislamiento físico y lógico**: permite separar datos por región, por tipo o por frecuencia de uso.

---

### **b) ¿Qué se entiende por Alta Disponibilidad y Reconfiguración en un Sistema de BDD?**

---

#### ✅ Alta Disponibilidad

Se refiere a la **capacidad del sistema de continuar operando** sin interrupción significativa, incluso cuando ocurren fallos en uno o más de sus componentes.

En un BDD, esto implica que:

* **Los datos siguen accesibles** a pesar de que uno o más nodos fallen.
* Se aplican técnicas como:

  * **Replicación sincrónica o asincrónica**
  * **Failover automático**
  * **Protocolos de recuperación distribuidos** como el **protocolo de compromiso de dos fases (2PC)**

**Ejemplo**: si un sitio que contiene una réplica cae, otro sitio puede seguir respondiendo a las consultas.

---

#### ✅ Reconfiguración

La **reconfiguración** es la **capacidad dinámica del sistema distribuido** para adaptarse ante:

* Fallos de nodos (caídas temporales o definitivas)
* Ingreso de nuevos nodos
* Cambios en la topología o carga del sistema

**Mecanismos implicados**:

* **Detección de fallos** (usualmente por heartbeats).
* **Redistribución automática de datos** o asignación de coordinadores.
* **Actualización de metadatos y catálogos distribuidos.**

**Importancia**:

* Garantiza que el sistema **no dependa de una configuración rígida**.
* Mantiene **operatividad, equilibrio de carga y tolerancia a fallos**.

---

### **c) El Algoritmo del Luchador**

Este algoritmo se refiere a una **estrategia de recuperación frente a interbloqueos** (deadlocks) en sistemas distribuidos.

---

#### 🔒 ¿Qué es un interbloqueo?

Ocurre cuando **dos o más transacciones están esperando recursos** que están siendo retenidos por otras, formando un ciclo de espera que **nunca se resuelve** por sí solo.

---

#### 🥊 El Algoritmo del Luchador (The Wound-Wait y Wait-Die)

Aunque "Algoritmo del Luchador" no es un nombre canónico, en literatura de BDD este tipo de solución hace referencia a **estrategias de prevención de deadlocks** donde:

### Estrategias típicas:

#### ✅ **Wait-Die**

* Si una transacción vieja solicita un recurso bloqueado por una más joven → **espera**.
* Si una transacción joven solicita un recurso de una más vieja → **se aborta ("muere")** y se reinicia después.

#### ✅ **Wound-Wait**

* Si una transacción más vieja solicita un recurso de una más joven → **la joven es abortada ("herida")**.
* Si una transacción más joven solicita un recurso de una más vieja → **espera**.

---

### 📌 Propósito del algoritmo:

* **Evitar interbloqueos** antes de que ocurran.
* Mantener un orden total de llegada (timestamp) para tomar decisiones.
* Minimizar abortos innecesarios (con respecto al modelo de víctima aleatoria).



## ✅ **Tema 2 – 10 p.**

**Objetivo**: Minimizar la transmisión de datos entre sitios durante un `JOIN` entre dos relaciones distribuidas.

---

### 🔹 Enunciado

Queremos realizar:

```sql
R ⨝ S ON R.A2 = S.A2
```

* La consulta fue **recibida en el Sitio 1 (donde está R)**.
* El resultado también debe generarse en **Sitio 1**.
* Queremos aplicar la **estrategia de la semireunión (semijoin)**.

---

## 🧠 ¿Qué es la Estrategia de la Semireunión?

El **semijoin** consiste en:

1. **Enviar solo las claves necesarias** desde el sitio destino al origen.
2. Filtrar las tuplas del sitio remoto.
3. Enviar **solo las filas relevantes** desde el sitio remoto al sitio origen.
4. Realizar el join completo localmente.

🔁 Esto **reduce el volumen de datos transmitidos** entre sitios, comparado con enviar una relación completa.

---

## 🧾 Paso a paso con el ejemplo:

### 🔹 **Relación R en S1**

| A1 | A2 |
| -- | -- |
| 1  | 3  |
| 1  | 4  |
| 1  | 6  |
| 2  | 7  |
| 2  | 10 |
| 3  | 4  |
| 3  | 5  |
| 3  | 8  |
| 3  | 9  |

### 🔹 **Relación S en S2**

| A2 | A3 | A4 |
| -- | -- | -- |
| 3  | 13 | 16 |
| 4  | 14 | 16 |
| 6  | 13 | 17 |
| 10 | 14 | 16 |
| 11 | 15 | 15 |
| 12 | 16 | 15 |

---

## 🧮 **Pasos de la Estrategia de Semireunión**

### 🔸 Paso 1: Proyectar en S1 los valores de A2 de R (Sitio 1)

```sql
π_A2(R)
```

Resultado:
`{3, 4, 5, 6, 7, 8, 9, 10}`

(Se descartan duplicados)

---

### 🔸 Paso 2: Enviar estos valores al Sitio 2 (S2)

Se transmite el conjunto `{3, 4, 5, 6, 7, 8, 9, 10}` → **8 valores**

---

### 🔸 Paso 3: En Sitio 2, seleccionar solo las tuplas de S donde A2 está en ese conjunto

```sql
σ_A2∈{3,4,5,6,7,8,9,10}(S)
```

Filtrado en S2 da como resultado:

| A2 | A3 | A4 |
| -- | -- | -- |
| 3  | 13 | 16 |
| 4  | 14 | 16 |
| 6  | 13 | 17 |
| 10 | 14 | 16 |

→ **4 filas relevantes**

---

### 🔸 Paso 4: Enviar esas 4 filas desde S2 a S1

---

### 🔸 Paso 5: Realizar el JOIN en S1

Ahora en S1 puedes hacer:

```sql
R ⨝ S_filtro
```

Usando las filas relevantes de S, se filtran los pares coincidentes:

* (1,3) ⨝ (3,13,16)
* (1,4) ⨝ (4,14,16)
* (1,6) ⨝ (6,13,17)
* (2,10) ⨝ (10,14,16)
* (3,4) ⨝ (4,14,16)

---

## ✅ Resultado final (en S1):

| A1 | A2 | A3 | A4 |
| -- | -- | -- | -- |
| 1  | 3  | 13 | 16 |
| 1  | 4  | 14 | 16 |
| 1  | 6  | 13 | 17 |
| 2  | 10 | 14 | 16 |
| 3  | 4  | 14 | 16 |

---

## 📉 Comparación: Estrategia Ingenua (Join completo)

La estrategia más simple sería **enviar toda la tabla S desde S2 a S1** (sin filtrado).

* Tabla **S** completa tiene **6 filas de 3 atributos** = 18 valores
* Semijoin envió:

  * Paso 2: 8 valores de A2
  * Paso 4: 4 filas de 3 atributos = 12 valores
  * Total: 8 + 12 = **20 valores transmitidos**

⚠️ **Sin semijoin** se transmitirían 18 valores
⚠️ **Con semijoin** se transmiten 20 valores
→ En este caso, **no hay ahorro neto**, pero en tablas más grandes, el semijoin reduce drásticamente el volumen transmitido.










Cuestionario 1, 2do. Parcial, 2021


(a) Defina el concepto de Transacción en SGBDs. (b) Indique y defina las fases del
Ciclo de Vida de una Transacción. (b) Indique y defina las propiedades que un
SGBD debe asegurar para las Transacciones.

(a) Explique que es una Planificación Secuencial. (b) Explique que es una
Planificación Secuenciable. (c) Fundamente a su criterio la importancia de la
Secuencialidad en SGBD.

(a) Describa el protocolo de Bloqueo de 2 Fases. (b) Indique cuales son las
variantes del mismo.

(a) Describa la función del Componente de Gestión de Concurrencia en un SGDB.
(b) Describa la estructura de datos utilizada para la gestión y concesión de
bloqueos.

Cuestionario 2, 2do. Parcial, 2021

Explique detalladamente las formas de almacenamiento distribuido en Bases de
Datos Distribuidas Relacionales.

(a) Detalle los pasos de cada fase del protocolo C2F en Bases de Datos
Distribuidas. (b) Indique como proceden los participantes en caso de falla del
coordinador. (c) Indique como se procede un sitio en caso de falla del mismo.

Conforme la figura de abajo y la consulta "select * from R join S". Indique los pasos
y el costo total de trasmisión de realizar la Estrategia de la Semireunión si la
consulta fue recibida: (a) en el Sitio 1, (b) en el Sitio 2.

📊 Tablas dadas
🔸 Sitio 1 – R
A1	A2
1	3
1	4
1	6
2	3
2	6
2	7
3	8
3	9

🔸 Sitio 2 – S
A2	A3	A4
3	13	16
3	14	16
7	13	17
10	14	16
10	15	17
11	15	16
11	15	16
12	15	16

Cuestionario 3, 2do. Parcial, 2021

Explique en sus términos: ¿Cuál es la diferencia entre bases de datos OLTP y
OLAP?. Así mismo, cite al menos dos ejemplos de aplicación para cada tipo.

Explique en sus términos en qué consisten las tablas de dimensiones, tablas de
hechos y medidas en el modelado multidimensional. Así mismo, enumere al menos
tres ejemplos para cada uno.