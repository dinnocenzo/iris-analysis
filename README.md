# Iris Dataset Analysis

Análisis exploratorio del dataset de Iris usando Python.

## ¿Qué hace este proyecto?

- Carga el dataset de Iris desde scikit-learn (150 flores, 3 especies, 4 medidas)
- Muestra estadísticas descriptivas de cada columna
- Calcula la matriz de correlación entre variables
- Genera dos gráficos: heatmap de correlación y scatter matrix por especie

## Resultados principales

| Par de variables | Correlación |
|---|---|
| petal_length ↔ petal_width | **0.963** (muy fuerte) |
| sepal_length ↔ petal_length | 0.872 |
| sepal_width ↔ petal_length | -0.428 (inversa) |

## Archivos

- `iris_analysis.py` — script principal
- `iris_correlation.png` — heatmap de correlación
- `iris_scatter_matrix.png` — scatter matrix por especie

## Requisitos

```
pip install scikit-learn pandas matplotlib seaborn
```

## Ejecutar

```
python iris_analysis.py
```
