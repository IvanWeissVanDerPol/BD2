# Índice de Temas

1. [Índices](01_Indices.md)
2. [Organización Física de Archivos](02_Organizacion_Fisica_Archivos.md)
3. [Medidas de Rendimiento de Discos](03_Medidas_Rendimiento_Discos.md)
4. [Niveles RAID](04_Niveles_RAID.md)
5. [Árboles B y B+](05_Arboles_B_Bplus.md)
6. [Algoritmos de Búsqueda](06_Algoritmos_Busqueda.md)
7. [Procesamiento de Consultas](07_Procesamiento_Consultas.md)
8. [Modelado Multidimensional](08_Modelado_Multidimensional.md)
9. [Transacciones (ACID)](09_Transacciones_ACID.md)
10. [Concurrencia](10_Concurrencia.md)
11. [Protocolos Distribuidos](11_Protocolos_Distribuidos.md)
12. [Almacenamiento Distribuido](12_Almacenamiento_Distribuido.md)
13. [Optimización de Consultas](13_Optimizacion_Consultas.md)
14. [Normalización y Dependencias Funcionales](14_Normalizacion_Dependencias_Funcionales.md)
15. [Modelado ER y SQL](15_Modelado_ER_SQL.md)

<!-- Script para cargar automáticamente el contenido de los archivos -->
<script>
document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('a');
    
    links.forEach(link => {
        fetch(link.getAttribute('href'))
            .then(response => response.text())
            .then(content => {
                const section = document.createElement('section');
                section.id = link.getAttribute('href').replace('.md', '');
                section.innerHTML = marked.parse(content);
                document.body.appendChild(section);
            })
            .catch(error => console.error('Error cargando el archivo:', error));
    });
});
</script>