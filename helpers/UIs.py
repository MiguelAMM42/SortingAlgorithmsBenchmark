import streamlit as st
from helpers.variables import sizes, style, algorithmsDict
from helpers.plots import *


def ScatterPlotEnergyTimeUI(completeDF, meanDF):
    col1, col2, col3 = st.columns(3)

    with col1:
        optionSizeSPET = st.selectbox('Select input size', sizes, key="scatterplot_input_size")
    with col2:
        optionAlgSPET = st.selectbox('Select algorithm', tuple(algorithmsDict.keys()), key="scatterplot_algorithm_energy_time")
    with col3:
        optionStyleSPET = st.selectbox('Select style', style, key="scatterplot_style")

    if optionStyleSPET == "All Values":
        showDF = completeDF
    else:
        showDF = meanDF

    showScatterPlotEnergyTime(showDF, optionSizeSPET, optionAlgSPET, optionStyleSPET)


def BarPlotTimeSizeUI(completeDF):
    optionAlgBPTS = st.selectbox('Select algorithm', tuple(algorithmsDict.keys()), key="barplot_algorithm_time_size")

    # using completeDF or meanDF gives the same result
    showDF = completeDF

    showBarPlotTimeSize(showDF, optionAlgBPTS)


def BarPlotEnergySizeUI(completeDF):
    optionAlgBPES = st.selectbox('Select algorithm', tuple(algorithmsDict.keys()), key="barplot_algorithm_energy_size")

    # using completeDF or meanDF gives the same result
    showDF = completeDF

    showBarPlotEnergySize(showDF, optionAlgBPES)


def BarLinePlotLanguageEnergyTimeUI(meanDF):
    col1, col2 = st.columns(2)

    with col1:
        optionAlgBLPLET = st.selectbox('Select algorithm', tuple(algorithmsDict.keys()), key="barlineplot_algorithm_energy_time")
    with col2:
        optionSizeBLPLET = st.selectbox('Select input size', sizes, key="barlineplot_algorithm_size")

    showBarLinePlotLanguageEnergyTime(meanDF, optionSizeBLPLET, optionAlgBLPLET)