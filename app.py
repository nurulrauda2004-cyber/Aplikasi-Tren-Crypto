# app.py
# Aplikasi Tren Crypto (Sangat Sederhana)
# Streamlit + GitHub

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Aplikasi Tren Crypto")

st.title("📈 Aplikasi Tren Crypto")
st.caption("Melihat naik atau turunnya harga crypto")

# Data dari GitHub (Bitcoin)
DATA_URL = "https://raw.githubusercontent.com/plotly/datasets/master/bitcoin.csv"

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data(DATA_URL)

# Grafik harga
fig, ax = plt.subplots()
ax.plot(df['Date'], df['Close'])
ax.set_xlabel("Tanggal")
ax.set_ylabel("Harga")
st.pyplot(fig)

# Analisis sederhana
harga_akhir = df['Close'].iloc[-1]
harga_awal = df['Close'].iloc[0]

if harga_akhir > harga_awal:
    st.success("📈 Tren Naik")
else:
    st.error("📉 Tren Turun")
