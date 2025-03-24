
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
