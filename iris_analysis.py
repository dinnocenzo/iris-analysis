import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Cargar dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Análisis de columnas
print("=== SHAPE ===")
print(df.shape)

print("\n=== TIPOS DE DATOS ===")
print(df.dtypes)

print("\n=== ESTADÍSTICAS DESCRIPTIVAS ===")
print(df.describe().round(2))

print("\n=== VALORES NULOS ===")
print(df.isnull().sum())

print("\n=== DISTRIBUCIÓN DE ESPECIES ===")
print(df['species'].value_counts())

print("\n=== MATRIZ DE CORRELACIÓN ===")
corr = df.drop(columns='species').corr().round(3)
print(corr)

# Gráfico de correlación
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Heatmap de correlación
sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    vmin=-1, vmax=1,
    square=True,
    linewidths=0.5,
    ax=axes[0]
)
axes[0].set_title("Matriz de Correlación — Iris Dataset", fontsize=13, pad=12)

# Pairplot embebido como scatter matrix por especie
colors = {'setosa': '#e74c3c', 'versicolor': '#3498db', 'virginica': '#2ecc71'}
features = iris.feature_names

for i, fx in enumerate(features):
    for j, fy in enumerate(features):
        if i == j:
            continue
        for sp in iris.target_names:
            sub = df[df['species'] == sp]
            axes[1].scatter([], [])  # placeholder — usamos figura separada

plt.tight_layout()
plt.savefig("iris_correlation.png", dpi=150, bbox_inches="tight")
plt.close()

# Scatter matrix por especie
fig2, ax2 = plt.subplots(figsize=(10, 8))
ax2.axis('off')

fig3 = plt.figure(figsize=(12, 10))
fig3.suptitle("Correlaciones por par de variables — Iris (por especie)", fontsize=13, y=1.01)

n = len(features)
palette = {'setosa': '#e74c3c', 'versicolor': '#3498db', 'virginica': '#2ecc71'}

for i, fy in enumerate(features):
    for j, fx in enumerate(features):
        ax = fig3.add_subplot(n, n, i * n + j + 1)
        if i == j:
            for sp in iris.target_names:
                sub = df[df['species'] == sp]
                ax.hist(sub[fx], bins=12, alpha=0.6, color=palette[sp], label=sp)
            ax.set_xlabel(fx.replace(" (cm)", ""), fontsize=7)
        else:
            for sp in iris.target_names:
                sub = df[df['species'] == sp]
                ax.scatter(sub[fx], sub[fy], s=10, alpha=0.7, color=palette[sp])
        ax.tick_params(labelsize=6)
        if j == 0:
            ax.set_ylabel(fy.replace(" (cm)", ""), fontsize=7)

handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=c, markersize=8, label=sp)
           for sp, c in palette.items()]
fig3.legend(handles=handles, loc='upper right', fontsize=9)
fig3.tight_layout()
fig3.savefig("iris_scatter_matrix.png", dpi=150, bbox_inches="tight")
plt.close()

print("\nGráficos guardados: iris_correlation.png  |  iris_scatter_matrix.png")
