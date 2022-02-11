# Installazione Grigliati
1. Scaricare l'archivio in C:\OSGeo4W64\share\proj

2. Inserire la riga nel db proj.db

``` sql
INSERT INTO "grid_transformation"
VALUES ('PROJ','EPSG_4265_TO_EPSG_4258','Monte Mario (ROMA40) TO
ETRS89/ETRF89 (GN)',
'Per tutto il territorio italiano, isole minori comprese - Ing.Sferlazza',
'LOCALE',
'EPSG','9615','NTv2',
'EPSG','4265','EPSG','4258',
'EPSG','1127', -- Area of use Tutta Italia
NULL,
'EPSG','8656','Latitude and longitude difference file',
'ItalyRome40ToWGS84_NTV2_GN.gsb',
NULL,NULL,NULL,NULL,NULL,NULL,NULL,0);
```
