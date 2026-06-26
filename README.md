# Cuadro de Mandos de Anuncios de Vehículos

Este es un proyecto interactivo desarrollado en Python utilizando **Streamlit** y **Plotly Express** para analizar un conjunto de datos de anuncios de venta de coches en los Estados Unidos.

## Características
- Visualización de la distribución del kilometraje (Odómetro) mediante histogramas.
- Análisis de la relación entre el precio del vehículo y su kilometraje mediante gráficos de dispersión.
- Panel de control web interactivo con filtros dinámicos.

## Tecnologías Utilizadas
- Python 3.9+
- Streamlit
- Pandas
- Plotly Express

## Cómo ejecutar localmente
1. Clonar el repositorio.
2. Crear un entorno virtual: `python3 -m venv vehicles_env`
3. Activar el entorno: `source vehicles_env/bin/activate`
4. Instalar dependencias: `pip install -r requirements.txt`
5. Lanzar la app: `streamlit run app.py`