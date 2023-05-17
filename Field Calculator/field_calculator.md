# Alcune funzioni
## aggregate
Restituisce valori aggregati (array, concatenati, somma, media, min, max, ...) di un campo degli elementi di un altro vettore.

aggregate (layer, aggregate, expression, filter, concatenator, order_by)

Esempio: 

aggregate(layer:='poligoni', aggregate:= 'array_agg', 
          expression:= "id", 
          filter:=intersects($geometry, start_point(geometry(@parent))))[0]
		  
Restituisce un array di elementi (array_agg), dei valori contenuti nel campo "id" del layer 'poligoni', utilizzando com filtro
la relazione spaziale tra i due vettori (poligoni e linee ed in particolare il punto iniziale start_point). @parent richiama la geometria
del layer corrente, mentre [0] alla fine dell'espressione restituisce il valore all'interno dell'array.