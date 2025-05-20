## 🧩 TRANSACCIONES Y CONTROL DE CONCURRENCIA

1. ¿Cuál de las siguientes propiedades asegura que una transacción sea completa o no se ejecute?

* A. Atomicidad⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Aislamiento
* C. Durabilidad
* D. Consistencia

2. ¿Qué técnica previene el acceso concurrente a los datos mediante exclusividad?

* A. Fragmentación
* B. Bloqueo⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* C. Indexación
* D. Replicación

3. ¿Qué situación se considera una lectura sucia?

* A. Leer datos eliminados
* B. Leer datos no confirmados de otra transacción⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* C. Leer datos bloqueados
* D. Leer datos antiguos

4. ¿Cuál es el objetivo del control de concurrencia en SGBD?

* A. Aumentar velocidad de red
* B. Reducir almacenamiento
* C. Optimizar consultas indexadas
* D. Mantener consistencia en accesos concurrentes⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

5. ¿Cuál es el orden correcto de las fases del ciclo de vida de una transacción?

* A. Ejecución → Inicio → Fin → Commit
* B. Inicio → Ejecución → Commit/Rollback → Fin⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* C. Inicio → Rollback → Commit → Fin
* D. Commit → Ejecución → Inicio → Fin

6. ¿Qué propiedad ACID garantiza que los cambios realizados persisten ante fallos?

* A. Durabilidad⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Consistencia
* C. Aislamiento
* D. Atomicidad

7. ¿Cuál de los siguientes evita el interbloqueo (deadlock)?

* A. Uso de múltiples índices
* B. Indexación extendida
* C. Replicación activa
* D. Ordenamiento de recursos⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

8. ¿Qué es una planificación secuencial?

* A. Una ejecución serial sin solapamientos entre transacciones⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Una ejecución concurrente con aislamiento
* C. Una transacción con rollback automático
* D. Una lectura con acceso exclusivo

9. ¿Qué estructura se usa para gestionar bloqueos?

* A. Tabla de bloqueos⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Árbol B+
* C. Hash Join
* D. Índice invertido

10. ¿Qué tipo de secuencialidad implica el mismo orden de accesos conflictivos?

* A. Secuencialidad por conflicto⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Secuencialidad por vistas
* C. Planificación válida
* D. Planificación parcial

---

## 🌐 BASES DE DATOS DISTRIBUIDAS

11. ¿Qué protocolo asegura un compromiso coordinado entre sitios distribuidos?

* A. Protocolo de dos fases⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Hash Join
* C. Control de versiones
* D. Esquema estrella

12. ¿Qué sucede si un participante falla durante el 2PC antes de responder?

* A. Se bloquea hasta recuperarse⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Abortan todas las transacciones
* C. El coordinador reenvía el commit
* D. Se confirma automáticamente

13. ¿Qué tipo de fragmentación divide una tabla en subconjuntos por filas?

* A. Fragmentación horizontal⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Replicación total
* C. Fragmentación vertical
* D. Almacenamiento lineal

14. ¿Qué tipo de replicación mejora la disponibilidad de los datos?

* A. Replicación completa⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Fragmentación de índices
* C. Indexación de vistas
* D. Agrupación de columnas

15. ¿Qué técnica evita la sobrecarga de red al enviar solo claves relevantes?

* A. Semijoin⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Hash Join
* C. Sort-Merge Join
* D. Full Join

16. ¿Qué acción debe tomar un nodo si el coordinador falla en 2PC?

* A. Esperar mensaje de recuperación⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Reiniciar sistema
* C. Abortar transacción local
* D. Confirmar commit

17. ¿Qué tipo de almacenamiento guarda copias idénticas en varios sitios?

* A. Replicación⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Indexación extendida
* C. Hash partitioning
* D. Join distribuido

18. ¿Qué garantiza la transparencia de ubicación en bases distribuidas?

* A. El usuario no necesita saber dónde están los datos⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Los datos están centralizados
* C. Las tablas son estáticas
* D. Se usan bases OLAP

19. ¿Cuál es el objetivo del protocolo de quorum en concurrencia?

* A. Asegurar consistencia mediante mayoría de votos⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Minimizar consultas
* C. Distribuir los datos equitativamente
* D. Evitar backups innecesarios

20. ¿Qué combinación de quorum permite simular protocolo sesgado?

* A. Lectura menor que escritura⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Lectura igual a escritura
* C. Escritura menor que lectura
* D. Lectura y escritura disjuntas

---

## 📊 DATA WAREHOUSING Y OLAP

21. ¿Qué característica NO es propia de un DW?

* A. Volatilidad⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Orientación a temas
* C. Integración
* D. No volatilidad

22. ¿Qué elemento almacena métricas cuantificables en un modelo dimensional?

* A. Tabla de hechos⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Tabla de dimensiones
* C. Vista materializada
* D. Índice OLAP

23. ¿Cuál de los siguientes representa un uso de OLAP?

* A. Análisis de ventas históricas⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Inserción de facturas en línea
* C. Validación de login
* D. Autenticación de usuarios

24. ¿Cuál es una diferencia entre OLTP y OLAP?

* A. OLAP realiza análisis y OLTP transacciones rápidas⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. OLAP permite múltiples escrituras
* C. OLTP tiene esquemas estrella
* D. OLTP es orientado a columnas

25. ¿Qué estructura usa el esquema estrella?

* A. Tabla de hechos central y dimensiones desnormalizadas⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Dimensiones en árbol
* C. Claves externas cruzadas
* D. Fragmentación horizontal

26. ¿Qué mide una tabla de hechos?

* A. Eventos de negocio con medidas numéricas⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Jerarquías semánticas
* C. Claves primarias
* D. Accesos concurrentes

27. ¿Qué representa un cubo OLAP?

* A. Estructura multidimensional de análisis⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Consulta SQL plana
* C. Join lineal
* D. Índice bidimensional

28. ¿Qué técnica permite resumir información de un cubo?

* A. Drill-up⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Drill-down
* C. Slice
* D. Pivot

29. ¿Qué operación OLAP permite ver solo un subconjunto de valores?

* A. Slice⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Dice
* C. Drill-up
* D. Roll-up

30. ¿Qué significa ETL en un DW?

* A. Extract, Transform, Load⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Extend, Translate, Limit
* C. Evaluate, Transfer, Locate
* D. Extract, Test, Loop

---

## 🗃️ BIG DATA Y NOSQL

31. ¿Qué propiedad describe la escalabilidad horizontal?

* A. Agregar nodos al sistema⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Incrementar RAM
* C. Optimizar una sola CPU
* D. Reducir consultas

32. ¿Cuál de estas tecnologías está más asociada a Big Data?

* A. Hadoop⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. MySQL
* C. SQLite
* D. Access

33. ¿Cuál de estas afirmaciones es falsa respecto a NoSQL?

* A. Usa solo datos estructurados⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Admite esquemas flexibles
* C. Se adapta bien a escalabilidad horizontal
* D. Puede trabajar con documentos JSON

34. ¿Cuál es una de las V del Big Data?

* A. Variedad⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Validación
* C. Visibilidad
* D. Veracidad

35. ¿Qué tipo de BD NoSQL almacena datos como clave-valor?

* A. Key-Value Store⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Document Store
* C. Graph Store
* D. Column Family

36. ¿Qué motor es común en procesamiento distribuido Big Data?

* A. MapReduce⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. SQL Server
* C. PostgreSQL
* D. MongoDB

37. ¿Qué significa que una base NoSQL sea eventualmente consistente?

* A. Los datos pueden no reflejar inmediatamente su último estado⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. No se requiere confirmación de escritura
* C. No pueden realizar lecturas
* D. El modelo es siempre transaccional

38. ¿Qué es 'sharding' en bases NoSQL?

* A. División horizontal de datos entre nodos⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Compresión de datos
* C. Replicación por columnas
* D. Reducción de joins

39. ¿Qué tipo de NoSQL es ideal para relaciones sociales complejas?

* A. Base de datos de grafos⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Columnar
* C. Claves-valor
* D. Documental

40. ¿Qué propiedad se busca maximizar en Big Data?

* A. Velocidad de procesamiento⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
* B. Normalización
* C. Uso de joins
* D. Lectura secuencial

41. ¿Cuál es el objetivo principal de la normalización en bases de datos relacionales?

* A. Eliminar redundancias y asegurar integridad de datos                                                                                  
* B. Mejorar la velocidad de red
* C. Aumentar la cantidad de joins
* D. Reducir el tamaño de las claves

42. ¿Qué representa una clave primaria en un modelo relacional?

* A. Un identificador único para cada fila                                                                                  
* B. Un atributo opcional
* C. Un índice secundario
* D. Un valor calculado

43. ¿Cuál es la característica de la Segunda Forma Normal (2NF)?

* A. Elimina dependencias parciales de la clave primaria                                                                                  
* B. Permite valores no atómicos
* C. Elimina dependencias transitivas
* D. Permite claves compuestas

44. ¿Qué tipo de dependencia funcional existe si un atributo depende solo de una parte de una clave compuesta?

* A. Dependencia parcial                                                                                  
* B. Dependencia total
* C. Dependencia transitiva
* D. Dependencia trivial

45. ¿Qué operación de álgebra relacional corresponde al filtrado de filas en SQL?

* A. Selección (σ)                                                                                  
* B. Proyección (π)
* C. Unión (∪)
* D. Producto cartesiano (×)

46. ¿Cuál de las siguientes consultas SQL utiliza una función de ventana?

* A. SELECT nombre, RANK() OVER (ORDER BY salario DESC) FROM empleados;                                                                                  
* B. SELECT COUNT(*) FROM empleados;
* C. SELECT * FROM empleados WHERE salario > 1000;
* D. SELECT nombre FROM empleados;

47. ¿Qué propiedad del álgebra relacional permite combinar filas de dos tablas según una condición?

* A. Join (⨝)                                                                                  
* B. Proyección (π)
* C. Unión (∪)
* D. Diferencia (−)

48. ¿Qué significa la propiedad de atomicidad en una transacción?

* A. Todas las operaciones se completan o ninguna                                                                                  
* B. Los datos se replican automáticamente
* C. Se permite acceso concurrente
* D. Se asegura la consistencia

49. ¿Cuál es la función principal de una tabla de hechos en un Data Warehouse?

* A. Almacenar métricas cuantificables y claves foráneas                                                                                  
* B. Describir dimensiones
* C. Mantener datos históricos
* D. Gestionar usuarios

50. ¿Qué herramienta del ecosistema Hadoop permite consultas SQL sobre grandes volúmenes de datos?

* A. Hive                                                                                  
* B. Pig
* C. Flume
* D. Sqoop
