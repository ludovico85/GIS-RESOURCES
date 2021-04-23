# SERIE DI FUNZIONI PER LAVORARE CON I RASTER UTILIZZANDO LA LIBRERIA GDAL ATTRAVERSO LA SHELL DI OSGEO4W
## COMPRESSIONE
La compressione jpeg è compatibile sono con una profonodità del pixel pari a 8 o 12 bit
```
gdal_translate -co COMPRESS=DEFLATE input.tif target.tif
```

## RICAMPIONAMENTO (20 pixel)
```
gdalwrap -tr 20 -20 input.tif output.tif
```

## CLIP
```
gdalwarp -of GTiff -cutline inputshape.shp -cl inputshape -crop_to_cutline -co COMPRESS=DEFLATE inpuraster.tif output.tif
```

## MBTILES
```
gdalwarp -t_srs EPSG:3857 -r near mymap1.tif mymap2.tif
gdal_translate -of mbtiles mymap3.tif mymap.mbtiles
gdaladdo -r nearest mymap.mbtiles 2 4 8 16 18
```

## RIPROIEZIONE E COMPRESSIONE
```
gdalwarp -s_srs EPSG:3004 -t_srs EPSG:32633 -ot Byte -r near -co COMPRESS=DEFLATE  input.tif output.tif
```

## MOSAICARE IMMAGINI
mergeInputFiles.txt file di testo con elenco raster da mosaicare nella cartella (un raster per ogni riga)
```
gdal_merge.py -co COMPRESS=jpeg -ot Byte -o output.tif --optfile mergeInputFiles.txt
```
## SALVARE UN RASTER NEL FORMATO GEOPACKAGE
```
gdal_translate --config OGR_SQLITE_SYNCHRONOUS OFF -co  APPEND_SUBDATASET=YES -co TILE_FORMAT=WEBP -a_srs EPSG:21781 -of GPKG input.tif output.gpkg
```
### Creare le piramidi
```
gdaladdo --config OGR_SQLITE_SYNCHRONOUS OFF -r AVERAGE output.gpkg 2 4 8 16 32 64 128 256
```
