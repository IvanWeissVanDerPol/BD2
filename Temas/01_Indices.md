

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

## 🧩 **Ejercicios de Examen Reales**

A continuación se presentan ejercicios reales de exámenes finales, útiles para practicar y entender cómo se aplican los conceptos de índices en situaciones concretas.

---

### 📝 **Ejercicio: Índice B+ y Hash sobre Cliente**

La siguiente tabla corresponde al estado actual del archivo de la relación **Cliente**, en el que cada bloque del archivo corresponde a 1 fila. Se pide:

**a.** Construir un índice en forma de árbol **B+** con nodos de 4 punteros para la clave primaria `id`, suponiendo que los registros/filas fueron insertados según el orden alfabético de la columna `nombre`.

**b.** Construir un índice hash estático cerrado con **cajones de 4 elementos**, cuya función de asociación es `x mod 4` sobre la columna `saldo`, siendo `x` el valor de cada fila en dicha columna.

**c.** Explique detalladamente en cada caso si el índice es **primario o secundario**.

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

**Pistas para resolver:**
- Para el árbol B+, recuerda que los nodos hoja deben estar enlazados y contener referencias a los registros.
- Para el hash, distribuye los saldos usando la función `x mod 4` y agrupa en cajones de hasta 4 elementos.
- Un índice es **primario** si está sobre la clave primaria (en este caso, `id`), y **secundario** si está sobre otro atributo (por ejemplo, `saldo`).

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
