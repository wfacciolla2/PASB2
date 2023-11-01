import streamlit as st
import pandas as pd
from Controller import controller as controler
from _datetime import datetime

st.write(datetime.today())

busca = st.selectbox('Selecione um nome:', controler.df().drop_duplicates(["nomecompleto"]))
endereco = controler.df()[controler.df().nomecompleto == busca][["endereco"]]
busca_completa = st.selectbox('Selecione o endereço:', endereco)
resultado = controler.df()[(controler.df().nomecompleto == busca) & (controler.df().endereco == busca_completa)]
