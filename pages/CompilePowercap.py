import streamlit as st
import pandas as pd
import os
from helpers.plots import *
from helpers.UIs import *


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

__completePath__ = os.path.join(APP_ROOT, f"../static/results/powercap/compile_clean.csv")
__meanPath__ = os.path.join(APP_ROOT, f"../static/results/powercap/compile_averages.csv")
with open(__completePath__, "r") as fCSVComplete:
    completeDF = pd.read_csv(fCSVComplete)
with open(__meanPath__, "r") as fCSVMean:
    meanDF = pd.read_csv(fCSVMean)

# ---------------------------------------------------- #


st.title("Sorting Algorithms Benchmarking :: Algorithms with Powercap")

st.divider()

st.header("Data")

DataInfoUI(completeDF,meanDF)

st.divider()

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

st.subheader("By Energy and Memory Peak Usage")

BarLinePlotLanguageEnergyMemoryUI(meanDF)

st.header("Comparing Languages")

st.subheader("By Time")

BarPlotTimeLanguageUI(completeDF)

st.subheader("By Energy Consumption")

BarPlotEnergyLanguageUI(completeDF)

st.subheader("By Memory Peak Usage")

BarPlotMemoryLanguageUI(completeDF)

st.subheader("By Energy and Time per Algorithm")

BarLinePlotLanguageEnergyTimePerAlgorithmUI(meanDF)

st.subheader("By Energy and Memory Peak Usage per Algorithm")

BarLinePlotLanguageEnergyMemoryPerAlgorithmUI(meanDF)

st.subheader("By Energy and Time per Size")

BarLinePlotLanguageEnergyTimePerSizeUI(meanDF)

st.subheader("By Energy and Memory Peak Usage per Size") #RAM ??? || why

BarLinePlotLanguageEnergyMemoryPerSizeUI(meanDF)
