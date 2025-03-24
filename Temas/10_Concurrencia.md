
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
