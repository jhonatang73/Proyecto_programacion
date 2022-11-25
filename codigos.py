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

import folium
mapa_base = fl.Map()
mapa_base.save("mapa_folium_001.html")
mapa_base

palacio_nacional = fl.Map(location=[18.47559892878191, -69.89774247032956],zoom_start=16)
palacio_nacional.save("mapa_folium_002.html")
palacio_nacional

"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st

# app_state = st.experimental_get_query_params()
# app_state = {k: v[0] if isinstance(v, list) else v for k, v in app_state.items()} # fetch the first item in each query string as we don't have multiple values for each query string key in this example


class MultiApp:
    """Framework for combining multiple streamlit applications.
    Usage:
        def foo():
            st.title("Hello Foo")
        def bar():
            st.title("Hello Bar")
        app = MultiApp()
        app.add_app("Foo", foo)
        app.add_app("Bar", bar)
        app.run()
    It is also possible keep each application in a separate file.
        import foo
        import bar
        app = MultiApp()
        app.add_app("Foo", foo.app)
        app.add_app("Bar", bar.app)
        app.run()
    """

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({"title": title, "function": func})

    def run(self):
        app_state = st.experimental_get_query_params()
        app_state = {
            k: v[0] if isinstance(v, list) else v for k, v in app_state.items()
        }  # fetch the first item in each query string as we don't have multiple values for each query string key in this example

        # st.write('before', app_state)

        titles = [a["title"] for a in self.apps]
        functions = [a["function"] for a in self.apps]
        default_radio = titles.index(app_state["page"]) if "page" in app_state else 0

        st.sidebar.title("Navigation")

        title = st.sidebar.radio("Go To", titles, index=default_radio, key="radio")

        app_state["page"] = st.session_state.radio
        # st.write('after', app_state)

        st.experimental_set_query_params(**app_state)
        # st.experimental_set_query_params(**st.session_state.to_dict())
        functions[titles.index(title)]()

        st.sidebar.title("Contribute")
        st.sidebar.info(
            "This is an open source project and you are very welcome to contribute your "
            "comments, questions, resources and apps as "
            "[issues](https://github.com/giswqs/streamlit-geospatial/issues) or "
            "[pull requests](https://github.com/giswqs/streamlit-geospatial/pulls) "
            "to the [source code](https://github.com/giswqs/streamlit-geospatial). "
        )
         
