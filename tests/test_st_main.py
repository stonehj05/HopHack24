# This is a test for some of the functions in the stream lit library

import streamlit as st

ss = st.session_state
if 'counter' not in ss:
    ss.counter = 0


ss.counter += 1
st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

st.button("Increment counter")