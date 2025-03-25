# Bases de Datos Avanzadas - Libro Completo

Este libro reÃºne todos los temas relacionados con Bases de Datos Avanzadas.

## Tabla de Contenidos

1. [Ãndices](#1-Ã­ndices)
2. [OrganizaciÃ³n FÃ­sica de Archivos](#2-organizaciÃ³n-fÃ­sica-de-archivos)
3. [Medidas de Rendimiento de Discos](#3-medidas-de-rendimiento-de-discos)
4. [Niveles RAID](#4-niveles-raid)
5. [Ãrboles B y B+](#5-Ã¡rboles-b-y-b)
6. [Algoritmos de BÃºsqueda](#6-algoritmos-de-bÃºsqueda)
7. [Procesamiento de Consultas](#7-procesamiento-de-consultas)
8. [Modelado Multidimensional](#8-modelado-multidimensional)
9. [Transacciones (ACID)](#9-transacciones-acid)
10. [Concurrencia](#10-concurrencia)
11. [Protocolos Distribuidos](#11-protocolos-distribuidos)
12. [Almacenamiento Distribuido](#12-almacenamiento-distribuido)
13. [OptimizaciÃ³n de Consultas](#13-optimizaciÃ³n-de-consultas)
14. [NormalizaciÃ³n y Dependencias Funcionales](#14-normalizaciÃ³n-y-dependencias-funcionales)
15. [Modelado ER y SQL](#15-modelado-er-y-sql)
## 1. Indices


## ðŸ” **Â¿QuÃ© es un Ãndice?**

Un **Ã­ndice** en bases de datos es una estructura auxiliar que facilita la recuperaciÃ³n eficiente de registros especÃ­ficos, reduciendo significativamente el tiempo de consulta. Funciona de manera similar al Ã­ndice al final de un libro: permite localizar informaciÃ³n rÃ¡pidamente sin revisar todo el contenido.

Un **archivo Ã­ndice** es un archivo fÃ­sico separado que almacena referencias a las filas del archivo principal de datos segÃºn el valor de la columna indexada.

### ðŸ“Œ **Tipos principales de Ã­ndices estudiados:**
1. **Ãndice ordenado** (basado en Ã¡rboles B y B+).
2. **Ãndice hash**.
3. **Ãndice bitmap**.

---

## ðŸ“— **Tipos de Ãndices segÃºn sus consultas apropiadas**

| Tipo Ã­ndice | Ideal para consultas |
|-------------|----------------------|
| Ordenado    | Rangos (ej. fechas, intervalos numÃ©ricos) |
| Hash        | Consultas exactas (condiciones de igualdad) |
| Bitmap      | Consultas mÃºltiples simultÃ¡neas (muchas condiciones sobre columnas booleanas o categÃ³ricas) |

---

## ðŸ“š **Tipos de Ãndices segÃºn su OrganizaciÃ³n FÃ­sica**

### 1. **Ãndice Ordenado (Ãrbol B/B+)**
- Almacena valores ordenados jerÃ¡rquicamente, permitiendo bÃºsquedas rÃ¡pidas y eficientes.
- AplicaciÃ³n ideal: consultas con rangos, valores cercanos.

### 2. **Ãndice Hash**
- Usa una funciÃ³n de hash para determinar la ubicaciÃ³n fÃ­sica de un dato.
- AplicaciÃ³n ideal: bÃºsquedas puntuales exactas.

### 3. **Ãndice Bitmap**
- Cada valor Ãºnico tiene un mapa de bits asociado, Ãºtil en columnas con pocos valores Ãºnicos.
- AplicaciÃ³n ideal: mÃºltiples condiciones simultÃ¡neas.

---

## ðŸ“ˆ **Costos AsintÃ³ticos de Algoritmos de BÃºsqueda**

| Algoritmo               | Costo AsintÃ³tico (promedio) |
|-------------------------|-----------------------------|
| (a) BÃºsqueda lineal     | O(n)                        |
| (b) BÃºsqueda binaria    | O(log n)                    |
| (c) Ãndice primario (B+) | O(log n)                   |
| (d) Ãndice secundario   | O(log n)                    |

---

## ðŸ“Œ **Condiciones fÃ­sicas para usar algoritmos (en igualdad):**

| Algoritmo           | CondiciÃ³n fÃ­sica ideal                  |
|---------------------|----------------------------------------|
| BÃºsqueda Lineal     | No existe Ã­ndice. Tabla pequeÃ±a.        |
| BÃºsqueda Binaria    | Tabla ordenada secuencialmente sin Ã­ndices disponibles.|
| Ãndice Primario (B+)| Existe Ã­ndice sobre clave primaria.     |
| Ãndice Secundario   | Existe Ã­ndice sobre atributo no clave.  |

---

## ðŸ“Š **GrÃ¡fico ilustrativo (Ejemplo Ãndice B+):**

```plaintext
                   [20, 40]
                  /    |    \
         [5,10,15] [25,30,35] [45,50,55]
```

- **BÃºsqueda**: Recorre Ã¡rbol desde raÃ­z hacia hojas rÃ¡pidamente.

---

## ðŸ§© **Ejercicios Resueltos**

### ðŸ› ï¸ **Tema 6: ConstrucciÃ³n Ãndice Hash (AsociaciÃ³n Extensible)**

La asociaciÃ³n extensible es una tÃ©cnica de hash dinÃ¡mico que permite expandir el espacio de almacenamiento conforme crece la base de datos.

**Ejemplo:**

- FunciÃ³n hash simple: `h(x) = x mod 4`
- Datos iniciales: `4, 8, 5, 7, 12, 15`

| CajÃ³n (bucket) | Valores almacenados |
|----------------|---------------------|
| 0              | 4, 8, 12            |
| 1              | 5                   |
| 2              |                    |
| 3              | 7, 15               |

Cuando un cajÃ³n excede capacidad, se duplica el Ã­ndice aumentando el nÃºmero de bits y re-distribuyendo valores.

---

### ðŸ› ï¸ **Tema 10: Ãndice B+ e Ãndice Hash EstÃ¡tico**

#### ðŸ”¹ **ConstrucciÃ³n Ãndice B+ (ejemplo sencillo):**

Datos: `[10,20,30,40,50,60,70,80]`, 4 punteros por nodo.

```plaintext
         [40]
      /        \
  [10,20,30]  [50,60,70,80]
```

- **ClasificaciÃ³n:** Primario (si Ã­ndice estÃ¡ sobre clave primaria).

#### ðŸ”¹ **ConstrucciÃ³n Ãndice Hash estÃ¡tico:**

Datos: `[21,32,43,54]`, funciÃ³n hash `h(x) = x mod 4`

| CajÃ³n | Datos     |
|-------|-----------|
| 0     | 32        |
| 1     | 21        |
| 2     | 54        |
| 3     | 43        |

- **ClasificaciÃ³n:** Secundario (generalmente Ã­ndices hash son secundarios, ya que suelen aplicarse a atributos no clave para bÃºsquedas exactas).

---

## âœ… **Ejercicios planteados:**

### **Ejercicio 1: Â¿QuÃ© es un Ã­ndice y archivo Ã­ndice?**
- **Ãndice:** Estructura auxiliar que acelera la recuperaciÃ³n de datos.
- **Archivo Ã­ndice:** Archivo fÃ­sico separado que contiene referencias a registros segÃºn columna indexada.

**Tres tipos de Ã­ndices estudiados:**
- Ãndice Ordenado (Ãrbol B+).
- Ãndice Hash.
- Ãndice Bitmap.

---

### **Ejercicio 2: Ãndices apropiados segÃºn consulta:**
- (a) **Ordenado:** Rangos, intervalos. (Ej: Fecha de nacimiento entre 1990-2000).
- (b) **Hash:** Igualdad exacta. (Ej: CI = 123456).
- (c) **Bitmap:** MÃºltiples condiciones simultÃ¡neas. (Ej: GÃ©nero=Femenino AND Ciudad=AsunciÃ³n).

---

### **Ejercicio 3: OrganizaciÃ³n fÃ­sica y aplicaciÃ³n:**
- **B+ (Ordenado):** Consultas rango, ordenaciÃ³n rÃ¡pida.
- **Hash:** Igualdad exacta rÃ¡pida.
- **Bitmap:** Consultas analÃ­ticas con mÃºltiples condiciones categÃ³ricas.

---

### **Ejercicio 4: Costos asintÃ³ticos explicados antes.**
- (a) Lineal: `O(n)`
- (b) Binaria: `O(log n)`
- (c) Primario: `O(log n)`
- (d) Secundario: `O(log n)`

---

### **Ejercicio 5: Condiciones fÃ­sicas explicadas antes.**

- **Lineal:** Sin Ã­ndice, tabla pequeÃ±a.
- **Binaria:** Tabla ordenada sin Ã­ndice.
- **Primario:** Ãndice clave primaria disponible.
- **Secundario:** Ãndice atributo no clave disponible.

---

### ðŸ“Œ **Resumen Visual del uso de Ã­ndices segÃºn tipo de consulta:**
```plaintext
Consultas de rango  â†’ Ãndice Ordenado (B+)
Consultas exactas   â†’ Ãndice Hash
Consultas complejas â†’ Ãndice Bitmap
```

---

## ðŸ“ **ConclusiÃ³n**

- **Ãndices** aceleran consultas significativamente.
- Cada tipo es ideal segÃºn tipo de consulta y estructura de datos.
- Importante evaluar costo-beneficio al elegir Ã­ndice.


## 2. Organizacion Fisica Archivos


# ðŸ“‚ **OrganizaciÃ³n FÃ­sica de Archivos**

La **organizaciÃ³n fÃ­sica de archivos** hace referencia a cÃ³mo se almacenan los registros en los archivos fÃ­sicos de un Sistema Gestor de Bases de Datos (SGBD). Elegir la estructura adecuada afecta considerablemente el rendimiento, especialmente en consultas e inserciones.

---

## ðŸ“‘ **Formas de OrganizaciÃ³n FÃ­sica**

Existen principalmente cuatro formas de organizaciÃ³n fÃ­sica:

### **1. Heap (MontÃ³n):**
- Los registros son almacenados en cualquier espacio libre disponible.
- **Ventaja:** InserciÃ³n muy rÃ¡pida.
- **Desventaja:** Consultas lentas (requiere escaneo completo).

**Ejemplo:**  
Agregar un nuevo cliente al archivo de clientes sin preocuparse de dÃ³nde queda ubicado exactamente.

---

### **2. Secuencial (Ordenado):**
- Registros almacenados consecutivamente en orden segÃºn una clave.
- **Ventaja:** Consultas por rango muy eficientes.
- **Desventaja:** Inserciones lentas, requieren reorganizaciÃ³n periÃ³dica.

**Ejemplo:**  
Historial de transacciones ordenado por fecha.

---

### **3. Hash:**
- UbicaciÃ³n de registros determinada por una funciÃ³n hash aplicada sobre la clave.
- **Ventaja:** BÃºsqueda puntual extremadamente rÃ¡pida.
- **Desventaja:** Mal rendimiento en consultas por rango.

**Ejemplo:**  
Buscar datos exactos como DNI o nÃºmero de telÃ©fono.

---

### **4. AgrupaciÃ³n (Cluster):**
- Almacena juntos registros relacionados o que se consultan con frecuencia.
- **Ventaja:** Consultas comunes aceleradas.
- **Desventaja:** Actualizaciones mÃ¡s lentas si afectan las columnas agrupadas.

**Ejemplo:**  
Datos de un cliente y todas sus facturas en bloques cercanos.

---

## ðŸ“‹ **OrganizaciÃ³n de registros en archivos (resumen en tÃ©rminos simples):**
- **Heap:** Cualquier lugar libre (desordenado, rÃ¡pido inserciÃ³n).
- **Secuencial:** Ordenado en funciÃ³n de una clave.
- **Hash:** UbicaciÃ³n mediante cÃ¡lculo hash.
- **Cluster:** AgrupaciÃ³n lÃ³gica de datos relacionados.

---

## ðŸ—‚ï¸ **Formas de organizaciÃ³n para implementar tablas/datos (simplificado):**
- Para datos que cambian mucho: **Heap**.
- Para consultas frecuentes de rangos: **Secuencial**.
- Para bÃºsquedas exactas rÃ¡pidas: **Hash**.
- Para consultas relacionadas frecuentes: **Cluster**.

---

## ðŸ“Œ **Tema 9: Estructura fÃ­sica de bloques (PÃ¡ginas por ranuras)**

La organizaciÃ³n por pÃ¡ginas y ranuras (slot-based pages) se implementa dividiendo cada bloque fÃ­sico del archivo en "ranuras" que almacenan registros individuales. Esto facilita inserciones, eliminaciones y modificaciones con mÃ­nima fragmentaciÃ³n.

### ðŸ”¹ **ImplementaciÃ³n:**
Cada pÃ¡gina se divide en dos partes:
- **Cabecera:** Contiene un directorio con punteros (slots) hacia los registros.
- **Cuerpo de datos:** Registros almacenados secuencialmente (no necesariamente contiguos).

Cada registro se accede mediante la referencia en la ranura, permitiendo eliminar y reutilizar espacios fÃ¡cilmente.

### Ejemplo visual (grÃ¡fico):

```
PÃ¡gina FÃ­sica (Bloque)
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
- Al insertar, se reutilizan ranuras vacÃ­as.

---

## ðŸ“Š **GrÃ¡fica Comparativa de rendimiento por tipo de organizaciÃ³n:**

```plaintext
Rendimiento (menor tiempo es mejor)

Consulta exacta:
Hash          [â– â– â– â– â– â– â– â– â– â– ]
Secuencial    [â– â– â– â– â– â–¡â–¡â–¡â–¡â–¡]
Heap          [â– â– â–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡]
Cluster       [â– â– â– â– â–¡â–¡â–¡â–¡â–¡â–¡]

Consulta rango:
Secuencial    [â– â– â– â– â– â– â– â– â– â– ]
Cluster       [â– â– â– â– â– â– â– â– â–¡â–¡]
Heap          [â– â–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡]
Hash          [â–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡]

InserciÃ³n rÃ¡pida:
Heap          [â– â– â– â– â– â– â– â– â– â– ]
Hash          [â– â– â– â– â– â– â– â– â–¡â–¡]
Cluster       [â– â– â– â– â– â– â–¡â–¡â–¡â–¡]
Secuencial    [â– â– â– â– â–¡â–¡â–¡â–¡â–¡â–¡]
```

---

## ðŸ“ **Respuestas detalladas a los ejercicios propuestos:**

### ðŸ”¹ **1. ExplicaciÃ³n de las formas de organizaciÃ³n fÃ­sica en SGBD:**

- **Heap:** No ordenado, rÃ¡pido insertar, lento consultar.
- **Secuencial:** Ordenado por clave, rÃ¡pido para rangos, lento insertar.
- **Hash:** DistribuciÃ³n por funciÃ³n hash, bÃºsquedas exactas rÃ¡pidas.
- **Cluster:** AgrupaciÃ³n lÃ³gica, mejora consultas frecuentes relacionadas.

---

### ðŸ”¹ **2. Formas resumidas de organizaciÃ³n de registros (propios tÃ©rminos):**

- **Heap:** Registros en espacio disponible rÃ¡pidamente.
- **Secuencial:** Registros siempre en orden especÃ­fico.
- **Hash:** UbicaciÃ³n segÃºn cÃ¡lculo matemÃ¡tico (hash).
- **Cluster:** Registros relacionados almacenados cerca.

---

### ðŸ”¹ **3. Formas apropiadas para implementaciÃ³n prÃ¡ctica de tablas/datos:**

| Uso habitual               | OrganizaciÃ³n ideal |
|----------------------------|--------------------|
| Insertar muy frecuentemente| Heap               |
| Rangos frecuentes          | Secuencial         |
| Igualdad frecuente         | Hash               |
| Datos relacionados juntos  | Cluster            |

---

### ðŸ”¹ **4. Detalle de la estructura de pÃ¡ginas por ranuras (Tema 9):**

- Divide pÃ¡gina en dos zonas: cabecera (ranuras) y cuerpo (registros).
- Usa directorio de ranuras con punteros hacia registros reales.
- Permite gestiÃ³n eficiente de inserciÃ³n/borrado con fragmentaciÃ³n mÃ­nima.

---

## âœ… **Ejemplo prÃ¡ctico de pÃ¡gina por ranuras:**

- InserciÃ³n:
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

- EliminaciÃ³n de registro B:
  - Ranura 2 queda libre, espacio disponible para inserciÃ³n futura.

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

## ðŸ“Œ **Conclusiones clave sobre OrganizaciÃ³n FÃ­sica de Archivos:**
- Elegir estructura depende del patrÃ³n de uso (insertar vs consultar).
- Heap es rÃ¡pido para insertar; secuencial ideal para consultas por rango.
- Hash destaca en igualdad exacta; Cluster ideal para datos relacionados frecuentes.
- Estructura de pÃ¡ginas por ranuras optimiza el almacenamiento y acceso fÃ­sico.


## 3. Medidas Rendimiento Discos

# ðŸ’¾ **Medidas de Rendimiento de Discos**

Al elegir discos magnÃ©ticos (HDD) para bases de datos, es esencial considerar ciertas medidas de rendimiento para garantizar eficiencia, rapidez y confiabilidad en el acceso a datos.

---

## ðŸ“ **Principales Medidas de Rendimiento**

### **1. Tiempo de acceso (Seek Time)**
- Tiempo necesario para mover la cabeza lectora hacia la pista deseada.
- **MediciÃ³n habitual:** milisegundos (ms).
- **Ejemplo tÃ­pico:** 3-15 ms.

### **2. Latencia rotacional (Rotational Latency)**
- Tiempo que tarda en girar el disco hasta que el sector correcto queda bajo la cabeza.
- Depende directamente de la velocidad de rotaciÃ³n del disco (RPM).
- **Ejemplo:**  
  - 7200 RPM â†’ 4,16 ms promedio  
  - 10.000 RPM â†’ 3 ms promedio

### **3. Tasa de transferencia (Transfer Rate)**
- Cantidad de datos transferidos desde el disco hacia la memoria por unidad de tiempo.
- **MediciÃ³n habitual:** MB/s o GB/s.
- **Ejemplo:**  
  - HDD tÃ­pico: 100-200 MB/s  
  - SSD tÃ­pico: 400-5000 MB/s

### **4. Tiempo medio entre fallos (Mean Time Between Failures - MTBF)**
- Tiempo promedio esperado antes de que el disco presente un fallo.
- **MediciÃ³n habitual:** Horas (usualmente miles o millones de horas).
- **Ejemplo tÃ­pico:** 1 millÃ³n de horas (114 aÃ±os aprox.); aunque es un promedio teÃ³rico.

---

## ðŸŽ¯ **Medida mÃ¡s determinante**

- En bases de datos, el **tiempo de acceso (seek time)** suele ser la medida mÃ¡s crÃ­tica.
- Esto se debe a que las bases de datos suelen realizar muchas operaciones aleatorias pequeÃ±as en lugar de grandes transferencias secuenciales.

---

## ðŸ›— **Algoritmo del Ascensor (Elevator Algorithm)**

Es un algoritmo utilizado para optimizar el movimiento del cabezal en discos magnÃ©ticos, minimizando el tiempo de acceso total.

### ðŸ”¹ **Funcionamiento:**
- El cabezal se mueve en una direcciÃ³n (por ejemplo, hacia afuera), atendiendo todas las solicitudes en esa direcciÃ³n.
- Al alcanzar el extremo, cambia de direcciÃ³n y atiende las solicitudes que quedaron pendientes hacia el otro lado.
- Simula el movimiento de un ascensor real en un edificio.

### ðŸ”¹ **Ventaja:**
- Reduce considerablemente el movimiento del cabezal, mejorando la eficiencia.

---

## ðŸ“ˆ **MÃ©tricas principales asociadas al rendimiento del disco:**

| MÃ©trica             | ExplicaciÃ³n breve                          |
|---------------------|--------------------------------------------|
| **Tiempo de acceso**| Tiempo de mover cabezal al lugar correcto. |
| **Latencia rotacional**| Tiempo en girar sector hasta el cabezal.|
| **Tasa transferencia** | Datos transferidos por unidad de tiempo. |
| **MTBF**            | Fiabilidad, vida Ãºtil antes de fallos.     |

---

## ðŸ“Š **GrÃ¡fico Ilustrativo del Algoritmo del Ascensor:**

**Ejemplo prÃ¡ctico**:

Solicitudes a pistas: `40, 70, 35, 80, 20`

Pista actual del cabezal: `50`, DirecciÃ³n inicial: hacia arriba (nÃºmeros mayores)

```plaintext
DirecciÃ³n inicial â†’ hacia arriba
20 ----- 35 ----- [40] ----- [50] ----- [70] ----- [80]
                         â†‘ inicio aquÃ­

- Primero atiende: 70, 80
- Luego cambia direcciÃ³n y atiende: 40, 35, 20
```

### Comparativa rÃ¡pida:

| Sin algoritmo | Con algoritmo Ascensor |
|---------------|------------------------|
| 50â†’40â†’70â†’35â†’80â†’20 | 50â†’70â†’80â†’40â†’35â†’20 |
| Movimientos innecesarios grandes | Menos movimientos, optimizaciÃ³n notable |

---

## ðŸ§© **Ejercicios Resueltos:**

### âœ… **1. ExplicaciÃ³n detallada de medidas de rendimiento de discos magnÃ©ticos:**

| Medida             | Detalle y ejemplo tÃ­pico |
|--------------------|--------------------------|
| **Tiempo de acceso** | Movimiento del cabezal (Ej: 8 ms promedio) |
| **Latencia rotacional**| Velocidad del giro hasta sector (Ej: 4 ms para 7200 RPM) |
| **Tasa transferencia** | Velocidad de datos (Ej: 150 MB/s) |
| **MTBF**            | Vida Ãºtil promedio (Ej: 1 millÃ³n horas) |

---

### âœ… **2. Â¿CuÃ¡l serÃ­a la mÃ¡s determinante?**
- La mÃ¡s determinante: **Tiempo de acceso**.
- Es crÃ­tica para consultas pequeÃ±as y aleatorias frecuentes, habituales en SGBD.

---

### âœ… **3. Algoritmo del Ascensor y sus principales mÃ©tricas:**
- **ExplicaciÃ³n breve:**  
  Atender solicitudes moviendo el cabezal en una direcciÃ³n hasta terminar todas las solicitudes pendientes, luego cambiar de direcciÃ³n.
  
- **Principales mÃ©tricas asociadas:**  
  - ReducciÃ³n del **tiempo promedio de acceso**.
  - ReducciÃ³n del desgaste mecÃ¡nico por menos movimientos.

---

## ðŸ“Œ **Ejemplo numÃ©rico detallado del algoritmo del Ascensor:**

- Solicitudes: `[15, 10, 22, 4, 9, 30]`
- PosiciÃ³n inicial cabezal: `12`
- DirecciÃ³n inicial: Hacia arriba (hacia nÃºmeros mayores).

GrÃ¡fico ilustrativo del proceso:

```
Inicial: 12
DirecciÃ³n â†’ arriba:
12 â†’ 15 â†’ 22 â†’ 30  [ascendente finalizado]

Cambio de direcciÃ³n â† abajo:
30 â†’ 10 â†’ 9 â†’ 4    [descendente finalizado]

Orden Ã³ptimo final: [12 â†’ 15 â†’ 22 â†’ 30 â†’ 10 â†’ 9 â†’ 4]
```

---

## ðŸš¦ **ConclusiÃ³n clave del tema:**
- Las medidas mÃ¡s importantes son tiempo de acceso y latencia rotacional, cruciales para el rendimiento en bases de datos.
- El algoritmo del ascensor optimiza estos tiempos reduciendo movimientos innecesarios.


## 4. Niveles RAID

# ðŸ“€ **IntroducciÃ³n a RAID**

**RAID (Redundant Array of Independent Disks)** es una tecnologÃ­a que combina mÃºltiples discos fÃ­sicos en una sola unidad lÃ³gica para aumentar la **velocidades de acceso a datos**, proveer **redundancia** (seguridad ante fallos) o una combinaciÃ³n de ambos.

---

## ðŸ“Œ **Principales Niveles RAID (0, 1 y 5)**

### 1. ðŸ”¹ **RAID 0 (Stripe - Sin redundancia)**

- Divide datos en bloques distribuidos secuencialmente entre mÃºltiples discos.
- **Ventajas:**  
  - Excelente rendimiento en velocidad de lectura/escritura.
  - Aprovecha al mÃ¡ximo la capacidad total (sin redundancia).

- **Desventaja:**  
  - Alta vulnerabilidad; la falla de un solo disco implica pÃ©rdida total de los datos.

- **Uso tÃ­pico:**  
  EdiciÃ³n de video/audio, gaming, aplicaciones que requieren altas velocidades.

**Ejemplo grÃ¡fico RAID 0 (dos discos):**

```
Disco 1: Bloque 1 - Bloque 3 - Bloque 5
Disco 2: Bloque 2 - Bloque 4 - Bloque 6
```

---

### 2. ðŸ”¹ **RAID 1 (Mirroring - Redundancia exacta)**

- Duplica los datos exactamente en dos o mÃ¡s discos (espejo exacto).
- **Ventajas:**  
  - Muy seguro, resistente a fallos (puede fallar un disco sin pÃ©rdida de informaciÃ³n).
  - Alta disponibilidad.

- **Desventaja:**  
  - MÃ¡s caro, capacidad Ãºtil reducida a la mitad.
  - Velocidad de escritura ligeramente inferior debido a la duplicaciÃ³n.

- **Uso tÃ­pico:**  
  Servidores de datos crÃ­ticos, bases de datos pequeÃ±as donde la fiabilidad es primordial.

**Ejemplo grÃ¡fico RAID 1 (dos discos espejo):**

```
Disco 1: Bloque A - Bloque B - Bloque C
Disco 2: Bloque A - Bloque B - Bloque C (Copia exacta)
```

---

### 3. ðŸ”¹ **RAID 5 (Paridad Distribuida - Equilibrio)**

- Distribuye los datos en mÃºltiples discos, pero tambiÃ©n guarda informaciÃ³n de paridad (para recuperaciÃ³n de datos) de manera distribuida.
- **Ventajas:**  
  - Buen equilibrio rendimiento/seguridad.
  - Permite recuperaciÃ³n ante falla de un solo disco.
  - Uso eficiente del espacio (solo un disco de capacidad se utiliza para paridad).

- **Desventaja:**  
  - ReconstrucciÃ³n lenta en caso de fallo.
  - Complejidad mayor.

- **Uso tÃ­pico:**  
  Servidores empresariales y bases de datos de tamaÃ±o mediano/grande.

**Ejemplo grÃ¡fico RAID 5 (tres discos):**

```
Disco 1: Bloque 1 - Bloque 4 - Paridad (P3)
Disco 2: Bloque 2 - Paridad (P2) - Bloque 5
Disco 3: Paridad (P1) - Bloque 3 - Bloque 6
```

---

## ðŸ“Œ **RazÃ³n Principal para la ImplementaciÃ³n de RAID con Redundancia:**

La principal razÃ³n es **garantizar la disponibilidad y seguridad** de los datos ante fallos de discos fÃ­sicos. RAID proporciona mecanismos automÃ¡ticos de recuperaciÃ³n y tolerancia a fallos.

---

## ðŸš€ **Ventajas clave del almacenamiento RAID:**

### ðŸ”¹ **En rendimiento:**
- Lecturas simultÃ¡neas mÃ¡s rÃ¡pidas (RAID 0, 5).
- Mejora en velocidad al distribuir carga en varios discos.

### ðŸ”¹ **En fiabilidad:**
- Seguridad de datos mediante redundancia (RAID 1 y RAID 5).
- RecuperaciÃ³n rÃ¡pida en fallos parciales (RAID 1).
- Tolerancia efectiva a fallos sin interrupciÃ³n (RAID 1, RAID 5).

---

## ðŸ“Š **GrÃ¡fico comparativo rÃ¡pido de niveles RAID:**

| CaracterÃ­stica | RAID 0             | RAID 1               | RAID 5             |
|----------------|--------------------|----------------------|--------------------|
| Rendimiento    | âœ… Muy alto        | âš ï¸ Moderado-Alto     | âœ… Alto            |
| Redundancia    | âŒ No              | âœ… Completa (espejo) | âœ… SÃ­ (paridad)    |
| Capacidad Ãºtil | âœ… 100% capacidad  | âŒ 50% capacidad     | âš ï¸ ~80% capacidad  |
| Seguridad      | âŒ Ninguna         | âœ… Muy alta          | âœ… Alta            |
| Ejemplo uso    | EdiciÃ³n video      | Datos crÃ­ticos       | Servidores grandes |

---

## ðŸ§© **Ejercicios resueltos en detalle:**

### âœ… **1. ExplicaciÃ³n detallada niveles RAID 0, 1 y 5:**

- **RAID 0:** Divide datos en varios discos (sin redundancia).
- **RAID 1:** DuplicaciÃ³n exacta en discos mÃºltiples (mÃ¡xima seguridad).
- **RAID 5:** Distribuye paridad en discos, equilibrio rendimiento/seguridad.

---

### âœ… **2. RazÃ³n principal implementaciÃ³n redundancia:**

- Proteger informaciÃ³n frente a fallos inevitables del hardware.
- Mantener alta disponibilidad del sistema.

---

### âœ… **3. Ventajas en rendimiento y fiabilidad detallada (RAID 1 y RAID 5):**

#### ðŸ”¸ **RAID 1:**
- **Fiabilidad:** Alta (espejo exacto).
- **Rendimiento:** Moderado en escritura (copia), alto en lectura (varios discos disponibles).

#### ðŸ”¸ **RAID 5:**
- **Fiabilidad:** Alta (permite recuperaciÃ³n automÃ¡tica).
- **Rendimiento:** Alto en lectura (datos distribuidos), escritura moderada por cÃ¡lculo paridad.

---

## ðŸ–¥ï¸ **Ejemplos prÃ¡cticos detallados (RAID 1 y RAID 5):**

### RAID 1:
- Servidor bancario con datos financieros crÃ­ticos.
- Disco A falla â†’ Disco B mantiene copia exacta inmediata.

### RAID 5:
- Servidor web empresarial con bases de datos medianas.
- 4 discos de 1 TB â†’ 3 TB datos Ãºtiles, 1 TB paridad distribuida.
- Un disco falla â†’ sistema sigue funcionando; al reemplazar disco, sistema reconstruye datos desde paridad.

---

## ðŸŽ¨ **GrÃ¡fico resumen niveles RAID:**

```
                Rendimiento â†‘
Alta  | RAID 0
      |
      |                 RAID 5
      |                      â€¢ Equilibrio
Media |
      |            RAID 1
      |                      â€¢ Seguridad MÃ¡xima
Baja  +-----------------------------------â†’ Seguridad
     Baja             Media                Alta
```

---

## ðŸ“ **ConclusiÃ³n clave sobre niveles RAID:**

- **RAID 0**: MÃ¡ximo rendimiento sin seguridad.
- **RAID 1**: MÃ¡xima seguridad con costo adicional.
- **RAID 5**: Balance entre rendimiento, capacidad y seguridad.

**ImplementaciÃ³n recomendada segÃºn escenario:**
- **RAID 0:** EdiciÃ³n multimedia, aplicaciones rÃ¡pidas sin datos crÃ­ticos.
- **RAID 1:** InformaciÃ³n confidencial, alta disponibilidad.
- **RAID 5:** Bases de datos medianas/grandes, equilibrio Ã³ptimo rendimiento y seguridad.


## 5. Arboles B Bplus

# ðŸŒ³ **IntroducciÃ³n a Ãrboles B y B+**

Los **Ã¡rboles B y B+** son estructuras de datos **auto-balanceadas**, utilizadas para mantener grandes volÃºmenes de datos ordenados y permitir bÃºsquedas rÃ¡pidas, inserciones eficientes y eliminaciones Ã¡giles en bases de datos y sistemas de archivos.

---

## ðŸ“– **CaracterÃ­sticas fundamentales**

**Ãrbol B:**
- Nodos almacenan claves y referencias directas a datos.
- Cada nodo tiene mÃºltiples claves y mÃºltiples punteros.
- Balanceado: garantiza la misma distancia a cualquier hoja desde la raÃ­z.

**Ãrbol B+:**
- Variante del Ãrbol B, pero **almacena todos los datos Ãºnicamente en hojas**.
- Nodos internos almacenan Ãºnicamente claves para direccionar bÃºsquedas.
- Las hojas se enlazan en una lista, facilitando consultas secuenciales muy rÃ¡pidas.

---

## ðŸŽ¯ **Â¿Por quÃ© Ãrboles B y B+ son ideales para Ã­ndices ordenados?**

### 1. ðŸ”¹ **Acceso rÃ¡pido y eficiente:**
- Su altura se mantiene siempre baja (balanceada).
- Esto asegura bÃºsquedas eficientes en grandes volÃºmenes de datos: tÃ­picamente `O(log n)`.

### 2. ðŸ”¹ **Operaciones optimizadas:**
- Inserciones, bÃºsquedas y eliminaciones rÃ¡pidas sin necesidad de reorganizar toda la estructura.
- Excelente desempeÃ±o incluso con millones de registros.

### 3. ðŸ”¹ **Rendimiento estable:**
- Acceso garantizado en pocas operaciones debido al balance constante.
- Ideal para bases de datos donde el rendimiento predecible es crÃ­tico.

### 4. ðŸ”¹ **Soporte eficiente para rangos:**
- En Ãrboles B+, las hojas enlazadas permiten consultas por rango (como fechas o nÃºmeros consecutivos) extremadamente rÃ¡pidas.

---

## ðŸ“Š **Comparativa rÃ¡pida Ãrbol B vs. Ãrbol B+:**

| CaracterÃ­stica       | Ãrbol B                  | Ãrbol B+                      |
|----------------------|--------------------------|-------------------------------|
| Almacenamiento datos | Nodos internos y hojas   | Solo hojas                    |
| Uso ideal            | Ãndices generales        | Ãndices optimizados para rangos|
| Complejidad bÃºsquedas| `O(log n)`               | `O(log n)`                    |
| Consultas rango      | Moderado                 | Excelente (hojas enlazadas)   |

---

## ðŸŒ² **Ejemplo grÃ¡fico claro (Ãrbol B+):**

```plaintext
                   [30, 60]
                 /     |      \
          [10, 20]  [40, 50]  [70, 80, 90]
              â†˜ï¸Ž         â†˜ï¸Ž         â†˜ï¸Ž
            datos      datos       datos
```

- **RaÃ­z:** GuÃ­a bÃºsquedas rÃ¡pidamente.
- **Hojas enlazadas:** Facilitan consultas secuenciales por rangos (10â†’20â†’40â†’50â†’70â†’80â†’90).

---

## ðŸ“š **Ejemplo prÃ¡ctico concreto:**

- SupÃ³n que buscas `50`:
  - Paso 1: Empieza en raÃ­z `[30, 60]`, 50 estÃ¡ entre 30 y 60, vas al nodo medio `[40, 50]`.
  - Paso 2: Encuentras `50` inmediatamente en este nodo hoja.

- BÃºsqueda eficiente: Solo dos accesos incluso en grandes cantidades de datos.

---

## âœ… **Razones detalladas para usar Ãrboles B y B+ en Ã­ndices ordenados:**

| RazÃ³n principal | ExplicaciÃ³n |
|-----------------|-------------|
| Altura Balanceada | Siempre mÃ­nima altura (`O(log n)`), rÃ¡pido acceso. |
| Menos accesos a disco | Menos operaciones fÃ­sicas, mÃ¡s eficiencia. |
| InserciÃ³n y eliminaciÃ³n Ã¡gil | Cambios locales mÃ­nimos, no reorganizaciÃ³n global. |
| Ã“ptimo para rangos | Ãrbol B+ especialmente ideal por hojas enlazadas. |

---

## ðŸŽ¨ **GrÃ¡fico resumen ventajas Ãrbol B+ para Ã­ndices ordenados:**

```plaintext
              Acceso a disco
Muchos  | Sin Ã­ndice ordenado
        |
        | Ãrbol B
        |       â€¢ eficiente general
Pocos   | Ãrbol B+
        |       â€¢ excelente rango/orden
        +--------------------------------â†’ Velocidad consulta por rango
           Baja                 Alta
```

---

## ðŸ“ **ConclusiÃ³n clave sobre Ãrboles B y B+:**

- **Ãrbol B:** Indicado para Ã­ndices generales equilibrados.
- **Ãrbol B+:** MÃ¡s usado en bases de datos modernas por su eficiencia adicional en consultas por rangos, gracias a hojas enlazadas y almacenamiento exclusivo de datos en hojas.

La estructura balanceada, velocidad de acceso garantizada y facilidad para realizar consultas secuenciales hacen de los Ãrboles B y especialmente B+, la mejor elecciÃ³n para implementar Ã­ndices ordenados en bases de datos modernas.


## 6. Algoritmos Busqueda

# ðŸ”Ž **IntroducciÃ³n a Algoritmos de BÃºsqueda**

Los algoritmos de bÃºsqueda determinan cÃ³mo se accede a los datos almacenados, siendo esenciales para el rendimiento de un Sistema Gestor de Bases de Datos (SGBD).

---

## âŒ› **Costos AsintÃ³ticos en Algoritmos**

La notaciÃ³n asintÃ³tica describe cÃ³mo se comporta un algoritmo a medida que crece el volumen de datos (`n`).

- **O(1)**: Tiempo constante (independiente del tamaÃ±o).
- **O(log n)**: LogarÃ­tmico (muy eficiente, aumenta lentamente).
- **O(n)**: Lineal (tiempo crece proporcionalmente al tamaÃ±o).

---

# ðŸ“š **AnÃ¡lisis de los Algoritmos Solicitados**

## ðŸ“ **(1) ProgramaciÃ³n DinÃ¡mica: (EvaluaciÃ³n de Ã¡rboles)**

### ðŸ”¸ (a) Sin optimizaciÃ³n (evaluaciÃ³n de Ã¡rboles completos):

- **Tiempo:** Exponencial `O(2^n)` en Ã¡rboles binarios.
- **Espacio:** `O(n)` por pila de llamadas recursivas.

**RazÃ³n:**  
EvalÃºa mÃºltiples veces las mismas subexpresiones, resultando en redundancia y mucho tiempo de cÃ³mputo.

### ðŸ”¸ (b) Con optimizaciÃ³n (MemoizaciÃ³n - ProgramaciÃ³n DinÃ¡mica):

- **Tiempo:** PolinÃ³mico `O(n^2)` o mejor, dependiendo del problema.
- **Espacio:** `O(n^2)` por almacenamiento en tablas (generalmente matrices).

**RazÃ³n:**  
Almacenamiento intermedio evita cÃ¡lculos repetidos (memoizaciÃ³n), reduciendo enormemente el tiempo a cambio de memoria adicional.

---

## ðŸ“ **(2) Algoritmos de SelecciÃ³n en SGBD (CondiciÃ³n Igualdad):**

### ðŸ”¸ **(a) BÃºsqueda Lineal:**

- **Uso:** Tabla sin orden ni Ã­ndice.
- **Costo:** `O(n)`
- Ejemplo:  
  Buscar cliente por nombre en tabla pequeÃ±a sin Ã­ndice.

---

### ðŸ”¸ **(b) BÃºsqueda Binaria:**

- **Uso:** Tabla ordenada fÃ­sicamente sin Ã­ndice.
- **Costo:** `O(log n)`
- Ejemplo:  
  Buscar fecha especÃ­fica en historial de eventos ordenados.

---

### ðŸ”¸ **(c) Ãndice Primario (clave):**

- **Uso:** Ãndice sobre atributo clave primaria con estructura tipo hash.
- **Costo:** `O(1)` idealmente (acceso directo hash) o `O(log n)` si es Ã¡rbol B+.
- Ejemplo:  
  Buscar usuario por ID Ãºnico usando Ã­ndice hash.

> Nota: El coste tÃ­pico realista en Ã­ndices primarios en bases de datos es generalmente **O(log n)** (Ã¡rboles B+), aunque un Ã­ndice hash idealizado serÃ­a **O(1)**.

---

### ðŸ”¸ **(d) Ãndice Secundario (no clave):**

- **Uso:** Ãndice sobre atributo no clave.
- **Costo:** Generalmente `O(log n)`.
- Ejemplo:  
  Buscar clientes por ciudad usando un Ã­ndice secundario.

---

# ðŸ“‰ **GrÃ¡fico comparativo claro:**

```plaintext
Eficiencia de bÃºsquedas segÃºn estructura:

Alto coste (lento)   Lineal â†’ O(n)
                          |
                          |
                          â†“
                    Binaria â†’ O(log n)
                          |
                          â†“
                    Ãndice secundario â†’ O(log n)
                          |
                          â†“
Bajo coste (rÃ¡pido) Ãndice primario â†’ O(1)/O(log n)
```

---

# ðŸ” **Tema 7: Ejemplos hipotÃ©ticos (cuatro casos con diferentes costes):**

### ðŸ“Œ **Caso 1: Tabla pequeÃ±a, sin Ã­ndice**

```sql
SELECT * FROM Clientes WHERE Nombre = 'Laura';
```
- **Algoritmo:** Lineal.
- **Costo:** `O(n)`.

---

### ðŸ“Œ **Caso 2: Tabla ordenada fÃ­sicamente por fecha**

```sql
SELECT * FROM Pedidos WHERE Fecha = '2024-03-24';
```
- **Algoritmo:** BÃºsqueda Binaria.
- **Costo:** `O(log n)`.

---

### ðŸ“Œ **Caso 3: Tabla con Ã­ndice primario (hash) por ID**

```sql
SELECT * FROM Usuarios WHERE ID = 12345;
```
- **Algoritmo:** Ãndice primario (hash o Ã¡rbol B+).
- **Costo:** `O(1)` (ideal hash), en la prÃ¡ctica `O(log n)` (Ã¡rbol B+).

---

### ðŸ“Œ **Caso 4: Tabla con Ã­ndice secundario (Ã¡rbol B+)**

```sql
SELECT * FROM Productos WHERE CategorÃ­a = 'ElectrÃ³nica';
```
- **Algoritmo:** Ãndice secundario (Ã¡rbol B+).
- **Costo:** `O(log n)` en Ã­ndice, aunque luego recupera mÃºltiples registros relacionados (coste adicional).

---

# âœ… **Resumen grÃ¡fico prÃ¡ctico de casos hipotÃ©ticos:**

| Caso | Estructura tabla                 | Ãndice         | Algoritmo usado | Costo teÃ³rico |
|------|----------------------------------|----------------|-----------------|---------------|
| 1    | PequeÃ±a, no ordenada             | Ninguno        | Lineal          | `O(n)`        |
| 2    | Orden fÃ­sico (fecha)             | Ninguno        | Binaria         | `O(log n)`    |
| 3    | Clave primaria con Ã­ndice        | Primario (hash)| Ãndice primario | `O(1)` ideal  |
| 4    | Ãndice secundario por atributo   | Secundario B+  | Ãndice secundario| `O(log n)`   |

---

## ðŸ“Œ **Conclusiones clave del tema Algoritmos de BÃºsqueda:**

- La elecciÃ³n del algoritmo depende de la estructura fÃ­sica y lÃ³gica del almacenamiento (tabla ordenada, existencia de Ã­ndice).
- BÃºsquedas lineales son lentas, pero simples; Ã­ndices primarios son extremadamente rÃ¡pidos.
- Ãndices secundarios permiten bÃºsquedas rÃ¡pidas, aunque recuperan mÃºltiples registros potencialmente.

---

## ðŸŽ¯ **Consejos prÃ¡cticos finales para mejorar rendimiento:**

- **Usar Ã­ndices** siempre que las consultas sean frecuentes y relevantes.
- **Considerar el balance costo-beneficio** al agregar Ã­ndices secundarios (ralentizan inserciones y actualizaciones, pero aceleran consultas).
- **Evaluar necesidades reales** para decidir usar hashing vs. Ã¡rboles B+ (hash muy rÃ¡pido para igualdad exacta, B+ para rangos o mÃºltiples registros).


## 7. Procesamiento Consultas


# ðŸ—ƒï¸ **Procesamiento de Consultas en SGBD**

El procesamiento de consultas se refiere a cÃ³mo un Sistema Gestor de Bases de Datos interpreta, optimiza y ejecuta las consultas SQL recibidas por parte del usuario, transformÃ¡ndolas en resultados concretos.

---

## ðŸ“Œ **Pasos LÃ³gicos del Procesamiento de Consultas**

El procesamiento de consultas tiene tres fases clave:

### 1ï¸âƒ£ **AnÃ¡lisis**
- Verifica la sintaxis y la semÃ¡ntica.
- Traduce la consulta a una forma intermedia (Ã¡lgebra relacional).

### 2ï¸âƒ£ **OptimizaciÃ³n**
- Selecciona el mejor plan de ejecuciÃ³n.
- EvalÃºa diferentes alternativas considerando Ã­ndices, estadÃ­sticas, costo de acceso a disco, y tiempos estimados.

### 3ï¸âƒ£ **EvaluaciÃ³n**
- Ejecuta el plan optimizado.
- Recupera datos usando estrategias como **materializaciÃ³n** (guardar resultados intermedios) o **pipelining** (transferencia directa de resultados).

---

## ðŸ“ **Diagrama del Procesamiento de Consultas (completo y explicado)**

```
                  Consulta SQL
                       â”‚
                       â–¼
             â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
             â”‚   AnÃ¡lisis        â”‚
             â”‚ (Sintaxis y       â”‚
             â”‚  TraducciÃ³n a     â”‚
             â”‚  Ã¡lgebra rel.)    â”‚
             â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                       â”‚
                       â–¼
             â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
             â”‚   OptimizaciÃ³n    â”‚
             â”‚  (Genera y elige  â”‚
             â”‚   mejor plan)     â”‚
             â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                       â”‚
                       â–¼
             â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
             â”‚    EvaluaciÃ³n     â”‚
             â”‚(Ejecuta el plan   â”‚
             â”‚optimizado y       â”‚
             â”‚obtiene resultados)â”‚
             â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                       â”‚
                       â–¼
                 Resultado final
```

---

## ðŸ“š **TraducciÃ³n a Ãlgebra Relacional (Tema 4)**

### ðŸ”¹ **Consulta original:**

```sql
SELECT e.LNAME 
FROM EMPLEADO e 
JOIN TRABAJA_EN te ON te.EMPLEADO = e.ID 
JOIN PROYECTO p ON p.ID = te.PROYECTO 
WHERE p.NOMBRE = 'AQUARIUS' AND e.FECHA_NAC >= '2000-01-01'
```

### ðŸ”¹ **TraducciÃ³n inicial (sin optimizar):**

```
Ï€_LNAME (
    Ïƒ_(NOMBRE='AQUARIUS' âˆ§ FECHA_NAC â‰¥ '2000-01-01') (
        EMPLEADO â¨_(EMPLEADO.ID=TRABAJA_EN.EMPLEADO) TRABAJA_EN 
        â¨_(TRABAJA_EN.PROYECTO=PROYECTO.ID) PROYECTO
    )
)
```

---

### ðŸ”¹ **OptimizaciÃ³n de la consulta (2 casos)**

**Caso 1: Empujar selecciones (optimizaciÃ³n clÃ¡sica):**

```
Ï€_LNAME (
    (Ïƒ_FECHA_NAC â‰¥ '2000-01-01'(EMPLEADO)) 
    â¨ TRABAJA_EN 
    â¨ (Ïƒ_NOMBRE='AQUARIUS'(PROYECTO))
)
```

- Reduce datos antes de realizar JOIN â†’ Mejora rendimiento notablemente.

**Caso 2: Cambiar orden de JOIN (optimizaciÃ³n segÃºn tamaÃ±o tablas):**

```
Ï€_LNAME (
    (Ïƒ_NOMBRE='AQUARIUS'(PROYECTO) â¨ TRABAJA_EN) 
    â¨ Ïƒ_FECHA_NAC â‰¥ '2000-01-01'(EMPLEADO)
)
```

- Empieza desde la tabla mÃ¡s pequeÃ±a (PROYECTO con filtro) para minimizar coste.

---

## ðŸ”— **EvaluaciÃ³n consulta JOIN con Bucle Anidado por Bloques (Tema 8)**

### ðŸ”¹ **Contexto del ejemplo prÃ¡ctico:**

- Consulta JOIN: `SELECT * FROM A JOIN B ON A.a = B.b`
- Tabla A: 20 bloques, Tabla B: 15 bloques, 10 bloques libres en memoria.

### ðŸ”¹ **Algoritmo Bucle Anidado por Bloques (Block Nested Loop Join)**:

**FÃ³rmula del coste (I/O):**
```
Coste = Bloques_A + (Bloques_A / (Bloques_memoria - 2)) * Bloques_B
```

- *(Bloques_memoria - 2)* porque uno se reserva para salida y otro para bloque actual.

### ðŸ”¹ **CÃ¡lculo detallado del coste:**

```
Bloques_A = 20, Bloques_B = 15, Bloques_memoria = 10

Coste = 20 + (20 / (10 - 2)) * 15
      = 20 + (20 / 8) * 15
      = 20 + 2.5 * 15
      = 20 + 37.5
      = 57.5 â‰ˆ 58 bloques de coste total
```

---

### ðŸ”¹ **LRU vs. MRU (estrategia de reemplazo de bloques)**:

- **LRU (Least Recently Used):**
  - Descarta el bloque menos recientemente utilizado.
  - Generalmente eficiente (mÃ¡s aciertos en cachÃ©).

- **MRU (Most Recently Used):**
  - Descarta el bloque mÃ¡s recientemente utilizado.
  - Ãštil si acceso repetitivo no frecuente; en este caso, generalmente menos eficiente.

---

## ðŸ“‰ **GrÃ¡fico resumen claro sobre Procesamiento de Consultas:**

```
Consulta SQL â”€â”€â–º AnÃ¡lisis â”€â”€â–º OptimizaciÃ³n â”€â”€â–º EvaluaciÃ³n â”€â”€â–º Resultados

(AnÃ¡lisis)        (OptimizaciÃ³n)                 (EvaluaciÃ³n)
â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€      â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€              â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
â€¢ Sintaxis       â€¢ Elegir mejor plan           â€¢ MaterializaciÃ³n
â€¢ SemÃ¡ntica      â€¢ Orden JOINs                 â€¢ Pipelining
â€¢ Ãlgebra        â€¢ Ãndices disponibles         â€¢ Acceso a disco
```

---

## ðŸ“Œ **Ejemplo hipotÃ©tico visual claro:**

- Consulta: 
```sql
SELECT Nombre FROM Estudiantes WHERE Edad >= 20
```

**Fases:**
- AnÃ¡lisis: Sintaxis OK â†’ Ãlgebra: Ïƒ_Edadâ‰¥20(Estudiantes)
- OptimizaciÃ³n: Ãndice sobre Edad disponible â†’ usa Ã­ndice.
- EvaluaciÃ³n: Recupera rÃ¡pidamente datos por Ã­ndice â†’ entrega resultados.

---

## âœ… **ConclusiÃ³n clave sobre Procesamiento de Consultas:**

- **AnÃ¡lisis:** TraducciÃ³n precisa y sintaxis correcta son clave.
- **OptimizaciÃ³n:** Crucial para eficiencia, especialmente en JOINs complejos.
- **EvaluaciÃ³n:** Depende de estrategias eficientes (materializaciÃ³n vs pipelining).

Una buena optimizaciÃ³n puede cambiar radicalmente el rendimiento de consultas, especialmente en grandes bases de datos.


## 8. Modelado Multidimensional

# ðŸ“Š **IntroducciÃ³n al Modelado Multidimensional**

El **Modelado Multidimensional** es una tÃ©cnica usada en sistemas de anÃ¡lisis de datos (OLAP) para representar grandes volÃºmenes de informaciÃ³n desde diferentes perspectivas (dimensiones), facilitando anÃ¡lisis efectivos y toma de decisiones.

---

## ðŸ“Œ **Conceptos Clave:**

### ðŸ”¹ **Tablas de Dimensiones:**
- Representan **caracterÃ­sticas o atributos** de los datos.
- Permiten "cortar" y filtrar los datos desde diferentes Ã¡ngulos.

**Ejemplos:**
- **Clientes:** Nombre, ciudad, paÃ­s.
- **Productos:** CategorÃ­a, marca, modelo.
- **Tiempo:** DÃ­a, mes, aÃ±o.

---

### ðŸ”¹ **Tablas de Hechos:**
- Contienen los **datos medibles**, generalmente numÃ©ricos.
- Vinculan las dimensiones con mÃ©tricas especÃ­ficas.

**Ejemplos:**
- **Ventas:** Cantidad vendida, ingresos generados.
- **Compras:** Total de compras, costos asociados.

---

### ðŸ”¹ **Medidas:**
- Son los valores numÃ©ricos especÃ­ficos dentro de tablas de hechos.
- Indican lo que realmente se estÃ¡ analizando.

**Ejemplos:**
- Cantidad de productos vendidos.
- Ventas totales en dÃ³lares.
- Cantidad de clientes nuevos por dÃ­a.

---

## ðŸ“ **Ejemplo GrÃ¡fico de un Esquema Estrella:**

```
           DIMENSIÃ“N CLIENTES
                   â”‚
                   â”‚
DIMENSIÃ“N TIEMPOâ”€â”€â”€â˜…â”€â”€â”€â”€DIMENSIÃ“N PRODUCTOS
                   â”‚
                   â”‚
           TABLA DE HECHOS (VENTAS)
                   â”‚
            (Medidas: Ventas, ingresos)
```

---

# ðŸ” **Diferencias entre OLTP y OLAP**

### ðŸ”¹ **OLTP (Online Transaction Processing):**
- Maneja **transacciones frecuentes** y operacionales.
- Transacciones rÃ¡pidas, pequeÃ±as y concurrentes.
- Ejemplos claros:  
  - Ventas en lÃ­nea (Amazon).  
  - Sistemas bancarios (transferencias).

### ðŸ”¹ **OLAP (Online Analytical Processing):**
- Orientado al **anÃ¡lisis y toma de decisiones**.
- Consultas complejas sobre grandes volÃºmenes de datos.
- Ejemplos claros:  
  - AnÃ¡lisis de ventas por regiÃ³n.  
  - Reportes financieros y planificaciÃ³n estratÃ©gica.

---

### ðŸ“ˆ **Comparativa rÃ¡pida OLTP vs. OLAP:**

| Aspecto           | OLTP                             | OLAP                            |
|-------------------|----------------------------------|---------------------------------|
| Uso               | Operaciones frecuentes           | AnÃ¡lisis y decisiones           |
| Transacciones     | Muchas, rÃ¡pidas, pequeÃ±as        | Menos frecuentes, muy grandes   |
| Consultas         | Simples, precisas                | Complejas, agregadas            |
| DiseÃ±o Modelo     | Normalizado                      | Multidimensional, desnormalizado|
| Ejemplo real      | Pagos online                     | Business Intelligence (BI)      |

---

## ðŸŽ² **Esquema Estrella vs. Cubos OLAP**

### ðŸ”¹ **Esquema Estrella:**
- Es un modelo de diseÃ±o fÃ­sico para **bases de datos relacionales** que facilita consultas rÃ¡pidas.
- Consiste en una tabla central de hechos y mÃºltiples tablas de dimensiones alrededor.
- Sencillo, eficiente en rendimiento de consultas rÃ¡pidas.

### ðŸ”¹ **Cubos OLAP:**
- RepresentaciÃ³n lÃ³gica **multidimensional**.
- Permite anÃ¡lisis interactivo ("slice & dice"), "drill-down" (detalle) y "roll-up" (agregado).
- No necesariamente fÃ­sico, generalmente lÃ³gico o conceptual.

---

### ðŸ“Œ **Consideraciones principales:**

| Aspecto        | Esquema Estrella                  | Cubos OLAP                          |
|----------------|-----------------------------------|-------------------------------------|
| Naturaleza     | FÃ­sica (tablas reales)            | LÃ³gica o conceptual (visualizaciÃ³n) |
| Almacenamiento | Bases de datos relacionales       | Sistemas OLAP                       |
| Uso            | Consultas rÃ¡pidas SQL             | AnÃ¡lisis interactivos, dinÃ¡micos    |
| Complejidad    | Baja                              | Alta (permite interacciÃ³n dinÃ¡mica) |

---

## ðŸŽ¯ **Ejemplos prÃ¡cticos del Modelo Multidimensional**

### ðŸ”¹ **Tabla de DimensiÃ³n (Clientes):**
| ID_Cliente | Nombre    | Ciudad    | PaÃ­s      |
|------------|-----------|-----------|-----------|
| 001        | Juan      | Madrid    | EspaÃ±a    |
| 002        | Laura     | AsunciÃ³n  | Paraguay  |

### ðŸ”¹ **Tabla de DimensiÃ³n (Productos):**
| ID_Producto | Nombre       | CategorÃ­a   |
|-------------|--------------|-------------|
| P001        | iPhone 15    | Smartphones |
| P002        | Lenovo Yoga  | Laptop      |

### ðŸ”¹ **Tabla de Hechos (Ventas):**
| ID_Cliente | ID_Producto | Fecha      | Cantidad | Ingresos |
|------------|-------------|------------|----------|----------|
| 001        | P001        | 2024-03-23 | 2        | $2000    |
| 002        | P002        | 2024-03-24 | 1        | $1200    |

---

## ðŸ“‰ **GrÃ¡fico resumen OLTP vs. OLAP:**

```
                Transacciones
Muchas â”‚ OLTP
       â”‚   â€¢ sistemas operativos
       â”‚   â€¢ bancos, ventas online
       â”‚
       â”‚
Pocas  â”‚            OLAP
       â”‚               â€¢ anÃ¡lisis profundo
       â”‚               â€¢ BI, planificaciÃ³n
       â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–º Complejidad Consultas
        Baja                 Alta
```

---

## ðŸ§© **Ejercicios resueltos claramente:**

### âœ… **(1) Tablas de Dimensiones, Hechos y Medidas:**
- **Dimensiones:** Atributos analÃ­ticos (Clientes, Productos, Tiempo).
- **Hechos:** Datos medibles (Ventas, ingresos).
- **Medidas:** Valores numÃ©ricos especÃ­ficos (Cantidad vendida, dinero generado).

---

### âœ… **(2) Diferencia entre OLTP y OLAP (tÃ©rminos propios con ejemplos):**
- **OLTP:** RÃ¡pido, pequeÃ±as operaciones frecuentes (Ej: Amazon, pagos).
- **OLAP:** AnÃ¡lisis, grandes operaciones complejas (Ej: Data Warehouse financiero).

---

### âœ… **(3) Diferencia entre esquema estrella y cubos OLAP:**
- **Esquema estrella:** FÃ­sico, rÃ¡pido para consultas especÃ­ficas SQL.
- **Cubos OLAP:** LÃ³gico, dinÃ¡mico para anÃ¡lisis interactivo y multidimensional.

---

## ðŸ”‘ **Conclusiones claves sobre Modelado Multidimensional:**
- Esencial para **Business Intelligence** (BI).
- Tablas de dimensiÃ³n dan contexto; hechos proporcionan mediciones numÃ©ricas.
- OLTP es operativo y rÃ¡pido; OLAP analÃ­tico y profundo.
- Esquema estrella facilita rapidez fÃ­sica; cubos OLAP permiten anÃ¡lisis interactivo lÃ³gico.


## 9. Transacciones ACID

# ðŸ” **IntroducciÃ³n a Transacciones (SGBD)**

Una **transacciÃ³n** en un Sistema Gestor de Bases de Datos (SGBD) es una unidad lÃ³gica que agrupa operaciones que se ejecutan de manera indivisible, asegurando que todas las operaciones dentro se completen correctamente o ninguna lo haga, garantizando la consistencia del sistema.

**Ejemplo sencillo:**  
Transferir dinero de la cuenta A a la cuenta B es una sola transacciÃ³n que incluye:

1. Restar dinero en cuenta A
2. Sumar dinero en cuenta B

Ambas deben completarse exitosamente o ninguna debe ejecutarse.

---

## ðŸ”„ **Fases del Ciclo de Vida de una TransacciÃ³n**

Una transacciÃ³n atraviesa claramente 5 fases:

### 1ï¸âƒ£ **Inicio (Begin)**
- La transacciÃ³n comienza formalmente.

### 2ï¸âƒ£ **EjecuciÃ³n (Execution)**
- Realiza las operaciones (INSERT, UPDATE, DELETE, SELECT).

### 3ï¸âƒ£ **ValidaciÃ³n (Validation)**
- Verifica si las operaciones pueden completarse (restricciones, bloqueos).

### 4ï¸âƒ£ **ConfirmaciÃ³n (Commit)**
- Guarda permanentemente cambios realizados en la base de datos.

### 5ï¸âƒ£ **CancelaciÃ³n (Rollback, si aplica)**
- Si algo falla, revierte todas las operaciones realizadas hasta el momento del fallo, volviendo al estado inicial.

---

## ðŸ“Œ **Propiedades ACID**

Estas propiedades garantizan la confiabilidad en un entorno transaccional:

| Propiedad    | DefiniciÃ³n breve |
|--------------|------------------|
| **Atomicidad**    | Todo o nada. La transacciÃ³n ocurre completamente o no ocurre. |
| **Consistencia**  | La base de datos pasa de un estado vÃ¡lido a otro estado vÃ¡lido. |
| **Aislamiento**   | Cada transacciÃ³n se ejecuta independientemente sin interferir con otras transacciones simultÃ¡neas. |
| **Durabilidad**   | Cambios confirmados permanecen permanentes aun ante fallos del sistema.|

---

## ðŸ“š **ExplicaciÃ³n detallada Propiedades ACID (estÃ¡ndar SQL)**

### ðŸ”¹ **Atomicidad (Atomicity):**
- Operaciones dentro de la transacciÃ³n son indivisibles.
- **Ejemplo:**  
  Si falla un paso de la transferencia bancaria, ambas cuentas permanecen intactas.

### ðŸ”¹ **Consistencia (Consistency):**
- La base de datos siempre permanece en un estado vÃ¡lido antes y despuÃ©s de la transacciÃ³n.
- **Ejemplo:**  
  No permitir saldo negativo tras transferencia bancaria.

### ðŸ”¹ **Aislamiento (Isolation):**
- Transacciones concurrentes no interfieren entre sÃ­.
- **Ejemplo:**  
  Dos transferencias simultÃ¡neas no causan inconsistencias en los saldos.

### ðŸ”¹ **Durabilidad (Durability):**
- Los cambios realizados son permanentes una vez confirmados (commit).
- **Ejemplo:**  
  Tras una transferencia exitosa, el saldo se mantiene actualizado incluso si ocurre un corte de energÃ­a.

---

## ðŸ“ˆ **GrÃ¡fico claro del Ciclo de Vida de una TransacciÃ³n:**

```
           TransacciÃ³n iniciada
                  â”‚
                  â–¼
           â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
           â”‚  EjecuciÃ³n  â”‚â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
           â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜         â”‚
                  â”‚                â”‚
                  â–¼                â–¼
           â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”   â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
           â”‚ ValidaciÃ³n  â”‚â”€â”€â”€â”‚ CancelaciÃ³n â”‚ (Rollback)
           â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜   â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                  â”‚
                  â–¼
           â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
           â”‚ConfirmaciÃ³n â”‚ (Commit)
           â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                  â”‚
                  â–¼
             Cambios permanentes
```

---

## ðŸ§© **Ejercicios Resueltos en detalle:**

### âœ… **(a) DefiniciÃ³n concreta de transacciÃ³n:**

- Es un conjunto lÃ³gico indivisible de operaciones en bases de datos.
- Todas se ejecutan exitosamente o todas fallan, asegurando integridad.

---

### âœ… **(b) Ciclo de vida detallado:**

- **Inicio:** Comienzo formal.
- **EjecuciÃ³n:** RealizaciÃ³n de operaciones.
- **ValidaciÃ³n:** Chequeo restricciones y bloqueos.
- **Commit:** ConfirmaciÃ³n final.
- **Rollback:** AnulaciÃ³n de operaciones si algo falla.

---

### âœ… **(c) Propiedades ACID definidas claramente:**

- **Atomicidad:** Todo o nada.
- **Consistencia:** Estado vÃ¡lido siempre.
- **Aislamiento:** Independencia entre transacciones simultÃ¡neas.
- **Durabilidad:** Permanencia de los cambios tras confirmaciÃ³n.

---

## ðŸ”‘ **Ejemplo prÃ¡ctico completo con propiedades ACID:**

### ðŸ”¹ **Caso prÃ¡ctico: Transferencia Bancaria (TransacciÃ³n T)**

- Estado inicial:
  - Cuenta A: 500 USD
  - Cuenta B: 300 USD

- Operaciones de la transacciÃ³n:
  1. Cuenta A â†’ -100 USD  
  2. Cuenta B â†’ +100 USD  

- Estado final (esperado si Commit):
  - Cuenta A: 400 USD
  - Cuenta B: 400 USD

### ðŸ”¹ **ValidaciÃ³n de propiedades ACID:**

| Propiedad     | ExplicaciÃ³n en ejemplo bancario |
|---------------|---------------------------------|
| Atomicidad    | Ambas cuentas cambian juntas o ninguna cambia.|
| Consistencia  | Saldos siempre coherentes, no negativos.|
| Aislamiento   | Otra transacciÃ³n simultÃ¡nea no afecta esta operaciÃ³n.|
| Durabilidad   | Una vez completada, transferencias permanecen aÃºn con fallos del sistema.|

---

## ðŸ“‰ **GrÃ¡fico resumen propiedades ACID:**

```
         Estado inicial vÃ¡lido
                  â”‚
Atomicidad        â”‚ TransacciÃ³n â”€â”€â”€â”€ (Si falla) â”€â”€â”€â–º Estado inicial
                  â–¼
Consistencia â”€â”€ Estado vÃ¡lido intermedio
                  â”‚
Aislamiento       â”‚ (Sin interferencia externa)
                  â–¼
Durabilidad â”€â”€ Estado final vÃ¡lido y permanente tras commit
```

---

## ðŸŽ¯ **ConclusiÃ³n clave del tema Transacciones y ACID:**

- Las **transacciones** garantizan integridad y coherencia.
- Las propiedades **ACID** (Atomicidad, Consistencia, Aislamiento y Durabilidad) son esenciales para mantener la fiabilidad del sistema.
- Sin estas propiedades, los datos serÃ­an vulnerables a inconsistencia y corrupciÃ³n.

Una implementaciÃ³n adecuada del modelo ACID es crÃ­tica para aplicaciones empresariales, bancarias y cualquier sistema que maneje datos sensibles.


## 10. Concurrencia

# ðŸ”„ **IntroducciÃ³n a la Concurrencia**

La **concurrencia** en bases de datos permite que mÃºltiples usuarios o aplicaciones interactÃºen simultÃ¡neamente con la base de datos, lo que genera eficiencia pero puede producir conflictos si no se gestiona correctamente.

---

## ðŸ“Œ **(a) FunciÃ³n del Componente de GestiÃ³n de Concurrencia en un SGBD**

El **Gestor de Concurrencia** asegura que las transacciones simultÃ¡neas no interfieran negativamente entre sÃ­, manteniendo la integridad y consistencia de los datos.  

**Funciones principales:**
- Controlar accesos simultÃ¡neos.
- Evitar conflictos en escrituras/lecturas simultÃ¡neas.
- Asegurar aislamiento entre transacciones.

---

## ðŸ“ **(b) Estructura de Datos para GestiÃ³n y ConcesiÃ³n de Bloqueos**

El sistema utiliza una estructura llamada **Tabla de Bloqueos**:

| Recurso (Dato) | Estado Bloqueo | TransacciÃ³n(es) que bloquean | Cola de Espera |
|----------------|----------------|-------------------------------|----------------|
| Registro A     | Exclusivo (X)  | T1                            | T2, T3         |
| Registro B     | Compartido (S) | T2, T4                        | T5             |

- **Bloqueo Exclusivo (X):** Para escrituras (una sola transacciÃ³n).
- **Bloqueo Compartido (S):** Para lecturas simultÃ¡neas (mÃºltiples transacciones).

---

## ðŸ”’ **(a) Protocolo de Bloqueo de 2 Fases (2PL - Two Phase Locking)**

Garantiza la **serializabilidad**, asegurando una ejecuciÃ³n concurrente equivalente a una secuencial.

### ðŸ”¹ **Fases del Protocolo 2PL:**
- **Fase 1 (Creciente):** Adquiere bloqueos necesarios; no libera ninguno.
- **Fase 2 (Decreciente):** Libera bloqueos; no adquiere nuevos bloqueos.

**Ejemplo grÃ¡fico:**
```
Tiempo â–º
T1: â”‚â”€â”€â”€ Adquiere Bloqueos â”€â”€â”€â”‚â”€â”€ Libera Bloqueos â”€â”€â”‚
    â–²                        â–²
Fase creciente          Fase decreciente
```

---

## ðŸ“‘ **(b) Variantes del Protocolo 2PL**

- **2PL BÃ¡sico:** Adquiere y libera bloqueos en dos fases estrictas.
- **2PL Estricto (Strict 2PL):** Libera bloqueos exclusivos (X) Ãºnicamente al terminar (Commit/Rollback).
- **2PL Riguroso (Rigorous 2PL):** Libera todos los bloqueos (S/X) sÃ³lo al finalizar (mÃ¡s restrictivo, mÃ¡s seguro).

---

## ðŸ“– **Tema 5: Conceptos de Control de Concurrencia**

### ðŸ”¹ **PlanificaciÃ³n (Schedule):**
- Orden especÃ­fico en que operaciones de mÃºltiples transacciones se ejecutan simultÃ¡neamente.

**Ejemplo:**
```
T1: Leer(A), Escribir(A)
T2: Leer(A), Escribir(A)
```

Una planificaciÃ³n posible:
```
Leer(A)T1 â†’ Leer(A)T2 â†’ Escribir(A)T1 â†’ Escribir(A)T2
```

---

### ðŸ”¹ **PlanificaciÃ³n Secuencial (Serial Schedule):**
- Las transacciones se ejecutan estrictamente una tras otra, sin simultaneidad.

**Ejemplo:**
```
(T1 completa) â†’ (T2 completa) â†’ (T3 completa)
```

---

### ðŸ”¹ **PlanificaciÃ³n Secuenciable (Serializable Schedule):**
- EjecuciÃ³n concurrente equivalente lÃ³gicamente a alguna planificaciÃ³n secuencial.

**Ejemplo:**
```
Leer(A)T1 â†’ Escribir(A)T1 â†’ Leer(B)T2 â†’ Escribir(B)T2
```

Aunque hay concurrencia, la planificaciÃ³n es equivalente a T1â†’T2 o T2â†’T1.

---

### ðŸ”¹ **Secuencialidad en Cuanto a Conflicto (Conflict Serializability):**
- Las operaciones conflictivas (lectura/escritura sobre el mismo recurso) siguen un orden estricto como en una planificaciÃ³n secuencial.

---

### ðŸ”¹ **Secuencialidad en Cuanto a Vistas (View Serializability):**
- Equivalencia lÃ³gica en tÃ©rminos de valores leÃ­dos y escritos, aunque el orden de operaciones pueda diferir levemente.

---

## ðŸ“ˆ **Importancia de la Secuencialidad (Serializabilidad)**

La serializabilidad es crÃ­tica porque asegura la **consistencia y correcciÃ³n** de la base de datos en ambientes concurrentes. Si las planificaciones no son serializables, pueden generarse inconsistencias en los datos.

---

## ðŸ§© **Ejercicios resueltos concretamente:**

### âœ… **(a) FunciÃ³n de GestiÃ³n Concurrencia en SGBD:**
- Garantiza que mÃºltiples usuarios trabajen simultÃ¡neamente sin conflictos.

---

### âœ… **(b) Estructura de datos para bloqueos:**
- **Tabla de bloqueos:** Registra recursos, bloqueos actuales y solicitudes en espera.

---

### âœ… **(a) Protocolo de 2 fases (2PL):**
- Dos fases claramente separadas: adquisiciÃ³n (creciente) y liberaciÃ³n (decreciente).

---

### âœ… **(b) Variantes protocolo 2PL:**
- **2PL bÃ¡sico, Estricto (strict) y Riguroso (rigorous)**.

---

### âœ… **ExplicaciÃ³n conceptos control concurrencia claramente:**

| Concepto                  | ExplicaciÃ³n simple                       |
|---------------------------|------------------------------------------|
| PlanificaciÃ³n             | Orden ejecuciÃ³n operaciones.             |
| PlanificaciÃ³n secuencial  | Transacciones una tras otra (sin concurrencia). |
| PlanificaciÃ³n secuenciable| Concurrencia, pero equivalente a secuencial.|
| Secuencialidad conflicto  | Operaciones conflictivas ordenadas estrictamente.|
| Secuencialidad vistas     | Equivalencia lÃ³gica en resultados obtenidos.|

---

## ðŸ“Œ **GrÃ¡fico claro resumen conceptos concurrencia:**

```
PlanificaciÃ³n
     â”‚
     â”œâ”€â”€ Secuencial â”€â”€â”€â”€ Una tras otra (segura, sin conflictos)
     â”‚
     â””â”€â”€ Secuenciable â”€â”€ Concurrente, pero equivalente a secuencial
                  â”‚
                  â”œâ”€â”€ Conflicto â”€â”€ Operaciones conflictivas respetan orden
                  â”‚
                  â””â”€â”€ Vistas â”€â”€â”€â”€â”€ Equivalente en resultados leÃ­dos/escritos
```

---

## ðŸ“š **Ejemplo grÃ¡fico concreto protocolo 2PL:**

- **TransacciÃ³n bancaria T1 (transferencia dinero)**:
  1. Bloquea cuenta A (X)
  2. Bloquea cuenta B (X)
  3. Actualiza saldos
  4. Libera bloqueos (X)

- **Protocolo estricto (Strict 2PL)**:
  - Libera bloqueos solo al terminar la transacciÃ³n completamente (commit).

```
Tiempo â–º
T1 â”‚â”€ Bloquear A â”€ Bloquear B â”€â”€ Actualizar â”€â”€ Commit & Liberar â”€â”‚
```

---

## ðŸŽ¯ **ConclusiÃ³n clave sobre Concurrencia en SGBD:**

- Controlar concurrencia es vital para asegurar integridad.
- El protocolo 2PL asegura serializabilidad (orden lÃ³gico seguro).
- La planificaciÃ³n secuenciable garantiza que concurrencia sea tan segura como la ejecuciÃ³n secuencial estricta.

Un buen control de concurrencia evita pÃ©rdida de datos, conflictos y mantiene la coherencia en bases de datos crÃ­ticas.


## 11. Protocolos Distribuidos

# ðŸŒ **IntroducciÃ³n a Protocolos Distribuidos en SGBD**

Los **protocolos distribuidos** gestionan la **coordinaciÃ³n y concurrencia** en sistemas donde los datos estÃ¡n repartidos en mÃºltiples sitios geogrÃ¡ficamente distribuidos. Aseguran consistencia y disponibilidad.

---

# ðŸ—³ï¸ **(a) Protocolo de Control de Concurrencia por Quorum de Consenso**

Este protocolo garantiza coherencia distribuida usando **pesos** asignados a cada sitio.

### ðŸ”¹ **Conceptos bÃ¡sicos:**
- Cada sitio recibe un peso asignado.
- Para realizar **lectura o escritura**, la transacciÃ³n debe sumar un **quorum mÃ­nimo** de pesos.
- Generalmente, se asignan pesos segÃºn la importancia o disponibilidad de sitios.

---

## ðŸ“Œ **(b) Implicancias para definir valores de Quorum:**

- **Mayor quorum de lectura:**  
  Mayor consistencia, menor velocidad.
- **Mayor quorum de escritura:**  
  Mayor costo, mayor seguridad en escrituras.
- La suma de quorum de lectura (Q_L) y quorum de escritura (Q_E) debe ser mayor al total de pesos asignados para asegurar consistencia:
  
  ```
  Q_L + Q_E > Peso_Total
  ```

---

## ðŸ“š **(c) Valores para protocolos especÃ­ficos:**

### ðŸ”¹ **Protocolo de MayorÃ­a (Majority Protocol):**
- **CondiciÃ³n:** Quorum lectura + Quorum escritura > total de pesos.
- **Ejemplo claro:** Si total = 10,  
  - Lectura â‰¥ 6 y Escritura â‰¥ 5 (o viceversa).  
  (Ej.: Q_L=6, Q_E=5; 6+5=11>10).

### ðŸ”¹ **Protocolo Sesgado (Biased Protocol):**
- Un sitio especial tiene peso dominante (sesgado).
- **Ejemplo claro:** Si total = 10  
  - Sitio principal tiene peso=7; demÃ¡s sitios peso=1.  
  - Quorum lectura y escritura puede satisfacerse con sitio sesgado solo (Ej.: Q_L=7, Q_E=7).

---

# âœ… **(a) Protocolo de Commit en 2 Fases (2PC - Two Phase Commit)**

Permite coordinar confirmaciÃ³n de transacciones distribuidas asegurando consistencia.

### ðŸ”¹ **Fases del protocolo 2PC:**

- **Fase 1 (PreparaciÃ³n):**
  1. **Coordinador** envÃ­a `PREPARE` a todos los participantes.
  2. **Participantes** ejecutan operaciones localmente y responden:
     - `READY` (preparado) o
     - `ABORT` (cancelar).

- **Fase 2 (ConfirmaciÃ³n):**
  - Si TODOS los participantes respondieron `READY`, coordinador envÃ­a `COMMIT` para confirmar cambios.
  - Si UNO responde `ABORT`, envÃ­a `ABORT` a todos para revertir cambios.

---

## ðŸ“Œ **Ejemplo grÃ¡fico Protocolo 2PC:**

```
         Coordinador
             â”‚
Fase 1:      â”‚ PREPARE?
             â”‚â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–º Participante 1
             â”‚â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–º Participante 2
             â”‚â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–º Participante 3
             â”‚
             â”‚ READY â—„â”€â”€â”€ Participante 1
             â”‚ READY â—„â”€â”€â”€ Participante 2
             â”‚ READY â—„â”€â”€â”€ Participante 3
             â”‚
Fase 2:      â”‚ COMMIT
             â”‚â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–º Participantes (ConfirmaciÃ³n)
```

---

# ðŸš§ **(b) QuÃ© pasa si falla el Coordinador en 2PC?**

- Los participantes quedan "bloqueados" temporalmente sin instrucciones claras (estado incertidumbre).
- Deben esperar recuperaciÃ³n del coordinador o usar tÃ©cnicas alternativas (backup, tiempo de espera, etc.).

---

# ðŸš¨ **(c) QuÃ© pasa si un Participante falla en 2PC?**

- Si falla en fase preparaciÃ³n: Coordinador envÃ­a `ABORT` al resto.
- Si falla despuÃ©s de `READY` (en confirmaciÃ³n): 
  - Al recuperarse, debe consultar al coordinador para saber si debe COMMIT o ABORT (consulta estado).

---

## ðŸ“Š **GrÃ¡fico claro resumen fallos protocolo 2PC:**

```
Coordinador         Participantes
    â”‚                    â”‚
    â–¼                    â–¼
Falla:                Falla:
- Incertidumbre       - Antes READY: ABORT
participantes.        - Tras READY: RecuperaciÃ³n consultando coordinador.
```

---

## ðŸ§© **Ejercicios resueltos claramente:**

### âœ… **(a) Quorum Consenso explicado claramente:**
- Controla concurrencia mediante quorum mÃ­nimo (pesos de sitios) para lecturas/escrituras.

---

### âœ… **(b) Implicancias definir valores quorum:**
- Mayor quorum lectura â†’ mÃ¡s consistencia, menor rendimiento.
- Mayor quorum escritura â†’ seguridad escrituras, menor eficiencia.
- CondiciÃ³n clave: Q_L + Q_E > peso total.

---

### âœ… **(c) Valores quorum MayorÃ­a y Sesgado ejemplos concretos:**
- **MayorÃ­a:** (total=10): Q_L=6, Q_E=5 (6+5>10)
- **Sesgado:** sitio principal con peso dominante (peso=7; quorum=7).

---

### âœ… **(a) Pasos protocolo Commit 2 Fases (2PC):**
- **PreparaciÃ³n:** PREPARE â†’ participantes READY/ABORT
- **ConfirmaciÃ³n:** COMMIT si todos READY; si no, ABORT.

---

### âœ… **(b) Falla coordinador (quÃ© hacen participantes?):**
- Estado incertidumbre (bloqueados). Esperan recuperaciÃ³n o consulta externa.

---

### âœ… **(c) Falla participante (quÃ© hace sitio?):**
- Antes READY: Coordinador aborta operaciÃ³n.
- DespuÃ©s READY: Participante recuperado consulta coordinador para resolver su estado (commit/abort).

---

## ðŸ”‘ **ConclusiÃ³n clave sobre Protocolos Distribuidos:**

- **Quorum de Consenso** garantiza concurrencia segura, sacrificando parcialmente velocidad por seguridad.
- **Protocolo Commit 2 Fases (2PC)** asegura consistencia distribuida mediante confirmaciÃ³n en fases, con riesgos claros si ocurre fallo coordinador o participante.

---

## ðŸŽ¯ **Resumen GrÃ¡fico Claro Protocolos Distribuidos:**

```
Protocolos Distribuidos â”€â”€â”€â–º CoordinaciÃ³n y Concurrencia Segura
          â”‚
          â”œâ”€â”€ Quorum Consenso â”€â”€â”€â–º Lectura/escritura por quorum
          â”‚        â”œâ”€ MayorÃ­a (lect+escr>total)
          â”‚        â””â”€ Sesgado (sitio dominante)
          â”‚
          â””â”€â”€ Commit 2 Fases â”€â”€â”€â”€â–º ConfirmaciÃ³n distribuida en fases
                   â”œâ”€ Fase preparaciÃ³n
                   â””â”€ Fase confirmaciÃ³n
```


## 12. Almacenamiento Distribuido

# ðŸŒ **IntroducciÃ³n al Almacenamiento Distribuido**

El **Almacenamiento Distribuido** se refiere a la forma en que los datos de una base de datos se almacenan y gestionan fÃ­sicamente en mÃºltiples sitios distribuidos, garantizando disponibilidad, rendimiento y seguridad.

---

## ðŸ“Œ **Formas Principales de Almacenamiento Distribuido**

Existen principalmente dos formas:

### ðŸ”¹ **1. ReplicaciÃ³n**
- Consiste en tener **copias exactas** de los mismos datos en diferentes sitios distribuidos.

**Ventajas:**
- Alta disponibilidad y fiabilidad.
- RÃ¡pido acceso local a datos comunes.

**Desventajas:**
- Costos mayores por almacenamiento redundante.
- Dificultad en mantener sincronizaciÃ³n constante.

**Ejemplo claro:**
- Datos de usuarios replicados en sitios distribuidos globalmente para acceso rÃ¡pido local.

---

### ðŸ”¹ **2. FragmentaciÃ³n**
Dividir los datos en partes mÃ¡s pequeÃ±as (**fragmentos**) almacenadas en diferentes sitios. Existen dos tipos:

#### (a) **FragmentaciÃ³n Horizontal**
- Divide filas de una tabla.
- Cada fragmento contiene un conjunto especÃ­fico de filas completas.

**Ejemplo:**
| Sitio   | Fragmento                           |
|---------|-------------------------------------|
| Europa  | Clientes europeos                   |
| AmÃ©rica | Clientes norteamericanos y latinos  |

#### (b) **FragmentaciÃ³n Vertical**
- Divide columnas de una tabla.
- Cada fragmento almacena un subconjunto de columnas en sitios diferentes.

**Ejemplo:**
| Sitio       | Fragmento                    |
|-------------|------------------------------|
| Finanzas    | Columnas (Salario, Cuentas)  |
| RRHH        | Columnas (Nombre, DirecciÃ³n) |

**Ventajas fragmentaciÃ³n:**
- Mejor rendimiento segÃºn necesidades locales.
- Menor cantidad de datos transmitidos en consultas especÃ­ficas.

**Desventajas fragmentaciÃ³n:**
- Mayor complejidad de gestiÃ³n.
- Consultas globales pueden ser lentas.

---

## ðŸ“¡ **Estrategia de SemireuniÃ³n (Semijoin)**

Es una estrategia que minimiza la transmisiÃ³n de datos en consultas distribuidas tipo JOIN. EnvÃ­a solo atributos necesarios para identificar filas relevantes.

### ðŸ”¹ **Pasos SemireuniÃ³n (si consulta recibida en sitio 1):**
- Consulta: `SELECT * FROM R JOIN S` (sitio 1 tiene tabla R, sitio 2 tabla S)

1. **Sitio 1** envÃ­a columna clave (join) de R al sitio 2.
2. **Sitio 2** calcula JOIN parcial usando claves recibidas.
3. **Sitio 2** devuelve al sitio 1 solo filas necesarias para completar JOIN final.
4. **Sitio 1** realiza JOIN final.

---

## ðŸ“Š **CÃ¡lculo detallado del coste transmisiÃ³n Semijoin**

SupÃ³n:
- Sitio 1: tabla R, 500 filas, claves 4 bytes.
- Sitio 2: tabla S, 1000 filas, 100 bytes/fila.

### ðŸ”¹ **CÃ¡lculo costes si consulta llega a sitio 1:**

| Paso | AcciÃ³n                                  | Coste transmisiÃ³n aproximado |
|------|-----------------------------------------|------------------------------|
| 1    | S1 envÃ­a claves R â†’ S2 (500 Ã— 4 bytes)  | **2000 bytes** (~2KB)        |
| 2    | S2 responde filas relevantes (200 filas Ã— 100 bytes)| **20000 bytes** (~20KB)|
|      | **Costo total aprox.:**                 | **22KB**                     |

---

### ðŸ”¹ **Si consulta llega a sitio 2 (invertido):**

| Paso | AcciÃ³n                                  | Coste transmisiÃ³n aproximado |
|------|-----------------------------------------|------------------------------|
| 1    | S2 envÃ­a claves S â†’ S1 (1000 Ã— 4 bytes) | **4000 bytes** (~4KB)        |
| 2    | S1 responde filas relevantes (300 filas Ã— 80 bytes)| **24000 bytes** (~24KB) |
|      | **Costo total aprox.:**                 | **28KB**                     |

---

## ðŸ“ˆ **Comparativa grÃ¡fica ReplicaciÃ³n vs. FragmentaciÃ³n**

```
                        ReplicaciÃ³n
               Alta â”‚  â€¢ disponibilidad mÃ¡xima
Disponibilidad     â”‚  â€¢ alto coste almacenamiento
                   â”‚
                   â”‚                 FragmentaciÃ³n
                   â”‚              â€¢ menos almacenamiento
               Bajaâ”‚              â€¢ mÃ¡s rendimiento local
                   â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–º Rendimiento local
                  Bajo                  Alto
```

---

## ðŸ§© **Ejercicios resueltos claramente:**

### âœ… **(1) Formas almacenamiento distribuido explicadas claramente:**
- **ReplicaciÃ³n:** Copias exactas en mÃºltiples sitios (alta disponibilidad).
- **FragmentaciÃ³n:** DivisiÃ³n horizontal o vertical segÃºn necesidad (rendimiento optimizado).

---

### âœ… **(2) Pasos claros y coste SemireuniÃ³n:**

**Ejemplo concreto (Consulta llega sitio 1):**

1. **Sitio 1 â†’ claves R â†’ Sitio 2**
2. **Sitio 2 â†’ filas relevantes â†’ Sitio 1**
3. **Sitio 1 completa JOIN**

**Coste aprox.:** ~22KB (menor que enviar tablas completas)

---

## ðŸ“Œ **Caso prÃ¡ctico especÃ­fico SemireuniÃ³n:**

- Consulta original: 
```sql
SELECT * FROM Clientes JOIN Compras ON Clientes.id = Compras.cliente_id
```

### ðŸ”¹ **Datos ejemplo:**
- Clientes (Sitio 1): 1000 filas, claves=4 bytes
- Compras (Sitio 2): 3000 filas, 50 bytes/fila

### ðŸ”¹ **Pasos Semijoin (consulta en Sitio 1):**
1. Sitio 1 envÃ­a claves Clientes (4KB aprox.) â†’ Sitio 2.
2. Sitio 2 devuelve filas coincidentes (ej: 500 filas Ã— 50 bytes = 25KB aprox.) â†’ Sitio 1.

### ðŸ”¹ **Coste total claro:** 
- Aproximadamente 29KB transmisiÃ³n (mucho menor que enviar toda tabla Compras â‰ˆ 150KB).

---

## ðŸ”‘ **Conclusiones clave Almacenamiento Distribuido:**

- **ReplicaciÃ³n**: Alta disponibilidad y redundancia, costo mayor.
- **FragmentaciÃ³n**: Optimiza rendimiento, menor almacenamiento, mayor complejidad.
- Estrategia de **SemireuniÃ³n** reduce significativamente costo transmisiÃ³n en JOINs distribuidos.

---

## ðŸŽ¯ **GrÃ¡fico resumen claro formas almacenamiento distribuido:**

```
Almacenamiento Distribuido
        â”‚
        â”œâ”€â”€ ReplicaciÃ³n â”€â”€â–º Alta disponibilidad
        â”‚       â””â”€ Copias exactas mÃºltiples sitios
        â”‚
        â””â”€â”€ FragmentaciÃ³n â”€â”€â–º OptimizaciÃ³n rendimiento
                â”œâ”€ Horizontal (filas)
                â””â”€ Vertical (columnas)
```

## 13. Optimizacion Consultas

# ðŸš€ **IntroducciÃ³n a la OptimizaciÃ³n de Consultas**

La **OptimizaciÃ³n de Consultas** es el proceso que usa un SGBD para transformar una consulta SQL escrita por el usuario en una versiÃ³n mÃ¡s eficiente en tÃ©rminos de rendimiento.

---

## ðŸ“ **Ãlgebra Relacional para OptimizaciÃ³n**

El SGBD transforma consultas SQL en **Ãlgebra Relacional**, que permite usar reglas matemÃ¡ticas para elegir el orden mÃ¡s eficiente de las operaciones.

### ðŸ”¹ **Operaciones bÃ¡sicas Ã¡lgebra relacional:**

- **Ïƒ (SelecciÃ³n):** Filtra filas.
- **Ï€ (ProyecciÃ³n):** Filtra columnas.
- **â¨ (Join):** Combina tablas.
- **Ã— (Producto cartesiano):** Combina cada fila de una tabla con cada fila de otra.

---

## ðŸ“š **Tema 4: TraducciÃ³n inicial y optimizaciÃ³n JOIN**

### ðŸ”¹ **Consulta original:**
```sql
SELECT e.LNAME 
FROM EMPLEADO e 
JOIN TRABAJA_EN te ON te.EMPLEADO = e.ID 
JOIN PROYECTO p ON p.ID = te.PROYECTO 
WHERE p.NOMBRE = 'AQUARIUS' AND e.FECHA_NAC >= '2000-01-01'
```

### ðŸ”¹ **TraducciÃ³n inicial (sin optimizar):**
```
Ï€_LNAME(
    Ïƒ_(NOMBRE='AQUARIUS' âˆ§ FECHA_NACâ‰¥'2000-01-01') (
        EMPLEADO â¨_(EMPLEADO.ID=te.EMPLEADO) TRABAJA_EN te
                 â¨_(te.PROYECTO=p.ID) PROYECTO p
    )
)
```

---

### ðŸ§© **OptimizaciÃ³n (2 casos prÃ¡cticos):**

#### **Caso 1: Empujar selecciones (Push selection)**

- Aplica primero selecciones para reducir el tamaÃ±o de tablas antes de JOIN.

```
Ï€_LNAME(
    (Ïƒ_FECHA_NACâ‰¥'2000-01-01'(EMPLEADO))
    â¨_(ID=EMPLEADO) TRABAJA_EN
    â¨_(PROYECTO=ID) (Ïƒ_NOMBRE='AQUARIUS'(PROYECTO))
)
```

- **Ventaja:** Menos datos al hacer JOINs, rendimiento notablemente mejorado.

---

#### **Caso 2: Cambiar orden JOIN segÃºn tamaÃ±o tablas (Join reordering)**

- Ordena JOINs comenzando por tablas pequeÃ±as para reducir el coste.

```
Ï€_LNAME(
    (Ïƒ_NOMBRE='AQUARIUS'(PROYECTO) â¨ TRABAJA_EN)
    â¨ Ïƒ_FECHA_NACâ‰¥'2000-01-01'(EMPLEADO)
)
```

- **Ventaja:** Reduce significativamente filas antes del JOIN final con tabla grande (EMPLEADO).

---

## ðŸ“Œ **Tema 7: Consultas hipotÃ©ticas SELECT y sus costes**

### ðŸ”¹ **Consulta original hipotÃ©tica:**
```sql
SELECT * FROM Clientes WHERE Pais = 'Paraguay';
```

#### **Caso 1: Tabla pequeÃ±a, sin Ã­ndices**
- **Algoritmo:** BÃºsqueda lineal.
- **Costo:** O(n) â†’ alto.
- **Ejemplo:** Tabla Clientes (500 filas).

---

#### **Caso 2: Tabla ordenada fÃ­sicamente**
- **Algoritmo:** BÃºsqueda binaria.
- **Costo:** O(log n) â†’ medio.
- **Ejemplo:** Tabla Clientes ordenada por paÃ­s.

---

#### **Caso 3: Ãndice secundario sobre paÃ­s**
- **Algoritmo:** Ãndice secundario (B+).
- **Costo:** O(log n) â†’ bajo.
- **Ejemplo:** Ãndice sobre columna Pais.

---

#### **Caso 4: Tabla replicada localmente**
- **Algoritmo:** Acceso local inmediato.
- **Costo:** O(1) â†’ muy bajo.
- **Ejemplo:** Copia local en servidor Paraguay.

---

## ðŸ“‰ **GrÃ¡fico claro comparativo coste consultas:**

```
Costo consulta (SELECT WHERE)

Alto â”‚ Lineal (sin Ã­ndices)
     â”‚
     â”‚        Binaria (tabla ordenada)
     â”‚
     â”‚                 Ãndice secundario (B+)
Bajo â”‚                           ReplicaciÃ³n local
     â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–º Eficiencia
```

---

## ðŸ“š **Resumen prÃ¡ctico optimizaciÃ³n consultas**

| TÃ©cnica optimizaciÃ³n | DescripciÃ³n clara             | Ventaja principal           |
|----------------------|-------------------------------|-----------------------------|
| Empujar selecciones  | Aplicar filtros antes JOINs   | Menos filas en JOIN         |
| Reordenar JOINs      | Tablas pequeÃ±as primero       | Menor coste JOINs grandes   |
| Ãndices secundarios  | Uso columnas frecuentes       | BÃºsqueda rÃ¡pida O(log n)    |
| ReplicaciÃ³n local    | Copias locales tablas comunes | Acceso inmediato O(1)       |

---

## âœ… **Ejercicios resueltos claramente:**

### **(Tema 4)** Ãlgebra relacional y optimizaciones claras:

- **Consulta original â†’ Ãlgebra relacional claramente explicada**
- **OptimizaciÃ³n 1:** Empujar selecciones.
- **OptimizaciÃ³n 2:** Cambiar orden JOIN.

---

### **(Tema 7)** Casos hipotÃ©ticos claramente definidos y explicados:

| Caso | DescripciÃ³n                           | Algoritmo usado       | Costo teÃ³rico |
|------|---------------------------------------|-----------------------|---------------|
| 1    | Sin Ã­ndices                           | Lineal                | O(n) alto     |
| 2    | Tabla ordenada fÃ­sicamente            | Binaria               | O(log n) medio|
| 3    | Ãndice secundario disponible          | Ãndice secundario (B+)| O(log n) bajo |
| 4    | ReplicaciÃ³n local                     | Acceso local          | O(1) muy bajo |

---

## ðŸŽ¯ **ConclusiÃ³n clave sobre OptimizaciÃ³n de Consultas:**

- Usar Ã¡lgebra relacional permite al SGBD reestructurar consultas para optimizar rendimiento.
- La selecciÃ³n temprana (push selection) y la reordenaciÃ³n de JOINs son las tÃ©cnicas mÃ¡s efectivas.
- Ãndices secundarios y replicaciÃ³n local proporcionan grandes mejoras en bÃºsquedas especÃ­ficas.

---

## ðŸ“Š **GrÃ¡fico resumen claro sobre OptimizaciÃ³n Consultas:**

```
OptimizaciÃ³n Consultas SQL â”€â”€â–º Mejor rendimiento
           â”‚
           â”œâ”€ Ãlgebra Relacional â”€â”€â–º reglas equivalentes
           â”‚
           â”œâ”€ Empujar Selecciones â”€â”€â–º menos filas JOIN
           â”‚
           â”œâ”€ Reordenar JOINs â”€â”€â–º menor coste global
           â”‚
           â””â”€ Uso Ãndices y ReplicaciÃ³n â”€â”€â–º acceso rÃ¡pido (log n o 1)
```


## 14. Normalizacion Dependencias Funcionales
# ðŸ“š **IntroducciÃ³n a la NormalizaciÃ³n**

La **normalizaciÃ³n** es un proceso en diseÃ±o de bases de datos que organiza los datos eficientemente para:

- Eliminar redundancias.
- Evitar anomalÃ­as (inserciÃ³n, actualizaciÃ³n, eliminaciÃ³n).
- Garantizar integridad y consistencia.

---

## ðŸ“Œ **Dependencias Funcionales**

Una **Dependencia Funcional (DF)** ocurre cuando el valor de un atributo (o conjunto de atributos) determina Ãºnicamente el valor de otro atributo.

NotaciÃ³n clara:  
```
A â†’ B ("A determina B")
```

---

# ðŸ§© **Ejercicio prÃ¡ctico claro (Empleado)**

Tabla inicial:  
```
Empleado (CI, Nombre, DirecciÃ³n, Cargo, Cod_Dep)
```

### ðŸ”¹ **Dependencias Funcionales (DF) iniciales:**

- `CI â†’ Nombre, DirecciÃ³n, Cargo, Cod_Dep`
  - Cada persona (CI) tiene un nombre, direcciÃ³n, cargo y departamento Ãºnicos.
- `Cod_Dep â†’ Cargo (en algunos casos)`
  - Posible dependencia parcial si el cargo depende directamente del departamento.

---

## ðŸ“ **AplicaciÃ³n de las Formas Normales (Empleado)**

### ðŸ”¹ **Primera Forma Normal (1FN):**

- No atributos multivaluados. Tabla ya cumple (cada atributo es atÃ³mico).

**Estado:**  
```
Empleado(CI, Nombre, DirecciÃ³n, Cargo, Cod_Dep)
```

---

### ðŸ”¹ **Segunda Forma Normal (2FN):**

- No dependencias parciales respecto a la clave primaria.

En este caso, la clave primaria es `CI`, que es un atributo simple, por lo que ya cumple 2FN directamente (no hay dependencias parciales posibles).

**Estado 2FN:**  
```
Empleado(CI, Nombre, DirecciÃ³n, Cargo, Cod_Dep)
```

---

### ðŸ”¹ **Tercera Forma Normal (3FN):**

- No dependencias transitivas (atributos no clave que dependen de otro atributo no clave).

**Analizar dependencia transitiva:**  
- Supongamos posible dependencia transitiva: `Cod_Dep â†’ Cargo`.
- Para evitar esta dependencia, separar atributos en dos tablas:

**Resultado claro en 3FN:**  
```
Empleado(CI, Nombre, DirecciÃ³n, Cod_Dep)
Departamento(Cod_Dep, Cargo)
```

---

## ðŸ”‘ **Claves Primarias y ForÃ¡neas claramente definidas:**

- **Empleado:**
  - Clave primaria: `CI`
  - Clave forÃ¡nea: `Cod_Dep` â†’ referencia a `Departamento(Cod_Dep)`

- **Departamento:**
  - Clave primaria: `Cod_Dep`

---

# ðŸ“š **Ejercicio prÃ¡ctico claro (Carrera, Materia, Docente)**

Tablas iniciales claramente definidas:

```
Carrera(CodCarrera, NombreCarrera)
Materia(CodMateria, NombreMateria, CodCarrera)
Docente(CI_Docente, NombreDocente, CodMateria)
```

### ðŸ”¹ **Dependencias Funcionales identificadas claramente:**

- **Carrera:** `CodCarrera â†’ NombreCarrera`
- **Materia:** `CodMateria â†’ NombreMateria, CodCarrera`
- **Docente:** `CI_Docente â†’ NombreDocente, CodMateria`

---

## ðŸ“Œ **Aplicar NormalizaciÃ³n claramente explicada:**

### ðŸ”¹ **1FN (Cumple desde inicio)**

Cada atributo atÃ³mico claramente definido.

### ðŸ”¹ **2FN (Cumple desde inicio)**

Cada tabla tiene una clave primaria simple. No existen dependencias parciales posibles.

### ðŸ”¹ **3FN (Dependencias transitivas a verificar)**

- No se detectan dependencias transitivas claras en estas tablas originales. 
- Ya cumplen claramente 3FN.

**Resultado final claro (en 3FN):**  
```
Carrera(CodCarrera, NombreCarrera)
Materia(CodMateria, NombreMateria, CodCarrera)
Docente(CI_Docente, NombreDocente, CodMateria)
```

---

## ðŸ“‘ **Claves Primarias y ForÃ¡neas claramente definidas:**

| Tabla        | Clave primaria | Claves forÃ¡neas                       |
|--------------|----------------|---------------------------------------|
| Carrera      | CodCarrera     | â€”                                     |
| Materia      | CodMateria     | CodCarrera â†’ Carrera(CodCarrera)      |
| Docente      | CI_Docente     | CodMateria â†’ Materia(CodMateria)      |

---

## ðŸ“Š **GrÃ¡fico resumen claro NormalizaciÃ³n 1FN â†’ 3FN:**

```
Tabla inicial (1FN) â”€â”€â–º (2FN: Sin dependencias parciales)
           â”‚
           â–¼
(3FN: Sin dependencias transitivas)
           â”‚
           â–¼
Tablas separadas claras (3FN, eficiente)
```

---

## ðŸŽ¯ **Ejemplo visual claro NormalizaciÃ³n Empleado (3FN):**

**ANTES (tabla Ãºnica con redundancia):**
| CI   | Nombre  | DirecciÃ³n | Cargo      | Cod_Dep |
|------|---------|-----------|------------|---------|
| 123  | Juan    | Calle A   | Analista   | D01     |
| 456  | Laura   | Calle B   | Analista   | D01     |

- Redundancia clara en "Cargo" (Analista repetido).

**DESPUÃ‰S (en 3FN):**

**Empleado**
| CI   | Nombre  | DirecciÃ³n | Cod_Dep |
|------|---------|-----------|---------|
| 123  | Juan    | Calle A   | D01     |
| 456  | Laura   | Calle B   | D01     |

**Departamento**
| Cod_Dep | Cargo    |
|---------|----------|
| D01     | Analista |

- Redundancia eliminada claramente.

---

## âœ… **ConclusiÃ³n clave sobre NormalizaciÃ³n y Dependencias Funcionales:**

- La normalizaciÃ³n elimina claramente redundancias y evita anomalÃ­as.
- La clave es identificar claramente dependencias funcionales, parciales y transitivas.
- Aplicar formas normales (1FN, 2FN, 3FN) resulta en un diseÃ±o mÃ¡s limpio, eficiente y robusto.

---

## ðŸ“ **Resumen grÃ¡fico claro NormalizaciÃ³n y Dependencias Funcionales:**

```
NormalizaciÃ³n y Dependencias Funcionales â”€â”€â–º Eficiencia diseÃ±o BD
              â”‚
              â”œâ”€ DF claras â”€â”€â–º Atributos determinantes
              â”‚
              â”œâ”€ 1FN (atÃ³micos) â”€â”€â–º Sin atributos multivaluados
              â”‚
              â”œâ”€ 2FN (parciales) â”€â”€â–º Dependencia completa clave primaria
              â”‚
              â””â”€ 3FN (transitivas) â”€â”€â–º No dependencias transitivas
```


## 15. Modelado ER SQL

# ðŸ“ **1. Modelo ER: Empresa-Empleados-Departamento**

## ðŸ”¹ **Modelo Entidad-RelaciÃ³n (MER):**

**Entidades:**
- **Empleado:** CI (PK), Nombre, DirecciÃ³n, Cargo
- **Departamento:** Cod_Dep (PK), Nombre_Dep

**Relaciones:**
- **Trabaja_en:** RelaciÃ³n N:1 (muchos empleados en un departamento).

**Diagrama ER claro:**
```
Empleado (CI, Nombre, DirecciÃ³n, Cargo)
     â”‚N
     â”‚
[Trabaja_en]
     â”‚1
     â–¼
Departamento (Cod_Dep, Nombre_Dep)
```

---

## ðŸ”¹ **TransformaciÃ³n al Modelo Relacional:**

```
Empleado(CI, Nombre, DirecciÃ³n, Cargo, Cod_Dep(FK))
Departamento(Cod_Dep, Nombre_Dep)
```

- **PK (primaria):** Empleado(CI), Departamento(Cod_Dep)
- **FK (forÃ¡nea):** Empleado(Cod_Dep â†’ Departamento)

---

# ðŸ“š **2. Modelo ER: Universidad (Carreras, Materias, Docentes, Alumnos)**

## ðŸ”¹ **Modelo ER claro:**

**Entidades:**
- **Carrera:** CodCarrera (PK), Nombre
- **Materia:** CodMateria (PK), Nombre, CodCarrera(FK)
- **Docente:** CI_Docente (PK), Nombre
- **Alumno:** CI_Alumno (PK), Nombre

**Relaciones:**
- **Dicta:** Docente 1:N Materia
- **InscripciÃ³n:** Alumno N:M Materia (Tabla intermedia)
- **Carrera-Materia:** Carrera 1:N Materia

**Diagrama ER claro:**
```
Carrera (CodCarrera, Nombre)
  â”‚1
  â”‚
[Tiene]
  â”‚N
  â–¼
Materia (CodMateria, Nombre)
  â”‚N           N
  â”‚            â”‚
[Dicta]     [InscripciÃ³n]
  â”‚1           â”‚
Docente(CI,Nombre) Alumno(CI,Nombre)
```

---

## ðŸ”¹ **Modelo Relacional claro:**

```
Carrera(CodCarrera, Nombre)
Materia(CodMateria, Nombre, CodCarrera(FK))
Docente(CI_Docente, Nombre)
Alumno(CI_Alumno, Nombre)
InscripciÃ³n(CI_Alumno(FK), CodMateria(FK), Nota)
Dicta(CI_Docente(FK), CodMateria(FK))
```

---

## ðŸ”‘ **Consultas SQL (Universidad):**

- **Materias por carrera especÃ­fica:**
```sql
SELECT M.Nombre
FROM Materia M
WHERE M.CodCarrera = 'INF';
```

- **Docentes que dictan materia especÃ­fica:**
```sql
SELECT D.Nombre
FROM Docente D
JOIN Dicta DT ON D.CI_Docente = DT.CI_Docente
WHERE DT.CodMateria = 'BD2';
```

- **Alumnos que rindieron exÃ¡menes en mÃ¡s de una materia:**
```sql
SELECT A.Nombre, COUNT(*) AS MateriasExamen
FROM Alumno A
JOIN InscripciÃ³n I ON A.CI_Alumno = I.CI_Alumno
GROUP BY A.Nombre
HAVING COUNT(*) > 1;
```

---

# ðŸ“– **3. Modelo ER: Biblioteca (Libro, Autor, Editorial, Socio, PrÃ©stamo)**

## ðŸ”¹ **Modelo ER claro:**

**Entidades:**
- **Libro:** CodLibro (PK), Titulo, CodEditorial(FK)
- **Autor:** CodAutor (PK), Nombre
- **Editorial:** CodEditorial (PK), Nombre
- **Socio:** CodSocio (PK), Nombre, DirecciÃ³n
- **PrÃ©stamo:** CodPrestamo (PK), Fecha, CodLibro(FK), CodSocio(FK)

**Relaciones:**
- **Libro-Autor:** N:M (tabla intermedia "LibroAutor")
- **Libro-Editorial:** N:1
- **PrÃ©stamo-Socio-Libro:** N:1 (cada prÃ©stamo para un libro especÃ­fico a un socio)

**Modelo relacional final claro:**
```
Libro(CodLibro, Titulo, CodEditorial(FK))
Autor(CodAutor, Nombre)
Editorial(CodEditorial, Nombre)
Socio(CodSocio, Nombre, DirecciÃ³n)
Prestamo(CodPrestamo, Fecha, CodLibro(FK), CodSocio(FK))
LibroAutor(CodLibro(FK), CodAutor(FK))
```

---

# ðŸ“Š **Consultas SQL y Ãlgebra relacional claras (Empresa-Empleado-Departamento)**

- **Lista empleados por departamento (SQL):**
```sql
SELECT E.Nombre, D.Nombre_Dep
FROM Empleado E
JOIN Departamento D ON E.Cod_Dep = D.Cod_Dep;
```

- **Ãlgebra relacional:**
```
Ï€_(Nombre,Nombre_Dep)(Empleado â¨_(Cod_Dep) Departamento)
```

- **Nombre empleados con cargo 'Analista' (SQL):**
```sql
SELECT Nombre
FROM Empleado
WHERE Cargo = 'Analista';
```

- **Ãlgebra relacional:**
```
Ï€_Nombre(Ïƒ_Cargo='Analista'(Empleado))
```

- **Total empleados por departamento (SQL):**
```sql
SELECT Cod_Dep, COUNT(*) AS TotalEmpleados
FROM Empleado
GROUP BY Cod_Dep;
```

---

# ðŸ“Œ **Consultas SQL (Universidad):**

- **Listar materias por carrera:**
```sql
SELECT Nombre
FROM Materia
WHERE CodCarrera = 'INF';
```

- **Buscar docentes por materia especÃ­fica:**
```sql
SELECT D.Nombre
FROM Docente D
JOIN Dicta DT ON D.CI_Docente = DT.CI_Docente
WHERE DT.CodMateria = 'BD2';
```

- **Mostrar alumnos que rindieron exÃ¡menes en mÃ¡s de una materia:**
```sql
SELECT A.Nombre, COUNT(I.CodMateria) AS MateriasExamen
FROM Alumno A
JOIN InscripciÃ³n I ON A.CI_Alumno = I.CI_Alumno
GROUP BY A.Nombre
HAVING COUNT(I.CodMateria) > 1;
```

---

# âœ… **Conclusiones clave (MER y SQL):**

- **Modelo ER** permite representar claramente entidades, relaciones y cardinalidades.
- **TransformaciÃ³n relacional** traduce ER en tablas especÃ­ficas (PKs/FKs).
- Las **consultas SQL** permiten extracciÃ³n precisa de informaciÃ³n especÃ­fica segÃºn necesidad.
- **Ãlgebra relacional** facilita la optimizaciÃ³n visual de consultas antes de ejecuciÃ³n en SGBD.

---

## ðŸŽ¯ **GrÃ¡fico resumen claro MER â†’ Relacional â†’ SQL:**

```
Requerimiento â”€â”€â–º Modelo ER
       â”‚
       â–¼
Modelo Relacional (tablas, PK/FK)
       â”‚
       â–¼
Consultas SQL claras y eficientes
       â”‚
       â–¼
Resultados rÃ¡pidos y exactos
```

