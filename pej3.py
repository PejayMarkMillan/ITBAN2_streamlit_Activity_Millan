
import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.title("🌍 COVID-19 Data Dashboard")

country = st.selectbox("Choose a country", ["USA", "Philippines", "India", "Brazil", "Germany"])

url = f"https://disease.sh/v3/covid-19/historical/{country}?lastdays=30"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    if 'timeline' in data:
        timeline = data['timeline']
        cases = pd.Series(timeline['cases'])
        deaths = pd.Series(timeline['deaths'])
        recovered = pd.Series(timeline['recovered'])

        df = pd.DataFrame({
            'Date': cases.index,
            'Cases': cases.values,
            'Deaths': deaths.values,
            'Recovered': recovered.values
        })

        df['Date'] = pd.to_datetime(df['Date'])

        st.subheader("📈 Line Chart - Daily Cases")
        st.line_chart(df.set_index('Date')['Cases'])

        st.subheader("📊 Bar Chart - Daily Deaths")
        st.bar_chart(df.set_index('Date')['Deaths'])

        st.subheader("📉 Area Chart - Daily Recovered")
        st.area_chart(df.set_index('Date')['Recovered'])

        st.subheader("📌 Pie Chart - Total Breakdown")
        totals = {
            'Cases': df['Cases'].iloc[-1],
            'Deaths': df['Deaths'].iloc[-1],
            'Recovered': df['Recovered'].iloc[-1]
        }
        fig, ax = plt.subplots()
        ax.pie(totals.values(), labels=totals.keys(), autopct="%1.1f%%", startangle=90)
        ax.axis("equal")
        st.pyplot(fig)

        st.subheader("📋 Summary")
        st.metric("Total Cases", f"{int(totals['Cases']):,}")
        st.metric("Total Deaths", f"{int(totals['Deaths']):,}")
        st.metric("Total Recovered", f"{int(totals['Recovered']):,}")
    else:
        st.error("No timeline data found.")
else:
    st.error(f"API request failed with status code {response.status_code}")