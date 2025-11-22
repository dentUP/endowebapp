import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from dati import DATI_PRE_OPERATORI, DATI_INTRA_OPERATORI, DATI_POST_OPERATORI

def carica_dati():
    try:
        return pd.read_csv("pazienti.csv")
    except FileNotFoundError:
        st.warning("⚠️ Nessun file CSV trovato. Inserisci almeno un paziente per generare il report.")
        return pd.DataFrame()

def mostra_grafico_variabile(df, voce):
    chiave = voce["chiave"]
    etichetta = voce["etichetta"]

    if chiave not in df.columns:
        st.write(f"❌ Variabile non trovata nel file CSV: `{chiave}`")
        return

    dati = df[chiave].dropna()

    if dati.empty:
        st.write("Nessun dato disponibile per questa variabile.")
        return

    conteggi = dati.value_counts()
    
    fig, ax = plt.subplots()
    if len(conteggi) <= 5:
        ax.pie(conteggi, labels=conteggi.index, autopct='%1.1f%%', startangle=90)
        ax.axis("equal")
        st.pyplot(fig)
    else:
        ax.bar(conteggi.index.astype(str), conteggi.values)
        ax.set_ylabel("Frequenza")
        ax.set_title(etichetta)
        plt.xticks(rotation=45)
        st.pyplot(fig)

def report_generale():
    st.title("📊 Report Generale")

    df = carica_dati()
    if df.empty:
        return

    st.subheader("🟩 Dati Pre-Operatori")
    for voce in DATI_PRE_OPERATORI:
        with st.expander(voce["etichetta"]):
            mostra_grafico_variabile(df, voce)

    st.subheader("🟦 Dati Intra-Operatori")
    for voce in DATI_INTRA_OPERATORI:
        with st.expander(voce["etichetta"]):
            mostra_grafico_variabile(df, voce)

    st.subheader("🟥 Dati Post-Operatori")
    for voce in DATI_POST_OPERATORI:
        with st.expander(voce["etichetta"]):
            mostra_grafico_variabile(df, voce)

    st.button("⬅️ Torna alla Home", on_click=lambda: cambia_pagina("home"))

def cambia_pagina(pagina):
    st.session_state.page = pagina
    st.rerun()
