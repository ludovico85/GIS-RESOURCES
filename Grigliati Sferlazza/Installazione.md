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
``` sql
INSERT INTO "grid_transformation"
VALUES (
'PROJ', -- auth_name
'EPSG_4265_TO_EPSG_4258', -- code
'Monte Mario (ROMA40) TO ETRS89/ETRF89 (GN)', -- name
'Per tutto il territorio italiano, isole minori comprese - Ing.Sferlazza', -- description
'EPSG', -- method_auth_name
'9615', -- method_code
'NTv2', -- method_name
'EPSG', -- source_crs_auth_name
'4265', -- source_crs_code
'EPSG', -- target_crs_auth_name
'4258', -- target_crs_name
NULL,  -- accuracy,
'ESPG', -- grid_param_auth_name
'1127', -- grid_param_code Area of use Tutta Italia
NULL, -- grid_param_name
'ItalyRome40ToWGS84_NTV2_GN.gsb', -- grid_name
'EPSG', -- grid2_param_auth_name
'8656', -- grid2_param_code
'Latitude and longitude difference file', -- grid2_param_name
NULL, -- grid2_name
NULL, -- interpolation_crs_auth_name
NULL, -- interpolation_crs_code
NULL, -- operation_version
NULL -- deprecated
);
```
