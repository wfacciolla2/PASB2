import streamlit as st
import csv
import time
from _datetime import datetime

st.title('Cadastros')


def save_name(nomecompleto, datahora, nomemae, numerocartao, cpf, rg, datanascimento, sexo, telefone, endereco, cep, municipio, estado, atendente):
    filename = 'db2.csv'
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nomecompleto,datahora, nomemae, numerocartao, cpf, rg, datanascimento, sexo, telefone, endereco, cep, municipio, estado, atendente])
    delay = 5
    start_time = time.time()
    st.markdown('Cadastro efetuado')
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= delay:
            st._rerun()
            break

st.success('Não utilize acentuação nem cidilha. Ex.: ~`ç')
nomecompleto = st.text_input('Nome completo:')
nomecompleto = nomecompleto.upper()
datahora = datetime.today().replace(microsecond=0)
nomemae = st.text_input('Nome da mãe:')
nomemae = nomemae.upper()
numerocartao = st.text_input('Numero do cartão:')
cpf = st.text_input('CPF')
if len(cpf) < 11 or len(cpf) > 11:
    st.error('O CPF deve conter 11 digitos')
rg = st.text_input('RG')
if len(rg) < 9 or len(rg) > 9:
    st.error('O CPF deve conter 09 digitos')
datanascimentorecebe = st.date_input('Data de Nascimento')
datanascimento = datanascimentorecebe.strftime('%d/%m/%Y')
sexo = st.selectbox('Sexo', ['Masculino', 'Feminino'])
sexo = sexo.upper()
telefone = st.text_input('Telefone')
endereco = st.text_input('Endereço completo')
endereco = endereco.upper()
cep = st.text_input('CEP')
municipio = st.selectbox('Municipio', ['SANTA BRANCA', 'JACAREI', 'SALESÓPOLIS'])
estado = st.selectbox('Estado', ['SP'])
atendente = st.text_input('Nome do Atendente')
atendente = atendente.upper()
if st.button('Salvar'):
    save_name(nomecompleto,datahora, nomemae, numerocartao, cpf, rg, datanascimento, sexo, telefone, endereco, cep, municipio, estado, atendente)
