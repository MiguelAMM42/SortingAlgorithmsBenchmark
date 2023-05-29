import streamlit as st
import pandas as pd
import os
from helpers.variables import algorithms, sizes, style
from helpers.plots import showScatterPlot



APP_ROOT = os.path.dirname(os.path.abspath(__file__))

__completePath__ = os.path.join(APP_ROOT, f"../results/no_powercap/algorithms_clean.csv")
__meanPath__ = os.path.join(APP_ROOT, f"../results/no_powercap/algorithms_averages.csv")
with open(__completePath__, "r") as fCSVComplete:
    completeDF = pd.read_csv(fCSVComplete)
with open(__meanPath__, "r") as fCSVMean:
    meanDF = pd.read_csv(fCSVMean)

st.title("Sorting Algorithms Benchmarking")


col1, col2, col3 = st.columns(3)

with col1:
    optionSize = st.selectbox('What input size do you want to see?', sizes)
with col2:
    optionAlg = st.selectbox('What algorithm do you want to see?', algorithms)
with col3:
    optionStyle = st.selectbox('What style do you want to see?', style)


if optionStyle == "Complete":
    showDF = completeDF
else:
    showDF = meanDF

showScatterPlot(showDF, optionSize, optionAlg)


    

