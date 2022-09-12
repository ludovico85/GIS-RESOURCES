# Installazione Grigliati
1. Scaricare l'archivio in C:\OSGeo4W64\share\proj

2. Inserire la riga nel db proj.db

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
'EPSG', -- grid_param_auth_name
'1127', -- grid_param_code Area of use Tutta Italia
'Latitude and longitude difference file', -- grid_param_name
'ItalyRome40ToWGS84_NTV2_GN.gsb', -- grid_name
'EPSG', -- grid2_param_auth_name
'8656', -- grid2_param_code
'Latitude and longitude difference file', -- grid2_param_name
NULL, -- grid2_name
NULL, -- interpolation_crs_auth_name
NULL, -- interpolation_crs_code
NULL, -- operation_version
0 -- deprecated
);
```
