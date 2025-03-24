# 📚 Guía de Estudio BD2

## 1. Índices
- **Índice ordenado:** Ideal para consultas con rangos (ej. fechas).
- **Índice hash:** Ideal para consultas exactas (condiciones de igualdad).
- **Índice bitmap:** Ideal para consultas múltiples simultáneas.

## 2. Organización Física de Archivos
- **Heap:** Registros en cualquier lugar libre (inserción rápida, consultas lentas).
- **Secuencial:** Registros ordenados según clave (buen rendimiento en rangos).
- **Hash:** Registros ubicados según función hash (ideal para consultas puntuales).
- **Agrupación:** Agrupa columnas frecuentes para consultas rápidas.

## 3. Medidas de Rendimiento de Discos
- **Tiempo de acceso:** Tiempo en ubicar y leer/escribir datos.
- **Latencia rotacional:** Tiempo en que el sector deseado pase bajo el cabezal.
- **Tasa de transferencia:** Cantidad de datos transferidos por segundo.
- **Tiempo medio de fallo:** Tiempo hasta fallos significativos del hardware.

## 4. Niveles RAID
- **RAID 0:** Sin redundancia, mejor rendimiento, alta vulnerabilidad.
- **RAID 1:** Redundancia exacta, más seguro, más lento y costoso.
- **RAID 5:** Paridad distribuida, equilibrio entre rendimiento y seguridad.

## 5. Árboles B y B+
- Estructuras eficientes para búsquedas, inserciones y eliminaciones.
- Ideal para mantener índices ordenados por su capacidad balanceada.

## 6. Algoritmos de Búsqueda
- **Lineal:** Tabla desordenada. Costo O(n).
- **Binaria:** Tabla ordenada físicamente. Costo O(log n).
- **Índice primario:** Atributo clave, costo O(1).
- **Índice secundario:** Atributo no clave, coste variable, generalmente O(log n).

## 7. Procesamiento de Consultas
- **Análisis:** Verifica sintaxis y traduce consultas.
- **Optimización:** Selecciona el plan más eficiente.
- **Evaluación:** Ejecuta el plan optimizado usando materialización o pipelining.

## 8. Modelado Multidimensional
- **OLTP (Online Transaction Processing):** Maneja transacciones operacionales frecuentes.
  - Ej.: Sistemas bancarios, ventas en línea.
- **OLAP (Online Analytical Processing):** Analiza grandes volúmenes de datos para toma de decisiones.
  - Ej.: Business Intelligence, Data Warehousing.
- **Tablas de Dimensiones:** Definen características (Clientes, Productos).
- **Tablas de Hechos:** Datos medibles (Ventas, Compras).

## 9. Transacciones (ACID)
- **Atomicidad:** Transacción completa o no ocurre.
- **Consistencia:** Mantiene integridad antes y después.
- **Aislamiento:** Transacciones independientes.
- **Durabilidad:** Cambios permanentes tras confirmación.

## 10. Concurrencia
- **Planificación secuencial:** Transacciones en secuencia una tras otra.
- **Planificación secuenciable:** Equivalente a planificación secuencial.
- **Protocolo 2 fases:** Adquiere y libera bloqueos en fases separadas.

## 11. Protocolos Distribuidos
- **Quorum de Consenso:** Control de lectura/escritura con pesos asignados.
- **C2F (Two-Phase Commit):** Coordinación distribuida para confirmar transacciones.

## 12. Almacenamiento Distribuido
- **Replicación:** Copias exactas en diferentes sitios (alta disponibilidad).
- **Fragmentación:** División horizontal o vertical de datos (mejor rendimiento).

## 13. Optimización de Consultas
- **Álgebra relacional:** Traduce consultas SQL para optimizarlas usando reglas equivalentes.

## 14. Normalización y Dependencias Funcionales
- Elimina redundancias, organiza tablas para evitar anomalías (1FN, 2FN, 3FN).


