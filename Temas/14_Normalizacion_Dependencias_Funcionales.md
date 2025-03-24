# 📚 **Introducción a la Normalización**

La **normalización** es un proceso en diseño de bases de datos que organiza los datos eficientemente para:

- Eliminar redundancias.
- Evitar anomalías (inserción, actualización, eliminación).
- Garantizar integridad y consistencia.

---

## 📌 **Dependencias Funcionales**

Una **Dependencia Funcional (DF)** ocurre cuando el valor de un atributo (o conjunto de atributos) determina únicamente el valor de otro atributo.

Notación clara:  
```
A → B ("A determina B")
```

---

# 🧩 **Ejercicio práctico claro (Empleado)**

Tabla inicial:  
```
Empleado (CI, Nombre, Dirección, Cargo, Cod_Dep)
```

### 🔹 **Dependencias Funcionales (DF) iniciales:**

- `CI → Nombre, Dirección, Cargo, Cod_Dep`
  - Cada persona (CI) tiene un nombre, dirección, cargo y departamento únicos.
- `Cod_Dep → Cargo (en algunos casos)`
  - Posible dependencia parcial si el cargo depende directamente del departamento.

---

## 📐 **Aplicación de las Formas Normales (Empleado)**

### 🔹 **Primera Forma Normal (1FN):**

- No atributos multivaluados. Tabla ya cumple (cada atributo es atómico).

**Estado:**  
```
Empleado(CI, Nombre, Dirección, Cargo, Cod_Dep)
```

---

### 🔹 **Segunda Forma Normal (2FN):**

- No dependencias parciales respecto a la clave primaria.

En este caso, la clave primaria es `CI`, que es un atributo simple, por lo que ya cumple 2FN directamente (no hay dependencias parciales posibles).

**Estado 2FN:**  
```
Empleado(CI, Nombre, Dirección, Cargo, Cod_Dep)
```

---

### 🔹 **Tercera Forma Normal (3FN):**

- No dependencias transitivas (atributos no clave que dependen de otro atributo no clave).

**Analizar dependencia transitiva:**  
- Supongamos posible dependencia transitiva: `Cod_Dep → Cargo`.
- Para evitar esta dependencia, separar atributos en dos tablas:

**Resultado claro en 3FN:**  
```
Empleado(CI, Nombre, Dirección, Cod_Dep)
Departamento(Cod_Dep, Cargo)
```

---

## 🔑 **Claves Primarias y Foráneas claramente definidas:**

- **Empleado:**
  - Clave primaria: `CI`
  - Clave foránea: `Cod_Dep` → referencia a `Departamento(Cod_Dep)`

- **Departamento:**
  - Clave primaria: `Cod_Dep`

---

# 📚 **Ejercicio práctico claro (Carrera, Materia, Docente)**

Tablas iniciales claramente definidas:

```
Carrera(CodCarrera, NombreCarrera)
Materia(CodMateria, NombreMateria, CodCarrera)
Docente(CI_Docente, NombreDocente, CodMateria)
```

### 🔹 **Dependencias Funcionales identificadas claramente:**

- **Carrera:** `CodCarrera → NombreCarrera`
- **Materia:** `CodMateria → NombreMateria, CodCarrera`
- **Docente:** `CI_Docente → NombreDocente, CodMateria`

---

## 📌 **Aplicar Normalización claramente explicada:**

### 🔹 **1FN (Cumple desde inicio)**

Cada atributo atómico claramente definido.

### 🔹 **2FN (Cumple desde inicio)**

Cada tabla tiene una clave primaria simple. No existen dependencias parciales posibles.

### 🔹 **3FN (Dependencias transitivas a verificar)**

- No se detectan dependencias transitivas claras en estas tablas originales. 
- Ya cumplen claramente 3FN.

**Resultado final claro (en 3FN):**  
```
Carrera(CodCarrera, NombreCarrera)
Materia(CodMateria, NombreMateria, CodCarrera)
Docente(CI_Docente, NombreDocente, CodMateria)
```

---

## 📑 **Claves Primarias y Foráneas claramente definidas:**

| Tabla        | Clave primaria | Claves foráneas                       |
|--------------|----------------|---------------------------------------|
| Carrera      | CodCarrera     | —                                     |
| Materia      | CodMateria     | CodCarrera → Carrera(CodCarrera)      |
| Docente      | CI_Docente     | CodMateria → Materia(CodMateria)      |

---

## 📊 **Gráfico resumen claro Normalización 1FN → 3FN:**

```
Tabla inicial (1FN) ──► (2FN: Sin dependencias parciales)
           │
           ▼
(3FN: Sin dependencias transitivas)
           │
           ▼
Tablas separadas claras (3FN, eficiente)
```

---

## 🎯 **Ejemplo visual claro Normalización Empleado (3FN):**

**ANTES (tabla única con redundancia):**
| CI   | Nombre  | Dirección | Cargo      | Cod_Dep |
|------|---------|-----------|------------|---------|
| 123  | Juan    | Calle A   | Analista   | D01     |
| 456  | Laura   | Calle B   | Analista   | D01     |

- Redundancia clara en "Cargo" (Analista repetido).

**DESPUÉS (en 3FN):**

**Empleado**
| CI   | Nombre  | Dirección | Cod_Dep |
|------|---------|-----------|---------|
| 123  | Juan    | Calle A   | D01     |
| 456  | Laura   | Calle B   | D01     |

**Departamento**
| Cod_Dep | Cargo    |
|---------|----------|
| D01     | Analista |

- Redundancia eliminada claramente.

---

## ✅ **Conclusión clave sobre Normalización y Dependencias Funcionales:**

- La normalización elimina claramente redundancias y evita anomalías.
- La clave es identificar claramente dependencias funcionales, parciales y transitivas.
- Aplicar formas normales (1FN, 2FN, 3FN) resulta en un diseño más limpio, eficiente y robusto.

---

## 📝 **Resumen gráfico claro Normalización y Dependencias Funcionales:**

```
Normalización y Dependencias Funcionales ──► Eficiencia diseño BD
              │
              ├─ DF claras ──► Atributos determinantes
              │
              ├─ 1FN (atómicos) ──► Sin atributos multivaluados
              │
              ├─ 2FN (parciales) ──► Dependencia completa clave primaria
              │
              └─ 3FN (transitivas) ──► No dependencias transitivas
```
