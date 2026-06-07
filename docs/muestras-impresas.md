# Muestras impresas PDF

La etapa de muestras impresas valida que la representacion PDF del DTE tenga timbre, CAF, TED y formato aceptable para SII.

## URL

Portal:

```text
https://www4.sii.cl/pdfdteInternet/
```

## Que se sube

El portal lista los PDFs esperados. No asumas que se suben todos los DTE enviados: revisa la lista exacta.

Columnas importantes:

- Tipo Doc.
- Folio.
- Copia.
- Caso de Prueba.
- Timbre.
- Caf.
- Ted.
- Validacion.

## Copia tributaria vs cedible

Para documentos como Factura Electronica y Factura de Compra Electronica, el SII puede pedir dos filas:

- `TRIBUTARIA`
- `CEDIBLE`

Ambas deben quedar con tic verde. Si las filas cedibles quedan pendientes, el boton `Enviar al SII` puede mantenerse deshabilitado.

## SimpleAPI y PDFs cedibles

SimpleAPI documenta la ruta:

```text
/api/v1/impresion/pdf/{carta|80mm}/{v1|v2}/[cedible]
```

Para carta v2 cedible:

```text
/api/v1/impresion/pdf/carta/v2/cedible
```

Aprendizaje practico:

- La ruta sin version puede devolver un PDF de una pagina que no contiene la marca `CEDIBLE`.
- La ruta `v2/cedible` puede devolver un PDF de dos paginas.
- La pagina 2 puede ser la copia cedible real.
- Si el portal SII rechaza PDFs de mas de una pagina, extrae solo la pagina cedible.

Usa:

```bash
python scripts/extract_cedible_page.py input-v2-cedible.pdf output-cedible.pdf
python scripts/validate_pdf_batch.py carpeta_pdf/
```

## Errores tipicos

### El PDF tiene mas de una pagina

Solucion:

- Generar una version de una pagina.
- Para cedibles SimpleAPI `v2/cedible`, extraer la pagina cedible.

### La fila CEDIBLE queda pendiente

Posibles causas:

- Subiste el tributario en vez del cedible.
- El PDF no contiene texto/marca `CEDIBLE`.
- El archivo tiene folio o tipo de documento distinto.
- El PDF no corresponde al caso de prueba.

Verifica:

```bash
python scripts/validate_pdf_batch.py carpeta_pdf/ --require-cedible-text
```

### El boton Enviar al SII no se habilita

Revisa filas con icono pendiente o X. En particular:

- Filas CEDIBLE sin subir.
- PDFs con validacion X.
- PDFs con mas de una pagina.
- Archivos subidos en una copia equivocada.

## Carpeta recomendada

Prepara una carpeta final, por ejemplo:

```text
outputs/upload_sii_final/
```

Debe contener solo los PDFs que el portal esta pidiendo. Evita mezclar alternativas, pruebas fallidas o versiones antiguas.
