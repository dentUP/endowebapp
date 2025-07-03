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
            "Segni o sintomi chiaramente riconducibili a problemi pulpari o periapicali (carie destruente, trauma, frattura, restauro in prossimità della camera pulpare, lesione periapicale, ecc.)",
            "È necessaria un’accurata diagnosi differenziale dei segni e sintomi comuni (zona radiotrasparente in zona camerale o radicolare riconducibile a riassorbimento interno e/o esterno, lesione periapicale a forma di J riconducibile a frattura verticale della radice, lesione endo-parodontale ecc.)",
            "Diagnosi complessa: segni e sintomi non definiti o presenza di sintomatologia cronica oro-facciale."
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
            1: "considerare di aprire la camera pulpare senza isolamento per mantenere l’asse di inserzione della fresa parallelo all’asse lungo dell’elemento dentale. In caso di dubbio verificare il tragitto di apertura con radiografie endorali con centratore.",
            2: "considerare di aprire la camera pulpare senza isolamento per mantenere l’asse di inserzione della fresa parallelo all’asse lungo dell’elemento dentale. In caso di dubbio verificare il tragitto di apertura con radiografie endorali con centratore."
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
            1: "considerare di aprire la camera pulpare senza isolamento per mantenere l’asse di inserzione della fresa parallelo all’asse lungo dell’elemento dentale. In caso di dubbio verificare il tragitto di apertura con radiografie endorali con centratore.",
            2: "considerare di aprire la camera pulpare senza isolamento per mantenere l’asse di inserzione della fresa parallelo all’asse lungo dell’elemento dentale. In caso di dubbio verificare il tragitto di apertura con radiografie endorali con centratore."
        }
    },
    {
        "testo": "Isolamento",
        "opzioni": [
            "Isolamento routinario con diga",
            "Necessarie procedure aggiuntive prima dell’isolamento con diga di gomma (rilocazione del margine cervicale, gengivectomia, modifica del gancio ecc.)",
            "Isolamento con diga di gomma non possibile"
        ],
        "suggerimenti": {
            2: "Probabilmente il trattamento endodontico e post-endodontico non sono fattibili senza prima una valutazione chirurgica del caso."
        }
    },
    {
        "testo": "Morfologia della corona del dente",
        "opzioni": [
            "Morfologia normale",
            "Elemento con morfologia alterata con difficoltà nel reperimento dei reperi anatomici (presenza di restauri estesi con alterazione anatomica occlusale, overlay, corone metal-free/metalliche, alterazione della morofologia usuale (taurodontismo, microdens ecc.)",
            "Restauro protesico con alterazione di inclinazione/rotazione/anatomia dell’elemento o presenza di significativa variante anatomica (dens-in-dente, fusione ecc.)"
        ],
        "suggerimenti": {
            1: "studiare attentamente il caso dal punto di vista radiografico, se necessario prescrivere un esame di secondo livello. Potrebbe essere utile prendere come punti di riferimento gli elementi dentali limitrofi e la loro angolazione, per l’inclinazione della fresa durante il disegno della cavità d’accesso",
            2: "studiare attentamente il caso dal punto di vista radiografico, se necessario prescrivere un esame di secondo livello. Potrebbe essere utile prendere come punti di riferimento gli elementi dentali limitrofi e la loro angolazione, per l’inclinazione della fresa durante il disegno della cavità d’accesso"
        }
    },
    {
    "testo": "Morfologia canalare",
    "opzioni": [
        "Curvatura leggera (< 20°)",
        "Curvatura moderata (20° - 50°)",
        "Curvatura complessa (> 30°) o doppia curvatura",
        "Anatomia canalare atipica (es. premolari con canali multipli, incisivi inferiori con 2 canali, split canalare, entomolaris/paramolaris)",
        "Canali C-shaped o presenza di istmi",
        "Lunghezza canalare > 25 mm"
    ],
        "suggerimenti": {
            1: "Adottare un approccio step-down: dopo apertura della camera pulpare, eseguire subito un early coronal flearing e un allargamento coronale precoce coronalmente rispetto all’inizio della curvatura. Se necessario fare un allargamento coronale selettivo in direzione opposta rispetto alla direzione della curvatura (ricordare che le curvature solitamente sono tridimensionali). Fatto ciò, ingaggiare la curvatura con uno strumento martensitico da glide path o da pre-sagomatura (es. 15/03, 20/04, 17/04) e portare lo strumento verso l’apice senza forzarlo. Se il file non progredisce spontaneamente, prendere il punto di massima inserzione come WL provvisoria ed allargare coronalmente ad esso. Ripetere fino al raggiungimento della WL effettiva. In questi casi un approccio con aperture camerali conservative potrebbe complicare le fasi di sagomatura e detersione, per cui ricordare il concetto di apertura dinamica della camera pulpare: se i file non progrediscono e non hanno accesso facile ai canali, allargare il disegno dell’apertura.",
            2: "Adottare un approccio step-down: dopo apertura della camera pulpare, eseguire subito un early coronal flearing e un allargamento coronale precoce coronalmente rispetto all’inizio della curvatura. Se necessario fare un allargamento coronale selettivo in direzione opposta rispetto alla direzione della curvatura (ricordare che le curvature solitamente sono tridimensionali). Fatto ciò, ingaggiare la curvatura con uno strumento martensitico da glide path o da pre-sagomatura (es. 15/03, 20/04, 17/04) e portare lo strumento verso l’apice senza forzarlo. Se il file non progredisce spontaneamente, prendere il punto di massima inserzione come WL provvisoria ed allargare coronalmente ad esso. Ripetere fino al raggiungimento della WL effettiva. In questi casi un approccio con aperture camerali conservative potrebbe complicare le fasi di sagomatura e detersione, per cui ricordare il concetto di apertura dinamica della camera pulpare: se i file non progrediscono e non hanno accesso facile ai canali, allargare il disegno dell’apertura.",
            3: "In caso di dubbio sulla presenza di un canale supplementare considerare l’opzione di prescrizione di un esame radiografico di secondo livello. Aumentare l’estensione dell’apertura della camera pulpare, ricordare le leggi di simmetria e di localizzazione degli orifizi. L’utilizzo di ingrandenti con luce e di punte ultrasoniche è cruciale. In caso di split canalari profondi, preferire una tecnica di otturazione controllabile come cono singolo e bioceramico, otturando un canale alla volta e tagliando la guttapercha alla base del tronco radicolare comune.",
            4: "In caso di dubbio sulla presenza di un canale supplementare considerare l’opzione di prescrizione di un esame radiografico di secondo livello. In questi casi è cruciale l’attivazione degli irriganti.",
            5: "Preferire strumenti a conicità variabile con rastremazione del terzo coronale (strumenti minimamente invasivi). Uno strumento troppo grande in D16 potrebbe complicare la discesa in apice per blocco dato dal torque limit e sacrificare troppa dentina sana nella zona di minor resistenza del dente."
        }
    },
    {
        "testo": "Diametro apicale (valutazione radiogafica e clinica)",
        "opzioni": [
            "Apice normale (< 0.55mm)",
            "Riassorbimento apicale infiammatorio e/o diametro compreso tra 0.55mm - 1mm",
            "Apice beante (> 1 mm)"
        ],
        "suggerimenti": {
            1: "Preferire utilizzo di bioceramico per evitare instabilità del sigillo apicale con tecniche di otturazione tradizionali e avere molta cura ed attenzione nella determinazione della lunghezza di lavoro e del gauging. Controllare il fitting del cono master radiograficamente.",
            2: "Eseguire apical plug con cementi bioceramici putty o provare una chiusura a freddo con cementi bioceramici fluidi. In questi casi bisogna avere molta cura ed attenzione nella determinazione della lunghezza di lavoro e del gauging. Controllare il fitting del cono master radiograficamente."
        }
    },
    {
        "testo": "Leggibilità radiografica del sistema canalare",
        "opzioni": [
            "Camera pulpare e canali radicolari ben visibili e non ridotti in dimensioni",
            "Camera pulpare e canali radicolari visibili ma di dimensioni ridotte o presenza di pulpoliti",
            "Calcificazione camerale e/o radicolare o interruzione improvvisa dell’immagine radiografica del canale radicolare"
        ],
        "suggerimenti": {
            1: "Durante la fase di localizzazione degli orifizi preferire l’uso di sistemi ingrandenti con buona fonte luminosa e punte ultrasonici. Allargare progressivamente i canali radicolari con più strumenti per evitare la concentrazione degli stress su un unico strumento. Considerare l’utilizzo di file manuali con modifica della loro rigidezza (es C-File). Evitare strumenti da glide path eccessivamente martensitici.",
            2: "Durante la fase di localizzazione degli orifizi preferire l’uso di sistemi ingrandenti con buona fonte luminosa e punte ultrasonici. Allargare progressivamente i canali radicolari con più strumenti per evitare la concentrazione degli stress su un unico strumento. Considerare l’utilizzo di file manuali con modifica della loro rigidezza (es C-File). Evitare strumenti da glide path eccessivamente martensitici."
        }
    },
    {
        "testo": "Prossimità degli apici radicolari rispetto a strutture nobili come nervi o seno mascellare",
        "opzioni": [
            "Distanza > 5mm",
            "Distanza compresa tra 2mm – 5mm o apice extracorticale",
            "Distanza < 2mm"
        ],
        "suggerimenti": {
            1: "Evitare uso di bioceramici e CaOH se vicino a strutture nobili"
        }
    },
    {
        "testo": "Presenza di riassorbimenti",
        "opzioni": [
            "Nessun riassorbimento evidente radiograficamente e/o clinicamente",
            "Riassorbimento apicale minimo",
            "Riassorbimento interno, esterno o esteso"
        ],
        "suggerimenti": {}
    },
    {
        "testo": "Anamnesi endodontica",
        "opzioni": [
            "Nessun trattamento",
            "Accesso camerale già eseguito con nessuna o minima alterazione o complicazione",
            "Ritrattamento endodontico con o senza: presenza di perforazioni, canali mancanti gradini, false strade, strumenti fratturati, perni intracanalari, restauri intracamerali ecc.)"
        ],
        "suggerimenti": {}
    },
    {
        "testo": "Condizioni endo-parodontali",
        "opzioni": [
            "Sano o parodontopatia lieve",
            "Lesione endo-parodontale",
            "Grave patologia parodontale, presenza di crack con complicazioni parodontale, rizectomia effettuata prima del trattamento endodontico."
        ],
        "suggerimenti": {}
    }
]