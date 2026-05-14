import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ceník OZ", layout="centered")

st.title("Vyhledávání v ceníku")

uploaded_file = st.file_uploader(
    "Nahraj Excel soubor",
    type=["xlsx"]
)

if uploaded_file:

    df = pd.read_excel(uploaded_file)

    st.success("Soubor načten")

    hledat = st.text_input("Zadej číslo produktu")

    if hledat:

        vysledek = df.astype(str).apply(
            lambda row: row.str.contains(hledat, case=False).any(),
            axis=1
        )

        nalezene = df[vysledek]

        if not nalezene.empty:
            st.dataframe(nalezene)
        else:
            st.warning("Nic nenalezeno")
