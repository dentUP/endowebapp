# File dati.py - Contiene le strutture per i dati pre-, intra- e post-operatori

DATI_PRE_OPERATORI = [
    {"chiave": "nome","etichetta": "Nome del paziente","tipo": "testo"},
    {"chiave": "cognome","etichetta": "Cognome del paziente","tipo": "testo"},
    {"chiave": "data_trattamento", "etichetta": "Data del trattamento", "tipo": "data"},
    {"chiave": "sede_trattamento", "etichetta": "Clinica o sede di trattamento", "tipo": "select", "opzioni": []},
    {"chiave": "sesso", "etichetta": "Sesso", "tipo": "select", "opzioni": ["M", "F"]},
    {"chiave": "eta", "etichetta": "Età", "tipo": "select", "opzioni": ["<17", "18-35", "36-65", ">66"]},
    {"chiave": "patologie", "etichetta": "Patologie sistemiche", "tipo": "multiselect", "opzioni": [
        "Nessuna", "Cardiopatia ischemica", "Ipertensione arteriosa", "Scompenso cardiaco", "Aritmie / Pacemaker",
        "Valvulopatia / Endocardite batterica", "Diabete tipo 1", "Diabete tipo 2", "Dislipidemia", "Obesità",
        "Asma", "BPCO", "Allergie farmacologiche", "Malattie autoimmuni", "IBD", "Epatopatia cronica",
        "Nefropatia", "Osteoporosi", "Tumore", "Radio/Chemioterapia testa-collo", "Disturbi coagulazione",
        "Epilessia", "Alzheimer / Demenza", "Depressione / Ansia", "Trapianto", "Immunodepressione / HIV",
        "Gravidanza", "Altro"
    ]},
    {"chiave": "tipologia_dente", "etichetta": "Tipologia di dente", "tipo": "select", "opzioni": [
        "Incisivi superiori", "Canino superiore", "Primo premolare superiore", "Secondo premolare superiore",
        "Primo molare superiore", "Secondo molare superiore", "Terzo molare superiore", "Incisivi inferiori",
        "Canino inferiore", "Primo premolare inferiore", "Secondo premolare inferiore", "Primo molare inferiore",
        "Secondo molare inferiore", "Terzo molare inferiore"
    ]},
    {"chiave": "tipologia_trattamento", "etichetta": "Tipologia di trattamento", "tipo": "select", "opzioni": [
        "Trattamento endodontico primario", "Ritrattamento non chirurgico", "Ritrattamento chirurgico"
    ]},
    {"chiave": "stato_periapicale", "etichetta": "Stato periapicale iniziale", "tipo": "select", "opzioni": [
        "Presenza di lesione", "Assenza di lesione"
    ]},
    {"chiave": "sintomi_iniziali", "etichetta": "Sintomatologia", "tipo": "select", "opzioni": ["Si", "No"]},
    {"chiave": "presenza_crack", "etichetta": "Presenza di crack", "tipo": "select", "opzioni": ["Si", "No"]},
    {"chiave": "lesione_endo_paro", "etichetta": "Presenza di lesione endo-parodontale", "tipo": "select", "opzioni": ["Si", "No"]},
    {"chiave": "motivo_trattamento", "etichetta": "Motivo del trattamento", "tipo": "multiselect", "opzioni": [
        "Carie destruente", "Riassorbimento", "Trauma", "Necrosi", "Pulpite", "Frattura coronale",
        "Restauro incongruo", "Esigenza protesica", "Altra causa"
    ]},
    {"chiave": "diagnosi_rx", "etichetta": "Esame radiografico di diagnosi", "tipo": "select", "opzioni": ["RX", "RX + CBCT"]},
    {"chiave": "difficolta_case", "etichetta": "Difficoltà calcolata con 'Case Assessment'", "tipo": "select", "opzioni": ["Facile", "Moderato", "Difficile"]}
]

DATI_INTRA_OPERATORI = [
    {"chiave": "ingrandimento", "etichetta": "Sistemi di ingrandimento", "tipo": "select", "opzioni": ["Si", "No"]},
    {"chiave": "design_accesso", "etichetta": "Design apertura camerale", "tipo": "select", "opzioni": [
        "Accesso tradizionale", "Accesso conservativo", "Accesso minimamente conservativo", "Accesso Truss",
        "Accesso ninja", "Accesso tramite restauri", "Accesso tramite carie", "Altro"
    ]},
    {"chiave": "ultrasuoni", "etichetta": "Utilizzo degli ultrasuoni", "tipo": "select", "opzioni": ["Si", "No"]},
    {"chiave": "isolamento_diga", "etichetta": "Isolamento con diga di gomma", "tipo": "select", "opzioni": ["Si", "No"]},
    {"chiave": "strumenti_utilizzati", "etichetta": "Sistematica strumenti utilizzati", "tipo": "select", "opzioni": [
        "HyFlex EDM", "HyFlex CM", "OneCurve", "Protaper Universal", "Protaper Gold", "Protaper Ultimate", 
        "Trunatomy", "Vortex Blue", "Reciproc", "Reciproc Blue", "WaveOne", "WaveOne Gold", "XP-Endo",
        "EdgeTaper", "EdgeTaper Platinum", "EdgeOne Fire", "EdgeFile X7", "EdgeV-Taper", "BlueShaper", 
        "BlueShaper PRO", "Excalibur", "Direct-R Gold", "Direct Gold", "Plex", "Sky Taper", "F 360",
        "ZenFlex", "F-One", "Armony", "Altro"
    ]},
    {"chiave": "irriganti", "etichetta": "Tipologia di irrigante utilizzato", "tipo": "multiselect", "opzioni": [
        "NaOCl 1-2%", "NaOCl 5%", "EDTA 17%", "EDTA gel", "HEDP", "CHX", "Acido citrico", "Altro"
    ]},
    {"chiave": "attivazione_irrigante", "etichetta": "Attivazione dell'irrigante", "tipo": "select", "opzioni": [
        "No", "Agitazione manuale", "Agitazione sonica", "Attivazione ultrasonica", "Attivazione laser",
        "Attivazione multisonica", "Irrigazione a pressione negativa", "Altro"
    ]},
    {"chiave": "otturazione", "etichetta": "Tecnica otturazione canalare", "tipo": "select", "opzioni": [
        "Compattazione verticale a caldo", "Carrier-based", "Termo-compattazione", "Guttapercha fluida",
        "Cemento bioceramico a freddo", "Cemento bioceramico a caldo", "Altro"
    ]},
    {"chiave": "cemento", "etichetta": "Tipologia di cemento utilizzato", "tipo": "select", "opzioni": ["ZOE", "Resinoso", "Bioceramico", "Altro"]},
    {"chiave": "complicanze", "etichetta": "Complicanze intraoperatorie", "tipo": "multiselect", "opzioni": [
        "Nessuna", "Strumento fratturato", "Perforazione", "Gradino", "Sanguinamento persistente",
        "Blowout apicale", "Altro"
    ]},
    {"chiave": "tempo_operatorio", "etichetta": "Tempo operatorio totale (minuti)", "tipo": "numero"}
]

DATI_POST_OPERATORI = [
    {"chiave": "sintomi_post", "etichetta": "Sintomatologia post-operatoria", "tipo": "select", "opzioni": ["Si", "No"]},
    {"chiave": "segni_clinici", "etichetta": "Segni clinici post-operatori", "tipo": "multiselect", "opzioni": [
        "Nessuno", "Gonfiore", "Fistola", "Sanguinamento persistente", "Difficoltà masticatoria", "Altri"
    ]},
    {"chiave": "antibiotico", "etichetta": "Copertura antibiotica", "tipo": "select", "opzioni": ["Si", "No"]},
    {"chiave": "medicazione", "etichetta": "Medicazione intermedia", "tipo": "select", "opzioni": ["No", "Idrossido di calcio", "Altro"]},
    {"chiave": "perno", "etichetta": "Inserimento perno", "tipo": "select", "opzioni": ["No", "Perno in fibra", "Perno-moncone", "Perno attivo"]},
    {"chiave": "restauro", "etichetta": "Tipologia di restauro post-endodontico", "tipo": "select", "opzioni": [
        "Restauro diretto", "Inlay", "Onlay", "Overlay", "Endocrown", "Corona"
    ]},
    {"chiave": "follow_up", "etichetta": "Follow-up", "tipo": "select", "opzioni": [
        "Nessun fallimento", "Fallimento a 2 mesi", "Fallimento 2–4 mesi", "Fallimento 4–6 mesi",
        "Fallimento 6–12 mesi", "Fallimento 12–24 mesi", "Fallimento 24–48 mesi", "Fallimento > 48 mesi"
    ]},
    {"chiave": "motivo_fallimento", "etichetta": "Motivo del fallimento", "tipo": "multiselect", "opzioni": [
        "Dolore persistente", "Gonfiore / ascesso", "Lesione periapicale persistente", "Nuova lesione periapicale",
        "Riassorbimento radicolare", "Frattura verticale", "Motivi parodontali", "Altro"
    ]}
]
