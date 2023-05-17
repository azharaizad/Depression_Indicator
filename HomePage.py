import streamlit as st
#import joblib 

# Create a session state to store the page selection
class SessionState:
    def __init__(self):
        self.page = "Home"

state = SessionState()
#model = joblib.load("C:/Users/aizad/OneDrive/Desktop/text_classification.py")
# Define different pages
def home():
    st.title("Home Page")
    st.write("Welcome to the Depression Indicator!")

def TextClassification():
    st.title("Text Classification")
    st.write("Welcome to Text Classification!")

def Questionnaire():
    st.title("Questionnaire")
    st.write("Welcome to the Questionnaire!")

# Render the selected page based on the session state
def render_page():
    if state.page == "Home":
        home()
    elif state.page == "Text Classification":
        TextClassification()
    elif state.page == "Questionnaire":
        Questionnaire()

# Main App
def main():
    st.sidebar.title("Menu")
    pages = ["Home","Text Classification", "Questionnaire"]
    selected_page = st.sidebar.radio("Go to", pages, index=0)
    state.page = selected_page

    render_page()



if __name__ == "__main__":
    main()
    print("helo world")


