import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import statsmodels.api as sm

st.title('Proyek Akhir Data Visualization')
st.subheader('By: Yhenis Apriliana')

day = pd.read_csv('/content/day.csv')
day.head()

day = day.rename(columns={'yr': 'year', 'weathersit': 'weather', 'hr': 'hour', 'hum': 'humadity', 'cnt': 'count'})
day.head()

# Data Visualitation Season
st.subheader("Data Visualization Season")
day['season'] = day['season'].replace({1: 'spring', 2: 'summer', 3: 'fall', 4: 'winter'})
season_count = day.groupby('season')['count'].sum()
season_chart = st.bar_chart(season_count)

# Data Visualitation Temperatur
st.subheader("Data Visualization Temperatur")
scatter_plot = sn.scatterplot(x='temp', y='count', data=day)
plt.xlabel('Temperature')
plt.ylabel('Jumlah Pengguna Sepeda')
st.pyplot(scatter_plot.figure)




