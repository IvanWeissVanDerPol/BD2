
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
