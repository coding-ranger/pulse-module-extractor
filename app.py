import streamlit as st
from module_extractor import run

st.title("AI Documentation Module Extractor")

urls = st.text_area("Enter documentation URLs (one per line)")
if st.button("Extract"):
    url_list = [u.strip() for u in urls.splitlines()]
    output = run(url_list)
    st.json(output)
