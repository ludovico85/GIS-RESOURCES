# Appunti per Google Earth Engine (GEE)
Appunti e script per l'utilizzo di GEE.

## Creazione account
1. Vai su [http://code.earthengine.google.com/](http://code.earthengine.google.com/)
2. Se non hai un account google crealo, altrimenti esegui il login con il tuo account
3. Segui le istruzione per la registrazione a Google Earth Engine


## Creazione di un progetto
1. Al primo accesso verrà chiesto se creare un nuovo progetto oppure se si è autorizzati ad utilizzare un progetto esistente. Scegliere la prima opzione.
> [!IMPORTANT]  
> GEE è disponibile per utilizzo commerciale (a pagamento) oppure gratuito per utilizzo accademico e di ricerca.
2. Scegliere il profilo e continuare con la creazione del progetto.
3. Accedere all'Editor.


## Caricare e visualizzare un dataset
Per caricare dataset geografici si deve utilizzare l'Asset Manager nell'editor del codice. Maggiori informazioni [qui](https://developers.google.com/earth-engine/guides/asset_manager)
**Esempio: Caricare lo shapefile dei comuni ISTAT della regione d'interesse. (Molise - consiglio di covertirli in WGS84 EPSG:4326)**
1. Recarsi su Assets, cliccare su NEW e creare una nuova cartella

![alt text](https://github.com/ludovico85/GIS-RESOURCES/blob/master/GEE/img/img1.png?raw=true)

2. Cliccare su NEW, Shapefiles, cliccare su SELECT e selezionare i file che compongono lo shapefile (.shp, .shx, .dbf, .prj)

![alt text](https://github.com/ludovico85/GIS-RESOURCES/blob/master/GEE/img/img2.png?raw=true)

3. Cliccare su UPLOAD per caricare il file
4. Attendere il caricamento. Lo stato del caricamento si può verificare nel tab Tasks

![alt text](https://github.com/ludovico85/GIS-RESOURCES/blob/master/GEE/img/img3.png?raw=true)

5. Una volta caricato effettuare un refresh nella scheda Assets per vedere il dataset caricato.
6. Per comodità si può spostare il dato appena caricato nella cartella creata in presenza semplicemente con un drag&drop
7. Cliccando sul dato caricato è possibile vedere alcune informazioni, tra le quali Table ID che servirà per richiamare il dato stesso
![alt text](https://github.com/ludovico85/GIS-RESOURCES/blob/master/GEE/img/img4.png?raw=true)
8. Recarsi nell'editor dello script e digitare
```javascript
var studyarea = ee.FeatureCollection('projects/ee-frateludovico-test/assets/dataset/molise') // Assegna il dato alla variabile studyarea
Map.addLayer(studyarea, {color: 'green'}, 'FeatureCollection'); // visualizza il dato
```
9. Cliccare su Run

![alt text](https://github.com/ludovico85/GIS-RESOURCES/blob/master/GEE/img/img5.png?raw=true)

10. E' possibile selezionare solo una feature del dataset.
```javascript
var studyarea = ee.FeatureCollection('projects/ee-frateludovico-test/assets/dataset/molise') // Assegna il dato alla variabile studyarea
var campobasso = studyarea.filter('COMUNE == "Campobasso"') // selezione

Map.addLayer(studyarea, {color: 'green'}, 'FeatureCollection');
Map.addLayer(campobasso, {color: 'red'}, 'FeatureCollection');
```
![alt text](https://github.com/ludovico85/GIS-RESOURCES/blob/master/GEE/img/img6.png?raw=true)


## Esercizio 01 - Ritagliare ed esportare un raster
Il raster utilizzato in questo esempio è il [Modello Digitale della Canopy a livello globale a 1 metro di risoluzione](https://gee-community-catalog.org/projects/meta_trees/?fbclid=IwZXh0bgNhZW0CMTAAAR0qEUr0dSkj3WQ5cUIHvfOwjLtXFtxEeUysNqynxtBMevFEF8CaP6a0OPQ_aem_AfeRztZ1Y8TUxqdUK-xLBSjkuWb8X6HCgjwrk2FmtjCLLz3N4ZGPzqCmujvdwAwENdIdnP5aKeakRJ3LSOsSP-XE) accessibile su GEE con il seguente codice sorgente
```javascript
var canopy_ht = ee.ImageCollection("projects/meta-forest-monitoring-okw37/assets/CanopyHeight")
```

Comandi utilizzati:
- Caricamento dati vettoriali [ee.FeatureCollection](https://developers.google.com/earth-engine/apidocs/ee-featurecollection)
- Caricamento dati raster [ee.ImageCollection](https://developers.google.com/earth-engine/apidocs/ee-imagecollection)
- Visualizzare una mappa [Map.addLayer](https://developers.google.com/earth-engine/apidocs/map-addlayer)
- Esportazione [Export.image.toDrive](https://developers.google.com/earth-engine/apidocs/export-image-todrive)


Per visualizzare la zona d'interesse utilizziamo il seguente script

```javascript
var comuni = ee.FeatureCollection('projects/ee-frateludovico-test/assets/dataset/molise') // Assegna il dato alla variabile comuni
var studyarea = comuni.filter('COMUNE == "Rionero Sannitico"') // selezione del comune che viene assegnato alla nuova variabile studyarea

var palettes = require('users/gena/packages:palettes'); // palette di colori per visualizzare il dataset raster
var canopyHeight = ee.ImageCollection('projects/meta-forest-monitoring-okw37/assets/CanopyHeight').mosaic().clip(studyarea);

Map.addLayer(studyarea, {color: 'green'}, 'FeatureCollection');
Map.addLayer(canopyHeight, {
    min: 0,
    max: 25,
    palette: palettes.matplotlib.viridis[7]
}, 'Canopy Height [meters]');

```
![alt text](https://github.com/ludovico85/GIS-RESOURCES/blob/master/GEE/img/img7.png?raw=true)


Per esportare la mappa raster utilizziamo il seguente script che salva il file risultante GeoTiff nel nostro account di Google Drive.

```javascript
var comuni = ee.FeatureCollection('projects/ee-frateludovico-test/assets/dataset/molise') // Assegna il dato alla variabile comuni
var studyarea = comuni.filter('COMUNE == "Rionero Sannitico"') // selezione del comune che viene assegnato alla nuova variabile studyarea



var palettes = require('users/gena/packages:palettes'); // palette di colori per visualizzare il dataset raster

var canopyHeight = ee.ImageCollection('projects/meta-forest-monitoring-okw37/assets/CanopyHeight').mosaic().clip(studyarea); // ritaglio del raster

Map.addLayer(studyarea, {color: 'green'}, 'FeatureCollection');
Map.addLayer(canopyHeight, {
    min: 0,
    max: 25,
    palette: palettes.matplotlib.viridis[7]
}, 'Canopy Height [meters]');

Export.image.toDrive({
 image: canopyHeight,
 description: 'canopyHeight',
 region: studyarea
});

```
Per terminare lo scaricamento, recarsi in Tasks e cliccare su Run.


![alt text](https://github.com/ludovico85/GIS-RESOURCES/blob/master/GEE/img/img8.png?raw=true)

![alt text](https://github.com/ludovico85/GIS-RESOURCES/blob/master/GEE/img/img9.png?raw=true)



> [!NOTE]  
> Per l'esportazione del raster sarà necessario qualche minuto.
> Se l'area di ritaglio è troppo estesa si potrebbe ricevre un'errore. In questo caso bisogna modificare i parametri di `maxPixels` e di `shardSize`

