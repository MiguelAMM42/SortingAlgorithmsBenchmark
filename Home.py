import streamlit as st
import os
import base64
from st_pages import Page, show_pages, add_page_title, Section
from streamlit import components

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# Center the content on the page
# -- not working --
# st.markdown(
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
# )

st.title("Sorting Algorithms Benchmarking")

# Specify what pages should be shown in the sidebar, and what their titles and icons should be
show_pages(
    [
        Page("Home.py", "Home", "🏠"),
        Page("pages/Algorithms_Powercap.py", "Algorithms :: Powercap", "📊"),
        Page("pages/Algorithms_No_Powercap.py",
             "Algorithms :: No Powercap", "📊"),
        Page("pages/Compile_Powercap.py", "Compile :: Powercap", "📊"),
        Page("pages/Compile_No_Powercap.py", "Compile :: No Powercap", "📊"),
    ]
)


def render_pdf(pdf_url):
    st.markdown(
        f'<iframe src="https://docs.google.com/viewer?url={pdf_url}&embedded=true" width="900" height="1000" style="border: none;"></iframe>', unsafe_allow_html=True)


# Paper PDF
st.header("Our paper")
pdf_filename = "On_the_Energy_Efficiency_of_Sorting_Algorithms.pdf"
pdf_path = os.path.join(APP_ROOT, f"static/{pdf_filename}")
pdf_data = open(pdf_path, "rb").read()
pdf_base64 = base64.b64encode(pdf_data).decode("utf-8")
# pdf_display = F'<iframe src="data:application/pdf;base64,{pdf_base64}" width="900" height="1000" type="application/pdf"></iframe>'
# st.markdown(pdf_display, unsafe_allow_html=True)


pdf_url = "https://github.com/MiguelAMM42/SortingAlgorithmsBenchmark/blob/main/static/On_the_Energy_Efficiency_of_Sorting_Algorithms.pdf"
render_pdf(pdf_url)


# Add a download button for the paper
def download_file(file_path, file_name):
    with open(file_path, "rb") as file:
        file_data = file.read()
    b64 = base64.b64encode(file_data).decode("utf-8")

    button_html = f"""
    <a href="data:application/octet-stream;base64,{b64}" download="On_the_Energy_Efficiency_of_Sorting_Algorithms.pdf">
        <button type="button" style="padding: 10px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer;">
            Download {file_name}
        </button>
    </a>
    """

    return button_html


st.markdown(download_file(
    pdf_path, "On the Energy Efficiency of Sorting Algorithms"), unsafe_allow_html=True)

# Center the content on the page
# -- not working --
# st.markdown('<div class="centered">', unsafe_allow_html=True)
