import streamlit as st
import pandas as pd
import os
from helpers.plots import *
from helpers.UIs import *


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

__completePath__ = os.path.join(APP_ROOT, f"../static/results/no_powercap/algorithms_clean.csv")
__meanPath__ = os.path.join(APP_ROOT, f"../static/results/no_powercap/algorithms_averages.csv")
with open(__completePath__, "r") as fCSVComplete:
    completeDF = pd.read_csv(fCSVComplete)
with open(__meanPath__, "r") as fCSVMean:
    meanDF = pd.read_csv(fCSVMean)

# ---------------------------------------------------- #


st.title("Sorting Algorithms Benchmarking")

st.header("Main Plots")

ScatterPlotEnergyTimeUI(completeDF, meanDF)

st.divider()

st.header("Comparing Algorithms")

st.subheader("By Time")

BarPlotTimeSizeUI(completeDF)

st.subheader("By Energy Consumption")

BarPlotEnergySizeUI(completeDF)

st.subheader("By Energy and Time")

BarLinePlotLanguageEnergyTimeUI(meanDF)










    

