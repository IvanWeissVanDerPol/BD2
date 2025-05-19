
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

**Razón detallada:**  
En la evaluación de árboles sin optimización, cada nodo puede requerir la evaluación de sus dos subárboles (izquierdo y derecho). Para un árbol con n nodos, esto genera un patrón recursivo donde:
- Cada nivel de recursión puede duplicar el trabajo
- Para un árbol balanceado, la altura es aproximadamente log₂(n)
- En el peor caso, se generan 2^0 + 2^1 + 2^2 + ... + 2^(n-1) evaluaciones
- Esta suma es igual a 2^n - 1, resultando en complejidad O(2^n)

El espacio es O(n) porque la pila de llamadas recursivas almacena como máximo n marcos de activación simultáneos, correspondientes a la altura del árbol en una evaluación en profundidad.

### 🔸 (b) Con optimización (Memoización - Programación Dinámica):

- **Tiempo:** Polinómico `O(n^2)` o mejor, dependiendo del problema.
- **Espacio:** `O(n^2)` por almacenamiento en tablas (generalmente matrices).

**Razón detallada:**  
La optimización mediante programación dinámica utiliza una tabla de memoización para almacenar resultados de subproblemas ya calculados. Para la evaluación de árboles en profundidad por la izquierda:

1. **Cálculo del tiempo:**
   - Cada subproblema se calcula exactamente una vez y se almacena
   - Para un árbol con n nodos, existen O(n²) posibles subproblemas distintos (combinaciones de subárboles)
   - Cada cálculo de subproblema requiere tiempo constante O(1) al consultar resultados ya calculados
   - Por tanto, el tiempo total es O(n²) en el peor caso

2. **Cálculo del espacio:**
   - Se requiere una matriz/tabla para almacenar todos los resultados intermedios
   - Esta tabla generalmente tiene dimensiones n×n para cubrir todos los posibles subárboles
   - Cada celda almacena el resultado óptimo para un subárbol específico
   - Esto resulta en un espacio de O(n²)

Esta optimización transforma un problema exponencial O(2^n) en uno polinómico O(n²), sacrificando espacio adicional por una mejora dramática en tiempo de ejecución.

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
