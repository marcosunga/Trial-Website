import streamlit as st 
from prediction import show_predict_page
from explore import show_explore_page

# Page config
st.set_page_config(
    page_title="Dev Salary Predictor",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar style
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color: #0d1b2a;
        color: white;
    }
    [data-testid="stSidebar"] .css-1d391kg {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main app style
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
    }
    .stButton>button {
        color: white;
        background-color: #1d3557;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #457b9d;
    }
    .stSlider .st-bf {
        color: #1d3557;
    }
    .stSelectbox label {
        font-weight: 600;
    }
    h1 {
        color: #1d3557;
    }
    h3 {
        color: #1d3557;
    }
    .stMarkdown {
        font-family: 'Segoe UI', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar options
st.sidebar.title("🔍 Navigation")
page = st.sidebar.selectbox("Explore or Predict", ("Predict", "Explore"))

# Routing
if page == "Predict":
    show_predict_page()
else:
    show_explore_page()
