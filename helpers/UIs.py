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
    
    if typeSection == "_compile_":
        optionLangBPTL = st.selectbox('Select language',languagesCompile, key="barplot_language_time"+typeSection+typePowercap)
    else:
        optionLangBPTL = st.selectbox('Select language',languages, key="barplot_language_time"+typeSection+typePowercap)

    showBarPlotTimeLanguage(completeDF, optionLangBPTL)


def BarPlotEnergyLanguageUI(completeDF,typeSection, typePowercap):

    optionLangBPTE = None

    if typeSection == "_compile_":
        optionLangBPTE = st.selectbox('Select language',languagesCompile, key="barplot_language_energy"+typeSection+typePowercap)
    else:
        optionLangBPTE = st.selectbox('Select language',languages, key="barplot_language_energy"+typeSection+typePowercap)

    showBarPlotEnergyLanguage(completeDF, optionLangBPTE)



def BarPlotMemoryLanguageUI(completeDF,typeSection, typePowercap):

    optionLangBPML = None

    if typeSection == "_compile_":
        optionLangBPML = st.selectbox('Select language',languagesCompile, key="barplot_language_memory"+typeSection+typePowercap)
    else:
        optionLangBPML = st.selectbox('Select language',languages, key="barplot_language_memory"+typeSection+typePowercap)

    showBarPlotMemoryLanguage(completeDF, optionLangBPML)


def BarLinePlotLanguageEnergyTimePerAlgorithmUI(meanDF,typeSection, typePowercap):
    col1, col2 = st.columns(2)

    optionLangBLPLET, optionSizeBLPLEM = None, None

    with col1:
        if typeSection == "_compile_":
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
        if typeSection == "_compile_":
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
        if typeSection == "_compile_":
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
        if typeSection == "_compile_":
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

        optionAlgParetoLang, optionSizeParetoLang, optionScoreLang = None, None, None

        with col1:
            optionAlgParetoLang = st.selectbox('Select algorithm', tuple(algorithmsDict.keys()), key="pareto_algorithm"+typeSection+typePowercap)
        with col2:
            optionSizeParetoLang = st.selectbox('Select input size', sizes, key="pareto_size_alg"+typeSection+typePowercap)
        with col3:
            optionScoreLang = st.selectbox('Consider the 2022 IEEE Score?', ('Yes', 'No'), key="pareto_score"+typeSection+typePowercap)


        showParetoAlg(meanDF,ieeeDF,optionAlgParetoLang,optionSizeParetoLang,optionScoreLang)
    
    else:

        col1, col2 = st.columns(2)

        optionLangParetoAlg, optionSizeParetoAlg = None, None

        with col1:
            if typeSection == "_compile_":
                optionLangParetoAlg = st.selectbox('Select language', languagesCompile, key="pareto_language"+typeSection+typePowercap)
            else:
                optionLangParetoAlg = st.selectbox('Select language', languages, key="pareto_language"+typeSection+typePowercap)
        with col2:
            optionSizeParetoAlg = st.selectbox('Select input size', sizes, key="pareto_size_lang"+typeSection+typePowercap)

        showParetoLang(meanDF,optionLangParetoAlg,optionSizeParetoAlg)


def PrometheeUI(meanDF,ieeeDF,typeSection, typePowercap):

    optionPromethee = st.selectbox('How do you want to see the promethee?', ('By Language', 'By Algorithm'), key="promethee_option"+typeSection+typePowercap)

    if optionPromethee == "By Language":
        col1, col2= st.columns(2)

        optionAlgPromethee, optionSizePromethee = None, None

        with col1:
            optionAlgPromethee = st.selectbox('Select algorithm', tuple(algorithmsDict.keys()), key="promethee_algorithm"+typeSection+typePowercap)
        with col2:
            optionSizePromethee = st.selectbox('Select input size', sizes, key="promethee_size_alg"+typeSection+typePowercap)

        # 4 sliders for the weights
        st.write("Select the weights for the criteria")
        colT, colE, colM, colS = st.columns(4)

        with colT:
            weightTime = st.slider('Time', 0.0, 10.0, 1.0, 0.1, key="promethee_time_Lang"+typeSection+typePowercap)
        with colE:
            weightEnergy = st.slider('Energy', 0.0, 10.0, 1.0, 0.1, key="promethee_energy_Lang"+typeSection+typePowercap)
        with colM:
            weightMemory = st.slider('Memory', 0.0, 10.0, 1.0, 0.1,key="promethee_memory_Lang"+typeSection+typePowercap)
        with colS:
            weightScore = st.slider('Score', 0.0, 10.0, 1.0, 0.1,key="promethee_score_Lang"+typeSection+typePowercap)

        weights = [weightEnergy, weightTime,weightMemory, weightScore]

        showPrometheeAlg(meanDF,ieeeDF,optionAlgPromethee,optionSizePromethee,weights)

    else:

        col1, col2 = st.columns(2)

        optionLangPromethee, optionSizePromethee = None, None

        with col1:
            if typeSection == "_compile_":
                optionLangPromethee = st.selectbox('Select language', languagesCompile, key="promethee_language"+typeSection+typePowercap)
            else:
                optionLangPromethee = st.selectbox('Select language', languages, key="promethee_language"+typeSection+typePowercap)
        with col2:
            optionSizePromethee = st.selectbox('Select input size', sizes, key="promethee_size_lang"+typeSection+typePowercap)

        # 3 sliders for the weights
        st.write("Select the weights for the criteria")
        colT, colE, colM = st.columns(3)

        with colT:  
            weightTime = st.slider('Time', 0.0, 10.0, 1.0, 0.1,key="promethee_time_Alg"+typeSection+typePowercap)
        with colE:
            weightEnergy = st.slider('Energy', 0.0, 10.0, 1.0, 0.1,key="promethee_energy_Alg"+typeSection+typePowercap)
        with colM:
            weightMemory = st.slider('Memory', 0.0, 10.0, 1.0, 0.1,key="promethee_memory_Alg"+typeSection+typePowercap)

        weights = [weightEnergy,weightTime, weightMemory]

        showPrometheeLang(meanDF,optionLangPromethee,optionSizePromethee, weights)


def WeightedSumUI(meanDF,ieeeDF,typeSection, typePowercap):
    optionWeightedSum = st.selectbox('How do you want to see the weighted sum?', ('By Language', 'By Algorithm'), key="weighted_sum_option"+typeSection+typePowercap)

    if optionWeightedSum == "By Language":
        col1, col2= st.columns(2)

        optionAlgWeightedSum, optionSizeWeightedSum = None, None

        with col1:
            optionAlgWeightedSum = st.selectbox('Select algorithm', tuple(algorithmsDict.keys()), key="weighted_sum_algorithm"+typeSection+typePowercap)
        with col2:
            optionSizeWeightedSum = st.selectbox('Select input size', sizes, key="weighted_sum_size_alg"+typeSection+typePowercap)

        # 4 sliders for the weights
        st.write("Select the weights for the criteria")
        colT, colE, colM, colS = st.columns(4)

        with colT:
            weightTime = st.slider('Time', 0.0, 10.0, 1.0, 0.1, key="weighted_sum_time_Lang"+typeSection+typePowercap)
        with colE:
            weightEnergy = st.slider('Energy', 0.0, 10.0, 1.0, 0.1, key="weighted_sum_energy_Lang"+typeSection+typePowercap)
        with colM:
            weightMemory = st.slider('Memory', 0.0, 10.0, 1.0, 0.1, key="weighted_sum_memory_Lang"+typeSection+typePowercap)
        with colS:
            weightScore = st.slider('Score', 0.0, 10.0, 1.0, 0.1, key="weighted_sum_score_Lang"+typeSection+typePowercap)

        weights = [weightEnergy, weightTime,weightMemory, weightScore]

        showWeightedSumAlg(meanDF,ieeeDF,optionAlgWeightedSum,optionSizeWeightedSum,weights)

    else:

        col1, col2 = st.columns(2)

        optionLangWeightedSum, optionSizeWeightedSum = None, None

        with col1:
            if typeSection == "_compile_":
                optionLangWeightedSum = st.selectbox('Select language', languagesCompile, key="weighted_sum_language_Alg"+typeSection+typePowercap)
            else:
                optionLangWeightedSum = st.selectbox('Select language', languages, key="weighted_sum_language_Alg"+typeSection+typePowercap)
        with col2:
            optionSizeWeightedSum = st.selectbox('Select input size', sizes, key="weighted_sum_size_lang_Alg"+typeSection+typePowercap)

        # 3 sliders for the weights
        st.write("Select the weights for the criteria")
        colT, colE, colM = st.columns(3)

        with colT:  
            weightTime = st.slider('Time', 0.0, 10.0, 1.0, 0.1)
        with colE:
            weightEnergy = st.slider('Energy', 0.0, 10.0, 1.0, 0.1)
        with colM:
            weightMemory = st.slider('Memory', 0.0, 10.0, 1.0, 0.1)

        weights = [weightEnergy,weightTime, weightMemory]

        showWeightedSumLang(meanDF,optionLangWeightedSum,optionSizeWeightedSum, weights)



def vetoesMaxAlg(meanDF,optionLang,optionSize):

    meanDF = meanDF[meanDF['Language'] == optionLang]
    meanDF = meanDF[meanDF['Size'] == optionSize]

    maxes = {}
    maxes['Energy'] = meanDF['Package'].max()
    maxes['Time'] = meanDF['Time(sec)'].max()
    maxes['Memory'] = meanDF['Memory(MB)'].max()

    return maxes

def vetoesMaxLang(meanDF,ieeeDF,optionAlg,optionSize):
    
    meanDF = meanDF[meanDF['Algorithm'] == algorithmsDict[optionAlg]]
    meanDF = meanDF[meanDF['Size'] == optionSize]

    maxes = {}
    maxes['Energy'] = meanDF['Package'].max()
    maxes['Time'] = meanDF['Time(sec)'].max()
    maxes['Memory'] = meanDF['Memory(MB)'].max()
    maxes['Score'] = ieeeDF['Score'].max()

    return maxes



def ElectreUI(meanDF,ieeeDF,typeSection, typePowercap):

    optionElectre = st.selectbox('How do you want to see the electre?', ('By Language', 'By Algorithm'), key="electre_option"+typeSection+typePowercap)

    if optionElectre == "By Language":

        col1, col2 = st.columns(2)

        optionAlgElectre, optionSizeElectre = None, None

        with col1:
    
            optionAlgElectre = st.selectbox('Select algorithm', tuple(algorithmsDict.keys()), key="electre_algorithm"+typeSection+typePowercap)

        with col2:

            optionSizeElectre = st.selectbox('Select input size', sizes, key="electre_size_lang"+typeSection+typePowercap)

        # 4 sliders for the weights
        st.write("Select the weights for the criteria")
        colT, colE, colM, colS = st.columns(4)

        with colT:
            weightTime = st.slider('Time', 0.0, 1.0, 0.25, 0.05, key="electre_time_Lang"+typeSection+typePowercap)
        with colE:
            weightEnergy = st.slider('Energy', 0.0, 1.0, 0.25, 0.05, key="electre_energy_Lang"+typeSection+typePowercap)
        with colM:
            weightMemory = st.slider('Memory', 0.0, 1.0, 0.25, 0.05, key="electre_memory_Lang"+typeSection+typePowercap)
        with colS:
            weightScore = st.slider('Score', 0.0, 1.0, 0.25, 0.05, key="electre_score_Lang"+typeSection+typePowercap)

        weights = [weightEnergy, weightTime, weightMemory, weightScore]

        if weights[0] + weights[1] + weights[2] + weights[3] != 1.0:
            st.error("The sum of the weights must be 1.0")
            return
        
        indifereceThreshold = st.slider('Indifference Threshold', 0.0, 1.0, 0.5, 0.05, key="electre_indiferece_Lang"+typeSection+typePowercap)

        vetoesMaxDictLang = vetoesMaxLang(meanDF,ieeeDF, optionAlgElectre,optionSizeElectre)

        # 4 sliders for the vetoes thresholds
        st.write("Select the vetoes for the criteria")
        colVT, colVE, colVM, colVS = st.columns(4)

        with colVT:
            vetoTime = st.slider('Time', 0.0, vetoesMaxDictLang['Time'], 0.0, 0.05, key="electre_veto_time_Lang"+typeSection+typePowercap)
        with colVE:
            vetoEnergy = st.slider('Energy', 0.0, vetoesMaxDictLang['Energy'], 0.0, 0.05, key="electre_veto_energy_Lang"+typeSection+typePowercap)
        with colVM:
            vetoMemory = st.slider('Memory', 0.0, vetoesMaxDictLang['Memory'], 0.0, 0.05, key="electre_veto_memory_Lang"+typeSection+typePowercap)
        with colVS:
            vetoScore = st.slider('Score', 0.0, vetoesMaxDictLang['Score'], 0.0, 0.05, key="electre_veto_score_Lang"+typeSection+typePowercap)

        vetoes1 = [vetoEnergy, vetoTime, vetoMemory, vetoScore]

        optionTypeElectre = st.selectbox('Select type of Electre', ("Electre Is", "Electre Iv"), key="electre_type_Lang"+typeSection+typePowercap)
            
        if optionTypeElectre == "Electre Is":
            # 4 sliders for the preferences thresholds

            st.write("Select the preferences thresholds for the criteria")

            colITT, colITE, colITM, colITS = st.columns(4)

            with colITT:
                prefTime = st.slider('Time', 0.0, 10.0, 2.0, 0.05, key="electre_pref_time_Lang"+typeSection+typePowercap)
            with colITE:
                prefEnergy = st.slider('Energy', 0.0, 10.0, 2.0, 0.05, key="electre_pref_energy_Lang"+typeSection+typePowercap)
            with colITM:
                prefMemory = st.slider('Memory', 0.0, 10.0, 2.0, 0.05, key="electre_pref_memory_Lang"+typeSection+typePowercap)
            with colITS:
                prefScore = st.slider('Score', 0.0, 10.0, 2.0, 0.05, key="electre_pref_score_Lang"+typeSection+typePowercap)

            preferencesTh1 = [prefEnergy, prefTime, prefMemory, prefScore]

            showElectreAlg(meanDF,ieeeDF, optionAlgElectre,optionSizeElectre, weights,indifereceThreshold,preferencesTh1,vetoes1)

        else:

            showElectreAlg(meanDF,ieeeDF, optionAlgElectre,optionSizeElectre, weights,indifereceThreshold, None,vetoes1)

    else:

        col1, col2 = st.columns(2)

        optionLangElectre, optionSizeElectre = None, None

        with col1:
            if typeSection == "_compile_":
                optionLangElectre = st.selectbox('Select language', languagesCompile, key="electre_language"+typeSection+typePowercap)
            else:
                optionLangElectre = st.selectbox('Select language', languages, key="electre_language"+typeSection+typePowercap)

        with col2:
            optionSizeElectre = st.selectbox('Select input size', sizes, key="electre_size"+typeSection+typePowercap)
            
        # 3 sliders for the weights
        st.write("Select the weights for the criteria")
        colT, colE, colM = st.columns(3)

        with colT:
            weightTime = st.slider('Time', 0.0, 1.0, 0.40, 0.05, key="electre_time_Alg"+typeSection+typePowercap)
        with colE:
            weightEnergy = st.slider('Energy', 0.0, 1.0, 0.30, 0.05, key="electre_energy_Alg"+typeSection+typePowercap)
        with colM:
            weightMemory = st.slider('Memory', 0.0, 1.0, 0.30, 0.05, key="electre_memory_Alg"+typeSection+typePowercap)

        weights = [weightEnergy,weightTime, weightMemory]

        if weights[0] + weights[1] + weights[2] != 1.0:
            st.error("The sum of the weights must be 1.0")
            return
        
        indifereceThreshold = st.slider('Indifference Threshold', 0.0, 1.0, 0.5, 0.05, key="electre_indifereceThreshold_Alg"+typeSection+typePowercap)

        optionTypeElectre = st.selectbox('Select type of Electre', ("Electre Is", "Electre Iv"), key="electre_type_Alg"+typeSection+typePowercap)

        vetoesMaxDictAlg= vetoesMaxAlg(meanDF, optionLangElectre,optionSizeElectre)

        # 3 sliders for the vetoes
        st.write("Select the vetoes for the criteria")
        colVT, colVE, colVM = st.columns(3)

        with colVT:
            vetoTime = st.slider('Time', 0.0, vetoesMaxDictAlg["Time"], 0.0, 0.05, key="electre_veto_time_Alg"+typeSection+typePowercap)
        with colVE:
            vetoEnergy = st.slider('Energy', 0.0, vetoesMaxDictAlg["Energy"], 0.0, 0.05, key="electre_veto_energy_Alg"+typeSection+typePowercap)
        with colVM:
            vetoMemory = st.slider('Memory', 0.0, vetoesMaxDictAlg["Memory"], 0.0, 0.05, key="electre_veto_memory_Alg"+typeSection+typePowercap)


        vetoes2 = [vetoEnergy, vetoTime, vetoMemory]

        if optionTypeElectre == "Electre Is":
            # 3 sliders for the preferences thresholds

            st.write("Select the preferences thresholds for the criteria")

            colITT, colITE, colITM = st.columns(3)

            with colITT:
                prefTime = st.slider('Time', 0.0, 10.0, 2.0, 0.05, key="electre_pref_time_Alg"+typeSection+typePowercap)
            with colITE:
                prefEnergy = st.slider('Energy', 0.0, 10.0, 2.0, 0.05, key="electre_pref_energy_Alg"+typeSection+typePowercap)
            with colITM:
                prefMemory = st.slider('Memory', 0.0, 10.0, 2.0, 0.05, key="electre_pref_memory_Alg"+typeSection+typePowercap)

            preferencesTh2 = [prefEnergy, prefTime, prefMemory]

            showElectreLang(meanDF,optionLangElectre,optionSizeElectre, weights,indifereceThreshold, preferencesTh2,vetoes2)

        else:

            showElectreLang(meanDF,optionLangElectre,optionSizeElectre, weights,indifereceThreshold, None,vetoes2)

