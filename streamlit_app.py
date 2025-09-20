import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌍 Climate Dashboard: Global Temperature Trends")

# Load data
df = pd.read_csv('GlobalLandTemperaturesByCountry.csv.zip')
df['dt'] = pd.to_datetime(df['dt'])
df['Year'] = df['dt'].dt.year
climate = df.groupby('Year').agg({
    'AverageTemperature':'mean',
    'AverageTemperatureUncertainty':'mean'
}).reset_index()

# Slider for year range
year_range = st.slider("Select Year Range:",
                       min_value=int(climate['Year'].min()),
                       max_value=int(climate['Year'].max()),
                       value=(1900, 2015))

# Filtered data
filtered = climate[(climate['Year'] >= year_range[0]) & (climate['Year'] <= year_range[1])]

# Line chart for average temperature
fig = px.line(filtered, x="Year", y="AverageTemperature",
              title="Global Average Temperature",
              labels={"AverageTemperature":"Average Temp (°C)"})
st.plotly_chart(fig)

# Optional: Select a specific year from the original data
selected_year = st.selectbox("Select Year", df['Year'].unique())
filtered_data = df[df['Year'] == selected_year]
st.write(filtered_data)
st.markdown("""
The graph illustrates the trajectory of global average temperatures from 1750 to 2015.  
For more than a century before the mid-1800s, temperatures remained relatively stable,  
though measurements from that period carry high uncertainty due to limited observational coverage.  
Beginning around the mid-19th century, coinciding with the Industrial Revolution,  
a distinct upward trend emerges. The rate of warming accelerated after 1970,  
with recent decades showing the sharpest and most consistent rise,  
reaching the highest recorded values near 20 °C.  
The narrowing uncertainty band reflects the reliability of modern climate data,  
strengthening confidence in these trends.
""")
