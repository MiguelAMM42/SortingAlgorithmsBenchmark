import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from helpers.variables import languages, sizeslst, algorithmsDict
import pandas as pd

# Plot a scatter plot of energy(x), time(y)
# ------------------------------------------ #
def showScatterPlotEnergyTime(df, optionSize, optionAlg, optionStyle):
    filtered_data = df[(df["Algorithm"] == algorithmsDict[optionAlg]) & (df["Size"] == optionSize)]

    if optionStyle == "All Values":
        st.write(f"#### {optionAlg} - {optionSize} elements : {optionStyle}")
    else:
        st.write(f"#### {optionAlg} - {optionSize} elements : {optionStyle}")

    # Pivot the filtered data to create a multi-index dataframe
    pivot_data = filtered_data.pivot_table(
        index=["Language", "Package"], values="Time(sec)", fill_value=0
    )

    # Reset the index to flatten the multi-index dataframe
    flat_data = pivot_data.reset_index()

    # Assign a unique color to each language
    color_palette = px.colors.qualitative.Set1[:len(languages)]
    color_map = dict(zip(languages, color_palette))


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
        xaxis_title="Energy (Joules)",
        yaxis_title="Time (sec)",
        showlegend=True
    )

    # Show the plot using Streamlit
    st.plotly_chart(fig)



# Plot a bar plot of time(x), input size(y)
# ------------------------------------------ #
def showBarPlotTimeSize(df, optionAlg):

    # Convert 'Size' column to categorical variable with desired order
    size_order = sizeslst  # Specify the desired order
    df['Size'] = pd.Categorical(df['Size'], categories=size_order, ordered=True)

    filtered_data = df[(df["Algorithm"] == algorithmsDict[optionAlg])  & (df["Size"].isin(size_order))]

    st.write(f"#### {optionAlg}")

    # Pivot the filtered data to create a multi-index dataframe
    pivot_data = filtered_data.pivot_table(
        index=["Language", "Size"], values="Time(sec)", fill_value=0
    )

    # Reset the index to flatten the multi-index dataframe
    flat_data = pivot_data.reset_index()

    # Assign a unique color to each language
    color_palette = px.colors.qualitative.Set1[:len(languages)]
    color_map = dict(zip(languages, color_palette))

    # Get unique languages
    unique_languages = flat_data["Language"].unique()

    # Create an empty list to store bar traces
    bar_traces = []

    # Iterate over each language and create a bar trace
    for language in unique_languages:
        language_data = flat_data[flat_data["Language"] == language]
        bar_trace = go.Bar(
            x=language_data["Size"],
            y=language_data["Time(sec)"],
            name=language,
            marker=dict(color=color_map[language])
        )
        bar_traces.append(bar_trace)

    # Create a Figure object and add bar traces
    fig = go.Figure(data=bar_traces)

    # Update the layout of the figure
    fig.update_layout(
        xaxis_title="Input Size",
        yaxis_title="Time (sec)",
        showlegend=True
    )

    # Show the plot using Streamlit
    st.plotly_chart(fig)



# Plot a bar plot of time(x), energy(y)
# ------------------------------------------ #
def showBarPlotEnergySize(df, optionAlg):

    # Convert 'Size' column to categorical variable with desired order
    size_order = sizeslst  # Specify the desired order
    df['Size'] = pd.Categorical(df['Size'], categories=size_order, ordered=True)

    filtered_data = df[(df["Algorithm"] == algorithmsDict[optionAlg])  & (df["Size"].isin(size_order))]

    st.write(f"#### {optionAlg}")

    # Pivot the filtered data to create a multi-index dataframe
    pivot_data = filtered_data.pivot_table(
        index=["Language", "Size"], values="Package", fill_value=0
    )

    # Reset the index to flatten the multi-index dataframe
    flat_data = pivot_data.reset_index()

    # Assign a unique color to each language
    color_palette = px.colors.qualitative.Set1[:len(languages)]
    color_map = dict(zip(languages, color_palette))

    # Get unique languages
    unique_languages = flat_data["Language"].unique()

    # Create an empty list to store bar traces
    bar_traces = []

    # Iterate over each language and create a bar trace
    for language in unique_languages:
        language_data = flat_data[flat_data["Language"] == language]
        bar_trace = go.Bar(
            x=language_data["Size"],
            y=language_data["Package"],
            name=language,
            marker=dict(color=color_map[language])
        )
        bar_traces.append(bar_trace)

    # Create a Figure object and add bar traces
    fig = go.Figure(data=bar_traces)

    # Update the layout of the figure
    fig.update_layout(
        xaxis_title="Input Size",
        yaxis_title="Energy (Joules)",
        showlegend=True
    )

    # Show the plot using Streamlit
    st.plotly_chart(fig)


def showBarLinePlotLanguageEnergyTime(df, optionSize, optionAlg):
    # Group the data by algorithm and size

    filtered_data = df[(df["Algorithm"] == algorithmsDict[optionAlg]) & (df["Size"] == optionSize)]

    st.write(f"#### {optionAlg} - {optionSize} elements")

    # Create the bar trace for the 'Package' values
    bar_trace = go.Bar(
        x=filtered_data['Language'],
        y=filtered_data['Package'],
        name='Energy (Joules)'
    )

    # Create the line trace for the 'Time' values
    line_trace = go.Scatter(
        x=filtered_data['Language'],
        y=filtered_data['Time(sec)'],
        name='Time (sec)',
        yaxis='y2'
    )

    # Create the data list with both traces
    data = [bar_trace, line_trace]

    # Create the layout with two y-axes
    layout = go.Layout(
        xaxis=dict(title='Language'),
        yaxis=dict(title='Energy (Joules)'),
        yaxis2=dict(title='Time (sec)', overlaying='y', side='right')
    )

    # Create the figure
    fig = go.Figure(data=data, layout=layout)

    # Show the plot using Streamlit
    st.plotly_chart(fig)

    
def showBarLinePlotLanguageEnergyMemory(df, optionSize, optionAlg):
    # Group the data by algorithm and size

    filtered_data = df[(df["Algorithm"] == algorithmsDict[optionAlg]) & (df["Size"] == optionSize)]

    st.write(f"#### {optionAlg} - {optionSize} elements")

    # Create the bar trace for the 'Package' values
    bar_trace = go.Bar(
        x=filtered_data['Language'],
        y=filtered_data['Package'],
        name='Energy (Joules)'
    )

    # Create the line trace for the 'Memory' values
    line_trace = go.Scatter(
        x=filtered_data['Language'],
        y=filtered_data['Memory(MB)'],
        name='Memory (MB)',
        yaxis='y2'
    )

    # Create the data list with both traces
    data = [bar_trace, line_trace]

    # Create the layout with two y-axes
    layout = go.Layout(
        xaxis=dict(title='Language'),
        yaxis=dict(title='Energy (Joules)'),
        yaxis2=dict(title='Memory (MB)', overlaying='y', side='right')
    )

    # Create the figure
    fig = go.Figure(data=data, layout=layout)

    # Show the plot using Streamlit
    st.plotly_chart(fig)


def showBarPlotTimeLanguage(df,optionLanguage):
    # Filter the data by language
    filtered_data = df[df['Language'] == optionLanguage]
    
    st.write(f"#### {optionLanguage} - Time (sec)")

    # Group the data by algorithm and calculate the mean time
    df_time = filtered_data.groupby('Algorithm')['Time(sec)'].mean().reset_index()

    # Create the bar plot using Plotly Express
    fig = px.bar(df_time, x='Algorithm', y='Time(sec)')
    fig.update_yaxes(title='Time (sec)')

    # Show the plot using Streamlit
    st.plotly_chart(fig)


def showBarPlotEnergyLanguage(df,optionLanguage):
    # Filter the data by language
    filtered_data = df[df['Language'] == optionLanguage]
    
    st.write(f"#### {optionLanguage} - Energy (Joules)")

    # Group the data by algorithm and calculate the mean time
    df_energy = filtered_data.groupby('Algorithm')['Package'].mean().reset_index()

    # Create the bar plot using Plotly Express
    fig = px.bar(df_energy, x='Algorithm', y='Package')
    fig.update_yaxes(title='Energy (Joules)')

    # Show the plot using Streamlit
    st.plotly_chart(fig)

def showBarPlotMemoryLanguage(df,optionLanguage):
    # Filter the data by language
    filtered_data = df[df['Language'] == optionLanguage]
    
    st.write(f"#### {optionLanguage} - Memory (MB)")

    # Group the data by algorithm and calculate the mean time
    df_memory = filtered_data.groupby('Algorithm')['Memory(MB)'].mean().reset_index()

    # Create the bar plot using Plotly Express
    fig = px.bar(df_memory, x='Algorithm', y='Memory(MB)')
    fig.update_yaxes(title='Memory (MB)')

    # Show the plot using Streamlit
    st.plotly_chart(fig)


def showBarLinePlotLanguageEnergyTimePerAlgorithm(df, optionSize, optionLanguage):
    # Filter the data by size and language
    filtered_data = df[(df['Size'] == optionSize) & (df['Language'] == optionLanguage)]

    st.write(f"#### {optionLanguage} - Size: {optionSize}")

    # Create the bar trace for the 'Package' values
    bar_trace = go.Bar(
        x=filtered_data['Algorithm'],
        y=filtered_data['Package'],
        name='Energy (Joules)',
    )

    # Create the line trace for the 'Time' values
    line_trace = go.Scatter(
        x=filtered_data['Algorithm'],
        y=filtered_data['Time(sec)'],
        name='Time (sec)',
        yaxis='y2',
    )

    # Create the data list with both traces
    data = [bar_trace, line_trace]

    # Create the layout with two y-axes
    layout = go.Layout(
        xaxis=dict(title='Algorithm'),
        yaxis=dict(title='Energy (Joules)'),
        yaxis2=dict(title='Time (sec)', overlaying='y', side='right')
    )

    # Create the figure
    fig = go.Figure(data=data, layout=layout)

    # Show the plot using Streamlit
    st.plotly_chart(fig)


def showBarLinePlotLanguageEnergyMemoryPerAlgorithm(df, optionSize, optionLanguage):
    # Filter the data by size and language
    filtered_data = df[(df['Size'] == optionSize) & (df['Language'] == optionLanguage)]

    st.write(f"#### {optionLanguage} - Size: {optionSize}")

    # Create the bar trace for the 'Energy' values
    bar_trace = go.Bar(
        x=filtered_data['Algorithm'],
        y=filtered_data['Package'],
        name='Energy (Joules)',
    )

    # Create the line trace for the 'Memory' values
    line_trace = go.Scatter(
        x=filtered_data['Algorithm'],
        y=filtered_data['Memory(MB)'],
        name='Memory (MB)',
        yaxis='y2',
    )

    # Create the data list with both traces
    data = [bar_trace, line_trace]

    # Create the layout with two y-axes
    layout = go.Layout(
        xaxis=dict(title='Algorithm'),
        yaxis=dict(title='Energy (Joules)'),
        yaxis2=dict(title='Memory (MB)', overlaying='y', side='right')
    )

    # Create the figure
    fig = go.Figure(data=data, layout=layout)

    # Show the plot using Streamlit
    st.plotly_chart(fig)




def showBarLinePlotLanguageEnergyTimePerSize(df, optionAlg, optionLang):
    # Filter the data by language and algorithm
    filtered_data = df[(df['Language'] == optionLang) & (df["Algorithm"] == algorithmsDict[optionAlg])]

    st.write(f"#### {optionLang} - {optionAlg}")

    # Create the bar trace for the 'Energy' values
    bar_trace = go.Bar(
        x=filtered_data['Size'],
        y=filtered_data['Package'],
        name='Energy (Joules)',
    )

    # Create the line trace for the 'Time' values
    line_trace = go.Scatter(
        x=filtered_data['Size'],
        y=filtered_data['Time(sec)'],
        name='Time (sec)',
        yaxis='y2',
    )

    # Create the data list with both traces
    data = [bar_trace, line_trace]

    # Create the layout with two y-axes
    layout = go.Layout(
        xaxis=dict(title='Size'),
        yaxis=dict(title='Energy (Joules)'),
        yaxis2=dict(title='Time (sec)', overlaying='y', side='right')
    )

    # Create the figure
    fig = go.Figure(data=data, layout=layout)

    # Show the plot using Streamlit's plotly_chart function
    st.plotly_chart(fig)


def showBarLinePlotLanguageEnergyMemoryPerSize(df, optionAlg, optionLang):
    # Filter the data by language and algorithm
    filtered_data = df[(df['Language'] == optionLang) & (df["Algorithm"] == algorithmsDict[optionAlg])]

    st.write(f"#### {optionLang} - {optionAlg}")

    # Create the bar trace for the 'Energy' values
    bar_trace = go.Bar(
        x=filtered_data['Size'],
        y=filtered_data['Package'],
        name='Energy (Joules)',
    )

    # Create the line trace for the 'Memory' values
    line_trace = go.Scatter(
        x=filtered_data['Size'],
        y=filtered_data['Memory(MB)'],
        name='Memory (MB)',
        yaxis='y2',
    )

    # Create the data list with both traces
    data = [bar_trace, line_trace]

    # Create the layout with two y-axes
    layout = go.Layout(
        xaxis=dict(title='Size'),
        yaxis=dict(title='Energy (Joules)'),
        yaxis2=dict(title='Memory (MB)', overlaying='y', side='right')
    )

    # Create the figure
    fig = go.Figure(data=data, layout=layout)

    # Show the plot using Streamlit's plotly_chart function
    st.plotly_chart(fig)