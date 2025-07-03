# domande.py

DOMANDE = [
    {
        "testo": "Collaboratività del paziente",
        "opzioni": [
            "Collaborante",
            "Ansioso ma collaborante",
            "Non collaborante"
        ],
        "suggerimenti": {
            1: "In caso di paziente ansioso collaborante valutare premedicazione con ansiolitici",
            2: "Considerare trattamento in sedazione profonda o anestesia generale"
        }
    },
    {
        "testo": "Capacità di apertura della bocca",
        "opzioni": [
            "Nessuna limitazione",
            "Leggera limitazione nell'apertura o presenza di massetere e/o bolla di Bichat ipersviluppati",
            "Significativa limitazione nell'apertura o presenza di massetere e/o bolla di Bichat ipersviluppati"
        ],
        "suggerimenti": {
            1: "Se la lunghezza del canale lo consente usare strumenti di ridotta lunghezza o abbassare preventivamente il tavolato occlusale dell’elemento."
        }
    },
    {
        "testo": "Riflesso del vomito",
        "opzioni": [
            "No",
            "Riflesso stimolato solo con dispositivi o strumenti",
            "Riflesso estremo che limita qualsiasi trattamento"
        ],
        "suggerimenti": {
            1: "Valutare premedicazioni anti GAG o inserimento di ago o k-file nel punto CV24"
        }
    },
    {
        "testo": "Condizioni d’emergenza",
        "opzioni": [
            "Assenza o minima presenza di dolore/gonfiore",
            "Moderata presenza di dolore/gonfiore",
            "Importante dolore/gonfiore"
        ],
        "suggerimenti": {}
    },
    {
        "testo": "Diagnosi",
        "opzioni": [
            "Segni/sintomi chiaramente riconducibili a cause endodontiche",
            "Necessaria diagnosi differenziale",
            "Diagnosi complessa o sintomatologia cronica oro-facciale"
        ],
        "suggerimenti": {
            1: "Approfondimento radiografico con esame di secondo livello",
            2: "Approfondimento radiografico con esame di secondo livello"
        }
    },
    {
        "testo": "Posizione del dente in arcata",
        "opzioni": [
            "Incisivo, canino, premolare",
            "Primo molare",
            "Secondo o terzo molare"
        ],
        "suggerimenti": {}
    },
    {
        "testo": "Inclinazione mesio-distale del dente",
        "opzioni": [
            "Inclinazione leggera (<10°)",
            "Inclinazione moderata (10° - 30°)",
            "Inclinazione severa (> 30°)"
        ],
        "suggerimenti": {
            1: "Considerare apertura senza isolamento per mantenere asse parallelo, verificare con RX endorale"
        }
    },
    {
        "testo": "Rotazione del dente",
        "opzioni": [
            "Rotazione leggera (<10°)",
            "Rotazione moderata (10° - 30°)",
            "Rotazione severa (> 30°)"
        ],
        "suggerimenti": {
            1: "Considerare apertura senza isolamento per mantenere asse parallelo, verificare con RX endorale"
        }
    },
    {
        "testo": "Isolamento",
        "opzioni": [
            "Isolamento routinario con diga",
            "Richieste modifiche per applicare diga",
            "Diga non possibile"
        ],
        "suggerimenti": {
            2: "Il trattamento potrebbe non essere fattibile senza valutazione chirurgica"
        }
    },
    {
        "testo": "Morfologia della corona del dente",
        "opzioni": [
            "Morfologia normale",
            "Morfologia alterata con difficoltà reperi anatomici",
            "Restauro protesico con gravi alterazioni"
        ],
        "suggerimenti": {
            1: "Studiare bene il caso, usare elementi limitrofi come riferimento, valutare esame di secondo livello",
            2: "Studiare bene il caso, usare elementi limitrofi come riferimento, valutare esame di secondo livello"
        }
    },
    {
        "testo": "Morfologia canalare",
        "opzioni": [
            "Curvatura leggera (<20°)",
            "Curvatura moderata (20° - 50°)",
            "Alterazione complessa: curva doppia, anatomia difficile, >25mm"
        ],
        "suggerimenti": {
            1: "Approccio step-down, early coronal flaring, progressione guidata e conservativa",
            2: "Approccio step-down, utilizzo strumenti martensitici, attenzione al disegno d’accesso",
            3: "Valutare CBCT, considerare strumenti con conicità ridotta, tecnica cono singolo + BC"
        }
    },
    {
        "testo": "Diametro apicale",
        "opzioni": [
            "Apice normale (< 0.55mm)",
            "Riassorbimento o diametro 0.55 - 1mm",
            "Apice beante (> 1 mm)"
        ],
        "suggerimenti": {
            1: "Usare bioceramico per maggiore sigillo e stabilità",
            2: "Apical plug o tecnica a freddo con bioceramici"
        }
    },
    {
        "testo": "Leggibilità radiografica del sistema canalare",
        "opzioni": [
            "Anatomia chiaramente visibile",
            "Canali visibili ma ridotti o con pulpoliti",
            "Calcificazioni o interruzioni canalari"
        ],
        "suggerimenti": {
            1: "Preferire ingrandenti e strumenti progressivi, attenzione al glide path",
            2: "Considerare C-File, evitare martensitici eccessivi"
        }
    },
    {
        "testo": "Prossimità apici a strutture nobili",
        "opzioni": [
            "Distanza > 5mm",
            "Distanza 2mm – 5mm o apice extracorticale",
            "Distanza < 2mm"
        ],
        "suggerimenti": {
            1: "Evitare uso di bioceramici e CaOH se vicino a strutture nobili"
        }
    },
    {
        "testo": "Presenza di riassorbimenti",
        "opzioni": [
            "Nessun riassorbimento clinico/radiografico",
            "Riassorbimento apicale minimo",
            "Riassorbimento interno, esterno o esteso"
        ],
        "suggerimenti": {}
    },
    {
        "testo": "Anamnesi endodontica",
        "opzioni": [
            "Nessun trattamento",
            "Accesso camerale già fatto ma semplice",
            "Ritrattamento con complicanze"
        ],
        "suggerimenti": {}
    },
    {
        "testo": "Condizioni endo-parodontali",
        "opzioni": [
            "Sano o parodontopatia lieve",
            "Lesione endo-parodontale",
            "Grave patologia parodontale, crack, rizectomia"
        ],
        "suggerimenti": {}
    }
]