import streamlit as st
import pandas as pd

st.set_page_config(page_title="Meu Site Streamlit")

with st.container():
    st.subheader("Meu primeiro site com o Streamlit")
    st.title("Dashboard de Contratos")
    st.write("Informações sobre os contratos fechados pela Hash&Co ao longo de maio")
    st.write("Quer aprender Python? [Clique aqui](https://www.hashtagtreinamentos.com/curso-python)")


with st.container():
    st.write("---")
    dados = pd.read_csv("resultados.csv")
    st.area_chart(dados, x="Data", y="Contratos")
