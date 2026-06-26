import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado principal de la aplicación
st.header('Cuadro de Mandos de Anuncios de Vehículos')

st.write('Selecciona los gráficos que deseas visualizar para analizar el conjunto de datos de anuncios de coches.')

# Crear casillas de verificación para los gráficos
build_histogram = st.checkbox('Mostrar Histograma del Odómetro')
build_scatter = st.checkbox(
    'Mostrar Gráfico de Dispersión (Precio vs. Odómetro)')

# Lógica para construir el histograma si la casilla está seleccionada
if build_histogram:
    st.write('### Distribución de los kilómetros recorridos (Odómetro)')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Lógica para construir el gráfico de dispersión si la casilla está seleccionada
if build_scatter:
    st.write('### Relación entre el Precio y el Odómetro')
    fig_scatter = px.scatter(car_data, x="odometer",
                             y="price", title="Precio vs Kilometraje")
    st.plotly_chart(fig_scatter, use_container_width=True)
