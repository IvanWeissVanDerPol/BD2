

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
