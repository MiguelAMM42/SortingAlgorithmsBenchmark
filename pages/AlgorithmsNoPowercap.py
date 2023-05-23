import streamlit as st
import pandas as pd
import os
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go



APP_ROOT = os.path.dirname(os.path.abspath(__file__))

__path__ = os.path.join(APP_ROOT, f"../static/clean.csv")
with open(__path__, "r") as fCSV:
    df = pd.read_csv(fCSV)


st.title("Sorting Algorithms Benchmarking")


languages = ('C', 'C++', 'C#', 'Go','Haskell','Python', 'Rust', 'Swift')

algorithms = (
    "bubblesort",
    "cyclesort",
    "heapsort",
    "insertionsort",
    "mergesort",
    "oddevensort",
    "quicksort",
    "selectionsort"
)

sizes = (25000, 50000, 100000)

optionSize = st.selectbox(
    'What input size do you want to see?',
    sizes)
optionAlg = st.selectbox(
    'What algorithm do you want to see?',
    algorithms)


    
filtered_data = df[(df["Algorithm"] == optionAlg) & (df["Size"] == optionSize)]

st.write(f"## {optionAlg} - {optionSize} elements")

# Pivot the filtered data to create a multi-index dataframe
pivot_data = filtered_data.pivot_table(
    index=["Language", "Package"], values="Time(sec)", fill_value=0
)

# Reset the index to flatten the multi-index dataframe
flat_data = pivot_data.reset_index()

# Assign a unique color to each language
color_palette = px.colors.qualitative.Set1[:len(languages)]
color_map = dict(zip(languages, color_palette))
colors = flat_data["Language"].map(color_map)


# Get unique languages
unique_languages = flat_data["Language"].unique()

# Create an empty list to store scatter traces
scatter_traces = []

# Iterate over each language and create a scatter trace
for language in unique_languages:
    language_data = flat_data[flat_data["Language"] == language]
    scatter_trace = go.Scatter(
        x=language_data["Package"],
        y=language_data["Time(sec)"],
        mode="markers",
        name=language,
        marker=dict(color=color_map[language])
    )
    scatter_traces.append(scatter_trace)

# Create a Figure object and add scatter traces
fig = go.Figure(data=scatter_traces)

# Update the layout of the figure
fig.update_layout(
    xaxis_title="Package",
    yaxis_title="Time (sec)",
    title=f"{optionAlg} - Size {optionSize}",
    showlegend=True
)

# Show the plot using Streamlit
st.plotly_chart(fig)
