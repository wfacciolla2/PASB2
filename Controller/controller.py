import pandas as pd
import streamlit as st
import csv
def df():
    df = pd.read_csv("C:/Users/welli/PycharmProjects/ProntoAtendimentoSB/db2.csv",
                     encoding="latin-1",
                     sep=",",
                     header=0)
    return df







