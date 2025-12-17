import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Aplikasi Tren Crypto")

st.title("📈 Aplikasi Tren Crypto")
st.caption("Melihat naik atau turunnya harga crypto")

# Baca data dari file lokal
df = pd.read_csv("bitcoin.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Tampilkan grafik
fig, ax = plt.subplots()
ax.plot(df["Date"], df["Price"])
ax.set_xlabel("Tanggal")
ax.set_ylabel("Harga")
st.pyplot(fig)

# Kesimpulan sederhana
if df["Price"].iloc[-1] > df["Pri]()
