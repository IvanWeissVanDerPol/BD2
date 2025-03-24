
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
