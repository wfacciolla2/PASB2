from fpdf import FPDF
import streamlit as st
from datetime import date, datetime
from Controller import controller as controler
import base64
import pytz


fuso_horario = pytz.timezone('America/Sao_Paulo')

now = datetime.now(fuso_horario).strftime('%d-%m-%Y %H:%M:%S')

st.write(now)

busca = st.selectbox('Selecione um nome:', controler.df().drop_duplicates(["nomecompleto"]))
endereco = controler.df()[controler.df().nomecompleto == busca][["endereco"]]
busca_completa = st.selectbox('Selecione o endereço:', endereco)
if st.button('Buscar Cadastro'):
    resultado = controler.df()[(controler.df().nomecompleto == busca) & (controler.df().endereco == busca_completa)]
    calculoidade = '--'
    with st.container():
        try:
            data_nascimento_string = resultado.head().iat[0, 6]
            data_nascimento = datetime.strptime(data_nascimento_string, "%d/%m/%Y").date()
            hoje = datetime.today().date()
            idade = hoje - data_nascimento
            calculoidade = idade.days // 365
        except ValueError:
            st.warning('Data de nascimento inserida incorretamente! Favor editar.')


        st.markdown(f'''

        **Nome do usuário:** `{resultado.head().iat[0, 0]}`

        **Nome da mãe:** `{resultado.head().iat[0, 2]}`

        **Cartão Nascional de Saúde:** `{resultado.head().iat[0, 3]}` **CPF:** `{resultado.head().iat[0, 4]} `
        **RG:** `{resultado.head().iat[0, 5]}`

        **Endereço:** `{resultado.head().iat[0, 9]}`

        **Municipio:** `{resultado.head().iat[0, 11]}`
        **UF:** `{resultado.head().iat[0, 12]}` **CEP:** `{resultado.head().iat[0, 10]}`


        **Data de Nascimento:** `{resultado.head().iat[0, 6]}`
        **idade:** `{calculoidade}`
        **Sexo:** `{resultado.head().iat[0, 7]}`
        **Tel:** `{resultado.head().iat[0, 8]}`
        ''')
        # Crie uma instância da classe FPDF e defina as propriedades básicas

        pdf = FPDF('P','mm','A4')
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        # fontes (times,courier,helvetica,symbol,zpfdingbats
        # 'B' negrito 'U' sublinhado 'I' italico
        pdf.set_font("Arial", size=15)
        # Adicione algum conteúdo ao PDF
        pdf.image('logo.jpg',10,8,30)
        pdf.image('sus.png',170,10,30)
        pdf.cell(190,4, txt="PRONTO ATENDIMENTO MUNICIPAL DE SANTA BRANCA", ln=True, align='C')
        pdf.cell(190,8, txt='FICHA DE ATENDIMENTO E URGÊNCIA', ln=True, align='C')
        pdf.cell(200,7, txt='',ln=True)
        pdf.set_font("Arial", size=10)
        pdf.cell(180,4, txt=f'Data e hora: {now}',ln=True, align='R')
        pdf.cell(190,4, txt=f'Ala respiratória (    )                                Ala não respiratória (    )',
                 ln=True,border=True, align='C')
        pdf.cell(190,7, txt='01 - DADOS DO PACIENTE/USUÁRIO/Nº DE REGISTRO:',ln=True)
        pdf.cell(100, 4, txt=f"Nome do usuário: {resultado.head().iat[0, 0]}", ln=True)
        pdf.cell(81, 4, txt=f"Nome da mãe: {resultado.head().iat[0, 2]}", ln=True)
        pdf.cell(127, 4, txt=f"Cartão Nacional de saúde: {resultado.head().iat[0, 3]} "
                              f"CPF: {resultado.head().iat[0, 4]}  RG: {resultado.head().iat[0, 5]}", ln=True)
        pdf.cell(138, 4, txt=f"Endereço: {resultado.head().iat[0, 9]}", ln=True)
        pdf.cell(98, 4, txt=f"Municipio: {resultado.head().iat[0, 11]} "
                              f"Estado: {resultado.head().iat[0, 12]} "
                              f"CEP: {resultado.head().iat[0, 10]}", ln=True)
        pdf.cell(140, 4, txt=f"Data de nascimento: {resultado.head().iat[0, 6]} "
                              f"Idade: {calculoidade} anos "
                              f"Sexo: {resultado.head().iat[0, 7]} "
                              f"Tel.: {resultado.head().iat[0, 8]} ", ln=True)
        pdf.cell(190,8, txt='', ln=True)
        pdf.cell(190,4, txt='_________________________________________________________________',align='C', ln=True)
        pdf.cell(190,4, txt='Assinatura do paciente', ln=True, align='C')
        pdf.cell(190,4, txt='Raça/Cor: (  ) Branca (  ) Preta (  ) Parda (  ) Amarela (  ) Indigena (  ) Sem informação',
                 align='C', ln=True)
        pdf.cell(190,4,txt='Portaria da obrigatoriedade de raça/cor GM/MS N 344 DE 01/02/1/2017.',align='C',ln=True)
        pdf.cell(190,4,txt='', ln=True)
        pdf.cell(190,4, txt='02 - Acolhimento', border=True,ln=True)
        pdf.cell(190,4, txt='TAX:_______ PA:_______ FC:_______ '
                            'FR:_______ Glascow:_______ DX:_______ SAT:_______', border=True)
        pdf.cell(190,4,txt='', ln=True)
        pdf.cell(190,4, txt='Vacinado COVID-19: (  ) Sim (  ) Não (  ) Primeira Dose (  ) Segunda Dose '
                            '(  ) Terceira Dose (  ) Dose única', ln=True)
        pdf.cell(190,4,txt='',ln=True)
        pdf.cell(190, 4, txt='Acolhimento com classificação de risco:',border=True, ln=True)
        pdf.cell(190,4,txt='',ln=True, border=True)
        pdf.cell(190,4,txt='',ln=True, border=True)
        pdf.cell(190, 4, txt='', ln=True)
        pdf.cell(190, 4, txt='03 - ANAMNESE:',border=True, ln=True)
        pdf.cell(190, 4, txt='',border=True, ln=True)
        pdf.cell(190, 4, txt='',border=True, ln=True)
        pdf.cell(190, 4, txt='',border=True, ln=True)
        pdf.cell(190, 4, txt='',border=True, ln=True)
        pdf.cell(190, 4, txt='Alergia: (   ) Não (   ) Sim - Qual:',border=True, ln=True)
        pdf.cell(190, 4, txt='', ln=True)
        pdf.cell(190, 4, txt='04 - EXAME FÍSICO:',border=True, ln=True)
        pdf.cell(190, 4, txt='',border=True, ln=True)
        pdf.cell(190, 4, txt='',border=True, ln=True)
        pdf.cell(190, 4, txt='',border=True, ln=True)
        pdf.cell(190, 4, txt='', ln=True)
        pdf.cell(190, 4, txt='05 - EXAMES COMPLEMENTARES SOLICITADOS:',border=True, ln=True)
        pdf.cell(190, 4, txt='(   ) Laboratório - (   ) Radiológico - (   ) ECG - '
                             '(   ) Outros:',border=True, ln=True)
        pdf.cell(190, 4,txt='Hipótese do Diagnóstico:',border=True,ln=True)
        pdf.cell(190, 4, txt='',border=True, ln=True)
        pdf.cell(190, 4, txt='',border=True, ln=True)
        pdf.cell(10, 10,txt='CID:', border=True)
        pdf.cell(20,10,txt='        ',border=True,ln=True)
        pdf.cell(190,4, txt='Conduta: (   ) Medicação - (   ) Observação - (   ) Cross',border=True, ln=True)
        pdf.cell(190,4, txt='Saída: Data/Hora____/____/_______ às _____:______h (   ) Alta Médica - (   ) Evasão - '
                            '(   ) Óbito',border=True,ln=True)
        pdf.cell(190, 4, txt='', ln=True)
        pdf.cell(190, 4, txt='06 - PRESCRIÇÃO MÉDICA:',border=True, ln=True)
        pdf.cell(190, 4, txt='',border=True, ln=True)
        pdf.cell(190, 4, txt='',border=True, ln=True)
        pdf.cell(190, 4, txt='',border=True, ln=True)
        pdf.cell(190, 4, txt='',border=True, ln=True)
        pdf.cell(190, 4, txt='',border=True, ln=True)
        pdf.cell(190, 4, txt='',border=True, ln=True)
        pdf.cell(190, 4, txt='',border=True, ln=True)
        pdf.cell(190, 4, txt='',border=True, ln=True)
        pdf.cell(190, 4, txt='',border=True, ln=True)
        pdf.cell(190, 4, txt=f'Responsável pelo cadastro: {resultado.head().iat[0, 13]}', ln=True)
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        # Adicione algum conteúdo ao PDF
        pdf.image('logo.jpg', 10, 8, 30)
        pdf.image('sus.png', 170, 10, 30)
        pdf.cell(190, 4, txt="PREFEITURA MUNICIPAL DE SANTA BRANCA", ln=True, align='C')
        pdf.cell(190, 8, txt='SECRETARIA MUNICIPAL DE SAÚDE', ln=True, align='C')
        pdf.cell(190, 7, txt='', ln=True)
        pdf.set_font("Arial", size=8)
        pdf.cell(190, 7, txt='Diretoria da Unidade de Urgência e Emergência 24 Horas',align='C', ln=True)
        pdf.cell(190, 12, txt='', ln=True)
        pdf.cell(190, 4, txt='SF(0,9%) (   )100ML (   )250ML (   )500ml (   )1000ml', ln=True)
        pdf.cell(190, 4, txt='SG: 5%________ML( ) RINGER ________ML( ) GLICOFISIOLÓGICO: ________ML( )', ln=True)
        pdf.cell(190, 4, txt='Medição:', border=True, ln=True)
        pdf.cell(190, 4, txt='', border=True, ln=True)
        pdf.cell(190, 4, txt='', border=True, ln=True)
        pdf.cell(190, 4, txt='', border=True, ln=True)
        pdf.cell(190, 4, txt='', border=True, ln=True)
        pdf.cell(190, 30, txt='', ln=True)
        pdf.set_font("Arial", size=12)
        pdf.cell(10,6,txt='(   ) Equipo',align='L')
        pdf.cell(130,6,txt='(   ) Agulha - 13x45',align='C')
        pdf.cell(14,6,txt='(   ) Seringa 1ML',ln=True, align='R')

        pdf.cell(10,6,txt='(   ) Poliflix',align='L')
        pdf.cell(134,6,txt='(   ) Agulha - 20x0,55',align='C')
        pdf.cell(10,6,txt='(   ) Seringa 3ML',ln=True, align='R')

        pdf.cell(10,6,txt='(   ) Jelco nº______',align='L')
        pdf.cell(128,6,txt='(   ) Agulha - 25x7',align='C')
        pdf.cell(16,6,txt='(   ) Seringa 5ML',ln=True, align='R')

        pdf.cell(10,6,txt='(   ) Scalp nº______',align='L')
        pdf.cell(128,6,txt='(   ) Agulha - 25x8',align='C')
        pdf.cell(18,6,txt='(   ) Seringa 10ML',ln=True, align='R')

        pdf.cell(10,6,txt='(   ) Água destilada',align='L')
        pdf.cell(128,6,txt='(   ) Agulha - 30x7', align='C')
        pdf.cell(18,6,txt='(   ) Seringa 20ML',ln=True, align='R')

        pdf.cell(10,6,txt='(   ) Cloreto 0,09 - 10 ml', align='L')
        pdf.cell(128,6,txt='(   ) Agulha - 30x8',ln=True, align='C')

        pdf.cell(10,6,txt='(   ) Glicose - 25%', align='L')
        pdf.cell(130,6,txt='(   ) Agulha - 40x12',ln=True, align='C')

        pdf.cell(10,6,txt='(   ) Glicose - 50%',ln=True, align='L')
        pdf.cell(10, 80, txt='', ln=True, align='L')
        pdf.cell(10, 5, txt='Saída da Unidade: _____/_____/_______  ás _____:_____h', ln=True, align='L')
        pdf.cell(10, 5, txt='(   ) Alta Médica  (   ) Evasão  (   ) Óbito', ln=True, align='L')
        pdf.cell(10, 5, txt='_____________________________________________________________________', ln=True, align='L')
        pdf.cell(190, 4, txt='Telefone: (12) 3972-6620 - E-mail: saude@santabra.sp.gov.br', ln=True, align='C')

        # Salve o PDF em uma variável
        pdf_output = pdf.output(dest='S').encode('latin1')

        # Codifique o PDF para base64
        b64 = base64.b64encode(pdf_output)
        b64 = b64.decode()

        # Crie um link de download para o PDF
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="ficha_paciente.pdf">{resultado.head().iat[0, 0]}</a>'
        st.markdown(href, unsafe_allow_html=True)
