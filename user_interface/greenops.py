# Green Ops Calculator

# Imports
import streamlit as st

def run_ui():
    tab_list = ["Building Parameters", "Occupancy Parameters"]
    tab1, tab2 = st.tabs(tab_list)

    with tab1:
        st.header(tab_list[0])

    with tab2:
        st.header(tab_list[1])
        num_emp = st.number_input("Number of employees", value=int)
        
