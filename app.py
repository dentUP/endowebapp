import streamlit as st
import os
import pandas as pd
from datetime import datetime
from domande import DOMANDE
from dati import DATI_PRE_OPERATORI, DATI_INTRA_OPERATORI, DATI_POST_OPERATORI
from storico_pazienti import storico_pazienti
from report_generale import report_generale


st.set_page_config(page_title="EndoWebApp", page_icon="🦷", layout="wide")

def custom_style():
    st.markdown(
        """
        <style>
        @font-face {
            font-family: 'ClashDisplay';
            src: url('ClashDisplay-Semibold.woff2') format('woff2');
            font-weight: normal;
            font-style: normal;
        }

        html, body, [class*="css"]  {
            font-family: 'ClashDisplay', sans-serif;
            background-color: white;
        }

        .button-container {
            display: flex;
            justify-content: center;
            margin-top: 100px;
            gap: 60px;
        }

        .custom-button {
            background-color: #82E7EC;
            color: black;
            padding: 1em 2em;
            font-size: 18px;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.2s ease-in-out;
            width: 250px;
            text-align: center;
        }

        .custom-button:hover {
            background-color: #6dd2d6;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

def login():
    with open("logo.png", "rb") as f:
        st.image(f.read(), width=200)
    st.markdown("<h2 style='text-align: center;'>EndoWebApp - Accesso</h2>", unsafe_allow_html=True)

    username = st.text_input("Inserisci il tuo nome utente (senza spazi):")

    if st.button("Entra"):
        if username.strip() == "":
            st.warning("Per favore inserisci un nome utente valido.")
        else:
            st.session_state.username = username.strip()
            st.session_state.logged_in = True
            filename = f"dati_{username}.csv"
            if not os.path.exists(filename):
                df = pd.DataFrame(columns=["dente", "canali", "strumento", "chiusura", "tempo", "esito", "follow_up"])
                df.to_csv(filename, index=False)
            st.rerun()

def homepage():
    with open("logo.png", "rb") as f:
        st.image(f.read(), width=200)

    st.markdown(f"<h2 style='text-align: center;'>Ciao, {st.session_state.username} 👋</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📋 Case Assessment"):
            st.session_state.page = "assessment"
            st.rerun()
    with col2:
        if st.button("👤 Area Personale"):
            st.session_state.page = "profilo"
            st.rerun()


def case_assessment():
    import random

    st.image("logo.png", width=100)
    st.title("📋 Case Assessment")

    if "step" not in st.session_state:
        st.session_state.step = 0
        st.session_state.risposte = [None] * len(DOMANDE)

    domanda_corrente = DOMANDE[st.session_state.step]
    st.markdown(f"**Domanda {st.session_state.step + 1} di {len(DOMANDE)}**")
    st.write(domanda_corrente["testo"])

    risposta = st.radio("Seleziona una risposta:", domanda_corrente["opzioni"], index=st.session_state.risposte[st.session_state.step] or 0)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        if st.session_state.step > 0:
            if st.button("⬅️ Indietro"):
                st.session_state.risposte[st.session_state.step] = domanda_corrente["opzioni"].index(risposta)
                st.session_state.step -= 1
                st.rerun()

    with col3:
        if st.session_state.step < len(DOMANDE) - 1:
            if st.button("Avanti ➡️"):
                st.session_state.risposte[st.session_state.step] = domanda_corrente["opzioni"].index(risposta)
                st.session_state.step += 1
                st.rerun()
        else:
            if st.button("📊 Visualizza report"):
                st.session_state.risposte[st.session_state.step] = domanda_corrente["opzioni"].index(risposta)
                st.session_state.page = "report"
                st.rerun()

def report_finale():
    from matplotlib import pyplot as plt
    import matplotlib.patches as patches
    import random

    st.image("logo.png", width=100)
    st.title("📈 Risultato Case Assessment")

    risposte = st.session_state.risposte
    punteggi = []
    for i, r in enumerate(risposte):
        if i == 10 and r in [2, 3, 4, 5]:  # Domanda 11, opzioni 3-6
            punteggi.append(3)
        else:
            punteggi.append(r + 1)


    somma = sum(punteggi)
    max_score = len(risposte) * 3
    score_percent = int((somma - len(risposte)) / (2 * len(risposte)) * 100)

    num_difficili = punteggi.count(3)
    if num_difficili == 2:
        score_percent = max(score_percent, 50)
    elif num_difficili == 3:
        score_percent = max(score_percent, 60)
    elif num_difficili >= 4:
        score_percent = max(score_percent, 70)

    if score_percent < 50:
        colore = "🟢 Facile"
    elif score_percent < 70:
        colore = "🟡 Moderato"
    else:
        colore = "🔴 Difficile"

    st.subheader(f"⚙️ Difficoltà del caso: **{colore}**")
    st.markdown("---")

    fig, ax = plt.subplots(figsize=(5, 1.5))
    ax.axis("off")
    ax.add_patch(patches.Rectangle((0, 0), 1, 0.3, color="lightgray", alpha=0.2))
    ax.add_patch(patches.Rectangle((0, 0), score_percent / 100, 0.3, color="green" if score_percent < 50 else "orange" if score_percent < 70 else "red", alpha=0.6))
    ax.text(0.5, 0.15, f"{score_percent}/100", ha='center', va='center', fontsize=16, color='black')
    st.pyplot(fig)

    st.markdown("### 📋 Riepilogo risposte e suggerimenti:")
    for i, r in enumerate(risposte):
        domanda = DOMANDE[i]["testo"]
        risposta = DOMANDE[i]["opzioni"][r]
        st.markdown(f"**{i+1}. {domanda}**")
        st.markdown(f"- Risposta: _{risposta}_")

        suggerimenti = DOMANDE[i].get("suggerimenti", {})
        if r in suggerimenti:
            emoji = random.choice(["💡", "⚠️", "💎", "🚀", "📌"])
            st.markdown(f"{emoji} **Suggerimento:** {suggerimenti[r]}")
        st.markdown("---")

def area_personale():
    with open("logo.png", "rb") as f:
        st.image(f.read(), width=100)

    st.title("👤 Area Personale")
    scelta = st.radio("Scegli una sezione:", ["📋 Nuovo Paziente", "📁 Storico Pazienti", "📊 Report Generale"])

    if scelta == "📋 Nuovo Paziente":
        nuovo_paziente()
    elif scelta == "📁 Storico Pazienti":
        storico_pazienti()
    elif scelta == "📊 Report Generale":
        report_generale()

    if st.button("⬅️ Torna alla Home"):
        st.session_state.page = "home"
        st.rerun()

def nuovo_paziente():
    st.image("logo.png", width=100)
    st.title("📋 Inserimento Nuovo Paziente")

    with st.form(key="form_paziente"):
        # 🟩 Dati Pre-Operatori
        with st.expander("🟩 Dati Pre-Operatori", expanded=True):
            for voce in DATI_PRE_OPERATORI:
                chiave = voce["chiave"]
                label = voce["etichetta"]
                tipo = voce["tipo"]
                opzioni = voce.get("opzioni", [])

                if tipo == "data":
                    st.date_input(label, key=chiave)
                elif tipo == "testo":
                    st.text_input(label, key=chiave)
                elif tipo == "select":
                    st.selectbox(label, options=opzioni, key=chiave)
                elif tipo == "multiselect":
                    st.multiselect(label, options=opzioni, key=chiave)
                elif tipo == "slider":
                    min_val = voce.get("min", 0)
                    max_val = voce.get("max", 100)
                    st.slider(label, min_val, max_val, key=chiave)

        # 🟦 Dati Intra-Operatori
        with st.expander("🟦 Dati Intra-Operatori", expanded=False):
            for voce in DATI_INTRA_OPERATORI:
                chiave = voce["chiave"]
                label = voce["etichetta"]
                tipo = voce["tipo"]
                opzioni = voce.get("opzioni", [])

                if tipo == "testo":
                    st.text_input(label, key=chiave)
                elif tipo == "select":
                    st.selectbox(label, options=opzioni, key=chiave)
                elif tipo == "multiselect":
                    st.multiselect(label, options=opzioni, key=chiave)
                elif tipo == "numero":
                    st.number_input(label, min_value=0, step=1, key=chiave)

        # 🟥 Dati Post-Operatori
        with st.expander("🟥 Dati Post-Operatori", expanded=False):
            for voce in DATI_POST_OPERATORI:
                chiave = voce["chiave"]
                label = voce["etichetta"]
                tipo = voce["tipo"]
                opzioni = voce.get("opzioni", [])

                if tipo == "testo":
                    st.text_input(label, key=chiave)
                elif tipo == "select":
                    st.selectbox(label, options=opzioni, key=chiave)
                elif tipo == "multiselect":
                    st.multiselect(label, options=opzioni, key=chiave)
                elif tipo == "numero":
                    st.number_input(label, min_value=0, step=1, key=chiave)

        submitted = st.form_submit_button("💾 Salva paziente")
        if submitted:
            # Estrai i dati inseriti
            dati_paziente = {"username": st.session_state.username}
            for lista in [DATI_PRE_OPERATORI, DATI_INTRA_OPERATORI, DATI_POST_OPERATORI]:
                for voce in lista:
                    chiave = voce["chiave"]
                    valore = st.session_state.get(chiave)
                    # Se è lista (es. multiselect), uniscila in stringa
                    if isinstance(valore, list):
                     valore = ", ".join(map(str, valore))
                dati_paziente[chiave] = valore


            # Identificatore univoco del paziente
            chiave_id = f"{dati_paziente.get('nome', '')}_{dati_paziente.get('cognome', '')}".strip().lower().replace(" ", "")
            if not chiave_id:
                st.error("⚠️ Inserisci nome e cognome del paziente per salvare i dati.")
                return

            # Nome del file CSV personale
            file_csv = f"dati_{st.session_state.username}.csv"

            # Carica dati esistenti
            if os.path.exists(file_csv):
                df = pd.read_csv(file_csv)
            else:
                df = pd.DataFrame()

            # Rimuovi righe con lo stesso ID paziente se già presenti
            df["chiave_id"] = df["nome"].astype(str).str.lower().str.replace(" ", "") + "_" + df["cognome"].astype(str).str.lower().str.replace(" ", "")
            df = df[df["chiave_id"] != chiave_id]
            df = df.drop(columns="chiave_id", errors="ignore")


            # Aggiungi la nuova riga
            df = pd.concat([df, pd.DataFrame([dati_paziente])], ignore_index=True)

            # Salva nel file CSV
            df.to_csv(file_csv, index=False)
            st.success("✅ Dati salvati con successo.")

# Funzione: profilo_paziente()
def profilo_paziente():
    st.image("logo.png", width=100)
    st.title("📝 Profilo Paziente")

    with st.form(key="form_modifica"):
        with st.expander("🟩 Dati Pre-Operatori", expanded=True):
            for voce in DATI_PRE_OPERATORI:
                chiave = voce["chiave"]
                tipo = voce["tipo"]
                label = voce["etichetta"]
                opzioni = voce.get("opzioni", [])

                valore = st.session_state.get(chiave, "")

                if tipo == "data":
                    st.date_input(label, value=valore, key=chiave)
                elif tipo == "testo":
                    st.text_input(label, value=valore, key=chiave)
                elif tipo == "select":
                    st.selectbox(label, options=opzioni, index=opzioni.index(valore) if valore in opzioni else 0, key=chiave)
                elif tipo == "multiselect":
                    st.multiselect(label, options=opzioni, default=valore, key=chiave)
                elif tipo == "slider":
                    min_val = voce.get("min", 0)
                    max_val = voce.get("max", 100)
                    st.slider(label, min_val, max_val, value=valore, key=chiave)

        with st.expander("🟦 Dati Intra-Operatori", expanded=False):
            for voce in DATI_INTRA_OPERATORI:
                chiave = voce["chiave"]
                tipo = voce["tipo"]
                label = voce["etichetta"]
                opzioni = voce.get("opzioni", [])

                valore = st.session_state.get(chiave, "")

                if tipo == "testo":
                    st.text_input(label, value=valore, key=chiave)
                elif tipo == "select":
                    st.selectbox(label, options=opzioni, index=opzioni.index(valore) if valore in opzioni else 0, key=chiave)
                elif tipo == "multiselect":
                    st.multiselect(label, options=opzioni, default=valore, key=chiave)
                elif tipo == "numero":
                    st.number_input(label, min_value=0, step=1, value=valore, key=chiave)

        with st.expander("🟥 Dati Post-Operatori", expanded=False):
            for voce in DATI_POST_OPERATORI:
                chiave = voce["chiave"]
                tipo = voce["tipo"]
                label = voce["etichetta"]
                opzioni = voce.get("opzioni", [])

                valore = st.session_state.get(chiave, "")

                if tipo == "testo":
                    st.text_input(label, value=valore, key=chiave)
                elif tipo == "select":
                    st.selectbox(label, options=opzioni, index=opzioni.index(valore) if valore in opzioni else 0, key=chiave)
                elif tipo == "multiselect":
                    st.multiselect(label, options=opzioni, default=valore, key=chiave)
                elif tipo == "numero":
                    st.number_input(label, min_value=0, step=1, value=valore, key=chiave)

        if st.form_submit_button("💾 Salva modifiche"):
            dati_paziente = {"username": st.session_state.username}
            for lista in [DATI_PRE_OPERATORI, DATI_INTRA_OPERATORI, DATI_POST_OPERATORI]:
                for voce in lista:
                    chiave = voce["chiave"]
                    dati_paziente[chiave] = st.session_state.get(chiave)

            file_csv = f"dati_{st.session_state.username}.csv"
            df = pd.read_csv(file_csv)
            index = st.session_state.get("paziente_index", None)
            if index is not None:
                df.loc[index] = dati_paziente
                df.to_csv(file_csv, index=False)
                st.success("✅ Modifiche salvate correttamente.")
                st.session_state.page = "storico"
                st.rerun()

def profilo_paziente():
    st.image("logo.png", width=100)
    st.title("👤 Modifica dati paziente")

    # Crea il form per la modifica dei dati
    with st.form("form_modifica_paziente"):
        dati_paziente = {"username": st.session_state.username}

        # Mostra tutti i campi suddivisi in pre-, intra- e post-operatori
        for lista in [DATI_PRE_OPERATORI, DATI_INTRA_OPERATORI, DATI_POST_OPERATORI]:
            for voce in lista:
                chiave = voce["chiave"]
                testo = voce["testo"]
                opzioni = voce["opzioni"]
                valore_corrente = st.session_state.get(chiave, opzioni[0])
                dati_paziente[chiave] = st.selectbox(testo, opzioni, index=opzioni.index(valore_corrente), key=chiave)

        submitted = st.form_submit_button("💾 Salva modifiche")

        # Pulsante per tornare indietro
    if st.button("🔙 Torna allo storico"):
        st.session_state.page = "storico"
        st.rerun()

    if submitted:
        # Recupera il file CSV
        file_csv = f"dati_{st.session_state.username}.csv"
        if os.path.exists(file_csv):
            df = pd.read_csv(file_csv)
        else:
            st.error("❌ File dati non trovato.")
            return

        # Sostituisci la riga esistente all'indice salvato
        index = st.session_state.get("paziente_index")
        if index is not None and index < len(df):
            for chiave, valore in dati_paziente.items():
                df.at[index, chiave] = valore
            df.to_csv(file_csv, index=False)
            st.success("✅ Modifiche salvate con successo.")
            st.session_state.page = "storico"
            st.session_state.modifica_paziente = False
            st.rerun()
        else:
            st.error("❌ Impossibile trovare il paziente da modificare.")


def report_generale():
    st.title("📊 Report Generale")
    username = st.session_state.username
    file_csv = f"dati_{username}.csv"

    try:
        df = pd.read_csv(file_csv)
        st.success(f"Sono stati caricati {len(df)} casi per l'utente {username}.")
    except FileNotFoundError:
        st.error("Nessun dato trovato. Inserisci almeno un paziente per generare un report.")
        return

    def genera_grafico(colonna, etichetta):
        if colonna not in df.columns:
            st.warning(f"Colonna '{colonna}' non trovata.")
            return

        serie = df[colonna].dropna()

        # Per i campi multirisposta separati da punto e virgola
        if serie.str.contains(";").any():
            tutte = serie.str.split(";").explode()
            conteggio = tutte.value_counts()
        else:
            conteggio = serie.value_counts()

        if conteggio.empty:
            st.info(f"Nessun dato disponibile per '{etichetta}'.")
            return

        st.subheader(etichetta)
        fig, ax = plt.subplots()
        if len(conteggio) <= 6:
            ax.pie(conteggio, labels=conteggio.index, autopct="%1.1f%%", startangle=90)
            ax.axis("equal")
        else:
            ax.bar(conteggio.index, conteggio.values)
            ax.set_ylabel("Frequenza")
            ax.set_xticklabels(conteggio.index, rotation=45, ha="right")
        st.pyplot(fig)

    # 🟩 PRE-OPERATORI
    with st.expander("🟩 Dati Pre-Operatori"):
        for campo in DATI_PRE_OPERATORI:
            if campo["tipo"] in ["select", "multiselect"]:
                genera_grafico(campo["chiave"], campo["etichetta"])

    # 🟦 INTRA-OPERATORI
    with st.expander("🟦 Dati Intra-Operatori"):
        for campo in DATI_INTRA_OPERATORI:
            if campo["tipo"] in ["select", "multiselect"]:
                genera_grafico(campo["chiave"], campo["etichetta"])

    # 🟥 POST-OPERATORI
    with st.expander("🟥 Dati Post-Operatori"):
        for campo in DATI_POST_OPERATORI:
            if campo["tipo"] in ["select", "multiselect"]:
                genera_grafico(campo["chiave"], campo["etichetta"])

    if st.button("⬅️ Torna all'Area Personale"):
        st.session_state.page = "area_personale"
        st.rerun()


# 🔁 Modifica finale nell’area_personale()
def area_personale():
    with open("logo.png", "rb") as f:
        st.image(f.read(), width=100)

    st.title("👤 Area Personale")
    scelta = st.radio("Scegli una sezione:", ["📋 Nuovo Paziente", "📁 Storico Pazienti", "📊 Report Generale"])

    if scelta == "📋 Nuovo Paziente":
        nuovo_paziente()
    elif scelta == "📁 Storico Pazienti":
        storico_pazienti()
    elif scelta == "📊 Report Generale":
        report_generale()

    if st.button("⬅️ Torna alla Home"):
        st.session_state.page = "home"
        st.rerun()



# Inizializzazione dello stato
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "home"

# Logica principale
# Logica principale
if not st.session_state.logged_in:
    login()
else:
    if st.session_state.page == "profilo":
        area_personale()
    elif st.session_state.page == "assessment":
        case_assessment()
    elif st.session_state.page == "report":
        report_finale()
    elif st.session_state.page == "storico":
        storico_pazienti()
    elif st.session_state.page == "modifica":
        profilo_paziente()
    else:
        homepage()




