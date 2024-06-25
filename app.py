import streamlit as st
import pandas as pd
import plotly.express as px

# Leer datos
data = pd.read_csv(r'C:\Users\crist\Documents\Documentos\ds_my_projects\app_web\vehicles_us.csv')

# Encabezado
st.header('Panel de Control de Anuncios de Venta de Coches')

# Crear una casilla de verificación para el histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write('Histograma de Odómetro')
    fig = px.histogram(data, x="odometer")
    st.plotly_chart(fig)

# Crear una casilla de verificación para el gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:
    st.write('Gráfico de Dispersión de Precio vs Odómetro')
    fig = px.scatter(data, x="odometer", y="price")
    st.plotly_chart(fig)