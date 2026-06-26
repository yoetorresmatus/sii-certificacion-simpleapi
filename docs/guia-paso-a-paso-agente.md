# Guia paso a paso para certificarse y comenzar a facturar con un agente

Esta guia esta escrita para una persona que quiere usar Codex, Claude Code u otro agente de codigo como copiloto durante la certificacion SII con SimpleAPI.

La regla principal es simple:

- El agente prepara, valida, ordena y documenta.
- El usuario inicia sesion, descarga certificados/CAF, confirma envios y realiza declaraciones legales.

## 0. Preparar el espacio de trabajo

Usuario:

1. Clona este repositorio o copialo como base.
2. Crea una carpeta privada de trabajo.
3. Copia `templates/.env.example` como `.env`.
4. Completa `.env` con sus datos reales.
5. Guarda certificado digital en `certs/`.

Agente:

1. Verifica que `.env`, `certs/`, `caf/`, `dte/`, `pdf/` y `trackids/` esten en `.gitignore`.
2. Crea `docs/ESTADO.md`.
3. Registra empresa, documentos a certificar y etapa inicial.

Evidencia esperada:

- `.env` local existe.
- Certificado local existe.
- No hay secretos versionados.

No avanzar si:

- El certificado no existe.
- No hay acceso SII.
- El agente detecta secretos en Git.

## 1. Postular en SII como software de mercado

Usuario:

1. Ingresa al portal SII de certificacion.
2. Postula como software de mercado.
3. Selecciona SimpleAPI como proveedor.
4. Selecciona los tipos DTE a certificar.
5. Confirma datos de contacto.

Agente:

1. Documenta software, tipos DTE, RUT empresa y correo.
2. Revisa que el firmante tenga permisos para firmar y enviar.

Evidencia esperada:

- Postulacion creada.
- Portal muestra etapas de certificacion.

No avanzar si:

- El firmante no esta autorizado.
- El portal no muestra set asignado.

## 2. Descargar CAF de certificacion

Usuario:

1. Entra a `https://maullin.sii.cl/`.
2. Usa `Solicitud de Timbraje Electronico de Documentos`.
3. Descarga CAF para cada tipo DTE.
4. Guarda los XML en `caf/certificacion/`.

Agente:

1. Lista los CAF descargados.
2. Verifica tipo DTE y rango de folios.
3. Registra folios disponibles en `docs/ESTADO.md`.

Evidencia esperada:

- CAF por cada tipo DTE requerido.
- Rango de folios documentado.

No avanzar si:

- Falta CAF de algun tipo DTE.
- El CAF corresponde a produccion cuando se esta certificando.

## 3. Generar y enviar set de pruebas

Usuario:

1. Descarga o copia el set asignado por SII.
2. Autoriza al agente a generar XML de certificacion.
3. Confirma antes de enviar al SII.

Agente:

1. Lee el set asignado.
2. Genera DTE con folios de certificacion.
3. Genera sobre `EnvioDTE`.
4. Valida estructura basica.
5. Envia solo si el usuario confirma.
6. Consulta TrackID.
7. Registra resultado.

Evidencia esperada:

- TrackID de envio.
- Portal o consulta muestra procesamiento.
- Set basico queda conforme.

No avanzar si:

- Hay rechazo de DTE.
- El portal sigue en `POR REALIZAR`.
- Los montos/referencias no coinciden con el set.

## 4. Completar libros de ventas y compras

Usuario:

1. Confirma que el portal solicita libros.
2. Revisa cualquier error que aparezca en SII.

Agente:

1. Genera libro de ventas y compras segun folios aprobados.
2. Firma XML si corresponde.
3. Sube o prepara subida segun flujo definido.
4. Registra TrackID/estado.

Evidencia esperada:

- Libro ventas conforme.
- Libro compras conforme.

No avanzar si:

- Aparecen errores de schema.
- El libro usa folios distintos a los DTE aprobados.

## 5. Generar y enviar set de simulacion

Usuario:

1. Avanza en el portal al set de simulacion.
2. Confirma envio cuando el agente tenga los XML listos.

Agente:

1. Genera DTE de simulacion.
2. Usa folios de certificacion disponibles.
3. Genera sobre.
4. Envia al SII con confirmacion del usuario.
5. Consulta TrackID.

Evidencia esperada:

- Set de simulacion conforme.
- Portal habilita intercambio.

No avanzar si:

- Faltan folios.
- Hay documentos rechazados.

## 6. Completar set de intercambio

Usuario:

1. Entra al portal de intercambio.
2. Descarga el XML de envio entregado por SII.
3. Sube los XML generados por el agente.

Agente:

1. Lee el XML de intercambio.
2. Genera:
   - Respuesta de intercambio.
   - Recibo de mercaderias o servicios.
   - Resultado de aprobacion comercial.
3. Firma los XML.
4. Indica exactamente que archivo subir en cada campo.

Evidencia esperada:

- Tres XML subidos.
- Portal muestra checks verdes.

No avanzar si:

- El XML no esta firmado.
- Se sube un archivo en el campo equivocado.

## 7. Preparar muestras impresas

Usuario:

1. Entra a `https://www4.sii.cl/pdfdteInternet/`.
2. Revisa la lista exacta de PDFs que pide el portal.

Agente:

1. Genera PDFs tributarios.
2. Genera PDFs cedibles cuando el portal los pide.
3. Verifica:
   - 1 pagina por PDF.
   - Timbre/CAF/TED presentes.
   - Texto `CEDIBLE` en cedibles.
4. Crea una carpeta final con solo los PDFs requeridos.

Comandos utiles:

```bash
python scripts/validate_pdf_batch.py outputs/upload_sii_final --require-cedible-text
```

Evidencia esperada:

- Carpeta final limpia.
- Todos los PDFs son de 1 pagina.
- Cedibles contienen `CEDIBLE`.

No avanzar si:

- Hay PDFs de mas de una pagina.
- Las filas cedibles quedan pendientes.
- Hay archivos viejos mezclados con los finales.

## 8. Subir muestras impresas

Usuario:

1. Sube los PDFs finales al portal.
2. Revisa que todas las filas queden con tic verde.
3. Presiona `Enviar al SII` cuando este habilitado.

Agente:

1. Inspecciona la tabla si el usuario lo permite.
2. Detecta filas pendientes o con error.
3. No presiona envio final sin confirmacion del usuario.

Evidencia esperada:

- Portal indica muestras enviadas a revision.

No avanzar si:

- El boton `Enviar al SII` sigue deshabilitado.
- Hay X o pendientes en la tabla.

## 9. Esperar aprobacion de muestras

Usuario:

1. Espera correo del SII.
2. Autoriza al agente a revisar correo si usa conector.

Agente:

1. Busca correos del SII.
2. Identifica aprobacion o rechazo.
3. Registra evidencia en `docs/ESTADO.md`.

Correo esperado:

```text
La revision de las muestras impresas ha sido APROBADA
```

No avanzar si:

- El correo indica rechazo.
- El portal sigue en revision.

## 10. Declarar cumplimiento

Usuario:

1. Entra como representante legal.
2. Lee la advertencia del portal.
3. Confirma expresamente que quiere declarar cumplimiento.

Agente:

1. Abre o guia a:

```text
https://maullin.sii.cl/cvc_cgi/dte/pe_avance7
```

2. Revisa que el RUT empresa sea correcto.
3. Pide confirmacion antes del clic final.
4. Registra resultado.

Resultado esperado:

```text
El contribuyente [RAZON SOCIAL] Rut [RUT], esta autorizada para operar como emisor de documentos tributarios electronicos.
```

No avanzar si:

- El usuario no confirma explicitamente.
- El portal muestra otra empresa.
- No hay plan para operar en produccion.

## 11. Solicitar CAF productivos

Usuario:

1. Entra al SII productivo.
2. Solicita folios productivos para tipos autorizados.
3. Descarga CAF productivos.
4. Guarda en `caf/produccion/`.

Agente:

1. Verifica tipo DTE y rango.
2. Registra folios disponibles.
3. Separa CAF productivos de los de certificacion.

No avanzar si:

- Se intenta usar CAF de certificacion en produccion.

## 12. Configurar produccion

Usuario:

1. Confirma que quiere pasar a produccion.

Agente:

1. Cambia entorno local:

```env
SIMPLEAPI_AMBIENTE=produccion
```

2. Usa `Ambiente: 1` en payloads SimpleAPI.
3. Verifica que el CAF seleccionado sea productivo.

No avanzar si:

- No hay CAF productivo.
- No hay folio disponible.

## 13. Primera factura productiva controlada

Usuario:

1. Entrega datos reales del receptor.
2. Revisa monto neto, IVA y total.
3. Confirma emision.

Agente:

1. Prepara payload.
2. Muestra resumen humano antes de emitir.
3. Emite solo con confirmacion.
4. Consulta TrackID.
5. Guarda XML/PDF/respuesta.

Evidencia esperada:

- DTE aceptado.
- XML y PDF respaldados.
- Folio marcado como usado.

No avanzar a emision masiva si:

- La primera factura no esta aceptada.
- No existe control de folios usados.
- No hay manejo de notas de credito/debito.

## 14. Operacion recurrente

Agente puede ayudar a:

- Emitir facturas.
- Generar PDFs.
- Enviar correos a clientes.
- Consultar estados.
- Registrar folios usados.
- Leer DTE recibidos desde casilla/portal/proveedor.
- Preparar acuses o reclamos comerciales.

Usuario debe mantener control de:

- Emisiones reales.
- Correcciones/anulaciones.
- Cumplimiento tributario mensual.
- Respaldos legales.

## Resumen de decisiones que siempre requieren humano

- Enviar sets al SII.
- Subir muestras definitivas.
- Enviar muestras a revision.
- Declarar cumplimiento.
- Pasar a produccion.
- Emitir la primera factura real.
- Emitir documentos masivos.
- Anular o corregir documentos emitidos.
