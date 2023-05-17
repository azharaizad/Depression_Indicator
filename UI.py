import streamlit as st
from Home import home
from TextClassification import TextClassification
from Questionnaire import Questionnaire

# Create a session state to store the page selection
class SessionState:
    def __init__(self):
        self.page = "Home"

state = SessionState()

# Define different pages
pages = {
    "Home": home,
    "Text Classification": TextClassification,
    "Questionnaire": Questionnaire
}

# Render the selected page based on the session state
def render_page():
    if state.page in pages:
        pages[state.page]()

# Main App
def main():
    st.sidebar.title("Menu")
    selected_page = st.sidebar.radio("Go to", tuple(pages.keys()))
    state.page = selected_page

    render_page()

if __name__ == "__main__":
    main()



