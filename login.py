# login.py
import streamlit as st
import os
import json

USERS_FILE = "utenti.json"

def carica_utenti():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}

def salva_utenti(utenti):
    with open(USERS_FILE, "w") as f:
        json.dump(utenti, f)

def registra_nuovo_utente(username):
    utenti = carica_utenti()
    if username in utenti:
        return False  # Username già esistente
    utenti[username] = {}
    salva_utenti(utenti)
    return True

def login_utente():
    st.title("🔐 Login DentUP")

    tab1, tab2 = st.tabs(["🔑 Login", "🆕 Registrati"])

    with tab1:
        username = st.text_input("Inserisci il tuo username", key="login_username")
        if st.button("Entra"):
            utenti = carica_utenti()
            if username in utenti:
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.rerun()
            else:
                st.error("❌ Username non trovato. Registrati prima.")

    with tab2:
        new_username = st.text_input("Scegli un username", key="register_username")
        if st.button("Registrati"):
            if registra_nuovo_utente(new_username):
                st.success("✅ Registrazione completata. Ora puoi fare login.")
            else:
                st.error("❌ Username già esistente.")
