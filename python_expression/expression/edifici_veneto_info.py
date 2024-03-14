from qgis.core import *
from qgis.gui import *
import requests

@qgsfunction(args='auto', group='Custom', usesgeometry=True)
def edifici_veneto_info(xx, yy, variabile, EPSG, feature, parent):
    """
    Restituisce il valore, definito dalla 'variabile' dell'edificio sottostante un punto
    <h2>Sintassi</h2>
    <p>edifici_veneto_info(x,y,'variabile', 'EPSG')</p>
    <h2>Argomenti</h2>
    <li>x coordinata x del punto</li>
    <li>y coordinata x del punto</li>
    <li>variabile valore dell'edificio che si vuole ottenre. I valori ammessi sono:
        <ul>
            <li>piede</li>
            <li>piede_min</li>
            <li>piede_max</li>
            <li>altezza</li>
            <li>gronda</li>
            <li>piani_fuori_terra</li>
        <ul>
    </li>
    <li>EPSG il codice EPSG con in quale viene caricato il wms. I valori ammessi dal servzio wms sono:
        <ul>
            <li>3003</li>
            <li>3857</li>
            <li>3785</li>
            <li>32736</li>
            <li>32647</li>
            <li>4326</li>
        <ul>
    </li>
    <br>
    <h2>Esempi</h2>
    <ul>
      <li>edifici_veneto_info($x, $y, 'altezza', '3003') -> 5.6</li>
    </ul>
    """
    req = "https://gaia.arpa.veneto.it/geoserver/ows?service=WMS&version=1.1.1&request=GetFeatureInfo&exceptions=application%2Fjson&id=geonode:v_edifici__10&layers=geonode:v_edifici&query_layers=geonode:v_edifici&x=51&y=51&height=101&width=101&srs=EPSG:"+str(EPSG)+"&bbox="+str(xx-1)+","+str(yy-1)+","+str(xx+1)+","+str(yy+1)+"&feature_count=10&INFO_FORMAT=text/plain"  
    request = requests.get(req)
    data = request.text
    lines = request.text.split('\n')
    for line in lines:
        if line.startswith(variabile):
            risultato = float(line.split('=')[1].strip())
    return(risultato)
