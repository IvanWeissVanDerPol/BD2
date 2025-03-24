
# 🌐 **Introducción a Protocolos Distribuidos en SGBD**

Los **protocolos distribuidos** gestionan la **coordinación y concurrencia** en sistemas donde los datos están repartidos en múltiples sitios geográficamente distribuidos. Aseguran consistencia y disponibilidad.

---

# 🗳️ **(a) Protocolo de Control de Concurrencia por Quorum de Consenso**

Este protocolo garantiza coherencia distribuida usando **pesos** asignados a cada sitio.

### 🔹 **Conceptos básicos:**
- Cada sitio recibe un peso asignado.
- Para realizar **lectura o escritura**, la transacción debe sumar un **quorum mínimo** de pesos.
- Generalmente, se asignan pesos según la importancia o disponibilidad de sitios.

---

## 📌 **(b) Implicancias para definir valores de Quorum:**

- **Mayor quorum de lectura:**  
  Mayor consistencia, menor velocidad.
- **Mayor quorum de escritura:**  
  Mayor costo, mayor seguridad en escrituras.
- La suma de quorum de lectura (Q_L) y quorum de escritura (Q_E) debe ser mayor al total de pesos asignados para asegurar consistencia:
  
  ```
  Q_L + Q_E > Peso_Total
  ```

---

## 📚 **(c) Valores para protocolos específicos:**

### 🔹 **Protocolo de Mayoría (Majority Protocol):**
- **Condición:** Quorum lectura + Quorum escritura > total de pesos.
- **Ejemplo claro:** Si total = 10,  
  - Lectura ≥ 6 y Escritura ≥ 5 (o viceversa).  
  (Ej.: Q_L=6, Q_E=5; 6+5=11>10).

### 🔹 **Protocolo Sesgado (Biased Protocol):**
- Un sitio especial tiene peso dominante (sesgado).
- **Ejemplo claro:** Si total = 10  
  - Sitio principal tiene peso=7; demás sitios peso=1.  
  - Quorum lectura y escritura puede satisfacerse con sitio sesgado solo (Ej.: Q_L=7, Q_E=7).

---

# ✅ **(a) Protocolo de Commit en 2 Fases (2PC - Two Phase Commit)**

Permite coordinar confirmación de transacciones distribuidas asegurando consistencia.

### 🔹 **Fases del protocolo 2PC:**

- **Fase 1 (Preparación):**
  1. **Coordinador** envía `PREPARE` a todos los participantes.
  2. **Participantes** ejecutan operaciones localmente y responden:
     - `READY` (preparado) o
     - `ABORT` (cancelar).

- **Fase 2 (Confirmación):**
  - Si TODOS los participantes respondieron `READY`, coordinador envía `COMMIT` para confirmar cambios.
  - Si UNO responde `ABORT`, envía `ABORT` a todos para revertir cambios.

---

## 📌 **Ejemplo gráfico Protocolo 2PC:**

```
         Coordinador
             │
Fase 1:      │ PREPARE?
             │──────────► Participante 1
             │──────────► Participante 2
             │──────────► Participante 3
             │
             │ READY ◄─── Participante 1
             │ READY ◄─── Participante 2
             │ READY ◄─── Participante 3
             │
Fase 2:      │ COMMIT
             │──────────► Participantes (Confirmación)
```

---

# 🚧 **(b) Qué pasa si falla el Coordinador en 2PC?**

- Los participantes quedan "bloqueados" temporalmente sin instrucciones claras (estado incertidumbre).
- Deben esperar recuperación del coordinador o usar técnicas alternativas (backup, tiempo de espera, etc.).

---

# 🚨 **(c) Qué pasa si un Participante falla en 2PC?**

- Si falla en fase preparación: Coordinador envía `ABORT` al resto.
- Si falla después de `READY` (en confirmación): 
  - Al recuperarse, debe consultar al coordinador para saber si debe COMMIT o ABORT (consulta estado).

---

## 📊 **Gráfico claro resumen fallos protocolo 2PC:**

```
Coordinador         Participantes
    │                    │
    ▼                    ▼
Falla:                Falla:
- Incertidumbre       - Antes READY: ABORT
participantes.        - Tras READY: Recuperación consultando coordinador.
```

---

## 🧩 **Ejercicios resueltos claramente:**

### ✅ **(a) Quorum Consenso explicado claramente:**
- Controla concurrencia mediante quorum mínimo (pesos de sitios) para lecturas/escrituras.

---

### ✅ **(b) Implicancias definir valores quorum:**
- Mayor quorum lectura → más consistencia, menor rendimiento.
- Mayor quorum escritura → seguridad escrituras, menor eficiencia.
- Condición clave: Q_L + Q_E > peso total.

---

### ✅ **(c) Valores quorum Mayoría y Sesgado ejemplos concretos:**
- **Mayoría:** (total=10): Q_L=6, Q_E=5 (6+5>10)
- **Sesgado:** sitio principal con peso dominante (peso=7; quorum=7).

---

### ✅ **(a) Pasos protocolo Commit 2 Fases (2PC):**
- **Preparación:** PREPARE → participantes READY/ABORT
- **Confirmación:** COMMIT si todos READY; si no, ABORT.

---

### ✅ **(b) Falla coordinador (qué hacen participantes?):**
- Estado incertidumbre (bloqueados). Esperan recuperación o consulta externa.

---

### ✅ **(c) Falla participante (qué hace sitio?):**
- Antes READY: Coordinador aborta operación.
- Después READY: Participante recuperado consulta coordinador para resolver su estado (commit/abort).

---

## 🔑 **Conclusión clave sobre Protocolos Distribuidos:**

- **Quorum de Consenso** garantiza concurrencia segura, sacrificando parcialmente velocidad por seguridad.
- **Protocolo Commit 2 Fases (2PC)** asegura consistencia distribuida mediante confirmación en fases, con riesgos claros si ocurre fallo coordinador o participante.

---

## 🎯 **Resumen Gráfico Claro Protocolos Distribuidos:**

```
Protocolos Distribuidos ───► Coordinación y Concurrencia Segura
          │
          ├── Quorum Consenso ───► Lectura/escritura por quorum
          │        ├─ Mayoría (lect+escr>total)
          │        └─ Sesgado (sitio dominante)
          │
          └── Commit 2 Fases ────► Confirmación distribuida en fases
                   ├─ Fase preparación
                   └─ Fase confirmación
```
