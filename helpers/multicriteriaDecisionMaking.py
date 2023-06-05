from EasyMCDM.models.WeightedSum import WeightedSum
from EasyMCDM.models.Pareto import Pareto
from EasyMCDM.models.Promethee import Promethee
import streamlit as st
from helpers.variables import languages, sizeslst, algorithmsDict
import pandas as pd
from helpers.outputsMulticriteria import ParetoGraph

def test(): #change to have correct values
    data = {
    "alfa_156": [23817.0, 201.0, 8.0, 39.6, 6.0, 378.0, 31.2],
    "audi_a4": [25771.0, 195.0, 5.7, 35.8, 7.0, 440.0, 33.0],
    "cit_xantia": [25496.0, 195.0, 7.9, 37.0, 2.0, 480.0, 34.0]
    }

    p = WeightedSum(data=data, verbose=False)
    res = p.solve(pref_indexes=[0,1,6],prefs=["min","max","min"], weights=[0.001,2,3], target='min')
    st.write(res)


def showParetoAlg(meanDF,ieeeDF,optionAlgPareto,optionSizePareto,considerScore):
    meanDF = meanDF[meanDF['Algorithm'] == algorithmsDict[optionAlgPareto]]
    meanDF = meanDF[meanDF['Size'] == optionSizePareto]

    if considerScore == "Yes":
        df = pd.DataFrame(columns=['Language', 'Energy', 'Time', 'Memory', 'Score'])
    else:
        df = pd.DataFrame(columns=['Language', 'Energy', 'Time', 'Memory'])
    df['Language'] = meanDF['Language']
    df['Energy'] = meanDF['Package']
    df['Time'] = meanDF['Time(sec)']
    df['Memory'] = meanDF['Memory(MB)']

    if considerScore == "Yes":
        # from ieeeDF get the score for each language
        for index,row in df.iterrows():
            df.loc[index,'Score'] = ieeeDF.loc[ieeeDF['Language'] == row['Language']]['Score'].values[0]
        
    dict = {}

    # for each langauge create list with values of energy, time and memory
    for index, row in df.iterrows():
        if row['Language'] not in dict:
            dict[row['Language']] = []
        if considerScore == "Yes":
            dict[row['Language']] += [row['Energy'], row['Time'], row['Memory'], row['Score']]
        else:
            dict[row['Language']] += [row['Energy'], row['Time'], row['Memory']]
    
    p = Pareto(data=dict, verbose=False) #False
    if considerScore == "Yes":
        res = p.solve(indexes=[0,1,2,3], prefs=["min","min","min","max"])
    else:
        res = p.solve(indexes=[0,1,2], prefs=["min","min","min"])

    ParetoGraph(res)


def showParetoLang(meanDF,optionLangPareto,optionSizePareto):
    meanDF = meanDF[meanDF['Language'] == optionLangPareto]
    meanDF = meanDF[meanDF['Size'] == optionSizePareto]

    df = pd.DataFrame(columns=['Algorithm', 'Energy', 'Time', 'Memory'])
    df['Algorithm'] = meanDF['Algorithm']
    df['Energy'] = meanDF['Package']
    df['Time'] = meanDF['Time(sec)']
    df['Memory'] = meanDF['Memory(MB)']

    dict = {}

    # for each langauge create list with values of energy, time and memory
    for index, row in df.iterrows():
        if row['Algorithm'] not in dict:
            dict[row['Algorithm']] = []
        dict[row['Algorithm']] += [row['Energy'], row['Time'], row['Memory']]

    p = Pareto(data=dict, verbose=False) #False
    res = p.solve(indexes=[0,1,2], prefs=["min","min","min"])

    ParetoGraph(res)



def showPromethee(df, weights, prefs):
    st.write(df)

    p = Promethee(data=df, verbose=False) #False
    res = p.solve(weights=weights, prefs=prefs) #weights can be greater than 1
    st.write(res)

    # show graph or text