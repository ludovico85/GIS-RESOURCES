from qgis.core import *
import requests
from pyproj import Transformer

@qgsfunction(args='auto', group='Custom')
def get_istat_attr_censimento(xx, yy, srid, legend_name, attr_name, feature, parent):
    """
    Estrae un attributo demografico dalla griglia ISTAT 2021 (LegendaEstesa)
    
    <h2>Parametri:</h2>
    <ul>
    <li>xx, yy: coordinate del punto
    <li>srid: EPSG del sistema di riferimento delle coordinate (es. 3045)
    <li>legenda_name: 'LegendaEstesa' oppure 'LegendaSintetica'
    <li>attr_name: nome dell'attributo da estrarre (es. "Popolazione totale")
    </ul>
    La richiesta viene inviata in EPSG:3857 (Web Mercator).
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
    """

    try:
        # Trasformazione coordinate da SR utente a EPSG:3857
        transformer = Transformer.from_crs(f"EPSG:{int(srid)}", "EPSG:3857", always_xy=True)
        x_merc, y_merc = transformer.transform(xx, yy)

        # Parametri REST
        url = "https://gisportal.istat.it/server/rest/services/griglia/GrigliaCensPop2021_1kmq_Ind/MapServer/identify"
        params = {
            "geometry": f"{x_merc},{y_merc}",
            "geometryType": "esriGeometryPoint",
            "sr": 3857,
            "layers": "all",
            "tolerance": 2,
            "mapExtent": f"{x_merc-100},{y_merc-100},{x_merc+100},{y_merc+100}",
            "imageDisplay": "200,200,96",
            "returnGeometry": "false",
            "f": "json"
        }

        # Richiesta al servizio REST
        r = requests.get(url, params=params)
        r.raise_for_status()
        data = r.json()

        for result in data.get("results", []):
            if result["layerName"] == legend_name:
                attr = result["attributes"]
                return attr.get(attr_name, "ND")

        return "Nessun dato nella legenda selezionata"

    except Exception as e:
        return f"Errore: {e}"