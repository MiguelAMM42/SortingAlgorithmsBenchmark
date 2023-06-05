import streamlit as st
import graphviz

def ParetoGraph(graphDict):
    graph = graphviz.Digraph()
    for elem in graphDict.keys():
        graph.node(elem)
        for i in graphDict[elem]["Strongly-Dominated-by"]:
            graph.edge(i,elem)

    st.graphviz_chart(graph)