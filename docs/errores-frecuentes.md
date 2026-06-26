# Errores frecuentes y soluciones

## Rut no autorizado a firmar

Sintoma:

- El envio se recibe, pero el portal no avanza.
- El SII indica que el RUT no esta autorizado.

Solucion:

- En el SII, autoriza al usuario firmante para firmar y enviar DTE por la empresa.

## EPR no significa conforme

`EPR` indica que el envio fue procesado a nivel de recepcion. No siempre significa que el set de certificacion quedo conforme.

Despues de enviar, revisa:

- Estado del envio.
- Estado de cada DTE.
- Estado del paso en el portal de certificacion.

## Invalid Schema Name en libros

Sintoma:

```text
SCH-00001: Invalid Schema Name
```

Posibles causas:

- XML con esquema incorrecto.
- Flujo de subida equivocado.
- Libro generado con estructura no aceptada por certificacion.

Solucion:

- Confirmar el flujo exacto para libros en certificacion.
- Preferir generacion del proveedor/software certificado.
- Evitar editar manualmente XML firmado.

## Caracteres incompatibles

El SII puede ser sensible a caracteres especiales.

Recomendacion:

- Evitar emojis.
- Evitar caracteres de control.
- Normalizar textos comerciales.
- Mantener XML en encoding esperado.
- No eliminar datos legales importantes.

Usa:

```bash
python scripts/sanitize_sii_text.py "Razón social con ñ y símbolos ®"
```

## Cedible no reconocido

Sintoma:

- Las filas `CEDIBLE` quedan pendientes.
- El boton `Enviar al SII` no se habilita.

Solucion:

- Generar PDF cedible real.
- Confirmar que el texto `CEDIBLE` aparece en el PDF.
- Confirmar que el PDF tiene una pagina.

## Limite de SimpleAPI

SimpleAPI gratis tiene limites de consumo.

Recomendacion:

- No regenerar todo el set innecesariamente.
- Guardar salidas validas.
- Probar con un documento antes de batch completo.
- Tener scripts idempotentes.

## Reenvios innecesarios

Si el portal dice "en revision", no vuelvas a enviar salvo que exista rechazo.

Reenviar durante revision puede confundir el seguimiento o consumir cupo innecesario.

## Declaracion de cumplimiento antes de estar listo

Sintoma:

- El usuario declara cumplimiento apenas se habilita el boton, sin preparar operacion productiva.

Riesgo:

- La empresa queda operando como emisor electronico.
- Debe cumplir las obligaciones desde el mes correspondiente.

Solucion:

- Antes de declarar, confirmar que hay plan para CAF productivos, folios, respaldos, consulta de estados y primera emision controlada.

## Mezclar folios de certificacion y produccion

Sintoma:

- Se intenta emitir en produccion usando CAF de certificacion, o viceversa.

Solucion:

- Separar carpetas: `caf/certificacion` y `caf/produccion`.
- Guardar en base de datos el tipo de ambiente por folio.
- No reutilizar scripts con rutas hardcodeadas.
