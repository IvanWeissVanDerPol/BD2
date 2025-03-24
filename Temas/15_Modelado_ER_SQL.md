
# 📐 **1. Modelo ER: Empresa-Empleados-Departamento**

## 🔹 **Modelo Entidad-Relación (MER):**

**Entidades:**
- **Empleado:** CI (PK), Nombre, Dirección, Cargo
- **Departamento:** Cod_Dep (PK), Nombre_Dep

**Relaciones:**
- **Trabaja_en:** Relación N:1 (muchos empleados en un departamento).

**Diagrama ER claro:**
```
Empleado (CI, Nombre, Dirección, Cargo)
     │N
     │
[Trabaja_en]
     │1
     ▼
Departamento (Cod_Dep, Nombre_Dep)
```

---

## 🔹 **Transformación al Modelo Relacional:**

```
Empleado(CI, Nombre, Dirección, Cargo, Cod_Dep(FK))
Departamento(Cod_Dep, Nombre_Dep)
```

- **PK (primaria):** Empleado(CI), Departamento(Cod_Dep)
- **FK (foránea):** Empleado(Cod_Dep → Departamento)

---

# 📚 **2. Modelo ER: Universidad (Carreras, Materias, Docentes, Alumnos)**

## 🔹 **Modelo ER claro:**

**Entidades:**
- **Carrera:** CodCarrera (PK), Nombre
- **Materia:** CodMateria (PK), Nombre, CodCarrera(FK)
- **Docente:** CI_Docente (PK), Nombre
- **Alumno:** CI_Alumno (PK), Nombre

**Relaciones:**
- **Dicta:** Docente 1:N Materia
- **Inscripción:** Alumno N:M Materia (Tabla intermedia)
- **Carrera-Materia:** Carrera 1:N Materia

**Diagrama ER claro:**
```
Carrera (CodCarrera, Nombre)
  │1
  │
[Tiene]
  │N
  ▼
Materia (CodMateria, Nombre)
  │N           N
  │            │
[Dicta]     [Inscripción]
  │1           │
Docente(CI,Nombre) Alumno(CI,Nombre)
```

---

## 🔹 **Modelo Relacional claro:**

```
Carrera(CodCarrera, Nombre)
Materia(CodMateria, Nombre, CodCarrera(FK))
Docente(CI_Docente, Nombre)
Alumno(CI_Alumno, Nombre)
Inscripción(CI_Alumno(FK), CodMateria(FK), Nota)
Dicta(CI_Docente(FK), CodMateria(FK))
```

---

## 🔑 **Consultas SQL (Universidad):**

- **Materias por carrera específica:**
```sql
SELECT M.Nombre
FROM Materia M
WHERE M.CodCarrera = 'INF';
```

- **Docentes que dictan materia específica:**
```sql
SELECT D.Nombre
FROM Docente D
JOIN Dicta DT ON D.CI_Docente = DT.CI_Docente
WHERE DT.CodMateria = 'BD2';
```

- **Alumnos que rindieron exámenes en más de una materia:**
```sql
SELECT A.Nombre, COUNT(*) AS MateriasExamen
FROM Alumno A
JOIN Inscripción I ON A.CI_Alumno = I.CI_Alumno
GROUP BY A.Nombre
HAVING COUNT(*) > 1;
```

---

# 📖 **3. Modelo ER: Biblioteca (Libro, Autor, Editorial, Socio, Préstamo)**

## 🔹 **Modelo ER claro:**

**Entidades:**
- **Libro:** CodLibro (PK), Titulo, CodEditorial(FK)
- **Autor:** CodAutor (PK), Nombre
- **Editorial:** CodEditorial (PK), Nombre
- **Socio:** CodSocio (PK), Nombre, Dirección
- **Préstamo:** CodPrestamo (PK), Fecha, CodLibro(FK), CodSocio(FK)

**Relaciones:**
- **Libro-Autor:** N:M (tabla intermedia "LibroAutor")
- **Libro-Editorial:** N:1
- **Préstamo-Socio-Libro:** N:1 (cada préstamo para un libro específico a un socio)

**Modelo relacional final claro:**
```
Libro(CodLibro, Titulo, CodEditorial(FK))
Autor(CodAutor, Nombre)
Editorial(CodEditorial, Nombre)
Socio(CodSocio, Nombre, Dirección)
Prestamo(CodPrestamo, Fecha, CodLibro(FK), CodSocio(FK))
LibroAutor(CodLibro(FK), CodAutor(FK))
```

---

# 📊 **Consultas SQL y Álgebra relacional claras (Empresa-Empleado-Departamento)**

- **Lista empleados por departamento (SQL):**
```sql
SELECT E.Nombre, D.Nombre_Dep
FROM Empleado E
JOIN Departamento D ON E.Cod_Dep = D.Cod_Dep;
```

- **Álgebra relacional:**
```
π_(Nombre,Nombre_Dep)(Empleado ⨝_(Cod_Dep) Departamento)
```

- **Nombre empleados con cargo 'Analista' (SQL):**
```sql
SELECT Nombre
FROM Empleado
WHERE Cargo = 'Analista';
```

- **Álgebra relacional:**
```
π_Nombre(σ_Cargo='Analista'(Empleado))
```

- **Total empleados por departamento (SQL):**
```sql
SELECT Cod_Dep, COUNT(*) AS TotalEmpleados
FROM Empleado
GROUP BY Cod_Dep;
```

---

# 📌 **Consultas SQL (Universidad):**

- **Listar materias por carrera:**
```sql
SELECT Nombre
FROM Materia
WHERE CodCarrera = 'INF';
```

- **Buscar docentes por materia específica:**
```sql
SELECT D.Nombre
FROM Docente D
JOIN Dicta DT ON D.CI_Docente = DT.CI_Docente
WHERE DT.CodMateria = 'BD2';
```

- **Mostrar alumnos que rindieron exámenes en más de una materia:**
```sql
SELECT A.Nombre, COUNT(I.CodMateria) AS MateriasExamen
FROM Alumno A
JOIN Inscripción I ON A.CI_Alumno = I.CI_Alumno
GROUP BY A.Nombre
HAVING COUNT(I.CodMateria) > 1;
```

---

# ✅ **Conclusiones clave (MER y SQL):**

- **Modelo ER** permite representar claramente entidades, relaciones y cardinalidades.
- **Transformación relacional** traduce ER en tablas específicas (PKs/FKs).
- Las **consultas SQL** permiten extracción precisa de información específica según necesidad.
- **Álgebra relacional** facilita la optimización visual de consultas antes de ejecución en SGBD.

---

## 🎯 **Gráfico resumen claro MER → Relacional → SQL:**

```
Requerimiento ──► Modelo ER
       │
       ▼
Modelo Relacional (tablas, PK/FK)
       │
       ▼
Consultas SQL claras y eficientes
       │
       ▼
Resultados rápidos y exactos
```