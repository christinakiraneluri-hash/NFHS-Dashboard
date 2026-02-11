import streamlit as st
import pandas as pd

# Load data
# Update path if needed
file_path = "All India National Family Health Survey.xlsx"

def load_data():
    return pd.read_excel(file_path)

st.set_page_config(page_title="NFHS Dashboard", layout="wide")

st.title("All India National Family Health Survey Dashboard")

# Load dataset
try:
    df = load_data()
    st.success("Data loaded successfully!")
except Exception as e:
    st.error(f"Failed to load data: {e}")

# Show raw data
if st.checkbox("Show Raw Data"):
    st.dataframe(df)

# Sidebar filters (example)
st.sidebar.header("Filters")
columns = df.columns.tolist()
selected_cols = st.sidebar.multiselect("Select columns to view", columns, default=columns[:5])

st.subheader("Filtered Data")
st.dataframe(df[selected_cols])

# Basic charts
st.subheader("Basic Visualization")
num_cols = df.select_dtypes(include=['int64','float64']).columns.tolist()

if num_cols:
    x_axis = st.selectbox("Select X-axis", num_cols)
    st.line_chart(df[x_axis])
else:
    st.write("No numeric columns available for charting.")
