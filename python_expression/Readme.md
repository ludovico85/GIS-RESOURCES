# python_espression
Serie di expressioni da utilizare nel calcolatroe campi di QGIS

## Installazione delle espressioni
- Scaricare la funzione con estensione .py
- Copiare la funzione nella cartella `expressions` del profilo di QGIS. Esempio su Windows `C:\Users\Pc\AppData\Roaming\QGIS\QGIS3\profiles\Default\python\expressions` dove `Default` è il nome del profilo utilizzato.

## Download delle espressioni
- [edifici_veneto_info.py](https://github.com/ludovico85/GIS-RESOURCES/blob/master/python_expression/expression/edifici_veneto_info.py)

### edifici_veneto_info.py
L'espressione permette di ottenere a partire da una geometria puntuale, le informazioni associate alla risorsa WMS [Edifici](https://gaia.arpa.veneto.it/layers/dbnir:geonode:v_edifici) del Geoportale ARPAV.

Utilizzo: `edifici_veneto_info(x,y,'variabile', EPSG)`
- **x** coordinata x del punto
- **y** coordinata x del punto
- **variabile** valore dell'edificio che si vuole ottenre. I valori ammessi sono:
	- piede
      piede_min
      piede_max
      altezza
      gronda
      piani_fuori_terra
- **EPSG** il codice EPSG con in quale viene caricato il wms. I valori ammessi dal servzio wms sono:
	- 3003
    - 3857
	- 3785
    - 32736
    - 32647
    - 4326

Esempio: `edifici_veneto_info($x, $y, 'altezza', 3003)` -> 5.6