import streamlit as st

st.write("# manimator")

prompt = st.text_input("Enter a prompt:", "")

if st.button("Generate"):
    st.write(prompt)

st.video("./backend/output/GTTSExample.mp4")
