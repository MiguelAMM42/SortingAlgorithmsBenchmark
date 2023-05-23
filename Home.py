import streamlit as st
import pandas as pd
from st_pages import Page, show_pages, add_page_title, Section


st.title("Sorting Algorithms Benchmarking")


# Optional -- adds the title and icon to the current page
add_page_title()

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("Home.py", "Home", "🏠"),
        Section("Algorithms", icon="🎈️"),
        Page("pages/AlgorithmsPowercap.py", "Powercap", in_section=True),
        Page("pages/AlgorithmsNoPowercap.py", "No Powercap", in_section=True),
        Section("Compile", icon="🎈️"),
        Page("pages/CompilePowercap.py", "Powercap", in_section=True),
        Page("pages/CompileNoPowercap.py", "No Powercap", in_section=True)
    ]
)