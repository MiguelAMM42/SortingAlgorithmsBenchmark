import streamlit as st
import graphviz
import pandas as pd
from helpers.variables import algorithmsDictInv

def ParetoGraph(graphDict, col):
    graph = graphviz.Digraph()
    for elem in graphDict.keys():
        if col == "Algorithm":
            node = algorithmsDictInv[elem]
        else:
            node = elem
        graph.node(node)
        for i in graphDict[elem]["Strongly-Dominated-by"]:
            if col == "Algorithm":
                graph.edge(algorithmsDictInv[i],node)
            else:
                graph.edge(i,node)

    st.graphviz_chart(graph, use_container_width=True)


def PrometheeDF(promDict, col):

    df = pd.DataFrame(columns=['Position',col, 'Score'])
    pos = 0
    for elem in promDict["phi"]:
        pos += 1
        if col == "Algorithm":
            first = algorithmsDictInv[elem[0]]
        else:
            first = elem[0]
        df.loc[len(df)] = [str(pos)+'º',first, elem[1]]

    st.dataframe(df, hide_index=True ,use_container_width=True)


def WeightedSumDF(wsLst, col):

    #reverse the list
    wsLst = wsLst[::-1]

    df = pd.DataFrame(columns=['Position',col, 'Score'])
    pos = 0
    for elem in wsLst:
        pos += 1
        if col == "Algorithm":
            first = algorithmsDictInv[elem[1]]
        else:
            first = elem[1]
        df.loc[len(df)] = [str(pos)+'º',first, elem[2]]

    st.dataframe(df, hide_index=True, use_container_width=True)

    