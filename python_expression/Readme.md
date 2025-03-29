# python_expressions
Serie di espressioni da utilizare nel calcolatore campi di QGIS

## Installazione delle espressioni
- Scaricare la funzione con estensione .py
- Copiare la funzione nella cartella `expressions` del profilo di QGIS. Esempio su Windows `C:\Users\Pc\AppData\Roaming\QGIS\QGIS3\profiles\Default\python\expressions` dove `Default` è il nome del profilo utilizzato.

## Download delle espressioni
- [edifici_veneto_info.py](https://raw.githubusercontent.com/ludovico85/GIS-RESOURCES/master/python_expression/expression/edifici_veneto_info.py)

### edifici_veneto_info.py
L'espressione permette di ottenere a partire da una geometria puntuale, le informazioni associate alla risorsa WMS [Edifici](https://gaia.arpa.veneto.it/layers/dbnir:geonode:v_edifici) del Geoportale ARPAV.

Utilizzo: `edifici_veneto_info(x,y,'variabile', EPSG)`
- **x** coordinata x del punto
- **y** coordinata x del punto
- **variabile** valore dell'edificio che si vuole ottenre. I valori ammessi sono:
	- piede
    - piede_min
	- piede_max
	- altezza
	- gronda
	- piani_fuori_terra
- **EPSG** il codice EPSG con in quale viene caricato il wms. I valori ammessi dal servzio wms sono:
	- 3003
    - 3857
	- 3785
    - 32736
    - 32647
    - 4326

Esempio: `edifici_veneto_info($x, $y, 'altezza', 3003)` -> 5.6

> [!NOTE] 
> Il wms e le coordinate dei punti (o il layer utilizzato) devono avere lo stesso sistema di riferimento!

### get_istat_attr_censimento.py
L'espressione permette di ottenere a partire da una geometria puntuale, le informazioni associate al servizio REST SERVICE del [Portale GIS ISTAT](https://gisportal.istat.it/server/rest/services)

<img src="img/Immagine 2025-03-29 110023.png" width="500">

Estrae un attributo demografico dalla griglia ISTAT 2021 (LegendaEstesa)
    
<h2>Parametri:</h2>
<ul>
<li>xx, yy: coordinate del punto
<li>srid: EPSG del sistema di riferimento delle coordinate (es. 3045)
<li>legenda_name: 'LegendaEstesa' oppure 'LegendaSintetica'
<li>attr_name: nome dell'attributo da estrarre (es. "Popolazione totale")
</ul>
<br>
<h2>Utilizzo:</h2>
<ul>
<li>get_istat_censimento_attr($x, $y, '32633', 'LegendaEstesa', 'Popolazione totale')</li>
</ul>
<br>
<h2>Attributi:</h2>
<ul>
<li>OBJECTID</li>  
<li>GRD_ID</li>  
<li>CNTR_ID</li>  
<li>Popolazione totale</li>  
<li>Popolazione totale maschile</li>  
<li>Popolazione totale femminile</li>  
<li>Popolazione (0-14 anni)</li>  
<li>Popolazione (15-64 anni)</li>  
<li>Popolazione (oltre 65 anni)</li>  
<li>Nati in Italia</li>  
<li>Nati in altro paese EU</li>  
<li>Nati in altro paese extra-EU</li>  
<li>Occupati</li>  
<li>Stessa dimora un anno prima</li>  
<li>Altra dimora un anno prima in Italia</li>  
<li>Altra dimora un anno prima all'estero</li>
</ul>

<img src="img/Immagine 2025-03-29 111419.png" width="500">
