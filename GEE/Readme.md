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
Esempio: Caricare lo shapefile dei comuni ISTAT della regione d'interesse. (Molise - consiglio di covertirli in WGS84 EPSG:4326)
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
var study_area = ee.FeatureCollection('projects/ee-frateludovico-test/assets/dataset/molise') // eprea

Map.addLayer(studyarea, {color: 'green'}, 'FeatureCollection');


```



























var studyarea = ee.FeatureCollection('projects/ee-frateludovico/assets/data/rionero')

Map.addLayer(studyarea, {color: 'green'}, 'FeatureCollection');
var palettes = require('users/gena/packages:palettes');

var canopyHeight = ee.ImageCollection('projects/meta-forest-monitoring-okw37/assets/CanopyHeight').mosaic().clip(studyarea);
var treenotree = canopyHeight.updateMask(canopyHeight.gte(1)).clip(studyarea);

Map.addLayer(treenotree, {
    min: 0,
    max: 3,
    palette: ['440154', 'fde725']
}, 'Canopy height (>=3 meter)', false);

Map.addLayer(canopyHeight, {
    min: 0,
    max: 25,
    palette: palettes.matplotlib.viridis[7]
}, 'Canopy Height [meters]');

var projection = canopyHeight.projection().getInfo();
print(projection)


Export.image.toDrive({
 image: canopyHeight,
 description: 'canopyHeight',
 region: studyarea
});



