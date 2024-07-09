# Esempi di Widget
## Relation Value
Testato in QGIS 3.34.6

Ho un layer `tabella` con due campi, oggetto e gruppo
oggetto|gruppo
————————
cane|animale
rosso|colore

Ho il layer `punto` con due campi, oggetto2 dove andrò ad inserire i valori cane o rosso e un campo gruppo2 dove in automatico si inserirà il valore animale o colore a seconda del valore selezionato in gruppo2

Nel layer puntuale imposti il widget di oggetto2 in modo che richiami i valori presenti in oggetto (tabella)

![alt text](https://github.com/ludovico85/GIS-RESOURCES/blob/master/Atals/img/Immagine%202024-05-04%20155305.png?raw=true)

Nel layer gruppo2 fai lo stesso inserendo però il filtro `"oggetto" = current_value("oggetto2")`

```

[Dati e progetto](https://github.com/ludovico85/GIS-RESOURCES/raw/master/Atals/dati/test_atante.gpkg)
