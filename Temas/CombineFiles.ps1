# PowerShell script to combine all Markdown files into a single book
# Create header for the combined file
$header = @"
# Bases de Datos Avanzadas - Libro Completo

Este libro reúne todos los temas relacionados con Bases de Datos Avanzadas.

## Tabla de Contenidos

1. [Índices](#1-índices)
2. [Organización Física de Archivos](#2-organización-física-de-archivos)
3. [Medidas de Rendimiento de Discos](#3-medidas-de-rendimiento-de-discos)
4. [Niveles RAID](#4-niveles-raid)
5. [Árboles B y B+](#5-árboles-b-y-b)
6. [Algoritmos de Búsqueda](#6-algoritmos-de-búsqueda)
7. [Procesamiento de Consultas](#7-procesamiento-de-consultas)
8. [Modelado Multidimensional](#8-modelado-multidimensional)
9. [Transacciones (ACID)](#9-transacciones-acid)
10. [Concurrencia](#10-concurrencia)
11. [Protocolos Distribuidos](#11-protocolos-distribuidos)
12. [Almacenamiento Distribuido](#12-almacenamiento-distribuido)
13. [Optimización de Consultas](#13-optimización-de-consultas)
14. [Normalización y Dependencias Funcionales](#14-normalización-y-dependencias-funcionales)
15. [Modelado ER y SQL](#15-modelado-er-y-sql)

"@

# Ensure UTF-8 encoding without BOM
$utf8NoBomEncoding = New-Object System.Text.UTF8Encoding $false

# Write header to the output file
[System.IO.File]::WriteAllText("LibroCompleto.md", $header, $utf8NoBomEncoding)

# Files to combine in order
$files = @(
    "01_Indices.md",
    "02_Organizacion_Fisica_Archivos.md",
    "03_Medidas_Rendimiento_Discos.md",
    "04_Niveles_RAID.md",
    "05_Arboles_B_Bplus.md",
    "06_Algoritmos_Busqueda.md",
    "07_Procesamiento_Consultas.md",
    "08_Modelado_Multidimensional.md",
    "09_Transacciones_ACID.md",
    "10_Concurrencia.md",
    "11_Protocolos_Distribuidos.md",
    "12_Almacenamiento_Distribuido.md",
    "13_Optimizacion_Consultas.md",
    "14_Normalizacion_Dependencias_Funcionales.md",
    "15_Modelado_ER_SQL.md"
)

# Process each file
for ($i = 0; $i -lt $files.Length; $i++) {
    $file = $files[$i]
    $chapterNum = $i + 1
    
    # Add chapter header
    $chapterTitle = "## $chapterNum. $(([System.IO.Path]::GetFileNameWithoutExtension($file) -replace '\d+_', '') -replace '_', ' ')`n"
    [System.IO.File]::AppendAllText("LibroCompleto.md", $chapterTitle, $utf8NoBomEncoding)
    
    # Append file content
    $content = Get-Content $file -Raw 
    [System.IO.File]::AppendAllText("LibroCompleto.md", $content, $utf8NoBomEncoding)
    
    # Add a newline between chapters
    [System.IO.File]::AppendAllText("LibroCompleto.md", "`n`n", $utf8NoBomEncoding)
}

Write-Host "Libro completo creado exitosamente en: LibroCompleto.md" 