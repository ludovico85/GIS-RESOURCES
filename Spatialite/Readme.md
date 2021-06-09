# Repository contenente alcune funzioni di SpatiaLite

[Link al libro How I do that in SQLite and SpatiaLite: illustrating classic GIS tasks](./pdf)

#### Effettuare un join spaziale (con lo spatial index ~ boundy box) e creare la tabella

``` sql
CREATE TABLE iuti_join as
SELECT r.PK_UID as rowid, r.ID_CELLA as id_cella_32, r.ID_CELLA_1 as id_cella_33, r.geometry as geom,p.COD_90 as cod_90, p.COD_00 as cod_00, p.COD_08 as cod_08
FROM iuti_punti as p, iuti_reticolo as r
WHERE ST_CONTAINS (r.geometry, p.geometry) = 1
AND r.ROWID IN (
SELECT rowid FROM SpatialIndex
WHERE f_table_name = 'iuti_reticolo'
AND search_frame =  p.geometry
)

```

Ricreare la geometria

``` sql
SELECT RecoverGeometryColumn('iuti_join', 'geom',32632, 'POLYGON', 1)
```

#### Creare un indice spaziale per velocizzare le operazioni
``` sql
SELECT CreateSpatialIndex('iuti_cod_08', 'geometry')
```
#### Creare un indice normale non spaziale
``` sql
CREATE INDEX idx_cod_00 ON iuti_join (cod_00)
```
#### Informazioni sui campi
``` sql
PRAGMA table_info(iuti_join)
```
#### aggiungere una colonna
``` sql
ALTER TABLE iuti_reticolo
 ADD COLUMN id_cella_iuti INTEGER
```
#### Aggiornare la colonna
``` sql
UPDATE iuti_join SET id_cella = id_cella_33 WHERE id_cella_32 = 0
```
#### Aggiornare le geometrie per poterle visualizzare in QGIS
``` sql
SELECT UpdateLayerStatistics(nome tabella)
```
#### Calcolo e inserimento dell’area
``` sql
update iuti_00
set area_ha = ST_Area(geometry)/10000
```
#### Calcolo dell’area
``` sql
SELECT ST_Area(geometry)/10000
FROM iuti_00
```
#### Aggiornare colonna con nuovi valori in un intervallo
``` sql
update iuti_join
set cell_type_90 = 1.1
where (id_cella between 309 and 1000);
```
``` sql
select *
from iuti_join
where (id_cella between (select min (id_cella) from iuti_join) and 1000)
order by id_cella asc
```
#### Calcolare la percentuale di ogni riga (serve una subquery, altrimenti fa il calcolo su tutto)
``` sql
SELECT cod_00, area_ha, (area_ha * 100)/(SELECT SUM(area_ha) FROM iuti_00) AS Total_Percentage
FROM iuti_00;
```
``` sql
UPDATE iuti_00
SET area_percentage = (area_ha * 100) / (SELECT SUM(area_ha) FROM iuti_00)
```
#### Numero di records in una tabella
``` sql
SELECT count (*) from iuti_join
```
#### Calcolare il numero di celle occupate utilizzando la percentuale e la somma (arrotondate a zero cifre decimali)
``` sql
SELECT area_percentage, round((area_percentage/100)*(SELECT count (*) from iuti_join),0) as cell_count
from iuti_90
```
``` sql
UPDATE iuti_90
set cell_count = round((area_percentage/100)*(SELECT count (*) from iuti_join),0)
```
#### Selezionare un numero di records che vanno da zero e successivi 10
``` sql
select *
from iuti_join
order by id_cella asc
LIMIT 10 OFFSET 0
```
#### Selezionare un numero di records che vanno da zero e successivi numeri di records che corrispondono a cell_count di iuti_90 in corrispondenza della categoria 1.1
``` sql
select cod_90
from iuti_join
order by id_cella asc
LIMIT (select cell_count from iuti_90 as i where cod_90 = 1.1) OFFSET 0
```
``` sql
update iuti_join
set cell_type_90 = 1.1
where id_cella in (select id_cella from iuti_join
order by id_cella asc
LIMIT (select cell_count from iuti_90 where cod_90 = 1.1) OFFSET 0)
```
``` sql
update iuti_join
set cell_type_90 = 1.2
where id_cella in (select id_cella from iuti_join
order by id_cella asc
LIMIT (select cell_count from iuti_90 where cod_90 = 1.2) OFFSET (select max(id_cella)+1 from iuti_join where cell_type_90 = 1.1))
```
#### Selezionare un numero di records che vanno da zero e successivi numeri di records che corrispondono a cell_count di iuti_90 in corrispondenza della categoria 1.1
``` sql
update iuti_join
set cell_type_90 = 1.2
where id_cella in (select id_cella from iuti_join
order by id_cella asc
LIMIT (select cell_count from iuti_90 where cod_90 = 1.2) OFFSET (select count(*) from iuti_join where cell_type_90 = 1.1))
```
``` sql
update iuti_join
set cell_type_90 = 3.1
where id_cella in (select id_cella from iuti_join
order by id_cella asc
LIMIT (select cell_count from iuti_90 where cod_90 = 3.1) OFFSET (select count(*) from iuti_join where cell_type_90 = 1.1 or cell_type_90 = 1.2))
```

#### Creare una spatial view

#### Registrare una geometria in una view
