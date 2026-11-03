

\# Customer Churn Prediction \& Analysis System



An end-to-end Machine Learning project that analyzes customer data and predicts the likelihood of customer churn in a telecommunications company.



\## Project Overview



Customer churn is a major challenge for subscription-based businesses. This project uses machine learning techniques to identify customers who are more likely to cancel their subscriptions.



The project includes data exploration, preprocessing, model training, evaluation, and an interactive web application built with Streamlit.



\## Dataset



The project uses the IBM Telco Customer Churn dataset.



\- 7,043 customer records

\- 19 input features

\- Target variable: Churn (Yes/No)



\## Technologies Used



\- Python

\- Pandas

\- NumPy

\- Matplotlib

\- Seaborn

\- Scikit-learn

\- Streamlit

\- Joblib

\- Jupyter Notebook



\## Machine Learning Workflow



1\. Data loading and exploration

2\. Data cleaning and preprocessing

3\. Feature encoding and scaling

4\. Train-test splitting with stratification

5\. Machine learning pipeline development

6\. Model training and comparison

7\. Hyperparameter tuning

8\. Decision threshold selection using validation data

9\. Model evaluation on the test set

10\. Model serialization using Joblib



\## Models Evaluated



\- Logistic Regression

\- Tuned Logistic Regression

\- Decision Tree

\- Random Forest



Logistic Regression was selected as the final model based on its overall evaluation results.



\## Model Performance



Final Logistic Regression test-set results at a 0.40 decision threshold:



| Metric | Score |

|---|---:|

| Accuracy | 77.7% |

| Precision (Churn) | 57.0% |

| Recall (Churn) | 66.8% |

| F1-score (Churn) | 61.4% |

| ROC-AUC | 84.2% |



\## Streamlit Application



The project includes an interactive web application where users can:



\- Enter customer information

\- View estimated churn probability

\- See customer churn risk classification



The application uses the saved machine learning pipeline to generate predictions.



\## Project Structure



```text

customer-churn-prediction/

│

├── app/

│   └── app.py

│

├── data/

│   └── WA\_Fn-UseC\_-Telco-Customer-Churn.csv

│

├── models/

│   └── churn\_pipeline.pkl

│

├── notebooks/

│   ├── 01\_data\_exploration.ipynb

│   └── 02\_model\_pipeline.ipynb

│

├── requirements.txt

├── .gitignore

└── README.md

```



\## Installation and Usage



\### 1. Clone the repository



```bash

git clone YOUR\_REPOSITORY\_URL

cd customer-churn-prediction

```



\### 2. Create a virtual environment



```bash

python -m venv .venv

```



\### 3. Activate the environment



Windows PowerShell:



```powershell

.venv\\Scripts\\Activate.ps1

```



\### 4. Install dependencies



```bash

pip install -r requirements.txt

```



\### 5. Run the Streamlit application



```bash

streamlit run app/app.py

```



\## Future Improvements



\- Test the application with additional customer profiles

\- Improve model performance and interpretability

\- Add visual analytics to the Streamlit dashboard

\- Explore additional customer retention insights



\## Author



Computer Science Student | AI \& Data Science



