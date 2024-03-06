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

## No data
Utilizzare il primo valore non valido rispetto al pixel type
| Bit depth      | Range of values that each cell can contain | No data value |
| :---        | :---        | :---        |
| 1 bit      | 0 to 1       | |
| 2 bit   | 0 to 3        | |
| 4 bit   | 0 to 15        | |
| Unsigned 8 bit   | 0 to 255        | 255|
| Signed 8 bit  | -128 to 127        ||
| Unsigned 16 bit   | 0 to 65535        |65535|
| Signed 16 bit   | -32768 to 32767        |-32768 o 32767|
| Unsigned 32 bit   | 0 to 4294967295        ||
|Signed 32 bit   | -2147483648 to 2147483647        ||
|Floating-point 32 bit  | -3.402823466e+38 to 3.402823466e+38        |-9999|
|Unsigned 64 bit   | 0 to 18446744073709551616        |-9999|


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

# APPLICARE FUNZIONI SIGMODALI CRESCENTI O DECRESCENTI
Esempio: Voglio applicare al mio raster un funzione sigmoidale crescente con limite inferiore pari a 14 (r<14 = 0) e limite superiore pari a 35 (r>35=0). Tra questi due estremi i valori devono essere normalizzati tra 0 e 1.

Dal calcolatore raster
```
("raster" < 14) * 0 + (("raster" >= 14) AND ("raster" <= 35)) * (("raster" - 14) / (35 - 14)) + ("raster" > 35) * 1

```