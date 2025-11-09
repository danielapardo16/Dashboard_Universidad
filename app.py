# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

st.title("Dashboard de Retencion y Satisfaccion Estudiantil")
st.write("""
Este dashboard analiza la **retención**, la **satisfacción** de los estudiantes y la **comparación por términos académicos**
en las diferentes áreas académicas de la universidad.
""")

# Cargar datos
df = pd.read_csv("university_student_data.csv")

# Convertir las columnas a minusculas y eliminar espacios en blanco
df.columns = df.columns.str.strip().str.lower()

# Mostrar columnas del dataset
st.write("Columnas del dataset:", list(df.columns))

# Filtros interactivos
year = st.selectbox("Selecciona el año academico", sorted(df['year'].unique()))
term = st.selectbox("Selecciona el termino academico", sorted(df['term'].unique()))

# Seleccion de area academica 

area = st.selectbox("Selecciona el area academica:", [
    'engineering enrolled', 
    'business enrolled',
    'arts enrolled', 
    'science enrolled'
])
# Filtrar datos segun selecciones 
filtered_data = df[(df['year']==year) & (df['term']==term)] 

# Visualizacion de Retencion
st.subheader("Tasa de Retencion por Año")
fig1, ax1 = plt.subplots(figsize=(8, 5))
sns.lineplot(data=filtered_data, x='year', y='retention rate (%)', marker='o', color='b', ax=ax1)
st.pyplot(fig1)
st.caption("Podemos observar la tendencia de la tasa de retencion a lo largo de los años academicos.")

# Visualizacion de Satisfaccion 
st.subheader("Promedio de satisfaccion estudiantil por año")
fig2, ax2 = plt.subplots(figsize=(8, 5))
sns.barplot(data=filtered_data, x='year', y='student satisfaction (%)', palette='viridis', ax=ax2)
st.pyplot(fig2)
st.caption("El grafico muestra el promedio de satisfaccion estudiantil por año academico.")

# Comparacio por Terminos Academicos
st.subheader("Comparacion de retencion y satisfaccion por terminos academicos")
fig3, ax3 = plt.subplots(figsize=(6, 5))
sns.scatterplot(data=filtered_data.melt(
                    id_vars=['year'], 
                    value_vars=['engineering enrolled', 'business enrolled', 'arts enrolled', 'science enrolled'], 
                    var_name='Area', 
                    value_name='Inscritos'
                ), 
                x='year', y='Inscritos', hue='Area', ax=ax3)
plt.title("Comparacion de incritos por area academica a lo largo de los años")
st.pyplot(fig3)
st.caption("El grafico compara la cantidad de estudiantes inscritos en diferentes areas academicas a lo largo de los años.")


# Mensaje de exito
st.success("Analisis completado exitosamente.")