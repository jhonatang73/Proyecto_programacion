import streamlit as st
import pandas as pd
import numpy as np

#Texto
st.title('Datos Hidrometereológicos Gobierno Regional Piura')
st.write('Agua y Saneamiento')

#Slider
st.title("Titulo")
num = st.slider("num", 0, 100, step=1)
st.write("El numero ingresado es {}".format(num))

#Slider de horario
from datetime import time
appointment = st.slider("Programe la asesoria:",value=(time(11, 30), time(12, 45)))
st.write("Esta agendado para:", appointment)

#Slider de fecha
from datetime import datetime
start_time = st.slider("Ver casos ocurridos en",value=datetime(2020, 1, 1, 9, 30),format="DD/MM/YY - hh:mm")
st.write("Fecha seleccionada:", start_time)

#Ingreso de fecha con calendario
import datetime
d = st.date_input("Fecha de cumpleaños",datetime.date(2019, 7, 6))
st.write('Tu cumpleños es:', d)

#Lista de selección:
option = st.selectbox('¿Cómo desearía ser contactado/a?',('Email', 'Teléfono', 'Whatsapp'))
st.write('Seleccionó:', option)

n = st.slider("n", 5,100, step=1)
chart_data = pd.DataFrame(np.random.randn(n),columns=['data'])
st.line_chart(chart_data)

df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])
#######
import folium
from folium.plugins import MiniMap
mapa = folium.Map()
mapa
         
