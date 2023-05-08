# -*- coding: utf-8 -*-
"""PI 4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tBaEd40s8A6x7tzYH8scGfqUBcyEW8SM
"""

import pandas as pd
import plotly.express as px
import streamlit as st 

#streamlit run codigoBase.py


df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')


df = df.rename(columns={'totalCases': 'Número acumulado de casos','newCases': 'Novos casos','deaths': 'Número acumulado de óbitos','newDeaths': 'Novos óbitos','vaccinated': 'Vacinas aplicadas - primeira dose','vaccinated_second': 'Vacinas aplicadas - segunda dose','vaccinated_single': 'Vacinas aplicadas - dose única','tests': 'Testes Realizados'})


state  = 'SP'
estados = list(df['state'].unique())
#estados = list(df['SP'].unique())
#state = st.sidebar.selectbox('ESTADO', SP)



colunas = ['Número acumulado de casos','Novos casos','Número acumulado de óbitos','Novos óbitos','Vacinas aplicadas - primeira dose','Vacinas aplicadas - segunda dose','Vacinas aplicadas - dose única','Testes Realizados',]
column = st.sidebar.selectbox('Qual tipo de informação?', colunas)


df = df[df['state'] == state]
df = px.data.iris()
 
fig = px.bar(df, x="sepal_width", y="sepal_length",
             color="species", barmode = 'group')
fig.show()

#fig = px.line(df, x="data", y=column, title=column + ' - ' + state)
#fig.update_layout( xaxis_title='Data', yaxis_title=column.upper(), title = {'x':0.5})

st.title('DADOS COVID-19')
st.write('Nessa aplicação, o usuário tem a possibilidade de interação,e visualização de dados sobre  covid-19. Utilize o menu lateral para alterar a mostragem.')

st.plotly_chart(fig, use_container_width=True)

st.caption('Projeto desenvolvido por alunos UNIVESP,PROJETO INTEGRADOR IV')
