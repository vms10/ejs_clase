# 🌳 Análisis del arbolado en espacios verdes de CABA

##  Archivo: `semana_04.py`

Este archivo contiene las funciones desarrolladas para analizar el dataset **"Arbolado en espacios verdes"** de la Ciudad Autónoma de Buenos Aires.

---

## 📄 Descripción del dataset

El archivo `arbolado-en-espacios-verdes.csv` incluye información detallada de cada árbol presente en espacios verdes. Algunas columnas importantes:

- `id_arbol`: Identificador único del árbol.
- `altura_tot`: Altura total del árbol (en metros).
- `diametro`: Diámetro del tronco (en cm).
- `nombre_com`: Nombre común de la especie.
- `espacio_ve`: Nombre del parque o espacio verde.
- `origen`: Indica si la especie es "Exótico" o "Nativo/Autóctono".

Las columnas `coord_x` y `coord_y` no fueron incluidas en este análisis.

---

##  Funciones principales

### 1. `arboles_parque(nombre_archivo, nombre_parque)`
Devuelve un diccionario con todos los árboles de un parque específico, donde cada clave es el ID del árbol y cada valor es un diccionario con sus datos (excepto las coordenadas X e Y).

### 2. `arbol_mas_popular(nombre_parque)`
Retorna la especie (nombre común) más frecuente en el parque indicado.

### 3. `n_mas_altos(nombre_parque, n)`
Devuelve una lista con los `n` árboles más altos del parque indicado. Cada elemento contiene el ID y los datos del árbol.

### 4. `altura_promedio(nombre_parque, especie)`
Devuelve la altura promedio de una especie determinada en el parque seleccionado.

---

##  Funciones adicionales para exploración (Ejercicio 5)

### ✅ `parques_mas_arboles(nombre_archivo)`
Devuelve el o los parques con **mayor cantidad total de árboles**.

### ✅ `parques_mas_altos_promedio(nombre_archivo)`
Retorna el/los parques con **mayor altura promedio** entre todos sus árboles.

### ✅ `parques_mas_variedad(nombre_archivo)`
Identifica el/los parques que tienen la **mayor diversidad de especies**.

### ✅ `especie_mas_frecuente(nombre_archivo)`
Devuelve la(s) especie(s) más común(es) en toda la ciudad (sin distinguir parques).

### ✅ `razon_exoticos_nativos(nombre_archivo)`
Calcula la **razón entre árboles exóticos y nativos/autóctonos** presentes en todos los espacios verdes (= exoticos/nativos).


## 📌 Consideraciones

- El código fue desarrollado sin usar `pandas`, utilizando únicamente `csv`, `collections` y estructuras nativas de Python.
- Se ignoran filas sin nombre de parque (`S/D`).
- Para garantizar precisión se normalizan strings (espacios, mayúsculas/minúsculas).

