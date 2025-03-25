#!/usr/bin/env python
# coding: utf-8

"""
Script para combinar archivos Markdown en un solo documento
"""

import os


def create_combined_markdown():
    # Lista de archivos a combinar en orden
    files = [
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
        "15_Modelado_ER_SQL.md",
    ]

    # Encabezado del libro
    header = """# Bases de Datos Avanzadas - Libro Completo

Este libro reúne todos los temas relacionados con Bases de Datos Avanzadas en un solo lugar.

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

"""

    # Crear archivo combinado
    with open("LibroCompleto_Python.md", "w", encoding="utf-8") as outfile:
        # Escribir encabezado
        outfile.write(header)

        # Procesar cada archivo
        for i, file in enumerate(files):
            chapter_num = i + 1

            # Extraer título del nombre del archivo
            title = os.path.splitext(file)[0]
            title = title.split("_", 1)[1] if "_" in title else title
            title = title.replace("_", " ")

            # Escribir encabezado del capítulo
            outfile.write(f"\n## {chapter_num}. {title}\n\n")

            # Leer y escribir contenido del archivo
            try:
                with open(file, "r", encoding="utf-8") as infile:
                    content = infile.read()
                    outfile.write(content)
                    outfile.write("\n\n")
            except UnicodeDecodeError:
                try:
                    # Intentar con otra codificación
                    with open(file, "r", encoding="latin-1") as infile:
                        content = infile.read()
                        outfile.write(content)
                        outfile.write("\n\n")
                except Exception as e:
                    outfile.write(f"Error al leer el archivo {file}: {str(e)}\n\n")
            except Exception as e:
                outfile.write(f"Error al leer el archivo {file}: {str(e)}\n\n")

    print(f"Libro completo creado exitosamente en: LibroCompleto_Python.md")


if __name__ == "__main__":
    create_combined_markdown()
