
from pathlib import Path

import streamlit as st
import pandas as pd
import os

def storico_pazienti():
    st.image("logo.png", width=100)
    st.title("📂 Storico Pazienti")

    # Percorso del file CSV personale
    file_csv = f"dati_{st.session_state.username}.csv"

    if os.path.exists(file_csv):
        df = pd.read_csv(file_csv)

        if df.empty:
            st.info("Nessun paziente salvato al momento.")
            return

        # Visualizza tutti i dati
        st.subheader("🗃️ Tutti i dati dei pazienti")
        st.dataframe(df, use_container_width=True)

        # Selezione del paziente da modificare
        st.subheader("✏️ Modifica un paziente")
        pazienti = df["nome"].str.title() + " " + df["cognome"].str.title()
        selezione = st.selectbox("Seleziona un paziente da modificare:", pazienti)

        if selezione:
            index = pazienti[pazienti == selezione].index[0]
            dati_paziente = df.loc[index].to_dict()

            if st.button("🔁 Modifica questo paziente"):
                for chiave, valore in dati_paziente.items():
                    if chiave not in st.session_state:
                        st.session_state[chiave] = valore
                st.session_state["modifica_paziente"] = True
                st.session_state["paziente_index"] = index
                st.session_state.page = "profilo"
                st.experimental_rerun()

    else:
        st.warning("Nessun file trovato. Inserisci prima un nuovo paziente.")



