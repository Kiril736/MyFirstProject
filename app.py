import streamlit as st
st.title("my first title")
name=st.text_input(f"vuvedi ime")
if name:
  st.write(f"Hello {name}!")
