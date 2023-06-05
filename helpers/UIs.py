import streamlit as st
from helpers.variables import sizes, style, algorithmsDict, languages, languagesCompile
from helpers.plots import *
from helpers.multicriteriaDecisionMaking import *


# change all the UIs to have the have default values for the selectboxes

def ScatterPlotEnergyTimeUI(completeDF, meanDF,typeSection, typePowercap):
    col1, col2, col3 = st.columns(3)

    optionAlgSPET, optionSizeSPET, optionStyleSPET = None, None, None

    with col1:
        optionSizeSPET = st.selectbox('Select input size', sizes, key="scatterplot_input_size"+typeSection+typePowercap)
    with col2:
        optionAlgSPET = st.selectbox('Select algorithm', tuple(algorithmsDict.keys()), key="scatterplot_algorithm_energy_time"+typeSection+typePowercap)
    with col3:
        optionStyleSPET = st.selectbox('Select style', style, key="scatterplot_style"+typeSection+typePowercap)

    if optionStyleSPET == "All Values":
        showDF = completeDF
    else:
        showDF = meanDF

    showScatterPlotEnergyTime(showDF, optionSizeSPET, optionAlgSPET, optionStyleSPET)


def BarPlotTimeSizeUI(completeDF,typeSection, typePowercap):

    optionAlgBPTS = None

    optionAlgBPTS = st.selectbox('Select algorithm', tuple(algorithmsDict.keys()), key="barplot_algorithm_time_size"+typeSection+typePowercap)

    # using completeDF or meanDF gives the same result
    showDF = completeDF

    showBarPlotTimeSize(showDF, optionAlgBPTS)


def BarPlotEnergySizeUI(completeDF,typeSection, typePowercap):

    optionAlgBPES = None

    optionAlgBPES = st.selectbox('Select algorithm', tuple(algorithmsDict.keys()), key="barplot_algorithm_energy_size"+typeSection+typePowercap)

    # using completeDF or meanDF gives the same result
    showDF = completeDF

    showBarPlotEnergySize(showDF, optionAlgBPES)


def BarLinePlotLanguageEnergyTimeUI(meanDF,typeSection, typePowercap):
    col1, col2 = st.columns(2)

    optionAlgBLPLET, optionSizeBLPLET = None, None

    with col1:
        optionAlgBLPLET = st.selectbox('Select algorithm', tuple(algorithmsDict.keys()), key="barlineplot_algorithm_energy_time"+typeSection+typePowercap)
    with col2:
        optionSizeBLPLET = st.selectbox('Select input size', sizes, key="barlineplot_energy_size"+typeSection+typePowercap)

    showBarLinePlotLanguageEnergyTime(meanDF, optionSizeBLPLET, optionAlgBLPLET)


def BarLinePlotLanguageEnergyMemoryUI(meanDF,typeSection, typePowercap):
    col1, col2 = st.columns(2)

    optionAlgBLPLEM, optionSizeBLPLEM = None, None

    with col1:
        optionAlgBLPLEM = st.selectbox('Select algorithm', tuple(algorithmsDict.keys()), key="barlineplot_algorithm_energy_memory"+typeSection+typePowercap)
    with col2:
        optionSizeBLPLEM = st.selectbox('Select input size', sizes, key="barlineplot_energy_memory"+typeSection+typePowercap)

    showBarLinePlotLanguageEnergyMemory(meanDF, optionSizeBLPLEM, optionAlgBLPLEM)



def BarPlotTimeLanguageUI(completeDF,typeSection, typePowercap):

    optionLangBPTL = None
    
    if typeSection == "compile":
        optionLangBPTL = st.selectbox('Select language',languagesCompile, key="barplot_language_time"+typeSection+typePowercap)
    else:
        optionLangBPTL = st.selectbox('Select language',languages, key="barplot_language_time"+typeSection+typePowercap)

    showBarPlotTimeLanguage(completeDF, optionLangBPTL)


def BarPlotEnergyLanguageUI(completeDF,typeSection, typePowercap):

    optionLangBPTE = None

    if typeSection == "compile":
        optionLangBPTE = st.selectbox('Select language',languagesCompile, key="barplot_language_energy"+typeSection+typePowercap)
    else:
        optionLangBPTE = st.selectbox('Select language',languages, key="barplot_language_energy"+typeSection+typePowercap)

    showBarPlotEnergyLanguage(completeDF, optionLangBPTE)



def BarPlotMemoryLanguageUI(completeDF,typeSection, typePowercap):

    optionLangBPML = None

    if typeSection == "compile":
        optionLangBPML = st.selectbox('Select language',languagesCompile, key="barplot_language_memory"+typeSection+typePowercap)
    else:
        optionLangBPML = st.selectbox('Select language',languages, key="barplot_language_memory"+typeSection+typePowercap)

    showBarPlotMemoryLanguage(completeDF, optionLangBPML)


def BarLinePlotLanguageEnergyTimePerAlgorithmUI(meanDF,typeSection, typePowercap):
    col1, col2 = st.columns(2)

    optionLangBLPLET, optionSizeBLPLEM = None, None

    with col1:
        if typeSection == "compile":
            optionLangBLPLET = st.selectbox('Select language', languagesCompile, key="barlineplot_language_energy_time"+typeSection+typePowercap)
        else:
            optionLangBLPLET = st.selectbox('Select language', languages, key="barlineplot_language_energy_time"+typeSection+typePowercap)
    with col2:
        optionSizeBLPLEM = st.selectbox('Select input size', sizes, key="barlineplot_energy_time"+typeSection+typePowercap)
        
    showBarLinePlotLanguageEnergyTimePerAlgorithm(meanDF, optionSizeBLPLEM, optionLangBLPLET)


def BarLinePlotLanguageEnergyMemoryPerAlgorithmUI(meanDF,typeSection, typePowercap):
    col1, col2 = st.columns(2)

    optionLangBLPLEM, optionSizeBLPLEM = None, None

    with col1:
        if typeSection == "compile":
            optionLangBLPLEM = st.selectbox('Select language', languagesCompile, key="barlineplot_language_energy_memory"+typeSection+typePowercap)
        else:
            optionLangBLPLEM = st.selectbox('Select language', languages, key="barlineplot_language_energy_memory"+typeSection+typePowercap)
    with col2:
        optionSizeBLPLEM = st.selectbox('Select input size', sizes, key="barlineplot_energy_memory_language"+typeSection+typePowercap)
        
    showBarLinePlotLanguageEnergyMemoryPerAlgorithm(meanDF, optionSizeBLPLEM, optionLangBLPLEM)


def BarLinePlotLanguageEnergyTimePerSizeUI(meanDF,typeSection, typePowercap):
    col1, col2 = st.columns(2)

    optionAlgBLPLET, optionLangBLPLET = None, None

    with col1:
        if typeSection == "compile":
            optionLangBLPLET = st.selectbox('Select language', languagesCompile, key="barlineplot_language_energy_time_size"+typeSection+typePowercap)
        else:
            optionLangBLPLET = st.selectbox('Select language', languages, key="barlineplot_language_energy_time_size"+typeSection+typePowercap)
    with col2:
        optionAlgBLPLET = st.selectbox('Select algorithm', tuple(algorithmsDict.keys()), key="barlineplot_energy_time_size"+typeSection+typePowercap)
        
    showBarLinePlotLanguageEnergyTimePerSize(meanDF, optionAlgBLPLET, optionLangBLPLET)


def BarLinePlotLanguageEnergyMemoryPerSizeUI(meanDF,typeSection, typePowercap):
    col1, col2 = st.columns(2)

    optionAlgBLPLEM, optionLangBLPLEM = None, None

    with col1:
        if typeSection == "compile":
            optionLangBLPLEM = st.selectbox('Select language', languagesCompile, key="barlineplot_language_energy_memory_size"+typeSection+typePowercap)
        else:
            optionLangBLPLEM = st.selectbox('Select language', languages, key="barlineplot_language_energy_memory_size"+typeSection+typePowercap)
    with col2:
        optionAlgBLPLEM = st.selectbox('Select algorithm', tuple(algorithmsDict.keys()), key="barlineplot_energy_memory_language_size"+typeSection+typePowercap)

    showBarLinePlotLanguageEnergyMemoryPerSize(meanDF, optionAlgBLPLEM, optionLangBLPLEM)


def DataInfoUI(completeDF,meanDF):
    st.subheader("Dataframe with complete data")
    st.dataframe(completeDF)
    st.subheader("Dataframe with mean values")
    st.dataframe(meanDF)

def ParetoUI(meanDF,ieeeDF,typeSection, typePowercap):

    optionPareto = st.selectbox('How do you want to see the pareto?', ('By Language', 'By Algorithm'), key="pareto_option"+typeSection+typePowercap)

    if optionPareto == "By Language":
        col1, col2, col3 = st.columns(3)

        optionAlgPareto, optionSizePareto = None, None

        with col1:
            optionAlgPareto = st.selectbox('Select algorithm', tuple(algorithmsDict.keys()), key="pareto_algorithm"+typeSection+typePowercap)
        with col2:
            optionSizePareto = st.selectbox('Select input size', sizes, key="pareto_size_alg"+typeSection+typePowercap)
        with col3:
            optionScore = st.selectbox('Consider the 2022 IEEE Score?', ('Yes', 'No'), key="pareto_score"+typeSection+typePowercap)


        showParetoAlg(meanDF,ieeeDF,optionAlgPareto,optionSizePareto,optionScore)
    
    else:

        col1, col2 = st.columns(2)

        optionLangPareto, optionSizePareto = None, None

        with col1:
            if typeSection == "compile":
                optionLangPareto = st.selectbox('Select language', languagesCompile, key="pareto_language"+typeSection+typePowercap)
            else:
                optionLangPareto = st.selectbox('Select language', languages, key="pareto_language"+typeSection+typePowercap)
        with col2:
            optionSizePareto = st.selectbox('Select input size', sizes, key="pareto_size_lang"+typeSection+typePowercap)

        showParetoLang(meanDF,optionLangPareto,optionSizePareto)


def PrometheeUI(meanDF,ieeeDF,typeSection, typePowercap):

    # will be edited

    # add the scoring from IEEE

    meanDF = meanDF[meanDF['Size'] == 25000]
    meanDF = meanDF[meanDF['Algorithm'] == 'bubblesort']

    df = pd.DataFrame(columns=['Language', 'Energy', 'Time', 'Memory'])
    df['Language'] = meanDF['Language']
    df['Energy'] = meanDF['Package']
    df['Time'] = meanDF['Time(sec)']
    df['Memory'] = meanDF['Memory(MB)']

    dict = {}

    # for each langauge create list with values of energy, time and memory
    for index, row in df.iterrows():
        if row['Language'] not in dict:
            dict[row['Language']] = []
        dict[row['Language']] += [row['Energy'], row['Time'], row['Memory']]


    showPromethee(dict,[0.1,0.8,0.1],["min","min","min"])

    

