
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