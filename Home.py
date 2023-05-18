import streamlit as st

def home():
    st.title("Home Page")
    st.write("### Welcome to the Depression Indicator!")
    st.markdown("##### WIE2003 (Group 7)")
    st.markdown("##### Team Member:")
    table_md = """
    |No.|Name|Matrix No.|
    |--|--|--|
    |1.|Muhammad Amirul Amin Bin Arman|17202969|
    |2.|Hong Kae Ren|U2102850|
    |3.|Muhammad Azhar Aizad Asfarizailin|U2100687|
    |4.|Aqilah Salihah Binti Ismail Yusoff|U2101806|
    |5.|Muhammad Hakim Bin Zairol Hisham|U2100997|
    """
    st.markdown(table_md)
    st.markdown("### Introduction to Depression")
    st.markdown(
    "<div style='text-align: justify'> Depression <b>(major depressive disorder)</b> is a common and serious medical illness that negatively affects how you feel, the way you think and how you act. It can lead to a variety of emotional and physical problems and can decrease your ability to function at work and at home. So, we build a text classification machine learning model which can predict depression level through text.</div>", unsafe_allow_html=True
)
if __name__ == "__main__":
    home()

