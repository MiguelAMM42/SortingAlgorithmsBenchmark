import streamlit as st
import pandas as pd
import os
import plotly.express as px


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

__path__ = os.path.join(APP_ROOT, f"../static/clean.csv")
with open(__path__, "r") as fCSV:
    df = pd.read_csv(fCSV)


st.title("Sorting Algorithms Benchmarking")
