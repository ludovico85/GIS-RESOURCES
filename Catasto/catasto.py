from qgis.core import *
from qgis.gui import *
import requests

@qgsfunction(args='auto', group='Custom')
def get_parcel_info(xx, yy, feature, parent):
    """
    Restituisce i dati della particella sottostante
    <h2>Esempio:</h2>
    <ul>
      <li>get_parcel_info(355461.5,4222490.7) -> IT.AGE.PLA.G273_0033A0.673</li>
      <li>get_parcel_info("field1", "field2") -> IT.AGE.PLA.G273_0033A0.673</li>
      <li>----</li>
      <li>NB: le coordinate X e Y del punto sono in EPSG 3045</li>
    </ul>
    """
    req = "https://wms.cartografia.agenziaentrate.gov.it/inspire/wms/ows01.php?REQUEST=GetFeatureInfo&SERVICE=WMS&SRS=EPSG:3045&STYLES=&VERSION=1.1&FORMAT=image/png&BBOX="+str(xx-1)+","+str(yy-1)+","+str(xx+1)+","+str(yy+1)+"&HEIGHT=9&WIDTH=9&LAYERS=CP.CadastralParcel&QUERY_LAYERS=CP.CadastralParcel&INFO_FORMAT=text/html&X=5&Y=5"

    r = requests.get(req, auth=('user', 'pass'))
    a = r.text.partition("InspireId localId")[2]
    b = a.partition("<td>")[2]
    c = b.partition("</td>")[0]

    return c
