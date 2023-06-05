import streamlit as st
import pandas as pd
import os
from helpers.plots import *
from helpers.UIs import *


APP_ROOT = os.path.dirname(os.path.abspath(__file__))


__completePath__ = os.path.join(APP_ROOT, f"../static/results/no_powercap/compile_clean.csv")
__meanPath__ = os.path.join(APP_ROOT, f"../static/results/no_powercap/compile_averages.csv")
__ieeePath__ = os.path.join(APP_ROOT, f"../static/IEEESpectrumTopProgrammingLanguages2022.csv")
with open(__completePath__, "r") as fCSVComplete:
    completeDF = pd.read_csv(fCSVComplete)
with open(__meanPath__, "r") as fCSVMean:
    meanDF = pd.read_csv(fCSVMean)
with open(__ieeePath__, "r") as fCSVIEEE:
    ieeeDF = pd.read_csv(fCSVIEEE)

# ---------------------------------------------------- #


st.title("Sorting Algorithms Benchmarking :: Algorithms without Powercap")

st.divider()

st.header("Data")

DataInfoUI(completeDF,meanDF)

st.divider()

st.header("Main Plots")

ScatterPlotEnergyTimeUI(completeDF, meanDF,"_compile_","no_powercap")

st.divider()

st.header("Comparing Algorithms")

st.subheader("By Time")

BarPlotTimeSizeUI(completeDF,"_compile_","no_powercap")

st.subheader("By Energy Consumption")

BarPlotEnergySizeUI(completeDF,"_compile_","no_powercap")

st.subheader("By Energy and Time")

BarLinePlotLanguageEnergyTimeUI(meanDF,"_compile_","no_powercap")

st.subheader("By Energy and Memory Peak Usage")

BarLinePlotLanguageEnergyMemoryUI(meanDF,"_compile_","no_powercap")

st.header("Comparing Languages")

st.subheader("By Time")

BarPlotTimeLanguageUI(completeDF,"_compile_","no_powercap")

st.subheader("By Energy Consumption")

BarPlotEnergyLanguageUI(completeDF,"_compile_","no_powercap")

st.subheader("By Memory Peak Usage")

BarPlotMemoryLanguageUI(completeDF,"_compile_","no_powercap")

st.subheader("By Energy and Time per Algorithm")

BarLinePlotLanguageEnergyTimePerAlgorithmUI(meanDF,"_compile_","no_powercap")

st.subheader("By Energy and Memory Peak Usage per Algorithm")

BarLinePlotLanguageEnergyMemoryPerAlgorithmUI(meanDF,"_compile_","no_powercap")

st.subheader("By Energy and Time per Size")

BarLinePlotLanguageEnergyTimePerSizeUI(meanDF,"_compile_","no_powercap")

st.subheader("By Energy and Memory Peak Usage per Size") #RAM ??? || why

BarLinePlotLanguageEnergyMemoryPerSizeUI(meanDF,"_compile_","no_powercap")

