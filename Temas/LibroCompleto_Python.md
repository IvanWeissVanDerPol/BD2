# Bases de Datos Avanzadas - Libro Completo

Este libro reúne todos los temas relacionados con Bases de Datos Avanzadas en un solo lugar.

## Tabla de Contenidos

1. [Índices](#1-índices)
2. [Organización Física de Archivos](#2-organización-física-de-archivos)
3. [Medidas de Rendimiento de Discos](#3-medidas-de-rendimiento-de-discos)
4. [Niveles RAID](#4-niveles-raid)
5. [Árboles B y B+](#5-árboles-b-y-b)
6. [Algoritmos de Búsqueda](#6-algoritmos-de-búsqueda)
7. [Procesamiento de Consultas](#7-procesamiento-de-consultas)
8. [Modelado Multidimensional](#8-modelado-multidimensional)
9. [Transacciones (ACID)](#9-transacciones-acid)
10. [Concurrencia](#10-concurrencia)
11. [Protocolos Distribuidos](#11-protocolos-distribuidos)
12. [Almacenamiento Distribuido](#12-almacenamiento-distribuido)
13. [Optimización de Consultas](#13-optimización-de-consultas)
14. [Normalización y Dependencias Funcionales](#14-normalización-y-dependencias-funcionales)
15. [Modelado ER y SQL](#15-modelado-er-y-sql)


## 1. Indices



## 🔍 **¿Qué es un Índice?**

Un **índice** en bases de datos es una estructura auxiliar que facilita la recuperación eficiente de registros específicos, reduciendo significativamente el tiempo de consulta. Funciona de manera similar al índice al final de un libro: permite localizar información rápidamente sin revisar todo el contenido.

Un **archivo índice** es un archivo físico separado que almacena referencias a las filas del archivo principal de datos según el valor de la columna indexada.

### 📌 **Tipos principales de índices estudiados:**
1. **Índice ordenado** (basado en árboles B y B+).
2. **Índice hash**.
3. **Índice bitmap**.

---

## 📗 **Tipos de Índices según sus consultas apropiadas**

| Tipo índice | Ideal para consultas |
|-------------|----------------------|
| Ordenado    | Rangos (ej. fechas, intervalos numéricos) |
| Hash        | Consultas exactas (condiciones de igualdad) |
| Bitmap      | Consultas múltiples simultáneas (muchas condiciones sobre columnas booleanas o categóricas) |

---

## 📚 **Tipos de Índices según su Organización Física**

### 1. **Índice Ordenado (Árbol B/B+)**
- Almacena valores ordenados jerárquicamente, permitiendo búsquedas rápidas y eficientes.
- Aplicación ideal: consultas con rangos, valores cercanos.

### 2. **Índice Hash**
- Usa una función de hash para determinar la ubicación física de un dato.
- Aplicación ideal: búsquedas puntuales exactas.

### 3. **Índice Bitmap**
- Cada valor único tiene un mapa de bits asociado, útil en columnas con pocos valores únicos.
- Aplicación ideal: múltiples condiciones simultáneas.

---

## 📈 **Costos Asintóticos de Algoritmos de Búsqueda**

| Algoritmo               | Costo Asintótico (promedio) |
|-------------------------|-----------------------------|
| (a) Búsqueda lineal     | O(n)                        |
| (b) Búsqueda binaria    | O(log n)                    |
| (c) Índice primario (B+) | O(log n)                   |
| (d) Índice secundario   | O(log n)                    |

---

## 📌 **Condiciones físicas para usar algoritmos (en igualdad):**

| Algoritmo           | Condición física ideal                  |
|---------------------|----------------------------------------|
| Búsqueda Lineal     | No existe índice. Tabla pequeña.        |
| Búsqueda Binaria    | Tabla ordenada secuencialmente sin índices disponibles.|
| Índice Primario (B+)| Existe índice sobre clave primaria.     |
| Índice Secundario   | Existe índice sobre atributo no clave.  |

---

## 📊 **Gráfico ilustrativo (Ejemplo Índice B+):**

```plaintext
                   [20, 40]
                  /    |    \
         [5,10,15] [25,30,35] [45,50,55]
```

- **Búsqueda**: Recorre árbol desde raíz hacia hojas rápidamente.

---

## 🧩 **Ejercicios Resueltos**

### 🛠️ **Tema 6: Construcción Índice Hash (Asociación Extensible)**

La asociación extensible es una técnica de hash dinámico que permite expandir el espacio de almacenamiento conforme crece la base de datos.

**Ejemplo:**

- Función hash simple: `h(x) = x mod 4`
- Datos iniciales: `4, 8, 5, 7, 12, 15`

| Cajón (bucket) | Valores almacenados |
|----------------|---------------------|
| 0              | 4, 8, 12            |
| 1              | 5                   |
| 2              |                    |
| 3              | 7, 15               |

Cuando un cajón excede capacidad, se duplica el índice aumentando el número de bits y re-distribuyendo valores.

---

### 🛠️ **Tema 10: Índice B+ e Índice Hash Estático**

#### 🔹 **Construcción Índice B+ (ejemplo sencillo):**

Datos: `[10,20,30,40,50,60,70,80]`, 4 punteros por nodo.

```plaintext
         [40]
      /        \
  [10,20,30]  [50,60,70,80]
```

- **Clasificación:** Primario (si índice está sobre clave primaria).

#### 🔹 **Construcción Índice Hash estático:**

Datos: `[21,32,43,54]`, función hash `h(x) = x mod 4`

| Cajón | Datos     |
|-------|-----------|
| 0     | 32        |
| 1     | 21        |
| 2     | 54        |
| 3     | 43        |

- **Clasificación:** Secundario (generalmente índices hash son secundarios, ya que suelen aplicarse a atributos no clave para búsquedas exactas).

---

## ✅ **Ejercicios planteados:**

### **Ejercicio 1: ¿Qué es un índice y archivo índice?**
- **Índice:** Estructura auxiliar que acelera la recuperación de datos.
- **Archivo índice:** Archivo físico separado que contiene referencias a registros según columna indexada.

**Tres tipos de índices estudiados:**
- Índice Ordenado (Árbol B+).
- Índice Hash.
- Índice Bitmap.

---

### **Ejercicio 2: Índices apropiados según consulta:**
- (a) **Ordenado:** Rangos, intervalos. (Ej: Fecha de nacimiento entre 1990-2000).
- (b) **Hash:** Igualdad exacta. (Ej: CI = 123456).
- (c) **Bitmap:** Múltiples condiciones simultáneas. (Ej: Género=Femenino AND Ciudad=Asunción).

---

### **Ejercicio 3: Organización física y aplicación:**
- **B+ (Ordenado):** Consultas rango, ordenación rápida.
- **Hash:** Igualdad exacta rápida.
- **Bitmap:** Consultas analíticas con múltiples condiciones categóricas.

---

### **Ejercicio 4: Costos asintóticos explicados antes.**
- (a) Lineal: `O(n)`
- (b) Binaria: `O(log n)`
- (c) Primario: `O(log n)`
- (d) Secundario: `O(log n)`

---

### **Ejercicio 5: Condiciones físicas explicadas antes.**

- **Lineal:** Sin índice, tabla pequeña.
- **Binaria:** Tabla ordenada sin índice.
- **Primario:** Índice clave primaria disponible.
- **Secundario:** Índice atributo no clave disponible.

---

### 📌 **Resumen Visual del uso de índices según tipo de consulta:**
```plaintext
Consultas de rango  → Índice Ordenado (B+)
Consultas exactas   → Índice Hash
Consultas complejas → Índice Bitmap
```

---

## 📝 **Conclusión**

- **Índices** aceleran consultas significativamente.
- Cada tipo es ideal según tipo de consulta y estructura de datos.
- Importante evaluar costo-beneficio al elegir índice.



## 2. Organizacion Fisica Archivos



# 📂 **Organización Física de Archivos**

La **organización física de archivos** hace referencia a cómo se almacenan los registros en los archivos físicos de un Sistema Gestor de Bases de Datos (SGBD). Elegir la estructura adecuada afecta considerablemente el rendimiento, especialmente en consultas e inserciones.

---

## 📑 **Formas de Organización Física**

Existen principalmente cuatro formas de organización física:

### **1. Heap (Montón):**
- Los registros son almacenados en cualquier espacio libre disponible.
- **Ventaja:** Inserción muy rápida.
- **Desventaja:** Consultas lentas (requiere escaneo completo).

**Ejemplo:**  
Agregar un nuevo cliente al archivo de clientes sin preocuparse de dónde queda ubicado exactamente.

---

### **2. Secuencial (Ordenado):**
- Registros almacenados consecutivamente en orden según una clave.
- **Ventaja:** Consultas por rango muy eficientes.
- **Desventaja:** Inserciones lentas, requieren reorganización periódica.

**Ejemplo:**  
Historial de transacciones ordenado por fecha.

---

### **3. Hash:**
- Ubicación de registros determinada por una función hash aplicada sobre la clave.
- **Ventaja:** Búsqueda puntual extremadamente rápida.
- **Desventaja:** Mal rendimiento en consultas por rango.

**Ejemplo:**  
Buscar datos exactos como DNI o número de teléfono.

---

### **4. Agrupación (Cluster):**
- Almacena juntos registros relacionados o que se consultan con frecuencia.
- **Ventaja:** Consultas comunes aceleradas.
- **Desventaja:** Actualizaciones más lentas si afectan las columnas agrupadas.

**Ejemplo:**  
Datos de un cliente y todas sus facturas en bloques cercanos.

---

## 📋 **Organización de registros en archivos (resumen en términos simples):**
- **Heap:** Cualquier lugar libre (desordenado, rápido inserción).
- **Secuencial:** Ordenado en función de una clave.
- **Hash:** Ubicación mediante cálculo hash.
- **Cluster:** Agrupación lógica de datos relacionados.

---

## 🗂️ **Formas de organización para implementar tablas/datos (simplificado):**
- Para datos que cambian mucho: **Heap**.
- Para consultas frecuentes de rangos: **Secuencial**.
- Para búsquedas exactas rápidas: **Hash**.
- Para consultas relacionadas frecuentes: **Cluster**.

---

## 📌 **Tema 9: Estructura física de bloques (Páginas por ranuras)**

La organización por páginas y ranuras (slot-based pages) se implementa dividiendo cada bloque físico del archivo en "ranuras" que almacenan registros individuales. Esto facilita inserciones, eliminaciones y modificaciones con mínima fragmentación.

### 🔹 **Implementación:**
Cada página se divide en dos partes:
- **Cabecera:** Contiene un directorio con punteros (slots) hacia los registros.
- **Cuerpo de datos:** Registros almacenados secuencialmente (no necesariamente contiguos).

Cada registro se accede mediante la referencia en la ranura, permitiendo eliminar y reutilizar espacios fácilmente.

### Ejemplo visual (gráfico):

```
Página Física (Bloque)
+-------------------------+
| Cabecera de ranuras     |
|-------------------------|
| Ranura 1 -> Registro A  |
| Ranura 2 -> Registro B  |
| Ranura 3 -> [libre]     |
| Ranura 4 -> Registro C  |
|-------------------------|
| Cuerpo de registros     |
| [Registro A]            |
| [Registro B]            |
| [espacio libre]         |
| [Registro C]            |
+-------------------------+
```

- Al borrar un registro, simplemente se marca la ranura como disponible.
- Al insertar, se reutilizan ranuras vacías.

---

## 📊 **Gráfica Comparativa de rendimiento por tipo de organización:**

```plaintext
Rendimiento (menor tiempo es mejor)

Consulta exacta:
Hash          [■■■■■■■■■■]
Secuencial    [■■■■■□□□□□]
Heap          [■■□□□□□□□□]
Cluster       [■■■■□□□□□□]

Consulta rango:
Secuencial    [■■■■■■■■■■]
Cluster       [■■■■■■■■□□]
Heap          [■□□□□□□□□□]
Hash          [□□□□□□□□□□]

Inserción rápida:
Heap          [■■■■■■■■■■]
Hash          [■■■■■■■■□□]
Cluster       [■■■■■■□□□□]
Secuencial    [■■■■□□□□□□]
```

---

## 📝 **Respuestas detalladas a los ejercicios propuestos:**

### 🔹 **1. Explicación de las formas de organización física en SGBD:**

- **Heap:** No ordenado, rápido insertar, lento consultar.
- **Secuencial:** Ordenado por clave, rápido para rangos, lento insertar.
- **Hash:** Distribución por función hash, búsquedas exactas rápidas.
- **Cluster:** Agrupación lógica, mejora consultas frecuentes relacionadas.

---

### 🔹 **2. Formas resumidas de organización de registros (propios términos):**

- **Heap:** Registros en espacio disponible rápidamente.
- **Secuencial:** Registros siempre en orden específico.
- **Hash:** Ubicación según cálculo matemático (hash).
- **Cluster:** Registros relacionados almacenados cerca.

---

### 🔹 **3. Formas apropiadas para implementación práctica de tablas/datos:**

| Uso habitual               | Organización ideal |
|----------------------------|--------------------|
| Insertar muy frecuentemente| Heap               |
| Rangos frecuentes          | Secuencial         |
| Igualdad frecuente         | Hash               |
| Datos relacionados juntos  | Cluster            |

---

### 🔹 **4. Detalle de la estructura de páginas por ranuras (Tema 9):**

- Divide página en dos zonas: cabecera (ranuras) y cuerpo (registros).
- Usa directorio de ranuras con punteros hacia registros reales.
- Permite gestión eficiente de inserción/borrado con fragmentación mínima.

---

## ✅ **Ejemplo práctico de página por ranuras:**

- Inserción:
  - Registro D entra en ranura 3 libre.

```
+-------------------------+
| Cabecera de ranuras     |
|-------------------------|
| Ranura 1 -> Registro A  |
| Ranura 2 -> Registro B  |
| Ranura 3 -> Registro D  |
| Ranura 4 -> Registro C  |
|-------------------------|
| Cuerpo de registros     |
| [Registro A]            |
| [Registro B]            |
| [Registro D]            |
| [Registro C]            |
+-------------------------+
```

- Eliminación de registro B:
  - Ranura 2 queda libre, espacio disponible para inserción futura.

```
+-------------------------+
| Cabecera de ranuras     |
|-------------------------|
| Ranura 1 -> Registro A  |
| Ranura 2 -> [libre]     |
| Ranura 3 -> Registro D  |
| Ranura 4 -> Registro C  |
|-------------------------|
| Cuerpo de registros     |
| [Registro A]            |
| [espacio disponible]    |
| [Registro D]            |
| [Registro C]            |
+-------------------------+
```

---

## 📌 **Conclusiones clave sobre Organización Física de Archivos:**
- Elegir estructura depende del patrón de uso (insertar vs consultar).
- Heap es rápido para insertar; secuencial ideal para consultas por rango.
- Hash destaca en igualdad exacta; Cluster ideal para datos relacionados frecuentes.
- Estructura de páginas por ranuras optimiza el almacenamiento y acceso físico.



## 3. Medidas Rendimiento Discos


# 💾 **Medidas de Rendimiento de Discos**

Al elegir discos magnéticos (HDD) para bases de datos, es esencial considerar ciertas medidas de rendimiento para garantizar eficiencia, rapidez y confiabilidad en el acceso a datos.

---

## 📏 **Principales Medidas de Rendimiento**

### **1. Tiempo de acceso (Seek Time)**
- Tiempo necesario para mover la cabeza lectora hacia la pista deseada.
- **Medición habitual:** milisegundos (ms).
- **Ejemplo típico:** 3-15 ms.

### **2. Latencia rotacional (Rotational Latency)**
- Tiempo que tarda en girar el disco hasta que el sector correcto queda bajo la cabeza.
- Depende directamente de la velocidad de rotación del disco (RPM).
- **Ejemplo:**  
  - 7200 RPM → 4,16 ms promedio  
  - 10.000 RPM → 3 ms promedio

### **3. Tasa de transferencia (Transfer Rate)**
- Cantidad de datos transferidos desde el disco hacia la memoria por unidad de tiempo.
- **Medición habitual:** MB/s o GB/s.
- **Ejemplo:**  
  - HDD típico: 100-200 MB/s  
  - SSD típico: 400-5000 MB/s

### **4. Tiempo medio entre fallos (Mean Time Between Failures - MTBF)**
- Tiempo promedio esperado antes de que el disco presente un fallo.
- **Medición habitual:** Horas (usualmente miles o millones de horas).
- **Ejemplo típico:** 1 millón de horas (114 años aprox.); aunque es un promedio teórico.

---

## 🎯 **Medida más determinante**

- En bases de datos, el **tiempo de acceso (seek time)** suele ser la medida más crítica.
- Esto se debe a que las bases de datos suelen realizar muchas operaciones aleatorias pequeñas en lugar de grandes transferencias secuenciales.

---

## 🛗 **Algoritmo del Ascensor (Elevator Algorithm)**

Es un algoritmo utilizado para optimizar el movimiento del cabezal en discos magnéticos, minimizando el tiempo de acceso total.

### 🔹 **Funcionamiento:**
- El cabezal se mueve en una dirección (por ejemplo, hacia afuera), atendiendo todas las solicitudes en esa dirección.
- Al alcanzar el extremo, cambia de dirección y atiende las solicitudes que quedaron pendientes hacia el otro lado.
- Simula el movimiento de un ascensor real en un edificio.

### 🔹 **Ventaja:**
- Reduce considerablemente el movimiento del cabezal, mejorando la eficiencia.

---

## 📈 **Métricas principales asociadas al rendimiento del disco:**

| Métrica             | Explicación breve                          |
|---------------------|--------------------------------------------|
| **Tiempo de acceso**| Tiempo de mover cabezal al lugar correcto. |
| **Latencia rotacional**| Tiempo en girar sector hasta el cabezal.|
| **Tasa transferencia** | Datos transferidos por unidad de tiempo. |
| **MTBF**            | Fiabilidad, vida útil antes de fallos.     |

---

## 📊 **Gráfico Ilustrativo del Algoritmo del Ascensor:**

**Ejemplo práctico**:

Solicitudes a pistas: `40, 70, 35, 80, 20`

Pista actual del cabezal: `50`, Dirección inicial: hacia arriba (números mayores)

```plaintext
Dirección inicial → hacia arriba
20 ----- 35 ----- [40] ----- [50] ----- [70] ----- [80]
                         ↑ inicio aquí

- Primero atiende: 70, 80
- Luego cambia dirección y atiende: 40, 35, 20
```

### Comparativa rápida:

| Sin algoritmo | Con algoritmo Ascensor |
|---------------|------------------------|
| 50→40→70→35→80→20 | 50→70→80→40→35→20 |
| Movimientos innecesarios grandes | Menos movimientos, optimización notable |

---

## 🧩 **Ejercicios Resueltos:**

### ✅ **1. Explicación detallada de medidas de rendimiento de discos magnéticos:**

| Medida             | Detalle y ejemplo típico |
|--------------------|--------------------------|
| **Tiempo de acceso** | Movimiento del cabezal (Ej: 8 ms promedio) |
| **Latencia rotacional**| Velocidad del giro hasta sector (Ej: 4 ms para 7200 RPM) |
| **Tasa transferencia** | Velocidad de datos (Ej: 150 MB/s) |
| **MTBF**            | Vida útil promedio (Ej: 1 millón horas) |

---

### ✅ **2. ¿Cuál sería la más determinante?**
- La más determinante: **Tiempo de acceso**.
- Es crítica para consultas pequeñas y aleatorias frecuentes, habituales en SGBD.

---

### ✅ **3. Algoritmo del Ascensor y sus principales métricas:**
- **Explicación breve:**  
  Atender solicitudes moviendo el cabezal en una dirección hasta terminar todas las solicitudes pendientes, luego cambiar de dirección.
  
- **Principales métricas asociadas:**  
  - Reducción del **tiempo promedio de acceso**.
  - Reducción del desgaste mecánico por menos movimientos.

---

## 📌 **Ejemplo numérico detallado del algoritmo del Ascensor:**

- Solicitudes: `[15, 10, 22, 4, 9, 30]`
- Posición inicial cabezal: `12`
- Dirección inicial: Hacia arriba (hacia números mayores).

Gráfico ilustrativo del proceso:

```
Inicial: 12
Dirección → arriba:
12 → 15 → 22 → 30  [ascendente finalizado]

Cambio de dirección ← abajo:
30 → 10 → 9 → 4    [descendente finalizado]

Orden óptimo final: [12 → 15 → 22 → 30 → 10 → 9 → 4]
```

---

## 🚦 **Conclusión clave del tema:**
- Las medidas más importantes son tiempo de acceso y latencia rotacional, cruciales para el rendimiento en bases de datos.
- El algoritmo del ascensor optimiza estos tiempos reduciendo movimientos innecesarios.



## 4. Niveles RAID


# 📀 **Introducción a RAID**

**RAID (Redundant Array of Independent Disks)** es una tecnología que combina múltiples discos físicos en una sola unidad lógica para aumentar la **velocidades de acceso a datos**, proveer **redundancia** (seguridad ante fallos) o una combinación de ambos.

---

## 📌 **Principales Niveles RAID (0, 1 y 5)**

### 1. 🔹 **RAID 0 (Stripe - Sin redundancia)**

- Divide datos en bloques distribuidos secuencialmente entre múltiples discos.
- **Ventajas:**  
  - Excelente rendimiento en velocidad de lectura/escritura.
  - Aprovecha al máximo la capacidad total (sin redundancia).

- **Desventaja:**  
  - Alta vulnerabilidad; la falla de un solo disco implica pérdida total de los datos.

- **Uso típico:**  
  Edición de video/audio, gaming, aplicaciones que requieren altas velocidades.

**Ejemplo gráfico RAID 0 (dos discos):**

```
Disco 1: Bloque 1 - Bloque 3 - Bloque 5
Disco 2: Bloque 2 - Bloque 4 - Bloque 6
```

---

### 2. 🔹 **RAID 1 (Mirroring - Redundancia exacta)**

- Duplica los datos exactamente en dos o más discos (espejo exacto).
- **Ventajas:**  
  - Muy seguro, resistente a fallos (puede fallar un disco sin pérdida de información).
  - Alta disponibilidad.

- **Desventaja:**  
  - Más caro, capacidad útil reducida a la mitad.
  - Velocidad de escritura ligeramente inferior debido a la duplicación.

- **Uso típico:**  
  Servidores de datos críticos, bases de datos pequeñas donde la fiabilidad es primordial.

**Ejemplo gráfico RAID 1 (dos discos espejo):**

```
Disco 1: Bloque A - Bloque B - Bloque C
Disco 2: Bloque A - Bloque B - Bloque C (Copia exacta)
```

---

### 3. 🔹 **RAID 5 (Paridad Distribuida - Equilibrio)**

- Distribuye los datos en múltiples discos, pero también guarda información de paridad (para recuperación de datos) de manera distribuida.
- **Ventajas:**  
  - Buen equilibrio rendimiento/seguridad.
  - Permite recuperación ante falla de un solo disco.
  - Uso eficiente del espacio (solo un disco de capacidad se utiliza para paridad).

- **Desventaja:**  
  - Reconstrucción lenta en caso de fallo.
  - Complejidad mayor.

- **Uso típico:**  
  Servidores empresariales y bases de datos de tamaño mediano/grande.

**Ejemplo gráfico RAID 5 (tres discos):**

```
Disco 1: Bloque 1 - Bloque 4 - Paridad (P3)
Disco 2: Bloque 2 - Paridad (P2) - Bloque 5
Disco 3: Paridad (P1) - Bloque 3 - Bloque 6
```

---

## 📌 **Razón Principal para la Implementación de RAID con Redundancia:**

La principal razón es **garantizar la disponibilidad y seguridad** de los datos ante fallos de discos físicos. RAID proporciona mecanismos automáticos de recuperación y tolerancia a fallos.

---

## 🚀 **Ventajas clave del almacenamiento RAID:**

### 🔹 **En rendimiento:**
- Lecturas simultáneas más rápidas (RAID 0, 5).
- Mejora en velocidad al distribuir carga en varios discos.

### 🔹 **En fiabilidad:**
- Seguridad de datos mediante redundancia (RAID 1 y RAID 5).
- Recuperación rápida en fallos parciales (RAID 1).
- Tolerancia efectiva a fallos sin interrupción (RAID 1, RAID 5).

---

## 📊 **Gráfico comparativo rápido de niveles RAID:**

| Característica | RAID 0             | RAID 1               | RAID 5             |
|----------------|--------------------|----------------------|--------------------|
| Rendimiento    | ✅ Muy alto        | ⚠️ Moderado-Alto     | ✅ Alto            |
| Redundancia    | ❌ No              | ✅ Completa (espejo) | ✅ Sí (paridad)    |
| Capacidad útil | ✅ 100% capacidad  | ❌ 50% capacidad     | ⚠️ ~80% capacidad  |
| Seguridad      | ❌ Ninguna         | ✅ Muy alta          | ✅ Alta            |
| Ejemplo uso    | Edición video      | Datos críticos       | Servidores grandes |

---

## 🧩 **Ejercicios resueltos en detalle:**

### ✅ **1. Explicación detallada niveles RAID 0, 1 y 5:**

- **RAID 0:** Divide datos en varios discos (sin redundancia).
- **RAID 1:** Duplicación exacta en discos múltiples (máxima seguridad).
- **RAID 5:** Distribuye paridad en discos, equilibrio rendimiento/seguridad.

---

### ✅ **2. Razón principal implementación redundancia:**

- Proteger información frente a fallos inevitables del hardware.
- Mantener alta disponibilidad del sistema.

---

### ✅ **3. Ventajas en rendimiento y fiabilidad detallada (RAID 1 y RAID 5):**

#### 🔸 **RAID 1:**
- **Fiabilidad:** Alta (espejo exacto).
- **Rendimiento:** Moderado en escritura (copia), alto en lectura (varios discos disponibles).

#### 🔸 **RAID 5:**
- **Fiabilidad:** Alta (permite recuperación automática).
- **Rendimiento:** Alto en lectura (datos distribuidos), escritura moderada por cálculo paridad.

---

## 🖥️ **Ejemplos prácticos detallados (RAID 1 y RAID 5):**

### RAID 1:
- Servidor bancario con datos financieros críticos.
- Disco A falla → Disco B mantiene copia exacta inmediata.

### RAID 5:
- Servidor web empresarial con bases de datos medianas.
- 4 discos de 1 TB → 3 TB datos útiles, 1 TB paridad distribuida.
- Un disco falla → sistema sigue funcionando; al reemplazar disco, sistema reconstruye datos desde paridad.

---

## 🎨 **Gráfico resumen niveles RAID:**

```
                Rendimiento ↑
Alta  | RAID 0
      |
      |                 RAID 5
      |                      • Equilibrio
Media |
      |            RAID 1
      |                      • Seguridad Máxima
Baja  +-----------------------------------→ Seguridad
     Baja             Media                Alta
```

---

## 📝 **Conclusión clave sobre niveles RAID:**

- **RAID 0**: Máximo rendimiento sin seguridad.
- **RAID 1**: Máxima seguridad con costo adicional.
- **RAID 5**: Balance entre rendimiento, capacidad y seguridad.

**Implementación recomendada según escenario:**
- **RAID 0:** Edición multimedia, aplicaciones rápidas sin datos críticos.
- **RAID 1:** Información confidencial, alta disponibilidad.
- **RAID 5:** Bases de datos medianas/grandes, equilibrio óptimo rendimiento y seguridad.



## 5. Arboles B Bplus


# 🌳 **Introducción a Árboles B y B+**

Los **árboles B y B+** son estructuras de datos **auto-balanceadas**, utilizadas para mantener grandes volúmenes de datos ordenados y permitir búsquedas rápidas, inserciones eficientes y eliminaciones ágiles en bases de datos y sistemas de archivos.

---

## 📖 **Características fundamentales**

**Árbol B:**
- Nodos almacenan claves y referencias directas a datos.
- Cada nodo tiene múltiples claves y múltiples punteros.
- Balanceado: garantiza la misma distancia a cualquier hoja desde la raíz.

**Árbol B+:**
- Variante del Árbol B, pero **almacena todos los datos únicamente en hojas**.
- Nodos internos almacenan únicamente claves para direccionar búsquedas.
- Las hojas se enlazan en una lista, facilitando consultas secuenciales muy rápidas.

---

## 🎯 **¿Por qué Árboles B y B+ son ideales para índices ordenados?**

### 1. 🔹 **Acceso rápido y eficiente:**
- Su altura se mantiene siempre baja (balanceada).
- Esto asegura búsquedas eficientes en grandes volúmenes de datos: típicamente `O(log n)`.

### 2. 🔹 **Operaciones optimizadas:**
- Inserciones, búsquedas y eliminaciones rápidas sin necesidad de reorganizar toda la estructura.
- Excelente desempeño incluso con millones de registros.

### 3. 🔹 **Rendimiento estable:**
- Acceso garantizado en pocas operaciones debido al balance constante.
- Ideal para bases de datos donde el rendimiento predecible es crítico.

### 4. 🔹 **Soporte eficiente para rangos:**
- En Árboles B+, las hojas enlazadas permiten consultas por rango (como fechas o números consecutivos) extremadamente rápidas.

---

## 📊 **Comparativa rápida Árbol B vs. Árbol B+:**

| Característica       | Árbol B                  | Árbol B+                      |
|----------------------|--------------------------|-------------------------------|
| Almacenamiento datos | Nodos internos y hojas   | Solo hojas                    |
| Uso ideal            | Índices generales        | Índices optimizados para rangos|
| Complejidad búsquedas| `O(log n)`               | `O(log n)`                    |
| Consultas rango      | Moderado                 | Excelente (hojas enlazadas)   |

---

## 🌲 **Ejemplo gráfico claro (Árbol B+):**

```plaintext
                   [30, 60]
                 /     |      \
          [10, 20]  [40, 50]  [70, 80, 90]
              ↘︎         ↘︎         ↘︎
            datos      datos       datos
```

- **Raíz:** Guía búsquedas rápidamente.
- **Hojas enlazadas:** Facilitan consultas secuenciales por rangos (10→20→40→50→70→80→90).

---

## 📚 **Ejemplo práctico concreto:**

- Supón que buscas `50`:
  - Paso 1: Empieza en raíz `[30, 60]`, 50 está entre 30 y 60, vas al nodo medio `[40, 50]`.
  - Paso 2: Encuentras `50` inmediatamente en este nodo hoja.

- Búsqueda eficiente: Solo dos accesos incluso en grandes cantidades de datos.

---

## ✅ **Razones detalladas para usar Árboles B y B+ en índices ordenados:**

| Razón principal | Explicación |
|-----------------|-------------|
| Altura Balanceada | Siempre mínima altura (`O(log n)`), rápido acceso. |
| Menos accesos a disco | Menos operaciones físicas, más eficiencia. |
| Inserción y eliminación ágil | Cambios locales mínimos, no reorganización global. |
| Óptimo para rangos | Árbol B+ especialmente ideal por hojas enlazadas. |

---

## 🎨 **Gráfico resumen ventajas Árbol B+ para índices ordenados:**

```plaintext
              Acceso a disco
Muchos  | Sin índice ordenado
        |
        | Árbol B
        |       • eficiente general
Pocos   | Árbol B+
        |       • excelente rango/orden
        +--------------------------------→ Velocidad consulta por rango
           Baja                 Alta
```

---

## 📝 **Conclusión clave sobre Árboles B y B+:**

- **Árbol B:** Indicado para índices generales equilibrados.
- **Árbol B+:** Más usado en bases de datos modernas por su eficiencia adicional en consultas por rangos, gracias a hojas enlazadas y almacenamiento exclusivo de datos en hojas.

La estructura balanceada, velocidad de acceso garantizada y facilidad para realizar consultas secuenciales hacen de los Árboles B y especialmente B+, la mejor elección para implementar índices ordenados en bases de datos modernas.



## 6. Algoritmos Busqueda


# 🔎 **Introducción a Algoritmos de Búsqueda**

Los algoritmos de búsqueda determinan cómo se accede a los datos almacenados, siendo esenciales para el rendimiento de un Sistema Gestor de Bases de Datos (SGBD).

---

## ⌛ **Costos Asintóticos en Algoritmos**

La notación asintótica describe cómo se comporta un algoritmo a medida que crece el volumen de datos (`n`).

- **O(1)**: Tiempo constante (independiente del tamaño).
- **O(log n)**: Logarítmico (muy eficiente, aumenta lentamente).
- **O(n)**: Lineal (tiempo crece proporcionalmente al tamaño).

---

# 📚 **Análisis de los Algoritmos Solicitados**

## 📍 **(1) Programación Dinámica: (Evaluación de árboles)**

### 🔸 (a) Sin optimización (evaluación de árboles completos):

- **Tiempo:** Exponencial `O(2^n)` en árboles binarios.
- **Espacio:** `O(n)` por pila de llamadas recursivas.

**Razón:**  
Evalúa múltiples veces las mismas subexpresiones, resultando en redundancia y mucho tiempo de cómputo.

### 🔸 (b) Con optimización (Memoización - Programación Dinámica):

- **Tiempo:** Polinómico `O(n^2)` o mejor, dependiendo del problema.
- **Espacio:** `O(n^2)` por almacenamiento en tablas (generalmente matrices).

**Razón:**  
Almacenamiento intermedio evita cálculos repetidos (memoización), reduciendo enormemente el tiempo a cambio de memoria adicional.

---

## 📍 **(2) Algoritmos de Selección en SGBD (Condición Igualdad):**

### 🔸 **(a) Búsqueda Lineal:**

- **Uso:** Tabla sin orden ni índice.
- **Costo:** `O(n)`
- Ejemplo:  
  Buscar cliente por nombre en tabla pequeña sin índice.

---

### 🔸 **(b) Búsqueda Binaria:**

- **Uso:** Tabla ordenada físicamente sin índice.
- **Costo:** `O(log n)`
- Ejemplo:  
  Buscar fecha específica en historial de eventos ordenados.

---

### 🔸 **(c) Índice Primario (clave):**

- **Uso:** Índice sobre atributo clave primaria con estructura tipo hash.
- **Costo:** `O(1)` idealmente (acceso directo hash) o `O(log n)` si es árbol B+.
- Ejemplo:  
  Buscar usuario por ID único usando índice hash.

> Nota: El coste típico realista en índices primarios en bases de datos es generalmente **O(log n)** (árboles B+), aunque un índice hash idealizado sería **O(1)**.

---

### 🔸 **(d) Índice Secundario (no clave):**

- **Uso:** Índice sobre atributo no clave.
- **Costo:** Generalmente `O(log n)`.
- Ejemplo:  
  Buscar clientes por ciudad usando un índice secundario.

---

# 📉 **Gráfico comparativo claro:**

```plaintext
Eficiencia de búsquedas según estructura:

Alto coste (lento)   Lineal → O(n)
                          |
                          |
                          ↓
                    Binaria → O(log n)
                          |
                          ↓
                    Índice secundario → O(log n)
                          |
                          ↓
Bajo coste (rápido) Índice primario → O(1)/O(log n)
```

---

# 🔍 **Tema 7: Ejemplos hipotéticos (cuatro casos con diferentes costes):**

### 📌 **Caso 1: Tabla pequeña, sin índice**

```sql
SELECT * FROM Clientes WHERE Nombre = 'Laura';
```
- **Algoritmo:** Lineal.
- **Costo:** `O(n)`.

---

### 📌 **Caso 2: Tabla ordenada físicamente por fecha**

```sql
SELECT * FROM Pedidos WHERE Fecha = '2024-03-24';
```
- **Algoritmo:** Búsqueda Binaria.
- **Costo:** `O(log n)`.

---

### 📌 **Caso 3: Tabla con índice primario (hash) por ID**

```sql
SELECT * FROM Usuarios WHERE ID = 12345;
```
- **Algoritmo:** Índice primario (hash o árbol B+).
- **Costo:** `O(1)` (ideal hash), en la práctica `O(log n)` (árbol B+).

---

### 📌 **Caso 4: Tabla con índice secundario (árbol B+)**

```sql
SELECT * FROM Productos WHERE Categoría = 'Electrónica';
```
- **Algoritmo:** Índice secundario (árbol B+).
- **Costo:** `O(log n)` en índice, aunque luego recupera múltiples registros relacionados (coste adicional).

---

# ✅ **Resumen gráfico práctico de casos hipotéticos:**

| Caso | Estructura tabla                 | Índice         | Algoritmo usado | Costo teórico |
|------|----------------------------------|----------------|-----------------|---------------|
| 1    | Pequeña, no ordenada             | Ninguno        | Lineal          | `O(n)`        |
| 2    | Orden físico (fecha)             | Ninguno        | Binaria         | `O(log n)`    |
| 3    | Clave primaria con índice        | Primario (hash)| Índice primario | `O(1)` ideal  |
| 4    | Índice secundario por atributo   | Secundario B+  | Índice secundario| `O(log n)`   |

---

## 📌 **Conclusiones clave del tema Algoritmos de Búsqueda:**

- La elección del algoritmo depende de la estructura física y lógica del almacenamiento (tabla ordenada, existencia de índice).
- Búsquedas lineales son lentas, pero simples; índices primarios son extremadamente rápidos.
- Índices secundarios permiten búsquedas rápidas, aunque recuperan múltiples registros potencialmente.

---

## 🎯 **Consejos prácticos finales para mejorar rendimiento:**

- **Usar índices** siempre que las consultas sean frecuentes y relevantes.
- **Considerar el balance costo-beneficio** al agregar índices secundarios (ralentizan inserciones y actualizaciones, pero aceleran consultas).
- **Evaluar necesidades reales** para decidir usar hashing vs. árboles B+ (hash muy rápido para igualdad exacta, B+ para rangos o múltiples registros).



## 7. Procesamiento Consultas



# 🗃️ **Procesamiento de Consultas en SGBD**

El procesamiento de consultas se refiere a cómo un Sistema Gestor de Bases de Datos interpreta, optimiza y ejecuta las consultas SQL recibidas por parte del usuario, transformándolas en resultados concretos.

---

## 📌 **Pasos Lógicos del Procesamiento de Consultas**

El procesamiento de consultas tiene tres fases clave:

### 1️⃣ **Análisis**
- Verifica la sintaxis y la semántica.
- Traduce la consulta a una forma intermedia (álgebra relacional).

### 2️⃣ **Optimización**
- Selecciona el mejor plan de ejecución.
- Evalúa diferentes alternativas considerando índices, estadísticas, costo de acceso a disco, y tiempos estimados.

### 3️⃣ **Evaluación**
- Ejecuta el plan optimizado.
- Recupera datos usando estrategias como **materialización** (guardar resultados intermedios) o **pipelining** (transferencia directa de resultados).

---

## 📐 **Diagrama del Procesamiento de Consultas (completo y explicado)**

```
                  Consulta SQL
                       │
                       ▼
             ┌───────────────────┐
             │   Análisis        │
             │ (Sintaxis y       │
             │  Traducción a     │
             │  álgebra rel.)    │
             └─────────┬─────────┘
                       │
                       ▼
             ┌───────────────────┐
             │   Optimización    │
             │  (Genera y elige  │
             │   mejor plan)     │
             └─────────┬─────────┘
                       │
                       ▼
             ┌───────────────────┐
             │    Evaluación     │
             │(Ejecuta el plan   │
             │optimizado y       │
             │obtiene resultados)│
             └─────────┬─────────┘
                       │
                       ▼
                 Resultado final
```

---

## 📚 **Traducción a Álgebra Relacional (Tema 4)**

### 🔹 **Consulta original:**

```sql
SELECT e.LNAME 
FROM EMPLEADO e 
JOIN TRABAJA_EN te ON te.EMPLEADO = e.ID 
JOIN PROYECTO p ON p.ID = te.PROYECTO 
WHERE p.NOMBRE = 'AQUARIUS' AND e.FECHA_NAC >= '2000-01-01'
```

### 🔹 **Traducción inicial (sin optimizar):**

```
π_LNAME (
    σ_(NOMBRE='AQUARIUS' ∧ FECHA_NAC ≥ '2000-01-01') (
        EMPLEADO ⨝_(EMPLEADO.ID=TRABAJA_EN.EMPLEADO) TRABAJA_EN 
        ⨝_(TRABAJA_EN.PROYECTO=PROYECTO.ID) PROYECTO
    )
)
```

---

### 🔹 **Optimización de la consulta (2 casos)**

**Caso 1: Empujar selecciones (optimización clásica):**

```
π_LNAME (
    (σ_FECHA_NAC ≥ '2000-01-01'(EMPLEADO)) 
    ⨝ TRABAJA_EN 
    ⨝ (σ_NOMBRE='AQUARIUS'(PROYECTO))
)
```

- Reduce datos antes de realizar JOIN → Mejora rendimiento notablemente.

**Caso 2: Cambiar orden de JOIN (optimización según tamaño tablas):**

```
π_LNAME (
    (σ_NOMBRE='AQUARIUS'(PROYECTO) ⨝ TRABAJA_EN) 
    ⨝ σ_FECHA_NAC ≥ '2000-01-01'(EMPLEADO)
)
```

- Empieza desde la tabla más pequeña (PROYECTO con filtro) para minimizar coste.

---

## 🔗 **Evaluación consulta JOIN con Bucle Anidado por Bloques (Tema 8)**

### 🔹 **Contexto del ejemplo práctico:**

- Consulta JOIN: `SELECT * FROM A JOIN B ON A.a = B.b`
- Tabla A: 20 bloques, Tabla B: 15 bloques, 10 bloques libres en memoria.

### 🔹 **Algoritmo Bucle Anidado por Bloques (Block Nested Loop Join)**:

**Fórmula del coste (I/O):**
```
Coste = Bloques_A + (Bloques_A / (Bloques_memoria - 2)) * Bloques_B
```

- *(Bloques_memoria - 2)* porque uno se reserva para salida y otro para bloque actual.

### 🔹 **Cálculo detallado del coste:**

```
Bloques_A = 20, Bloques_B = 15, Bloques_memoria = 10

Coste = 20 + (20 / (10 - 2)) * 15
      = 20 + (20 / 8) * 15
      = 20 + 2.5 * 15
      = 20 + 37.5
      = 57.5 ≈ 58 bloques de coste total
```

---

### 🔹 **LRU vs. MRU (estrategia de reemplazo de bloques)**:

- **LRU (Least Recently Used):**
  - Descarta el bloque menos recientemente utilizado.
  - Generalmente eficiente (más aciertos en caché).

- **MRU (Most Recently Used):**
  - Descarta el bloque más recientemente utilizado.
  - Útil si acceso repetitivo no frecuente; en este caso, generalmente menos eficiente.

---

## 📉 **Gráfico resumen claro sobre Procesamiento de Consultas:**

```
Consulta SQL ──► Análisis ──► Optimización ──► Evaluación ──► Resultados

(Análisis)        (Optimización)                 (Evaluación)
───────────      ────────────────              ────────────────
• Sintaxis       • Elegir mejor plan           • Materialización
• Semántica      • Orden JOINs                 • Pipelining
• Álgebra        • Índices disponibles         • Acceso a disco
```

---

## 📌 **Ejemplo hipotético visual claro:**

- Consulta: 
```sql
SELECT Nombre FROM Estudiantes WHERE Edad >= 20
```

**Fases:**
- Análisis: Sintaxis OK → Álgebra: σ_Edad≥20(Estudiantes)
- Optimización: Índice sobre Edad disponible → usa índice.
- Evaluación: Recupera rápidamente datos por índice → entrega resultados.

---

## ✅ **Conclusión clave sobre Procesamiento de Consultas:**

- **Análisis:** Traducción precisa y sintaxis correcta son clave.
- **Optimización:** Crucial para eficiencia, especialmente en JOINs complejos.
- **Evaluación:** Depende de estrategias eficientes (materialización vs pipelining).

Una buena optimización puede cambiar radicalmente el rendimiento de consultas, especialmente en grandes bases de datos.



## 8. Modelado Multidimensional


# 📊 **Introducción al Modelado Multidimensional**

El **Modelado Multidimensional** es una técnica usada en sistemas de análisis de datos (OLAP) para representar grandes volúmenes de información desde diferentes perspectivas (dimensiones), facilitando análisis efectivos y toma de decisiones.

---

## 📌 **Conceptos Clave:**

### 🔹 **Tablas de Dimensiones:**
- Representan **características o atributos** de los datos.
- Permiten "cortar" y filtrar los datos desde diferentes ángulos.

**Ejemplos:**
- **Clientes:** Nombre, ciudad, país.
- **Productos:** Categoría, marca, modelo.
- **Tiempo:** Día, mes, año.

---

### 🔹 **Tablas de Hechos:**
- Contienen los **datos medibles**, generalmente numéricos.
- Vinculan las dimensiones con métricas específicas.

**Ejemplos:**
- **Ventas:** Cantidad vendida, ingresos generados.
- **Compras:** Total de compras, costos asociados.

---

### 🔹 **Medidas:**
- Son los valores numéricos específicos dentro de tablas de hechos.
- Indican lo que realmente se está analizando.

**Ejemplos:**
- Cantidad de productos vendidos.
- Ventas totales en dólares.
- Cantidad de clientes nuevos por día.

---

## 📐 **Ejemplo Gráfico de un Esquema Estrella:**

```
           DIMENSIÓN CLIENTES
                   │
                   │
DIMENSIÓN TIEMPO───★────DIMENSIÓN PRODUCTOS
                   │
                   │
           TABLA DE HECHOS (VENTAS)
                   │
            (Medidas: Ventas, ingresos)
```

---

# 🔍 **Diferencias entre OLTP y OLAP**

### 🔹 **OLTP (Online Transaction Processing):**
- Maneja **transacciones frecuentes** y operacionales.
- Transacciones rápidas, pequeñas y concurrentes.
- Ejemplos claros:  
  - Ventas en línea (Amazon).  
  - Sistemas bancarios (transferencias).

### 🔹 **OLAP (Online Analytical Processing):**
- Orientado al **análisis y toma de decisiones**.
- Consultas complejas sobre grandes volúmenes de datos.
- Ejemplos claros:  
  - Análisis de ventas por región.  
  - Reportes financieros y planificación estratégica.

---

### 📈 **Comparativa rápida OLTP vs. OLAP:**

| Aspecto           | OLTP                             | OLAP                            |
|-------------------|----------------------------------|---------------------------------|
| Uso               | Operaciones frecuentes           | Análisis y decisiones           |
| Transacciones     | Muchas, rápidas, pequeñas        | Menos frecuentes, muy grandes   |
| Consultas         | Simples, precisas                | Complejas, agregadas            |
| Diseño Modelo     | Normalizado                      | Multidimensional, desnormalizado|
| Ejemplo real      | Pagos online                     | Business Intelligence (BI)      |

---

## 🎲 **Esquema Estrella vs. Cubos OLAP**

### 🔹 **Esquema Estrella:**
- Es un modelo de diseño físico para **bases de datos relacionales** que facilita consultas rápidas.
- Consiste en una tabla central de hechos y múltiples tablas de dimensiones alrededor.
- Sencillo, eficiente en rendimiento de consultas rápidas.

### 🔹 **Cubos OLAP:**
- Representación lógica **multidimensional**.
- Permite análisis interactivo ("slice & dice"), "drill-down" (detalle) y "roll-up" (agregado).
- No necesariamente físico, generalmente lógico o conceptual.

---

### 📌 **Consideraciones principales:**

| Aspecto        | Esquema Estrella                  | Cubos OLAP                          |
|----------------|-----------------------------------|-------------------------------------|
| Naturaleza     | Física (tablas reales)            | Lógica o conceptual (visualización) |
| Almacenamiento | Bases de datos relacionales       | Sistemas OLAP                       |
| Uso            | Consultas rápidas SQL             | Análisis interactivos, dinámicos    |
| Complejidad    | Baja                              | Alta (permite interacción dinámica) |

---

## 🎯 **Ejemplos prácticos del Modelo Multidimensional**

### 🔹 **Tabla de Dimensión (Clientes):**
| ID_Cliente | Nombre    | Ciudad    | País      |
|------------|-----------|-----------|-----------|
| 001        | Juan      | Madrid    | España    |
| 002        | Laura     | Asunción  | Paraguay  |

### 🔹 **Tabla de Dimensión (Productos):**
| ID_Producto | Nombre       | Categoría   |
|-------------|--------------|-------------|
| P001        | iPhone 15    | Smartphones |
| P002        | Lenovo Yoga  | Laptop      |

### 🔹 **Tabla de Hechos (Ventas):**
| ID_Cliente | ID_Producto | Fecha      | Cantidad | Ingresos |
|------------|-------------|------------|----------|----------|
| 001        | P001        | 2024-03-23 | 2        | $2000    |
| 002        | P002        | 2024-03-24 | 1        | $1200    |

---

## 📉 **Gráfico resumen OLTP vs. OLAP:**

```
                Transacciones
Muchas │ OLTP
       │   • sistemas operativos
       │   • bancos, ventas online
       │
       │
Pocas  │            OLAP
       │               • análisis profundo
       │               • BI, planificación
       └─────────────────────────► Complejidad Consultas
        Baja                 Alta
```

---

## 🧩 **Ejercicios resueltos claramente:**

### ✅ **(1) Tablas de Dimensiones, Hechos y Medidas:**
- **Dimensiones:** Atributos analíticos (Clientes, Productos, Tiempo).
- **Hechos:** Datos medibles (Ventas, ingresos).
- **Medidas:** Valores numéricos específicos (Cantidad vendida, dinero generado).

---

### ✅ **(2) Diferencia entre OLTP y OLAP (términos propios con ejemplos):**
- **OLTP:** Rápido, pequeñas operaciones frecuentes (Ej: Amazon, pagos).
- **OLAP:** Análisis, grandes operaciones complejas (Ej: Data Warehouse financiero).

---

### ✅ **(3) Diferencia entre esquema estrella y cubos OLAP:**
- **Esquema estrella:** Físico, rápido para consultas específicas SQL.
- **Cubos OLAP:** Lógico, dinámico para análisis interactivo y multidimensional.

---

## 🔑 **Conclusiones claves sobre Modelado Multidimensional:**
- Esencial para **Business Intelligence** (BI).
- Tablas de dimensión dan contexto; hechos proporcionan mediciones numéricas.
- OLTP es operativo y rápido; OLAP analítico y profundo.
- Esquema estrella facilita rapidez física; cubos OLAP permiten análisis interactivo lógico.



## 9. Transacciones ACID


# 🔐 **Introducción a Transacciones (SGBD)**

Una **transacción** en un Sistema Gestor de Bases de Datos (SGBD) es una unidad lógica que agrupa operaciones que se ejecutan de manera indivisible, asegurando que todas las operaciones dentro se completen correctamente o ninguna lo haga, garantizando la consistencia del sistema.

**Ejemplo sencillo:**  
Transferir dinero de la cuenta A a la cuenta B es una sola transacción que incluye:

1. Restar dinero en cuenta A
2. Sumar dinero en cuenta B

Ambas deben completarse exitosamente o ninguna debe ejecutarse.

---

## 🔄 **Fases del Ciclo de Vida de una Transacción**

Una transacción atraviesa claramente 5 fases:

### 1️⃣ **Inicio (Begin)**
- La transacción comienza formalmente.

### 2️⃣ **Ejecución (Execution)**
- Realiza las operaciones (INSERT, UPDATE, DELETE, SELECT).

### 3️⃣ **Validación (Validation)**
- Verifica si las operaciones pueden completarse (restricciones, bloqueos).

### 4️⃣ **Confirmación (Commit)**
- Guarda permanentemente cambios realizados en la base de datos.

### 5️⃣ **Cancelación (Rollback, si aplica)**
- Si algo falla, revierte todas las operaciones realizadas hasta el momento del fallo, volviendo al estado inicial.

---

## 📌 **Propiedades ACID**

Estas propiedades garantizan la confiabilidad en un entorno transaccional:

| Propiedad    | Definición breve |
|--------------|------------------|
| **Atomicidad**    | Todo o nada. La transacción ocurre completamente o no ocurre. |
| **Consistencia**  | La base de datos pasa de un estado válido a otro estado válido. |
| **Aislamiento**   | Cada transacción se ejecuta independientemente sin interferir con otras transacciones simultáneas. |
| **Durabilidad**   | Cambios confirmados permanecen permanentes aun ante fallos del sistema.|

---

## 📚 **Explicación detallada Propiedades ACID (estándar SQL)**

### 🔹 **Atomicidad (Atomicity):**
- Operaciones dentro de la transacción son indivisibles.
- **Ejemplo:**  
  Si falla un paso de la transferencia bancaria, ambas cuentas permanecen intactas.

### 🔹 **Consistencia (Consistency):**
- La base de datos siempre permanece en un estado válido antes y después de la transacción.
- **Ejemplo:**  
  No permitir saldo negativo tras transferencia bancaria.

### 🔹 **Aislamiento (Isolation):**
- Transacciones concurrentes no interfieren entre sí.
- **Ejemplo:**  
  Dos transferencias simultáneas no causan inconsistencias en los saldos.

### 🔹 **Durabilidad (Durability):**
- Los cambios realizados son permanentes una vez confirmados (commit).
- **Ejemplo:**  
  Tras una transferencia exitosa, el saldo se mantiene actualizado incluso si ocurre un corte de energía.

---

## 📈 **Gráfico claro del Ciclo de Vida de una Transacción:**

```
           Transacción iniciada
                  │
                  ▼
           ┌─────────────┐
           │  Ejecución  │─────────┐
           └─────────────┘         │
                  │                │
                  ▼                ▼
           ┌─────────────┐   ┌─────────────┐
           │ Validación  │───│ Cancelación │ (Rollback)
           └─────────────┘   └─────────────┘
                  │
                  ▼
           ┌─────────────┐
           │Confirmación │ (Commit)
           └─────────────┘
                  │
                  ▼
             Cambios permanentes
```

---

## 🧩 **Ejercicios Resueltos en detalle:**

### ✅ **(a) Definición concreta de transacción:**

- Es un conjunto lógico indivisible de operaciones en bases de datos.
- Todas se ejecutan exitosamente o todas fallan, asegurando integridad.

---

### ✅ **(b) Ciclo de vida detallado:**

- **Inicio:** Comienzo formal.
- **Ejecución:** Realización de operaciones.
- **Validación:** Chequeo restricciones y bloqueos.
- **Commit:** Confirmación final.
- **Rollback:** Anulación de operaciones si algo falla.

---

### ✅ **(c) Propiedades ACID definidas claramente:**

- **Atomicidad:** Todo o nada.
- **Consistencia:** Estado válido siempre.
- **Aislamiento:** Independencia entre transacciones simultáneas.
- **Durabilidad:** Permanencia de los cambios tras confirmación.

---

## 🔑 **Ejemplo práctico completo con propiedades ACID:**

### 🔹 **Caso práctico: Transferencia Bancaria (Transacción T)**

- Estado inicial:
  - Cuenta A: 500 USD
  - Cuenta B: 300 USD

- Operaciones de la transacción:
  1. Cuenta A → -100 USD  
  2. Cuenta B → +100 USD  

- Estado final (esperado si Commit):
  - Cuenta A: 400 USD
  - Cuenta B: 400 USD

### 🔹 **Validación de propiedades ACID:**

| Propiedad     | Explicación en ejemplo bancario |
|---------------|---------------------------------|
| Atomicidad    | Ambas cuentas cambian juntas o ninguna cambia.|
| Consistencia  | Saldos siempre coherentes, no negativos.|
| Aislamiento   | Otra transacción simultánea no afecta esta operación.|
| Durabilidad   | Una vez completada, transferencias permanecen aún con fallos del sistema.|

---

## 📉 **Gráfico resumen propiedades ACID:**

```
         Estado inicial válido
                  │
Atomicidad        │ Transacción ──── (Si falla) ───► Estado inicial
                  ▼
Consistencia ── Estado válido intermedio
                  │
Aislamiento       │ (Sin interferencia externa)
                  ▼
Durabilidad ── Estado final válido y permanente tras commit
```

---

## 🎯 **Conclusión clave del tema Transacciones y ACID:**

- Las **transacciones** garantizan integridad y coherencia.
- Las propiedades **ACID** (Atomicidad, Consistencia, Aislamiento y Durabilidad) son esenciales para mantener la fiabilidad del sistema.
- Sin estas propiedades, los datos serían vulnerables a inconsistencia y corrupción.

Una implementación adecuada del modelo ACID es crítica para aplicaciones empresariales, bancarias y cualquier sistema que maneje datos sensibles.



## 10. Concurrencia


# 🔄 **Introducción a la Concurrencia**

La **concurrencia** en bases de datos permite que múltiples usuarios o aplicaciones interactúen simultáneamente con la base de datos, lo que genera eficiencia pero puede producir conflictos si no se gestiona correctamente.

---

## 📌 **(a) Función del Componente de Gestión de Concurrencia en un SGBD**

El **Gestor de Concurrencia** asegura que las transacciones simultáneas no interfieran negativamente entre sí, manteniendo la integridad y consistencia de los datos.  

**Funciones principales:**
- Controlar accesos simultáneos.
- Evitar conflictos en escrituras/lecturas simultáneas.
- Asegurar aislamiento entre transacciones.

---

## 📐 **(b) Estructura de Datos para Gestión y Concesión de Bloqueos**

El sistema utiliza una estructura llamada **Tabla de Bloqueos**:

| Recurso (Dato) | Estado Bloqueo | Transacción(es) que bloquean | Cola de Espera |
|----------------|----------------|-------------------------------|----------------|
| Registro A     | Exclusivo (X)  | T1                            | T2, T3         |
| Registro B     | Compartido (S) | T2, T4                        | T5             |

- **Bloqueo Exclusivo (X):** Para escrituras (una sola transacción).
- **Bloqueo Compartido (S):** Para lecturas simultáneas (múltiples transacciones).

---

## 🔒 **(a) Protocolo de Bloqueo de 2 Fases (2PL - Two Phase Locking)**

Garantiza la **serializabilidad**, asegurando una ejecución concurrente equivalente a una secuencial.

### 🔹 **Fases del Protocolo 2PL:**
- **Fase 1 (Creciente):** Adquiere bloqueos necesarios; no libera ninguno.
- **Fase 2 (Decreciente):** Libera bloqueos; no adquiere nuevos bloqueos.

**Ejemplo gráfico:**
```
Tiempo ►
T1: │─── Adquiere Bloqueos ───│── Libera Bloqueos ──│
    ▲                        ▲
Fase creciente          Fase decreciente
```

---

## 📑 **(b) Variantes del Protocolo 2PL**

- **2PL Básico:** Adquiere y libera bloqueos en dos fases estrictas.
- **2PL Estricto (Strict 2PL):** Libera bloqueos exclusivos (X) únicamente al terminar (Commit/Rollback).
- **2PL Riguroso (Rigorous 2PL):** Libera todos los bloqueos (S/X) sólo al finalizar (más restrictivo, más seguro).

---

## 📖 **Tema 5: Conceptos de Control de Concurrencia**

### 🔹 **Planificación (Schedule):**
- Orden específico en que operaciones de múltiples transacciones se ejecutan simultáneamente.

**Ejemplo:**
```
T1: Leer(A), Escribir(A)
T2: Leer(A), Escribir(A)
```

Una planificación posible:
```
Leer(A)T1 → Leer(A)T2 → Escribir(A)T1 → Escribir(A)T2
```

---

### 🔹 **Planificación Secuencial (Serial Schedule):**
- Las transacciones se ejecutan estrictamente una tras otra, sin simultaneidad.

**Ejemplo:**
```
(T1 completa) → (T2 completa) → (T3 completa)
```

---

### 🔹 **Planificación Secuenciable (Serializable Schedule):**
- Ejecución concurrente equivalente lógicamente a alguna planificación secuencial.

**Ejemplo:**
```
Leer(A)T1 → Escribir(A)T1 → Leer(B)T2 → Escribir(B)T2
```

Aunque hay concurrencia, la planificación es equivalente a T1→T2 o T2→T1.

---

### 🔹 **Secuencialidad en Cuanto a Conflicto (Conflict Serializability):**
- Las operaciones conflictivas (lectura/escritura sobre el mismo recurso) siguen un orden estricto como en una planificación secuencial.

---

### 🔹 **Secuencialidad en Cuanto a Vistas (View Serializability):**
- Equivalencia lógica en términos de valores leídos y escritos, aunque el orden de operaciones pueda diferir levemente.

---

## 📈 **Importancia de la Secuencialidad (Serializabilidad)**

La serializabilidad es crítica porque asegura la **consistencia y corrección** de la base de datos en ambientes concurrentes. Si las planificaciones no son serializables, pueden generarse inconsistencias en los datos.

---

## 🧩 **Ejercicios resueltos concretamente:**

### ✅ **(a) Función de Gestión Concurrencia en SGBD:**
- Garantiza que múltiples usuarios trabajen simultáneamente sin conflictos.

---

### ✅ **(b) Estructura de datos para bloqueos:**
- **Tabla de bloqueos:** Registra recursos, bloqueos actuales y solicitudes en espera.

---

### ✅ **(a) Protocolo de 2 fases (2PL):**
- Dos fases claramente separadas: adquisición (creciente) y liberación (decreciente).

---

### ✅ **(b) Variantes protocolo 2PL:**
- **2PL básico, Estricto (strict) y Riguroso (rigorous)**.

---

### ✅ **Explicación conceptos control concurrencia claramente:**

| Concepto                  | Explicación simple                       |
|---------------------------|------------------------------------------|
| Planificación             | Orden ejecución operaciones.             |
| Planificación secuencial  | Transacciones una tras otra (sin concurrencia). |
| Planificación secuenciable| Concurrencia, pero equivalente a secuencial.|
| Secuencialidad conflicto  | Operaciones conflictivas ordenadas estrictamente.|
| Secuencialidad vistas     | Equivalencia lógica en resultados obtenidos.|

---

## 📌 **Gráfico claro resumen conceptos concurrencia:**

```
Planificación
     │
     ├── Secuencial ──── Una tras otra (segura, sin conflictos)
     │
     └── Secuenciable ── Concurrente, pero equivalente a secuencial
                  │
                  ├── Conflicto ── Operaciones conflictivas respetan orden
                  │
                  └── Vistas ───── Equivalente en resultados leídos/escritos
```

---

## 📚 **Ejemplo gráfico concreto protocolo 2PL:**

- **Transacción bancaria T1 (transferencia dinero)**:
  1. Bloquea cuenta A (X)
  2. Bloquea cuenta B (X)
  3. Actualiza saldos
  4. Libera bloqueos (X)

- **Protocolo estricto (Strict 2PL)**:
  - Libera bloqueos solo al terminar la transacción completamente (commit).

```
Tiempo ►
T1 │─ Bloquear A ─ Bloquear B ── Actualizar ── Commit & Liberar ─│
```

---

## 🎯 **Conclusión clave sobre Concurrencia en SGBD:**

- Controlar concurrencia es vital para asegurar integridad.
- El protocolo 2PL asegura serializabilidad (orden lógico seguro).
- La planificación secuenciable garantiza que concurrencia sea tan segura como la ejecución secuencial estricta.

Un buen control de concurrencia evita pérdida de datos, conflictos y mantiene la coherencia en bases de datos críticas.



## 11. Protocolos Distribuidos


# 🌐 **Introducción a Protocolos Distribuidos en SGBD**

Los **protocolos distribuidos** gestionan la **coordinación y concurrencia** en sistemas donde los datos están repartidos en múltiples sitios geográficamente distribuidos. Aseguran consistencia y disponibilidad.

---

# 🗳️ **(a) Protocolo de Control de Concurrencia por Quorum de Consenso**

Este protocolo garantiza coherencia distribuida usando **pesos** asignados a cada sitio.

### 🔹 **Conceptos básicos:**
- Cada sitio recibe un peso asignado.
- Para realizar **lectura o escritura**, la transacción debe sumar un **quorum mínimo** de pesos.
- Generalmente, se asignan pesos según la importancia o disponibilidad de sitios.

---

## 📌 **(b) Implicancias para definir valores de Quorum:**

- **Mayor quorum de lectura:**  
  Mayor consistencia, menor velocidad.
- **Mayor quorum de escritura:**  
  Mayor costo, mayor seguridad en escrituras.
- La suma de quorum de lectura (Q_L) y quorum de escritura (Q_E) debe ser mayor al total de pesos asignados para asegurar consistencia:
  
  ```
  Q_L + Q_E > Peso_Total
  ```

---

## 📚 **(c) Valores para protocolos específicos:**

### 🔹 **Protocolo de Mayoría (Majority Protocol):**
- **Condición:** Quorum lectura + Quorum escritura > total de pesos.
- **Ejemplo claro:** Si total = 10,  
  - Lectura ≥ 6 y Escritura ≥ 5 (o viceversa).  
  (Ej.: Q_L=6, Q_E=5; 6+5=11>10).

### 🔹 **Protocolo Sesgado (Biased Protocol):**
- Un sitio especial tiene peso dominante (sesgado).
- **Ejemplo claro:** Si total = 10  
  - Sitio principal tiene peso=7; demás sitios peso=1.  
  - Quorum lectura y escritura puede satisfacerse con sitio sesgado solo (Ej.: Q_L=7, Q_E=7).

---

# ✅ **(a) Protocolo de Commit en 2 Fases (2PC - Two Phase Commit)**

Permite coordinar confirmación de transacciones distribuidas asegurando consistencia.

### 🔹 **Fases del protocolo 2PC:**

- **Fase 1 (Preparación):**
  1. **Coordinador** envía `PREPARE` a todos los participantes.
  2. **Participantes** ejecutan operaciones localmente y responden:
     - `READY` (preparado) o
     - `ABORT` (cancelar).

- **Fase 2 (Confirmación):**
  - Si TODOS los participantes respondieron `READY`, coordinador envía `COMMIT` para confirmar cambios.
  - Si UNO responde `ABORT`, envía `ABORT` a todos para revertir cambios.

---

## 📌 **Ejemplo gráfico Protocolo 2PC:**

```
         Coordinador
             │
Fase 1:      │ PREPARE?
             │──────────► Participante 1
             │──────────► Participante 2
             │──────────► Participante 3
             │
             │ READY ◄─── Participante 1
             │ READY ◄─── Participante 2
             │ READY ◄─── Participante 3
             │
Fase 2:      │ COMMIT
             │──────────► Participantes (Confirmación)
```

---

# 🚧 **(b) Qué pasa si falla el Coordinador en 2PC?**

- Los participantes quedan "bloqueados" temporalmente sin instrucciones claras (estado incertidumbre).
- Deben esperar recuperación del coordinador o usar técnicas alternativas (backup, tiempo de espera, etc.).

---

# 🚨 **(c) Qué pasa si un Participante falla en 2PC?**

- Si falla en fase preparación: Coordinador envía `ABORT` al resto.
- Si falla después de `READY` (en confirmación): 
  - Al recuperarse, debe consultar al coordinador para saber si debe COMMIT o ABORT (consulta estado).

---

## 📊 **Gráfico claro resumen fallos protocolo 2PC:**

```
Coordinador         Participantes
    │                    │
    ▼                    ▼
Falla:                Falla:
- Incertidumbre       - Antes READY: ABORT
participantes.        - Tras READY: Recuperación consultando coordinador.
```

---

## 🧩 **Ejercicios resueltos claramente:**

### ✅ **(a) Quorum Consenso explicado claramente:**
- Controla concurrencia mediante quorum mínimo (pesos de sitios) para lecturas/escrituras.

---

### ✅ **(b) Implicancias definir valores quorum:**
- Mayor quorum lectura → más consistencia, menor rendimiento.
- Mayor quorum escritura → seguridad escrituras, menor eficiencia.
- Condición clave: Q_L + Q_E > peso total.

---

### ✅ **(c) Valores quorum Mayoría y Sesgado ejemplos concretos:**
- **Mayoría:** (total=10): Q_L=6, Q_E=5 (6+5>10)
- **Sesgado:** sitio principal con peso dominante (peso=7; quorum=7).

---

### ✅ **(a) Pasos protocolo Commit 2 Fases (2PC):**
- **Preparación:** PREPARE → participantes READY/ABORT
- **Confirmación:** COMMIT si todos READY; si no, ABORT.

---

### ✅ **(b) Falla coordinador (qué hacen participantes?):**
- Estado incertidumbre (bloqueados). Esperan recuperación o consulta externa.

---

### ✅ **(c) Falla participante (qué hace sitio?):**
- Antes READY: Coordinador aborta operación.
- Después READY: Participante recuperado consulta coordinador para resolver su estado (commit/abort).

---

## 🔑 **Conclusión clave sobre Protocolos Distribuidos:**

- **Quorum de Consenso** garantiza concurrencia segura, sacrificando parcialmente velocidad por seguridad.
- **Protocolo Commit 2 Fases (2PC)** asegura consistencia distribuida mediante confirmación en fases, con riesgos claros si ocurre fallo coordinador o participante.

---

## 🎯 **Resumen Gráfico Claro Protocolos Distribuidos:**

```
Protocolos Distribuidos ───► Coordinación y Concurrencia Segura
          │
          ├── Quorum Consenso ───► Lectura/escritura por quorum
          │        ├─ Mayoría (lect+escr>total)
          │        └─ Sesgado (sitio dominante)
          │
          └── Commit 2 Fases ────► Confirmación distribuida en fases
                   ├─ Fase preparación
                   └─ Fase confirmación
```



## 12. Almacenamiento Distribuido


# 🌐 **Introducción al Almacenamiento Distribuido**

El **Almacenamiento Distribuido** se refiere a la forma en que los datos de una base de datos se almacenan y gestionan físicamente en múltiples sitios distribuidos, garantizando disponibilidad, rendimiento y seguridad.

---

## 📌 **Formas Principales de Almacenamiento Distribuido**

Existen principalmente dos formas:

### 🔹 **1. Replicación**
- Consiste en tener **copias exactas** de los mismos datos en diferentes sitios distribuidos.

**Ventajas:**
- Alta disponibilidad y fiabilidad.
- Rápido acceso local a datos comunes.

**Desventajas:**
- Costos mayores por almacenamiento redundante.
- Dificultad en mantener sincronización constante.

**Ejemplo claro:**
- Datos de usuarios replicados en sitios distribuidos globalmente para acceso rápido local.

---

### 🔹 **2. Fragmentación**
Dividir los datos en partes más pequeñas (**fragmentos**) almacenadas en diferentes sitios. Existen dos tipos:

#### (a) **Fragmentación Horizontal**
- Divide filas de una tabla.
- Cada fragmento contiene un conjunto específico de filas completas.

**Ejemplo:**
| Sitio   | Fragmento                           |
|---------|-------------------------------------|
| Europa  | Clientes europeos                   |
| América | Clientes norteamericanos y latinos  |

#### (b) **Fragmentación Vertical**
- Divide columnas de una tabla.
- Cada fragmento almacena un subconjunto de columnas en sitios diferentes.

**Ejemplo:**
| Sitio       | Fragmento                    |
|-------------|------------------------------|
| Finanzas    | Columnas (Salario, Cuentas)  |
| RRHH        | Columnas (Nombre, Dirección) |

**Ventajas fragmentación:**
- Mejor rendimiento según necesidades locales.
- Menor cantidad de datos transmitidos en consultas específicas.

**Desventajas fragmentación:**
- Mayor complejidad de gestión.
- Consultas globales pueden ser lentas.

---

## 📡 **Estrategia de Semireunión (Semijoin)**

Es una estrategia que minimiza la transmisión de datos en consultas distribuidas tipo JOIN. Envía solo atributos necesarios para identificar filas relevantes.

### 🔹 **Pasos Semireunión (si consulta recibida en sitio 1):**
- Consulta: `SELECT * FROM R JOIN S` (sitio 1 tiene tabla R, sitio 2 tabla S)

1. **Sitio 1** envía columna clave (join) de R al sitio 2.
2. **Sitio 2** calcula JOIN parcial usando claves recibidas.
3. **Sitio 2** devuelve al sitio 1 solo filas necesarias para completar JOIN final.
4. **Sitio 1** realiza JOIN final.

---

## 📊 **Cálculo detallado del coste transmisión Semijoin**

Supón:
- Sitio 1: tabla R, 500 filas, claves 4 bytes.
- Sitio 2: tabla S, 1000 filas, 100 bytes/fila.

### 🔹 **Cálculo costes si consulta llega a sitio 1:**

| Paso | Acción                                  | Coste transmisión aproximado |
|------|-----------------------------------------|------------------------------|
| 1    | S1 envía claves R → S2 (500 × 4 bytes)  | **2000 bytes** (~2KB)        |
| 2    | S2 responde filas relevantes (200 filas × 100 bytes)| **20000 bytes** (~20KB)|
|      | **Costo total aprox.:**                 | **22KB**                     |

---

### 🔹 **Si consulta llega a sitio 2 (invertido):**

| Paso | Acción                                  | Coste transmisión aproximado |
|------|-----------------------------------------|------------------------------|
| 1    | S2 envía claves S → S1 (1000 × 4 bytes) | **4000 bytes** (~4KB)        |
| 2    | S1 responde filas relevantes (300 filas × 80 bytes)| **24000 bytes** (~24KB) |
|      | **Costo total aprox.:**                 | **28KB**                     |

---

## 📈 **Comparativa gráfica Replicación vs. Fragmentación**

```
                        Replicación
               Alta │  • disponibilidad máxima
Disponibilidad     │  • alto coste almacenamiento
                   │
                   │                 Fragmentación
                   │              • menos almacenamiento
               Baja│              • más rendimiento local
                   └─────────────────────► Rendimiento local
                  Bajo                  Alto
```

---

## 🧩 **Ejercicios resueltos claramente:**

### ✅ **(1) Formas almacenamiento distribuido explicadas claramente:**
- **Replicación:** Copias exactas en múltiples sitios (alta disponibilidad).
- **Fragmentación:** División horizontal o vertical según necesidad (rendimiento optimizado).

---

### ✅ **(2) Pasos claros y coste Semireunión:**

**Ejemplo concreto (Consulta llega sitio 1):**

1. **Sitio 1 → claves R → Sitio 2**
2. **Sitio 2 → filas relevantes → Sitio 1**
3. **Sitio 1 completa JOIN**

**Coste aprox.:** ~22KB (menor que enviar tablas completas)

---

## 📌 **Caso práctico específico Semireunión:**

- Consulta original: 
```sql
SELECT * FROM Clientes JOIN Compras ON Clientes.id = Compras.cliente_id
```

### 🔹 **Datos ejemplo:**
- Clientes (Sitio 1): 1000 filas, claves=4 bytes
- Compras (Sitio 2): 3000 filas, 50 bytes/fila

### 🔹 **Pasos Semijoin (consulta en Sitio 1):**
1. Sitio 1 envía claves Clientes (4KB aprox.) → Sitio 2.
2. Sitio 2 devuelve filas coincidentes (ej: 500 filas × 50 bytes = 25KB aprox.) → Sitio 1.

### 🔹 **Coste total claro:** 
- Aproximadamente 29KB transmisión (mucho menor que enviar toda tabla Compras ≈ 150KB).

---

## 🔑 **Conclusiones clave Almacenamiento Distribuido:**

- **Replicación**: Alta disponibilidad y redundancia, costo mayor.
- **Fragmentación**: Optimiza rendimiento, menor almacenamiento, mayor complejidad.
- Estrategia de **Semireunión** reduce significativamente costo transmisión en JOINs distribuidos.

---

## 🎯 **Gráfico resumen claro formas almacenamiento distribuido:**

```
Almacenamiento Distribuido
        │
        ├── Replicación ──► Alta disponibilidad
        │       └─ Copias exactas múltiples sitios
        │
        └── Fragmentación ──► Optimización rendimiento
                ├─ Horizontal (filas)
                └─ Vertical (columnas)
```


## 13. Optimizacion Consultas


# 🚀 **Introducción a la Optimización de Consultas**

La **Optimización de Consultas** es el proceso que usa un SGBD para transformar una consulta SQL escrita por el usuario en una versión más eficiente en términos de rendimiento.

---

## 📐 **Álgebra Relacional para Optimización**

El SGBD transforma consultas SQL en **Álgebra Relacional**, que permite usar reglas matemáticas para elegir el orden más eficiente de las operaciones.

### 🔹 **Operaciones básicas álgebra relacional:**

- **σ (Selección):** Filtra filas.
- **π (Proyección):** Filtra columnas.
- **⨝ (Join):** Combina tablas.
- **× (Producto cartesiano):** Combina cada fila de una tabla con cada fila de otra.

---

## 📚 **Tema 4: Traducción inicial y optimización JOIN**

### 🔹 **Consulta original:**
```sql
SELECT e.LNAME 
FROM EMPLEADO e 
JOIN TRABAJA_EN te ON te.EMPLEADO = e.ID 
JOIN PROYECTO p ON p.ID = te.PROYECTO 
WHERE p.NOMBRE = 'AQUARIUS' AND e.FECHA_NAC >= '2000-01-01'
```

### 🔹 **Traducción inicial (sin optimizar):**
```
π_LNAME(
    σ_(NOMBRE='AQUARIUS' ∧ FECHA_NAC≥'2000-01-01') (
        EMPLEADO ⨝_(EMPLEADO.ID=te.EMPLEADO) TRABAJA_EN te
                 ⨝_(te.PROYECTO=p.ID) PROYECTO p
    )
)
```

---

### 🧩 **Optimización (2 casos prácticos):**

#### **Caso 1: Empujar selecciones (Push selection)**

- Aplica primero selecciones para reducir el tamaño de tablas antes de JOIN.

```
π_LNAME(
    (σ_FECHA_NAC≥'2000-01-01'(EMPLEADO))
    ⨝_(ID=EMPLEADO) TRABAJA_EN
    ⨝_(PROYECTO=ID) (σ_NOMBRE='AQUARIUS'(PROYECTO))
)
```

- **Ventaja:** Menos datos al hacer JOINs, rendimiento notablemente mejorado.

---

#### **Caso 2: Cambiar orden JOIN según tamaño tablas (Join reordering)**

- Ordena JOINs comenzando por tablas pequeñas para reducir el coste.

```
π_LNAME(
    (σ_NOMBRE='AQUARIUS'(PROYECTO) ⨝ TRABAJA_EN)
    ⨝ σ_FECHA_NAC≥'2000-01-01'(EMPLEADO)
)
```

- **Ventaja:** Reduce significativamente filas antes del JOIN final con tabla grande (EMPLEADO).

---

## 📌 **Tema 7: Consultas hipotéticas SELECT y sus costes**

### 🔹 **Consulta original hipotética:**
```sql
SELECT * FROM Clientes WHERE Pais = 'Paraguay';
```

#### **Caso 1: Tabla pequeña, sin índices**
- **Algoritmo:** Búsqueda lineal.
- **Costo:** O(n) → alto.
- **Ejemplo:** Tabla Clientes (500 filas).

---

#### **Caso 2: Tabla ordenada físicamente**
- **Algoritmo:** Búsqueda binaria.
- **Costo:** O(log n) → medio.
- **Ejemplo:** Tabla Clientes ordenada por país.

---

#### **Caso 3: Índice secundario sobre país**
- **Algoritmo:** Índice secundario (B+).
- **Costo:** O(log n) → bajo.
- **Ejemplo:** Índice sobre columna Pais.

---

#### **Caso 4: Tabla replicada localmente**
- **Algoritmo:** Acceso local inmediato.
- **Costo:** O(1) → muy bajo.
- **Ejemplo:** Copia local en servidor Paraguay.

---

## 📉 **Gráfico claro comparativo coste consultas:**

```
Costo consulta (SELECT WHERE)

Alto │ Lineal (sin índices)
     │
     │        Binaria (tabla ordenada)
     │
     │                 Índice secundario (B+)
Bajo │                           Replicación local
     └───────────────────────────────────► Eficiencia
```

---

## 📚 **Resumen práctico optimización consultas**

| Técnica optimización | Descripción clara             | Ventaja principal           |
|----------------------|-------------------------------|-----------------------------|
| Empujar selecciones  | Aplicar filtros antes JOINs   | Menos filas en JOIN         |
| Reordenar JOINs      | Tablas pequeñas primero       | Menor coste JOINs grandes   |
| Índices secundarios  | Uso columnas frecuentes       | Búsqueda rápida O(log n)    |
| Replicación local    | Copias locales tablas comunes | Acceso inmediato O(1)       |

---

## ✅ **Ejercicios resueltos claramente:**

### **(Tema 4)** Álgebra relacional y optimizaciones claras:

- **Consulta original → Álgebra relacional claramente explicada**
- **Optimización 1:** Empujar selecciones.
- **Optimización 2:** Cambiar orden JOIN.

---

### **(Tema 7)** Casos hipotéticos claramente definidos y explicados:

| Caso | Descripción                           | Algoritmo usado       | Costo teórico |
|------|---------------------------------------|-----------------------|---------------|
| 1    | Sin índices                           | Lineal                | O(n) alto     |
| 2    | Tabla ordenada físicamente            | Binaria               | O(log n) medio|
| 3    | Índice secundario disponible          | Índice secundario (B+)| O(log n) bajo |
| 4    | Replicación local                     | Acceso local          | O(1) muy bajo |

---

## 🎯 **Conclusión clave sobre Optimización de Consultas:**

- Usar álgebra relacional permite al SGBD reestructurar consultas para optimizar rendimiento.
- La selección temprana (push selection) y la reordenación de JOINs son las técnicas más efectivas.
- Índices secundarios y replicación local proporcionan grandes mejoras en búsquedas específicas.

---

## 📊 **Gráfico resumen claro sobre Optimización Consultas:**

```
Optimización Consultas SQL ──► Mejor rendimiento
           │
           ├─ Álgebra Relacional ──► reglas equivalentes
           │
           ├─ Empujar Selecciones ──► menos filas JOIN
           │
           ├─ Reordenar JOINs ──► menor coste global
           │
           └─ Uso Índices y Replicación ──► acceso rápido (log n o 1)
```



## 14. Normalizacion Dependencias Funcionales

# 📚 **Introducción a la Normalización**

La **normalización** es un proceso en diseño de bases de datos que organiza los datos eficientemente para:

- Eliminar redundancias.
- Evitar anomalías (inserción, actualización, eliminación).
- Garantizar integridad y consistencia.

---

## 📌 **Dependencias Funcionales**

Una **Dependencia Funcional (DF)** ocurre cuando el valor de un atributo (o conjunto de atributos) determina únicamente el valor de otro atributo.

Notación clara:  
```
A → B ("A determina B")
```

---

# 🧩 **Ejercicio práctico claro (Empleado)**

Tabla inicial:  
```
Empleado (CI, Nombre, Dirección, Cargo, Cod_Dep)
```

### 🔹 **Dependencias Funcionales (DF) iniciales:**

- `CI → Nombre, Dirección, Cargo, Cod_Dep`
  - Cada persona (CI) tiene un nombre, dirección, cargo y departamento únicos.
- `Cod_Dep → Cargo (en algunos casos)`
  - Posible dependencia parcial si el cargo depende directamente del departamento.

---

## 📐 **Aplicación de las Formas Normales (Empleado)**

### 🔹 **Primera Forma Normal (1FN):**

- No atributos multivaluados. Tabla ya cumple (cada atributo es atómico).

**Estado:**  
```
Empleado(CI, Nombre, Dirección, Cargo, Cod_Dep)
```

---

### 🔹 **Segunda Forma Normal (2FN):**

- No dependencias parciales respecto a la clave primaria.

En este caso, la clave primaria es `CI`, que es un atributo simple, por lo que ya cumple 2FN directamente (no hay dependencias parciales posibles).

**Estado 2FN:**  
```
Empleado(CI, Nombre, Dirección, Cargo, Cod_Dep)
```

---

### 🔹 **Tercera Forma Normal (3FN):**

- No dependencias transitivas (atributos no clave que dependen de otro atributo no clave).

**Analizar dependencia transitiva:**  
- Supongamos posible dependencia transitiva: `Cod_Dep → Cargo`.
- Para evitar esta dependencia, separar atributos en dos tablas:

**Resultado claro en 3FN:**  
```
Empleado(CI, Nombre, Dirección, Cod_Dep)
Departamento(Cod_Dep, Cargo)
```

---

## 🔑 **Claves Primarias y Foráneas claramente definidas:**

- **Empleado:**
  - Clave primaria: `CI`
  - Clave foránea: `Cod_Dep` → referencia a `Departamento(Cod_Dep)`

- **Departamento:**
  - Clave primaria: `Cod_Dep`

---

# 📚 **Ejercicio práctico claro (Carrera, Materia, Docente)**

Tablas iniciales claramente definidas:

```
Carrera(CodCarrera, NombreCarrera)
Materia(CodMateria, NombreMateria, CodCarrera)
Docente(CI_Docente, NombreDocente, CodMateria)
```

### 🔹 **Dependencias Funcionales identificadas claramente:**

- **Carrera:** `CodCarrera → NombreCarrera`
- **Materia:** `CodMateria → NombreMateria, CodCarrera`
- **Docente:** `CI_Docente → NombreDocente, CodMateria`

---

## 📌 **Aplicar Normalización claramente explicada:**

### 🔹 **1FN (Cumple desde inicio)**

Cada atributo atómico claramente definido.

### 🔹 **2FN (Cumple desde inicio)**

Cada tabla tiene una clave primaria simple. No existen dependencias parciales posibles.

### 🔹 **3FN (Dependencias transitivas a verificar)**

- No se detectan dependencias transitivas claras en estas tablas originales. 
- Ya cumplen claramente 3FN.

**Resultado final claro (en 3FN):**  
```
Carrera(CodCarrera, NombreCarrera)
Materia(CodMateria, NombreMateria, CodCarrera)
Docente(CI_Docente, NombreDocente, CodMateria)
```

---

## 📑 **Claves Primarias y Foráneas claramente definidas:**

| Tabla        | Clave primaria | Claves foráneas                       |
|--------------|----------------|---------------------------------------|
| Carrera      | CodCarrera     | —                                     |
| Materia      | CodMateria     | CodCarrera → Carrera(CodCarrera)      |
| Docente      | CI_Docente     | CodMateria → Materia(CodMateria)      |

---

## 📊 **Gráfico resumen claro Normalización 1FN → 3FN:**

```
Tabla inicial (1FN) ──► (2FN: Sin dependencias parciales)
           │
           ▼
(3FN: Sin dependencias transitivas)
           │
           ▼
Tablas separadas claras (3FN, eficiente)
```

---

## 🎯 **Ejemplo visual claro Normalización Empleado (3FN):**

**ANTES (tabla única con redundancia):**
| CI   | Nombre  | Dirección | Cargo      | Cod_Dep |
|------|---------|-----------|------------|---------|
| 123  | Juan    | Calle A   | Analista   | D01     |
| 456  | Laura   | Calle B   | Analista   | D01     |

- Redundancia clara en "Cargo" (Analista repetido).

**DESPUÉS (en 3FN):**

**Empleado**
| CI   | Nombre  | Dirección | Cod_Dep |
|------|---------|-----------|---------|
| 123  | Juan    | Calle A   | D01     |
| 456  | Laura   | Calle B   | D01     |

**Departamento**
| Cod_Dep | Cargo    |
|---------|----------|
| D01     | Analista |

- Redundancia eliminada claramente.

---

## ✅ **Conclusión clave sobre Normalización y Dependencias Funcionales:**

- La normalización elimina claramente redundancias y evita anomalías.
- La clave es identificar claramente dependencias funcionales, parciales y transitivas.
- Aplicar formas normales (1FN, 2FN, 3FN) resulta en un diseño más limpio, eficiente y robusto.

---

## 📝 **Resumen gráfico claro Normalización y Dependencias Funcionales:**

```
Normalización y Dependencias Funcionales ──► Eficiencia diseño BD
              │
              ├─ DF claras ──► Atributos determinantes
              │
              ├─ 1FN (atómicos) ──► Sin atributos multivaluados
              │
              ├─ 2FN (parciales) ──► Dependencia completa clave primaria
              │
              └─ 3FN (transitivas) ──► No dependencias transitivas
```



## 15. Modelado ER SQL


# 📐 **1. Modelo ER: Empresa-Empleados-Departamento**

## 🔹 **Modelo Entidad-Relación (MER):**

**Entidades:**
- **Empleado:** CI (PK), Nombre, Dirección, Cargo
- **Departamento:** Cod_Dep (PK), Nombre_Dep

**Relaciones:**
- **Trabaja_en:** Relación N:1 (muchos empleados en un departamento).

**Diagrama ER claro:**
```
Empleado (CI, Nombre, Dirección, Cargo)
     │N
     │
[Trabaja_en]
     │1
     ▼
Departamento (Cod_Dep, Nombre_Dep)
```

---

## 🔹 **Transformación al Modelo Relacional:**

```
Empleado(CI, Nombre, Dirección, Cargo, Cod_Dep(FK))
Departamento(Cod_Dep, Nombre_Dep)
```

- **PK (primaria):** Empleado(CI), Departamento(Cod_Dep)
- **FK (foránea):** Empleado(Cod_Dep → Departamento)

---

# 📚 **2. Modelo ER: Universidad (Carreras, Materias, Docentes, Alumnos)**

## 🔹 **Modelo ER claro:**

**Entidades:**
- **Carrera:** CodCarrera (PK), Nombre
- **Materia:** CodMateria (PK), Nombre, CodCarrera(FK)
- **Docente:** CI_Docente (PK), Nombre
- **Alumno:** CI_Alumno (PK), Nombre

**Relaciones:**
- **Dicta:** Docente 1:N Materia
- **Inscripción:** Alumno N:M Materia (Tabla intermedia)
- **Carrera-Materia:** Carrera 1:N Materia

**Diagrama ER claro:**
```
Carrera (CodCarrera, Nombre)
  │1
  │
[Tiene]
  │N
  ▼
Materia (CodMateria, Nombre)
  │N           N
  │            │
[Dicta]     [Inscripción]
  │1           │
Docente(CI,Nombre) Alumno(CI,Nombre)
```

---

## 🔹 **Modelo Relacional claro:**

```
Carrera(CodCarrera, Nombre)
Materia(CodMateria, Nombre, CodCarrera(FK))
Docente(CI_Docente, Nombre)
Alumno(CI_Alumno, Nombre)
Inscripción(CI_Alumno(FK), CodMateria(FK), Nota)
Dicta(CI_Docente(FK), CodMateria(FK))
```

---

## 🔑 **Consultas SQL (Universidad):**

- **Materias por carrera específica:**
```sql
SELECT M.Nombre
FROM Materia M
WHERE M.CodCarrera = 'INF';
```

- **Docentes que dictan materia específica:**
```sql
SELECT D.Nombre
FROM Docente D
JOIN Dicta DT ON D.CI_Docente = DT.CI_Docente
WHERE DT.CodMateria = 'BD2';
```

- **Alumnos que rindieron exámenes en más de una materia:**
```sql
SELECT A.Nombre, COUNT(*) AS MateriasExamen
FROM Alumno A
JOIN Inscripción I ON A.CI_Alumno = I.CI_Alumno
GROUP BY A.Nombre
HAVING COUNT(*) > 1;
```

---

# 📖 **3. Modelo ER: Biblioteca (Libro, Autor, Editorial, Socio, Préstamo)**

## 🔹 **Modelo ER claro:**

**Entidades:**
- **Libro:** CodLibro (PK), Titulo, CodEditorial(FK)
- **Autor:** CodAutor (PK), Nombre
- **Editorial:** CodEditorial (PK), Nombre
- **Socio:** CodSocio (PK), Nombre, Dirección
- **Préstamo:** CodPrestamo (PK), Fecha, CodLibro(FK), CodSocio(FK)

**Relaciones:**
- **Libro-Autor:** N:M (tabla intermedia "LibroAutor")
- **Libro-Editorial:** N:1
- **Préstamo-Socio-Libro:** N:1 (cada préstamo para un libro específico a un socio)

**Modelo relacional final claro:**
```
Libro(CodLibro, Titulo, CodEditorial(FK))
Autor(CodAutor, Nombre)
Editorial(CodEditorial, Nombre)
Socio(CodSocio, Nombre, Dirección)
Prestamo(CodPrestamo, Fecha, CodLibro(FK), CodSocio(FK))
LibroAutor(CodLibro(FK), CodAutor(FK))
```

---

# 📊 **Consultas SQL y Álgebra relacional claras (Empresa-Empleado-Departamento)**

- **Lista empleados por departamento (SQL):**
```sql
SELECT E.Nombre, D.Nombre_Dep
FROM Empleado E
JOIN Departamento D ON E.Cod_Dep = D.Cod_Dep;
```

- **Álgebra relacional:**
```
π_(Nombre,Nombre_Dep)(Empleado ⨝_(Cod_Dep) Departamento)
```

- **Nombre empleados con cargo 'Analista' (SQL):**
```sql
SELECT Nombre
FROM Empleado
WHERE Cargo = 'Analista';
```

- **Álgebra relacional:**
```
π_Nombre(σ_Cargo='Analista'(Empleado))
```

- **Total empleados por departamento (SQL):**
```sql
SELECT Cod_Dep, COUNT(*) AS TotalEmpleados
FROM Empleado
GROUP BY Cod_Dep;
```

---

# 📌 **Consultas SQL (Universidad):**

- **Listar materias por carrera:**
```sql
SELECT Nombre
FROM Materia
WHERE CodCarrera = 'INF';
```

- **Buscar docentes por materia específica:**
```sql
SELECT D.Nombre
FROM Docente D
JOIN Dicta DT ON D.CI_Docente = DT.CI_Docente
WHERE DT.CodMateria = 'BD2';
```

- **Mostrar alumnos que rindieron exámenes en más de una materia:**
```sql
SELECT A.Nombre, COUNT(I.CodMateria) AS MateriasExamen
FROM Alumno A
JOIN Inscripción I ON A.CI_Alumno = I.CI_Alumno
GROUP BY A.Nombre
HAVING COUNT(I.CodMateria) > 1;
```

---

# ✅ **Conclusiones clave (MER y SQL):**

- **Modelo ER** permite representar claramente entidades, relaciones y cardinalidades.
- **Transformación relacional** traduce ER en tablas específicas (PKs/FKs).
- Las **consultas SQL** permiten extracción precisa de información específica según necesidad.
- **Álgebra relacional** facilita la optimización visual de consultas antes de ejecución en SGBD.

---

## 🎯 **Gráfico resumen claro MER → Relacional → SQL:**

```
Requerimiento ──► Modelo ER
       │
       ▼
Modelo Relacional (tablas, PK/FK)
       │
       ▼
Consultas SQL claras y eficientes
       │
       ▼
Resultados rápidos y exactos
```

