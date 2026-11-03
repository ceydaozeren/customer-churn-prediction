# Customer Churn Prediction & Analysis System

An end-to-end Machine Learning project that analyzes customer data and predicts the likelihood of customer churn in the telecommunications industry.

## Project Overview

Customer churn is a major challenge for subscription-based businesses. Retaining existing customers is often more cost-effective than acquiring new ones.

This project uses machine learning techniques to identify customers who are more likely to cancel their subscriptions.

The project covers the complete machine learning workflow, including data exploration, preprocessing, model development, evaluation, and deployment through an interactive Streamlit web application.

## Dataset

The project uses the IBM Telco Customer Churn dataset.

- **Total records:** 7,043 customers
- **Input features:** 19
- **Target variable:** Churn (Yes/No)

## Technologies & Tools

- **Programming Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn
- **Web Application:** Streamlit
- **Model Serialization:** Joblib
- **Development Environment:** Jupyter Notebook

## Machine Learning Workflow

1. Data loading and exploratory data analysis (EDA)
2. Data cleaning and handling missing values
3. Feature encoding and numerical scaling
4. Stratified train-test splitting
5. Building a machine learning pipeline using Scikit-learn
6. Training and comparing multiple classification algorithms
7. Hyperparameter tuning using GridSearchCV
8. Decision threshold selection using validation data
9. Final model evaluation on unseen test data
10. Saving the trained pipeline using Joblib

## Models Evaluated

The following classification algorithms were implemented and compared:

- Logistic Regression
- Tuned Logistic Regression
- Decision Tree
- Random Forest

**Final Model: Logistic Regression**

Logistic Regression was selected based on its overall performance, particularly its Recall, F1-score, and ROC-AUC results.

## Model Performance

Final Logistic Regression results on the test set using a 0.40 classification threshold:

| Metric | Score |
|---|---:|
| Accuracy | 77.7% |
| Precision (Churn) | 57.0% |
| Recall (Churn) | 66.8% |
| F1-score (Churn) | 61.4% |
| ROC-AUC | 84.2% |

The decision threshold was selected using validation data before evaluating the final model on the test set.

## Streamlit Web Application

An interactive web application was developed using Streamlit.

Users can:

- Enter customer information and subscription details
- Calculate the estimated probability of customer churn
- View the predicted churn risk classification
- Identify customers who may require additional retention attention

The application loads the saved machine learning pipeline and generates predictions based on user-provided customer information.

## Project Structure

```text
customer-churn-prediction/
│
├── app/
│   └── app.py
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── models/
│   └── churn_pipeline.pkl
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   └── 02_model_pipeline.ipynb
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/ceydaozeren/customer-churn-prediction.git

cd customer-churn-prediction
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit application

```bash
streamlit run app/app.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

## Future Improvements

- Test the application with additional customer profiles
- Improve model performance and interpretability
- Add visual analytics and interactive charts
- Explore additional customer retention strategies
