import streamlit as st
import os
import base64
from st_pages import Page, show_pages, add_page_title, Section

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# Center the content on the page
# -- not working --
#st.markdown(
#    """
#    <style>
#    .centered {
#        display: flex;
#        flex-direction: column;
#        align-items: center;
#        justify-content: center;
#        height: 100vh;
#        text-align: center;
#    }
#    </style>
#    """,
#    unsafe_allow_html=True,
#)

st.title("Sorting Algorithms Benchmarking")

# Optional -- adds the title and icon to the current page
add_page_title()

# Specify what pages should be shown in the sidebar, and what their titles and icons should be
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

# Paper PDF
st.header("Our paper")
pdf_filename = "StrategicProgramming.pdf"
pdf_path = os.path.join(APP_ROOT, f"static/{pdf_filename}")
pdf_data = open(pdf_path, "rb").read()
pdf_base64 = base64.b64encode(pdf_data).decode("utf-8")
pdf_display = F'<iframe src="data:application/pdf;base64,{pdf_base64}" width="900" height="1000" type="application/pdf"></iframe>'
st.markdown(pdf_display, unsafe_allow_html=True)

# Add a download button for the paper
def download_file(file_path, file_name):
    with open(file_path, "rb") as file:
        file_data = file.read()
    b64 = base64.b64encode(file_data).decode("utf-8")

    button_html = f"""
    <a href="data:application/octet-stream;base64,{b64}" download="{file_name}">
        <button type="button" style="padding: 10px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer;">
            Download {file_name}
        </button>
    </a>
    """

    return button_html


st.markdown(download_file(pdf_path, pdf_filename), unsafe_allow_html=True)

# Center the content on the page
# -- not working --
#st.markdown('<div class="centered">', unsafe_allow_html=True)
