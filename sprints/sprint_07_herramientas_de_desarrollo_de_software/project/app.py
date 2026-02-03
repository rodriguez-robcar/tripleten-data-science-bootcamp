import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header("Sprint 7 project")

manufacturer_histogram_button = st.button('Histograma de las manufactureras')

if manufacturer_histogram_button:
         
         st.write('Creación de un histograma de las manufactureras')

         car_data["manufacturer"] = car_data["model"].str.split().str[0]
         
         fig = px.histogram(car_data, x="manufacturer")
     
         st.plotly_chart(fig, use_container_width=True)

odometer_year_scatter_button = st.button('Diagrama de dispersión para el odómetro y el precio')

if odometer_year_scatter_button:
         st.write('Creación de un diagrama de dispersión para el odómetro y el precio')
         
         fig = px.scatter(car_data, x="odometer", y="price")
     
         st.plotly_chart(fig, use_container_width=True)

price_histogram_checkbox = st.checkbox('Histograma para los tipos de vehiculo')

if price_histogram_checkbox: # si la casilla de verificación está seleccionada
    st.write('Creación de un histograma de los tipos de vehiculos')
    fig = px.histogram(car_data, x="type")
    st.plotly_chart(fig, use_container_width=True)

price_year_scatter_checkbox = st.checkbox('Diagrama de dispersion para el año del modelo y el precio')

if price_year_scatter_checkbox :
    st.write("Creación de un diagrama de dispersion para el año del modelo y el precio")
    fig = px.scatter(car_data, x="model_year", y="price")
    st.plotly_chart(fig, use_container_width=True)

