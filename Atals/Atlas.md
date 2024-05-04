# Esempi avanzati di Atlante in QGIS
## Filtrare l'Atlante con un layer non geometrico che ha una relazione con un layer geometrico
Testato in QGIS 3.34.6
>...vorrei fare un atlante di un layer di poligoni che è in relazione uno-a-molti con una tabella.
>il layer poligonale governa l'atlante ma io vorrei generare l'atlante solo per i poligoni che hanno elementi collegati nella tabella.
>come inserire la relazione nel filtro dell'atlante?..

Abbiamo un progetto con il layer `comuni_abruzzo` con geometria poligonale e il layer `tabella` contenente i campi comune e densita_popolazione. Esiste una relazione 1:1 tra i due layer sulla base del campo comune.
Creiamo un atlante utilizzando come vettore di copertura il layer `comuni_abruzzo`. Si vuole però poter visualizzare solo i comuni con densita_popolazione > 100 (dato che è contenuto nella tabella).
Nella configurazione dell'Atlante nel `filtra con` si inserisce l'espressione: 

```
array_contains(aggregate(
layer:='tabella',
aggregate:='array_agg',
expression:="COMUNE",
filter:="densita_pop">100
), "COMUNE")
```
[Dati e progetto](https://github.com/ludovico85/GIS-RESOURCES/raw/master/Atals/dati/test_atante.gpkg)

## Utilizzo dell'Atlante con vettore di copertura non geometrico e con più layer in relazione tra di loro
>Devo generare un Atlante e voglio che per ogni matricola ci sia una pagina distinta sull'Atlas. Le matricole (Contatori) sono legate all'idrante
>e possono essere diverse per un solo idrante. Il lavoro è organizzato nel seguente modo: ho un layer puntuale che è anche il layer di copertura dell'atlante
>e si chiama LETTURE_EXTRA, all'interno ho un campo UUID, con questo campo ho messo in relazione il campo ID_UUID che si trova nel layer UTENTI_EXTRA che è un
>layer tabellare, questa relazione si chiama UTENTI. Dentro il layer UTENTI_EXTRA ho un campo che si chiama MATRICOLA che è anche utilizzato per mettere in
>relazione il layer CONSUMI con il corrispondente campo MATRICOLA, questa seconda relazione si chiama LETTURE. Nel layer consumi è presente un campo che si
>chiama Ph_uuid che è relazionato con il campo C_uuid che si trova nel layer FOTO, questa terza relazione si chiama FOTO.

Riorganizziamo i layer e i nomi dei campi:
- letture_extra: fid, UUID, IDRANTE
- utenti_extra: fid, FK_UUID, MATRICOLA
- consumi: fid, C_UUID, FK_MATRICOLA, consumi
- foto: fid, foto, FK_C_UUID.
I layer sono messi in relazione così strutturate.

![alt text](https://github.com/ludovico85/GIS-RESOURCES/blob/master/Atals/img/Immagine%202024-05-04%20155305.png?raw=true)

Si vuole creare un atlante con il layer utenti_extra in modo da avere una pagina per ogni matricola. Una geometria in letture_extra può avere più records associati in utenti_extra.
Per creare l'atlante sfruttando la geometria di letture_extra si utilizza uno pseudo-atlante ossia si impostano i valori di x_min, x_max, y_min, y_max utilizzando la geometria della relazione.

```
x_min(bounds(buffer(geometry(get_feature ('letture_extra',  'UUID', "FK_UUID")), 0.0005)))
```

In questo caso è stato utilizzato un buffer poiché la geometria è di tipo puntuale. La funzione `get_feature(layer,attribute,value)` permettere di prendere prendere l'elemento di un altro layer che corrisponde al valore dell'attributo indicato.
Nel caso specifico è l'elemento del layer letture_extra il cui valore nel campo UUID è uguale al valore di FK_UUID (valore che si ottiene grazie alla relazione).
