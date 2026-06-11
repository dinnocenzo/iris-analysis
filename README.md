# Iris Dataset Analysis

A Python-based exploratory data analysis (EDA) of the classic Iris dataset, featuring descriptive statistics, correlation analysis, and publication-quality visualizations.

## Overview

The [Iris dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set) contains 150 samples from three species of iris flowers (*Setosa*, *Versicolor*, and *Virginica*). Each sample records four morphological measurements: sepal length, sepal width, petal length, and petal width (all in centimeters).

This project loads the dataset directly from scikit-learn, performs a full column-level analysis, computes the correlation matrix, and exports two charts:

| Output file | Description |
|---|---|
| `iris_correlation.png` | Heatmap of Pearson correlations between all numeric features |
| `iris_scatter_matrix.png` | Scatter matrix colored by species |

## Key Findings

| Feature pair | Correlation | Interpretation |
|---|---|---|
| petal length ↔ petal width | **0.963** | Near-perfect positive correlation |
| sepal length ↔ petal length | 0.872 | Strong positive correlation |
| sepal length ↔ petal width | 0.818 | Strong positive correlation |
| sepal width ↔ petal length | -0.428 | Moderate inverse correlation |

## Requirements

- Python 3.9+
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:

```bash
git clone https://github.com/dinnocenzo/iris-analysis.git
cd iris-analysis
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the analysis script:

```bash
python iris_analysis.py
```

The script will print a full statistical summary to the console and save both chart files in the current directory.

### Example output

```
=== SHAPE ===
(150, 5)

=== DESCRIPTIVE STATISTICS ===
       sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
count             150.00            150.00             150.00            150.00
mean                5.84              3.06               3.76              1.20
std                 0.83              0.44               1.77              0.76
...

=== CORRELATION MATRIX ===
                   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
sepal length (cm)              1.000            -0.118              0.872             0.818
sepal width (cm)              -0.118             1.000             -0.428            -0.366
petal length (cm)              0.872            -0.428              1.000             0.963
petal width (cm)               0.818            -0.366              0.963             1.000
```

## Project Structure

```
iris-analysis/
├── iris_analysis.py          # Main analysis script
├── iris_correlation.png      # Correlation heatmap
├── iris_scatter_matrix.png   # Scatter matrix by species
├── requirements.txt          # Python dependencies
├── LICENSE                   # MIT License
└── README.md
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
