from EasyMCDM.models.WeightedSum import WeightedSum
from EasyMCDM.models.Pareto import Pareto
from EasyMCDM.models.Promethee import Promethee
import streamlit as st

def test(): #change to have correct values
    data = {
    "alfa_156": [23817.0, 201.0, 8.0, 39.6, 6.0, 378.0, 31.2],
    "audi_a4": [25771.0, 195.0, 5.7, 35.8, 7.0, 440.0, 33.0],
    "cit_xantia": [25496.0, 195.0, 7.9, 37.0, 2.0, 480.0, 34.0]
    }

    p = WeightedSum(data=data, verbose=False)
    res = p.solve(pref_indexes=[0,1,6],prefs=["min","max","min"], weights=[0.001,2,3], target='min')
    st.write(res)


def showPareto(df, indexes, prefs):
    
    p = Pareto(data=df, verbose=True) #False
    res = p.solve(indexes=indexes, prefs=prefs)
    st.write(res)


def showPromethee(df, weights, prefs):

    p = Promethee(data=df, verbose=True) #False
    res = p.solve(weights=weights, prefs=prefs)
    st.write(res)