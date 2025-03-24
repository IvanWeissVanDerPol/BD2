
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
