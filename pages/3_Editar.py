import streamlit as st
import pandas as pd
from Controller import controller as controler
# Carregue o arquivo CSV



df = pd.read_csv('db2.csv')


# Solicite ao usuário que insira o nome para pesquisa
nome_editar = st.selectbox('Selecione um nome para editar:', df.drop_duplicates(["nomecompleto"]))
if nome_editar == '':
    st.warning("O nome esta em branco")
else:
    # Filtrar o dataframe com base no nome
    filtrado = df[df['nomecompleto'] == nome_editar]  # substitua 'nome' pelo nome da coluna que contém os nomes

    # Exiba o dataframe filtrado no editor de dados
    filtrado = st.dataframe(filtrado).data_editor(filtrado)
    indice = filtrado.index
    #st.write(indice)
    lista = df.index
    #st.write(lista)
    if st.button('Salvar alterações'):
        df.update(filtrado)
        df.to_csv('db2.csv', index=False)
        st.success('Editado com sucesso!')
