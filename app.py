import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Aplikasi Tren Crypto")

st.title("📈 Aplikasi Tren Crypto")
st.caption("Melihat naik atau turunnya harga crypto")

# Data Bitcoin dari GitHub
DATA_URL = "https://raw.githubusercontent.com/plotly/datasets/master/bitcoin.csv"

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data(DATA_URL)

# Grafik harga
fig, ax = plt.subplots()
ax.plot(df["Date"], df["Close"])
ax.set_xlabel("Tanggal")
ax.set_ylabel("Harga")
st.pyplot(fig)

# Hasil sederhana
if df["Close"].iloc[-1] > df["Close"].iloc[0]:
    st.success("📈 Tren Naik")
else:
    st.error("📉 Tren Turun")
