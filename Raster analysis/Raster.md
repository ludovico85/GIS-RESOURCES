# INFORMAZIONI GENERICHE SUI RASTER
## Pixel depth

| Bit depth      | Range of values that each cell can contain |
| :---        | :---        |
| 1 bit      | 0 to 1       |
| 2 bit   | 0 to 3        |
| 4 bit   | 0 to 15        |
| Unsigned 8 bit   | 0 to 255        |
| Signed 8 bit  | -128 to 127        |
| Unsigned 16 bit   | 0 to 65535        |
| Signed 16 bit   | -32768 to 32767        |
| Unsigned 32 bit   | 0 to 4294967295        |
|Signed 32 bit   | -2147483648 to 2147483647        |
|Floating-point 32 bit  | -3.402823466e+38 to 3.402823466e+38        |
|Unsigned 64 bit   | 0 to 18446744073709551616        |

# OPERAZIONI RASTER
## Fill raster (raster1) (no data value) con valori provenienti da un altro raster (raster2)
1) Settare l'estensione del raster2 uguale a quella del raster1 (anche la risoluzione deve essere identica) via gdalwarp

```
gdalwarp -te xmin, ymin, xmax, ymax input.tif output.tif
```

2) Deselzionare il valore di trasparenza del nodata in entrambi i raster (`Proprietà` -> `Trasparenza`) (ad esempio -9999)

3) Nel calcolatore raster inserire la seguente formula
```
("raster1" = -9999)*"raster2" + ("raster1" != -9999)*"raster1"
```