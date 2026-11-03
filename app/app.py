
import streamlit as st
import joblib
import pandas as pd
from pathlib import Path

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Customer Churn Analytics",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# Load the trained machine learning pipeline
# --------------------------------------------------
MODEL_PATH = (
    Path(__file__).resolve().parents[1]
    / "models"
    / "churn_pipeline.pkl"
)

model = joblib.load(MODEL_PATH)

# Threshold selected during validation
THRESHOLD = 0.40

# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("📊 Customer Churn Analytics")
st.caption("AI-powered customer retention insights")

st.markdown(
    """
    Predict the likelihood of a telecom customer cancelling
    their subscription using a trained machine learning model.
    """
)

st.divider()

# --------------------------------------------------
# Customer information form
# --------------------------------------------------
st.subheader("👤 Customer Profile")
st.write("Enter the customer's information below.")

with st.form("customer_form"):

    st.markdown("#### Personal Information")

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox(
            "Gender",
            ["Female", "Male"]
        )

        senior_citizen = st.selectbox(
            "Senior Citizen",
            ["No", "Yes"]
        )

    with col2:
        partner = st.selectbox(
            "Has a Partner?",
            ["No", "Yes"]
        )

        dependents = st.selectbox(
            "Has Dependents?",
            ["No", "Yes"]
        )

    st.divider()
    st.markdown("#### Subscription Details")

    col3, col4 = st.columns(2)

    with col3:
        tenure = st.number_input(
            "Tenure (months)",
            min_value=0,
            max_value=72,
            value=12,
            step=1
        )

        contract = st.selectbox(
            "Contract Type",
            ["Month-to-month", "One year", "Two year"]
        )

    with col4:
        phone_service = st.selectbox(
            "Phone Service",
            ["Yes", "No"]
        )

        multiple_lines = st.selectbox(
            "Multiple Lines",
            ["No phone service", "No", "Yes"]
        )

    st.divider()
    st.markdown("#### Internet Services")

    col5, col6 = st.columns(2)

    with col5:
        internet_service = st.selectbox(
            "Internet Service",
            ["DSL", "Fiber optic", "No"]
        )

        online_security = st.selectbox(
            "Online Security",
            ["No internet service", "No", "Yes"]
        )

        online_backup = st.selectbox(
            "Online Backup",
            ["No internet service", "No", "Yes"]
        )

        device_protection = st.selectbox(
            "Device Protection",
            ["No internet service", "No", "Yes"]
        )

    with col6:
        tech_support = st.selectbox(
            "Tech Support",
            ["No internet service", "No", "Yes"]
        )

        streaming_tv = st.selectbox(
            "Streaming TV",
            ["No internet service", "No", "Yes"]
        )

        streaming_movies = st.selectbox(
            "Streaming Movies",
            ["No internet service", "No", "Yes"]
        )

    st.divider()
    st.markdown("#### Billing and Payments")

    col7, col8 = st.columns(2)

    with col7:
        paperless_billing = st.selectbox(
            "Paperless Billing",
            ["Yes", "No"]
        )

        payment_method = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ]
        )

    with col8:
        monthly_charges = st.number_input(
            "Monthly Charges ($)",
            min_value=0.0,
            max_value=200.0,
            value=70.0,
            step=1.0
        )

        total_charges = st.number_input(
            "Total Charges ($)",
            min_value=0.0,
            max_value=10000.0,
            value=840.0,
            step=10.0
        )

    submitted = st.form_submit_button(
        "🔍 Predict Churn",
        type="primary",
        use_container_width=True
    )

# --------------------------------------------------
# Prediction
# --------------------------------------------------
if submitted:

    customer = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen": 1 if senior_citizen == "Yes" else 0,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }])

    churn_probability = model.predict_proba(customer)[0, 1]
    is_high_risk = churn_probability >= THRESHOLD

    st.divider()
    st.subheader("📈 Prediction Results")

    result_col1, result_col2 = st.columns(2)

    with result_col1:
        st.metric(
            "Estimated Churn Probability",
            f"{churn_probability:.1%}"
        )

    with result_col2:
        st.metric(
            "Risk Classification",
            "High Risk" if is_high_risk else "Low Risk"
        )

    st.progress(float(churn_probability))

    if is_high_risk:
        st.error(
            "⚠️ **High churn risk**\n\n"
            "The model estimates an elevated likelihood that "
            "this customer may cancel their subscription."
        )
    else:
        st.success(
            "✅ **Low churn risk**\n\n"
            "The model estimates a lower likelihood that "
            "this customer may cancel their subscription."
        )

    st.caption(
        f"Classification threshold: {THRESHOLD:.0%}. "
        "This is a model estimate, not a guarantee of customer behavior."
    )

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.divider()

st.caption(
    "Customer Churn Analytics | Machine Learning Portfolio Project"
)
