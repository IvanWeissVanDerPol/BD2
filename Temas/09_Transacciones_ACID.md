
# 🔐 **Introducción a Transacciones (SGBD)**

Una **transacción** en un Sistema Gestor de Bases de Datos (SGBD) es una unidad lógica que agrupa operaciones que se ejecutan de manera indivisible, asegurando que todas las operaciones dentro se completen correctamente o ninguna lo haga, garantizando la consistencia del sistema.

**Ejemplo sencillo:**  
Transferir dinero de la cuenta A a la cuenta B es una sola transacción que incluye:

1. Restar dinero en cuenta A
2. Sumar dinero en cuenta B

Ambas deben completarse exitosamente o ninguna debe ejecutarse.

---

## 🔄 **Fases del Ciclo de Vida de una Transacción**

Una transacción atraviesa claramente 5 fases:

### 1️⃣ **Inicio (Begin)**
- La transacción comienza formalmente.

### 2️⃣ **Ejecución (Execution)**
- Realiza las operaciones (INSERT, UPDATE, DELETE, SELECT).

### 3️⃣ **Validación (Validation)**
- Verifica si las operaciones pueden completarse (restricciones, bloqueos).

### 4️⃣ **Confirmación (Commit)**
- Guarda permanentemente cambios realizados en la base de datos.

### 5️⃣ **Cancelación (Rollback, si aplica)**
- Si algo falla, revierte todas las operaciones realizadas hasta el momento del fallo, volviendo al estado inicial.

---

## 📌 **Propiedades ACID**

Estas propiedades garantizan la confiabilidad en un entorno transaccional:

| Propiedad    | Definición breve |
|--------------|------------------|
| **Atomicidad**    | Todo o nada. La transacción ocurre completamente o no ocurre. |
| **Consistencia**  | La base de datos pasa de un estado válido a otro estado válido. |
| **Aislamiento**   | Cada transacción se ejecuta independientemente sin interferir con otras transacciones simultáneas. |
| **Durabilidad**   | Cambios confirmados permanecen permanentes aun ante fallos del sistema.|

---

## 📚 **Explicación detallada Propiedades ACID (estándar SQL)**

### 🔹 **Atomicidad (Atomicity):**
- Operaciones dentro de la transacción son indivisibles.
- **Ejemplo:**  
  Si falla un paso de la transferencia bancaria, ambas cuentas permanecen intactas.

### 🔹 **Consistencia (Consistency):**
- La base de datos siempre permanece en un estado válido antes y después de la transacción.
- **Ejemplo:**  
  No permitir saldo negativo tras transferencia bancaria.

### 🔹 **Aislamiento (Isolation):**
- Transacciones concurrentes no interfieren entre sí.
- **Ejemplo:**  
  Dos transferencias simultáneas no causan inconsistencias en los saldos.

### 🔹 **Durabilidad (Durability):**
- Los cambios realizados son permanentes una vez confirmados (commit).
- **Ejemplo:**  
  Tras una transferencia exitosa, el saldo se mantiene actualizado incluso si ocurre un corte de energía.

---

## 📈 **Gráfico claro del Ciclo de Vida de una Transacción:**

```
           Transacción iniciada
                  │
                  ▼
           ┌─────────────┐
           │  Ejecución  │─────────┐
           └─────────────┘         │
                  │                │
                  ▼                ▼
           ┌─────────────┐   ┌─────────────┐
           │ Validación  │───│ Cancelación │ (Rollback)
           └─────────────┘   └─────────────┘
                  │
                  ▼
           ┌─────────────┐
           │Confirmación │ (Commit)
           └─────────────┘
                  │
                  ▼
             Cambios permanentes
```

---

## 🧩 **Ejercicios Resueltos en detalle:**

### ✅ **(a) Definición concreta de transacción:**

- Es un conjunto lógico indivisible de operaciones en bases de datos.
- Todas se ejecutan exitosamente o todas fallan, asegurando integridad.

---

### ✅ **(b) Ciclo de vida detallado:**

- **Inicio:** Comienzo formal.
- **Ejecución:** Realización de operaciones.
- **Validación:** Chequeo restricciones y bloqueos.
- **Commit:** Confirmación final.
- **Rollback:** Anulación de operaciones si algo falla.

---

### ✅ **(c) Propiedades ACID definidas claramente:**

- **Atomicidad:** Todo o nada.
- **Consistencia:** Estado válido siempre.
- **Aislamiento:** Independencia entre transacciones simultáneas.
- **Durabilidad:** Permanencia de los cambios tras confirmación.

---

## 🔑 **Ejemplo práctico completo con propiedades ACID:**

### 🔹 **Caso práctico: Transferencia Bancaria (Transacción T)**

- Estado inicial:
  - Cuenta A: 500 USD
  - Cuenta B: 300 USD

- Operaciones de la transacción:
  1. Cuenta A → -100 USD  
  2. Cuenta B → +100 USD  

- Estado final (esperado si Commit):
  - Cuenta A: 400 USD
  - Cuenta B: 400 USD

### 🔹 **Validación de propiedades ACID:**

| Propiedad     | Explicación en ejemplo bancario |
|---------------|---------------------------------|
| Atomicidad    | Ambas cuentas cambian juntas o ninguna cambia.|
| Consistencia  | Saldos siempre coherentes, no negativos.|
| Aislamiento   | Otra transacción simultánea no afecta esta operación.|
| Durabilidad   | Una vez completada, transferencias permanecen aún con fallos del sistema.|

---

## 📉 **Gráfico resumen propiedades ACID:**

```
         Estado inicial válido
                  │
Atomicidad        │ Transacción ──── (Si falla) ───► Estado inicial
                  ▼
Consistencia ── Estado válido intermedio
                  │
Aislamiento       │ (Sin interferencia externa)
                  ▼
Durabilidad ── Estado final válido y permanente tras commit
```

---

## 🎯 **Conclusión clave del tema Transacciones y ACID:**

- Las **transacciones** garantizan integridad y coherencia.
- Las propiedades **ACID** (Atomicidad, Consistencia, Aislamiento y Durabilidad) son esenciales para mantener la fiabilidad del sistema.
- Sin estas propiedades, los datos serían vulnerables a inconsistencia y corrupción.

Una implementación adecuada del modelo ACID es crítica para aplicaciones empresariales, bancarias y cualquier sistema que maneje datos sensibles.
