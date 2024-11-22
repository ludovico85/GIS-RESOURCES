# Alcune funzioni
## aggregate
Restituisce valori aggregati (array, concatenati, somma, media, min, max, ...) di un campo degli elementi di un altro vettore.

``aggregate (layer, aggregate, expression, filter, concatenator, order_by)``

Esempio: 

aggregate(layer:='poligoni', aggregate:= 'array_agg', 
          expression:= "id", 
          filter:=intersects($geometry, start_point(geometry(@parent))))[0]
		  
Restituisce un array di elementi (array_agg), dei valori contenuti nel campo "id" del layer 'poligoni', utilizzando com filtro
la relazione spaziale tra i due vettori (poligoni e linee ed in particolare il punto iniziale start_point). @parent richiama la geometria
del layer corrente, mentre [0] alla fine dell'espressione restituisce il valore all'interno dell'array.
## array
### creare un campo id ordinato secondo la distanza da un punto

Esempio:

array_find(array_sort(array_agg("distanza")), distanza)

Il campo distanza contiene il valore di distanza da un punto stabilito rispetto ai punti del layer


## overaly_
### overaly_nearest
``overlay_nearest(layer[,expression][,filter][,limit])``

Esempio: trovare la linea più vicina al punto (overlay_nearest). Il layer è il nome del layer di interesse, "id" è il campo (univoco in questo caso) che serve per valutare gli elementi del layer di destinazione. 


``overlay_nearest (layer:='tratto', expression:="id")[0]``
restituisce l'elemento del layer tratto più vicino al layer sorgente
``attribute(get_feature_by_id('tratto',array_to_string(overlay_nearest ('tratto',  "id" ))),'nome_tratto')``
restituisce il valore dell'attributo (nome_tratto) del layer tratto più vicino al layer sorgente 

``make_line($geometry,(closest_point(geometry(get_feature_by_id('tratto', array_to_string(overlay_nearest ('tratto', "id")))),$geometry)))``
Rappresentazione grafica del problema

![alt text](https://github.com/ludovico85/GIS-RESOURCES/blob/master/Field%20Calculator/img/overlay_nearest.PNG?raw=true)

## attribute + get_feature
Permette di ottenere i valori di un campo (target) della tabella attributi di un altro layer (layerB) grazie ad un campo in comune (campo) presente nei due layer (A e B).
``attribute(get_feature('layerB',  'campo_layerB', "campo_layerA"), 'campo_target_layerA')``


