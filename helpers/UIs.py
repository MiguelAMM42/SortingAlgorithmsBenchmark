import streamlit as st
from helpers.variables import sizes, style, algorithmsDict, languages
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
        optionSizeBLPLET = st.selectbox('Select input size', sizes, key="barlineplot_energy_size")

    showBarLinePlotLanguageEnergyTime(meanDF, optionSizeBLPLET, optionAlgBLPLET)


def BarLinePlotLanguageEnergyMemoryUI(meanDF):
    col1, col2 = st.columns(2)

    with col1:
        optionAlgBLPLEM = st.selectbox('Select algorithm', tuple(algorithmsDict.keys()), key="barlineplot_algorithm_energy_memory")
    with col2:
        optionSizeBLPLEM = st.selectbox('Select input size', sizes, key="barlineplot_energy_memory")

    showBarLinePlotLanguageEnergyMemory(meanDF, optionSizeBLPLEM, optionAlgBLPLEM)



def BarPlotTimeLanguageUI(completeDF):
    optionLangBPTL = st.selectbox('Select language',languages, key="barplot_language_time")
    showBarPlotTimeLanguage(completeDF, optionLangBPTL)


def BarPlotEnergyLanguageUI(completeDF):
    optionLangBPTE = st.selectbox('Select language',languages, key="barplot_language_energy")
    showBarPlotEnergyLanguage(completeDF, optionLangBPTE)



def BarPlotMemoryLanguageUI(completeDF):
    optionLangBPML = st.selectbox('Select language',languages, key="barplot_language_memory")
    showBarPlotMemoryLanguage(completeDF, optionLangBPML)


def BarLinePlotLanguageEnergyTimePerAlgorithmUI(meanDF):
    col1, col2 = st.columns(2)

    with col1:
        optionLangBLPLET = st.selectbox('Select language', languages, key="barlineplot_language_energy_time")
    with col2:
        optionSizeBLPLEM = st.selectbox('Select input size', sizes, key="barlineplot_energy_time")
        
    showBarLinePlotLanguageEnergyTimePerAlgorithm(meanDF, optionSizeBLPLEM, optionLangBLPLET)


def BarLinePlotLanguageEnergyMemoryPerAlgorithmUI(meanDF):
    col1, col2 = st.columns(2)

    with col1:
        optionLangBLPLEM = st.selectbox('Select language', languages, key="barlineplot_language_energy_memory")
    with col2:
        optionSizeBLPLEM = st.selectbox('Select input size', sizes, key="barlineplot_energy_memory_language")
        
    showBarLinePlotLanguageEnergyMemoryPerAlgorithm(meanDF, optionSizeBLPLEM, optionLangBLPLEM)


def BarLinePlotLanguageEnergyTimePerSizeUI(meanDF):
    col1, col2 = st.columns(2)

    with col1:
        optionLangBLPLET = st.selectbox('Select language', languages, key="barlineplot_language_energy_time_size")
    with col2:
        optionAlgBLPLET = st.selectbox('Select algorithm', tuple(algorithmsDict.keys()), key="barlineplot_energy_time_size")
        
    showBarLinePlotLanguageEnergyTimePerSize(meanDF, optionAlgBLPLET, optionLangBLPLET)


def BarLinePlotLanguageEnergyMemoryPerSizeUI(meanDF):
    col1, col2 = st.columns(2)

    with col1:
        optionLangBLPLEM = st.selectbox('Select language', languages, key="barlineplot_language_energy_memory_size")
    with col2:
        optionAlgBLPLEM = st.selectbox('Select algorithm', tuple(algorithmsDict.keys()), key="barlineplot_energy_memory_language_size")

    showBarLinePlotLanguageEnergyMemoryPerSize(meanDF, optionAlgBLPLEM, optionLangBLPLEM)