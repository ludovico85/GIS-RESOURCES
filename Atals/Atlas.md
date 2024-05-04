# Esempi avanzati di Atlante in QGIS
## Filtrare l'Atlante con un layer non geometrico che ha una relazione con un layer geometrico
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

==Testato in QGIS 3.34.6==
