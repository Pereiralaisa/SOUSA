# -*- coding: utf-8 -*-
"""PI 4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tBaEd40s8A6x7tzYH8scGfqUBcyEW8SM
"""

import pandas as pd
import plotly.express as px
import streamlit as st 
import numpy

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

def validate():
    if origin.value in df['origin'].unique() and textbox.value in df['carrier'].unique():
        return True
    else:
        return False


def response(change):
    if validate():
        if use_date.value:
            filter_list = [i and j and k for i, j, k in
                           zip(df['month'] == month.value, df['carrier'] == textbox.value,
                               df['origin'] == origin.value)]
            temp_df = df[filter_list]

        else:
            filter_list = [i and j for i, j in
                           zip(df['carrier'] == 'DL', df['origin'] == origin.value)]
            temp_df = df[filter_list]
        x1 = temp_df['arr_delay']
        x2 = temp_df['dep_delay']
        with g.batch_update():
            g.data[0].x = x1
            g.data[1].x = x2
            g.layout.barmode = 'overlay'
            g.layout.xaxis.title = 'Delay in Minutes'
            g.layout.yaxis.title = 'Number of Delays'







#fig = px.line(df, x="date", y=column, title=column + ' - ' + state)
#fig.update_layout( xaxis_title='Data', yaxis_title=column.upper(), title = {'x':0.5})


st.title('DADOS COVID-19')
st.write('Nessa aplicação, o usuário tem a possibilidade de interação,e visualização de dados sobre  covid-19. Utilize o menu lateral para alterar a mostragem.')

#st.plotly_chart(fig, use_container_width=True)

st.caption('Projeto desenvolvido por alunos UNIVESP,PROJETO INTEGRADOR IV')
