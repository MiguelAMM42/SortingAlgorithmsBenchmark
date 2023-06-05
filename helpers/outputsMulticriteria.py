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

    st.graphviz_chart(graph)


def PrometheeDF(promDict, col):

    df = pd.DataFrame(columns=[col, 'Score'])
    for elem in promDict["phi"]:
        if col == "Algorithm":
            first = algorithmsDictInv[elem[0]]
        else:
            first = elem[0]
        df.loc[len(df)] = [first, elem[1]]

    st.dataframe(df)

    