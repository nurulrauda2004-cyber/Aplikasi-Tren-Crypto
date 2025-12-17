import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Aplikasi Tren Crypto", layout="wide")

# ===== DATA =====
data = {
    "Tanggal": pd.to_datetime([
        "2024-01-01", "2024-02-01", "2024-03-01",
        "2024-04-01", "2024-05-01"
    ]),
    "Harga": [42000, 45000, 48000, 47000, 50000],
    "Pemasukan": [2000, 3000, 4000, 3500, 5000],
    "Pengeluaran": [1500, 1800, 2000, 2200, 2500],
}

df = pd.DataFrame(data)

# ===== SIDEBAR =====
st.sidebar.title("📊 Menu")
menu = st.sidebar.radio(
    "Pilih Tampilan",
    ["Tren Harga", "Pemasukan", "Pengeluaran"]
)

# ===== HEADER =====
st.title("📊 Dashboard Keuangan Crypto")
st.caption("Dashboard sederhana untuk melihat tren dan keuangan")

# ===== LAYOUT =====
col1, col2 = st.columns([2, 1])

with col1:
    fig, ax = plt.subplots()

    if menu == "Tren Harga":
        ax.plot(df["Tanggal"], df["Harga"])
        ax.set_title("Tren Harga Crypto")
        ax.set_ylabel("Harga")

    elif menu == "Pemasukan":
        ax.bar(df["Tanggal"], df["Pemasukan"])
        ax.set_title("Pemasukan")
        ax.set_ylabel("Jumlah")

    elif menu == "Pengeluaran":
        ax.bar(df["Tanggal"], df["Pengeluaran"])
        ax.set_title("Pengeluaran")
        ax.set_ylabel("Jumlah")

    ax.set_xlabel("Tanggal")
    st.pyplot(fig)

with col2:
    st.subheader("📌 Ringkasan")

    total_masuk = df["Pemasukan"].sum()
    total_keluar = df["Pengeluaran"].sum()
    saldo = total_masuk - total_keluar

    st.metric("Total Pemasukan", f"${total_masuk}")
    st.metric("Total Pengeluaran", f"${total_keluar}")
    st.metric("Saldo", f"${saldo}")
