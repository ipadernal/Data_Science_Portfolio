# Credit Card Default Features
## Credit Risk Modeling: Default Prediction with Logistic Regression

### Project Goal
Developed and evaluated a machine learning model to accurately predict the probability of credit card default, minimizing financial losses associated with high-risk customers.

### Key Achievements

* Achieved **90.73% accuracy** using Logistic Regression for binary classification of cardholder default risk.
* Quantified risk drivers (model coefficients), identifying **derogatory reports (MAJORDRG, MINORDRG)** as the strongest positive predictors of default.
* Optimized the model's decision threshold (from 50% to **20%**) to strategically reduce critical **False Negative** errors (customers who default but were predicted safe).
* Employed a confusion matrix and probability scoring (`predict_proba`) to establish a risk-based framework.

### Technologies & Tools

* **Language:** Python
* **Libraries:** scikit-learn, Pandas
* **Methods:** Logistic Regression, `StandardScaler`, Threshold Optimization

---
*Data Source: [Kaggle Credit Data](https://www.kaggle.com/datasets/surekharamireddy/credit-data)*