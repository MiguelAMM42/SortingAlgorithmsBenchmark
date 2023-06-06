from EasyMCDM.models.WeightedSum import WeightedSum
from EasyMCDM.models.Pareto import Pareto
from EasyMCDM.models.Promethee import Promethee
import streamlit as st
from helpers.variables import languages, sizeslst, algorithmsDict
import pandas as pd
from helpers.outputsMulticriteria import *


def showWeightedSumAlg(meanDF,ieeeDF,optionAlgWeightedSum,optionSizeWeightedSum,weights):
    meanDF = meanDF[meanDF['Algorithm'] == algorithmsDict[optionAlgWeightedSum]]
    meanDF = meanDF[meanDF['Size'] == optionSizeWeightedSum]

    df = pd.DataFrame(columns=['Language', 'Energy', 'Time', 'Memory', 'Score'])
    df['Language'] = meanDF['Language']
    df['Energy'] = meanDF['Package']
    df['Time'] = meanDF['Time(sec)']
    df['Memory'] = meanDF['Memory(MB)']

    # from ieeeDF get the score for each language
    for index,row in df.iterrows():
        df.loc[index,'Score'] = ieeeDF.loc[ieeeDF['Language'] == row['Language']]['Score'].values[0]

    dict = {}

    # for each langauge create list with values of energy, time and memory
    for index, row in df.iterrows():
        if row['Language'] not in dict:
            dict[row['Language']] = []
            dict[row['Language']] += [row['Energy'], row['Time'], row['Memory'], row['Score']]

    p = WeightedSum(data=dict, verbose=False)
    res = p.solve(pref_indexes=[0,1,2,3],prefs=["min","min","min","max"], weights=weights, target='min')

    WeightedSumDF(res, "Language")


def showWeightedSumLang(meanDF,optionLangWeightedSum,optionSizeWeightedSum,weights):

    meanDF = meanDF[meanDF['Language'] == optionLangWeightedSum]
    meanDF = meanDF[meanDF['Size'] == optionSizeWeightedSum]

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

    p = WeightedSum(data=dict, verbose=False)
    res = p.solve(pref_indexes=[0,1,2],prefs=["min","min","min"], weights=weights, target='min')

    WeightedSumDF(res, "Algorithm")


    

    
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

    ParetoGraph(res, "Language")


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

    ParetoGraph(res, "Algorithm")



def showPrometheeAlg(meanDF,ieeeDF,optionAlgPromethee,optionSizePromethee,weights):

    meanDF = meanDF[meanDF['Algorithm'] == algorithmsDict[optionAlgPromethee]]
    meanDF = meanDF[meanDF['Size'] == optionSizePromethee]

    df = pd.DataFrame(columns=['Language', 'Energy', 'Time', 'Memory', 'Score'])
    df['Language'] = meanDF['Language']
    df['Energy'] = meanDF['Package']
    df['Time'] = meanDF['Time(sec)']
    df['Memory'] = meanDF['Memory(MB)']

    # from ieeeDF get the score for each language
    for index,row in df.iterrows():
        df.loc[index,'Score'] = ieeeDF.loc[ieeeDF['Language'] == row['Language']]['Score'].values[0]

    dict = {}

    # for each langauge create list with values of energy, time and memory
    for index, row in df.iterrows():
        if row['Language'] not in dict:
            dict[row['Language']] = []
        dict[row['Language']] += [row['Energy'], row['Time'], row['Memory'], row['Score']]

    p = Promethee(data=dict, verbose=False) #False
    res = p.solve(weights=weights, prefs=["min","min","min","max"]) #weights can be greater than 1

    PrometheeDF(res,"Language")

def showPrometheeLang(meanDF,optionLangPromethee,optionSizePromethee,weights):

    meanDF = meanDF[meanDF['Language'] == optionLangPromethee]
    meanDF = meanDF[meanDF['Size'] == optionSizePromethee]

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

    p = Promethee(data=dict, verbose=False) #False
    res = p.solve(weights=weights, prefs=["min","min","min"]) #weights can be greater than 1

    PrometheeDF(res,"Algorithm")
    



