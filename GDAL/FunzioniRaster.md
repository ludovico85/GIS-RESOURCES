# SERIE DI FUNZIONI PER LAVORARE CON I RASTER UTILIZZANDO LA LIBRERIA GDAL ATTRAVERSO LA SHELL DI OSGEO4W
## Compressione
La compressione jpeg è compatibile sono con una profonodità del pixel pari a 8 o 12 bit
```
gdal_translate -co COMPRESS=DEFLATE input.tif target.tif
```

## Ricampionamento (20 pixel)
```
gdalwrap -tr 20 -20 input.tif output.tif
```

## Clip
```
gdalwarp -of GTiff -cutline inputshape.shp -cl inputshape -crop_to_cutline -co COMPRESS=DEFLATE inpuraster.tif output.tif
```

## MBTILES
```
gdalwarp -t_srs EPSG:3857 -r near mymap1.tif mymap2.tif
gdal_translate -of mbtiles mymap3.tif mymap.mbtiles
gdaladdo -r nearest mymap.mbtiles 2 4 8 16 18
```

## Riproiezione e compressione
```
gdalwarp -s_srs EPSG:3004 -t_srs EPSG:32633 -ot Byte -r near -co COMPRESS=DEFLATE  input.tif output.tif
```

## Mosaicare immagini
### Di default utilizza il metodo nearest neighbour

mergeInputFiles.txt file di testo con elenco raster da mosaicare nella cartella (un raster per ogni riga)
```
gdal_merge.py -co COMPRESS=jpeg -ot Byte -o output.tif --optfile mergeInputFiles.txt
```

### Per controllare il metodo, utilizzare gdalwarp

```
C:> cd \path\to\input_images
C:> dir /o/b *.tif > list.txt

gdalwarp -s_srs EPSG:4326 -t_srs EPSG:25833 -multi -r bilinear -ot Float32 --optfile list.txt output.tif
```

## Salvare un raster nel formato geopackage
```
gdal_translate --config OGR_SQLITE_SYNCHRONOUS OFF -co  APPEND_SUBDATASET=YES -co TILE_FORMAT=WEBP -a_srs EPSG:21781 -of GPKG input.tif output.gpkg
```
```
gdal_translate -of GPKG -co APPEND_SUBDATASET=YES -co RASTER_TABLE=raster_name input.tif output.gpkg"
```

### Creare le piramidi
```
gdaladdo --config OGR_SQLITE_SYNCHRONOUS OFF -r AVERAGE output.gpkg 2 4 8 16 32 64 128 256
```

## Estrarre le bande da un RGB (per i.rgb.his)
```
gdal_translate -b 1 a_nodata -999 -ot Int16 input.tif output1.tif
gdal_translate -b 2 a_nodata -999 -ot Int16 input.tif output2.tif
gdal_translate -b 3 a_nodata -999 -ot Int16 input.tif output3.tif
```

## Vettorializzazione di un Raster
```
gdal_polygonize.py input.tif -b 1 -f GPKG out.gpkg layer_name
```
