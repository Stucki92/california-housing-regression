# 🏠 California Housing – Prédiction des prix immobiliers

Ce projet utilise le dataset **California Housing** pour prédire la valeur médiane des logements à l’aide de modèles de régression linéaire. 

---

## 📂 Contenu

- Exploration des données (EDA)
- Prétraitement (scaling, split)
- Modélisation :
  - Régression linéaire
  - Ridge Regression
  - Lasso Regression
  - Decision Tree Regression
  - Random Forest Regression
  - SVR
  - Gradient Boosting Regression
  - XGBoost Regression
- Évaluation (MSE, R², cross-validation)
- Optimisation des hyperparamètres (`GridSearchCV`)
- Visualisation des prédictions

---

## 🧰 Technologies

- Python 3.11
- [scikit-learn](https://scikit-learn.org/)
- pandas / numpy
- matplotlib / seaborn
- xgboost
- shap

---

## 📊 Résultats

| Modèle                       | R² Score |
|------------------------------|----------|
| LinearRegression             | 0.57     |
| Ridge (best alpha)           | 0.57     |
| Lasso (best alpha)           | 0.58     |
| Decision Tree Regression     | 0.65     |
| Random Forest Regression     | 0.71     |
| SVR                          | 0.75     |
| Gradient Boosting Regression | 0.84     |
| XGBoost Regression           | 0.84     |


> Ces résultats peuvent varier légèrement selon les splits / machines.

---

## 🚀 Pour exécuter ce projet

1. Cloner ce repo :
git clone https://github.com/Stucki92/california-housing-regression.git

2. Installer les dépendances :
pip install -r requirements.txt

3. Lance le notebook :
jupyter notebook housing_california.ipynb

---

## Auteur

Nicolas STUCKI @Stucki92
