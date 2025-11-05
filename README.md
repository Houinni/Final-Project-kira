# Final Project: Bank Marketing Prediction

This project analyzes the **UCI Bank Marketing Dataset** to predict whether a client will subscribe to a term deposit based on demographic and marketing data.  
It was developed as the final project for **CSC293**.

---

## 📊 Overview
The project explores various machine learning models to evaluate prediction performance on a real-world dataset.  
We focus on understanding the **factors influencing customer subscription** and comparing model accuracy and interpretability.

---

## 🧠 Methods and Models
- **Logistic Regression** — Baseline linear model for binary classification  
- **Decision Tree** — Visual, interpretable model to capture non-linear relationships  
- **Random Forest** — Ensemble model improving generalization and accuracy  
- **K-Means Clustering** — Exploratory analysis of client groups  
- **PCA (Principal Component Analysis)** — Dimensionality reduction for visualization

---

## 🗂️ Files in Repository
| File | Description |
|------|--------------|
| `bank-additional-full.csv` | Dataset used for training and testing |
| `bank-names.txt` | Column names for the dataset |
| `logistic_regression.ipynb` | Logistic Regression model implementation |
| `tree.ipynb` | Decision Tree model |
| `random-forest.ipynb` | Random Forest model |
| `random-forest2.ipynb` | Extended Random Forest analysis |
| `Principle-component-analysis.ipynb` | PCA visualization and feature reduction |
| `plot.py` | Plotting and data visualization script |
| `modelCompare.md` | Comparison of model performance and results |
| `CSC293-Final-Project-Poster.pdf` | Final project poster presentation |
| `.png` files | Visualization outputs (feature importance, clusters, etc.) |

---

## ⚙️ Requirements
Install the dependencies with:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
