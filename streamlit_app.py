import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌍 Climate Dashboard: Global Temperature Trends")

# Load data
df = pd.read_csv('/workspaces/temp-time/GlobalLandTemperaturesByCountry.csv.zip', compression='zip')
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
