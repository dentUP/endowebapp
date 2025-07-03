import streamlit as st
import os
import pandas as pd
from domande import DOMANDE

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
    punteggi = [r + 1 for r in risposte]

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

# Inizializzazione dello stato
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "home"

# Logica principale
if not st.session_state.logged_in:
    login()
else:
    if st.session_state.page == "profilo":
        st.header("👤 Profilo personale")
        st.info("Qui vedrai il report dei tuoi trattamenti endodontici (in arrivo).")
    elif st.session_state.page == "assessment":
        case_assessment()
    elif st.session_state.page == "report":
        report_finale()
    else:
        homepage()

