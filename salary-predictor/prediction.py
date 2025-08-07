import streamlit as st
import pickle
import numpy as np

def load_model():
    with open("salary-predictor/saved_steps.pkl", "rb") as file:
        data = pickle.load(file)
    return data

data = load_model()
regressor = data["model"]
le_education = data["le_education"]
le_country = data["le_country"]

def clean_education(x):
    if "Bachelor’s degree" in x:
        return "Bachelor’s degree"
    if "Master’s degree" in x:
        return "Master’s degree"
    if "Professional degree" in x or "Other doctoral" in x:
        return "Post grad"
    return "Less than a Bachelor's"

def show_predict_page():
    st.title("Software Developer Salary Prediction 💼")

    st.write("""### Please provide some information to predict your salary""")

    countries = (
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
    )

    education_levels = (
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )

    experience_levels = [str(i) for i in range(0, 51)]  # 0 to 50 years

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education_levels)
    experience = st.slider("Years of Experience", 0, 50, 3)

    ok = st.button("Calculate Salary")
    if ok:
        # Clean the education input before transforming
        cleaned_education = clean_education(education)

        X = np.array([[country, cleaned_education, str(experience)]])
        X[:, 0] = le_country.transform(X[:, 0])
        X[:, 1] = le_education.transform(X[:, 1])
        X = X.astype(float)

        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is: ${salary[0]:,.2f}")
