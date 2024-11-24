#!/usr/bin/env python
# coding: utf-8

# In[2]:


######################
# Import libraries
######################

import pandas as pd
import streamlit as st
import numpy as np
import altair as alt
from PIL import Image

######################
# Page Title
######################

image = Image.open('Nucleotidos_ADN.png')

st.image(image, use_column_width=True)
st.write("""
<style>
h1 {
    color: #02c74d;
    font-size: 32px;
    text-align: center;
    margin-bottom: 20px;
}

h2 {
    color: #0366d6;
    font-size: 24px;
    margin-bottom: 10px;
}

.subheader {
    color: #02b3c7;
    font-size: 18px;
    margin-bottom: 5px;
}

.output {
    margin-top: 30px;
}

table.dataframe {
    border-collapse: collapse;
    margin-top: 10px;
}

table.dataframe th, table.dataframe td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}

table.dataframe th {
    background-color: #f5f5f5;
}

.chart {
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

st.write("""
# Cuenta de Nucléotidos en ADN
Con esta aplicación se pueden obtener datos detalladamente de la composición de nucleotidos de la cadena de ADN que desees conocer.
Simplemente con escribir una pequeña secuencia de la cadena que gustes podrás conseguir datos para tus investigaciones, proyectos,
experimentos o conocimiento propio.
***
""")


######################
# Input Text Box
######################

#st.sidebar.header('Enter DNA sequence')
st.header('Introduzca secuencia de ADN')

#sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)
sequence = st.text_area("Secuencia", height=100)
sequence = sequence.splitlines()
sequence = sequence[1:] # Skips the sequence name (first line)
sequence = ''.join(sequence) # Concatenates list to string

st.write("""
***
""")

## Prints the input DNA sequence
st.header('secuencia introducida')
sequence

## DNA nucleotide count
st.header('composicion de nucleotidos')


# 1. Print dictionary
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader('1. Print dictionary')
    def DNA_nucleotide_count(seq):
        d = dict([
            ('A', seq.count('A')),
            ('T', seq.count('T')),
            ('G', seq.count('G')),
            ('C', seq.count('C'))
        ])
        return d

    X = DNA_nucleotide_count(sequence)
    st.write(X)

with col2:
    # 2. Print text
    st.subheader('2. Print text')
    st.write('There are ' + str(X['A']) + ' adenine (A)')
    st.write('There are ' + str(X['T']) + ' thymine (T)')
    st.write('There are ' + str(X['G']) + ' guanine (G)')
    st.write('There are ' + str(X['C']) + ' cytosine (C)')

with col3:
    # 3. Display DataFrame
    st.subheader('Tabla')
    df = pd.DataFrame.from_dict(X, orient='index')
    df = df.rename({0: 'count'}, axis='columns')
    df.reset_index(inplace=True)
    df = df.rename(columns={'index': 'nucleotide'})
    st.write(df)

# Add CSS styling for subheaders
st.markdown(
    """
    <style>
    .stHeader > .deco-btn-container > div {
        display: inline-block;
        margin-right: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

### 4. Display Bar Chart using Altair
st.subheader('Gráfica de Barras')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)

p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)

### 5. Display Pie Chart using Altair
st.subheader('Gráfica Circular')

import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'A', 'G', 'T', 'C'
sizes = [seq.count('A'), seq.count('G'), seq.count('T'), seq.count('C')]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'G')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)

st.header('Contact Information')
st.markdown('**Name:** Dipraj Howlader')
st.markdown('- **Email:** dip07.raz@gmail.com')
st.markdown('- **Phone:** +8801710023365')
