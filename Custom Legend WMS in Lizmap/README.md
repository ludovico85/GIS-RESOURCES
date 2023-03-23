# Javascript per Lizmap per la modifica della legenda di defautl di un servizio WMS (custom legend)
Alcune volte capita che la legenda distribuita tramite servizio WMS non si ottimizzata e la restituzione in Lizmap non è sempre ottimale. E' possibile, quindi, bypasare la legenda che viene distribuita in automatico e sostituirla con un'immagine personalizzata.
Per questo scopo è necessario creare uno script in Javascript da integrare in Lizamp.
Per l'implemetazione di script Javascript in Lizamp fare riferimento alla documentazione ufficiale https://docs.lizmap.com/3.4/en/publish/customization/javascript.html
 
## Esempio
L'esempio si riferisce al servizio wms ISPRA IdroGEO ed in particolare al layer Fenomeni Franosi https://idrogeo.isprambiente.it/geoserver/idrogeo/wms

<img src="https://github.com/ludovico85/GIS-RESOURCES/blob/master/Custom%20Legend%20WMS%20in%20Lizmap/img/image_1.PNG?raw=true" height="50%" width="50%">

La legenda è stata ricostruita con il layout di QGIS

<img src="https://github.com/ludovico85/GIS-RESOURCES/blob/master/Custom%20Legend%20WMS%20in%20Lizmap/wms_legends/idrogeo_frane_iffi.png?raw=true" height="50%" width="50%">

Utilizzando lo strumento ispeziona di Google Chrome oppure lo strumento Analizza di Mozzilla Firefox individuare gli oggetti layer e legenda da utilizzare nello script. Nel caso in esame:
. layer-fenomeni_franosi
. legend-fenomeni_franosi

<img src="https://github.com/ludovico85/GIS-RESOURCES/blob/master/Custom%20Legend%20WMS%20in%20Lizmap/img/image_2.png?raw=true" height="50%" width="50%">

Lo script da implementare permette il caricamento della legenda custom al caricamento della legenda di default
```
lizMap.events.on({
    uicreated:function(e){
		var newimage_1 = 'https://github.com/ludovico85/GIS-RESOURCES/blob/master/Custom%20Legend%20WMS%20in%20Lizmap/wms_legends/idrogeo_frane_iffi.png?raw=true';
		$('#legend-fenomeni_franosi div.legendGraphics img').on('load', function() {
			console.log('immagine caricata!');
			$('#legend-fenomeni_franosi div.legendGraphics img').attr('src', newimage_1);
			$('#legend-fenomeni_franosi div.legendGraphics img').attr('data-src', newimage_1);	
			});
			}
})

```

