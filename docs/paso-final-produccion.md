# Paso final y puesta en produccion

Esta guia cubre lo que ocurre despues de subir muestras impresas al SII.

## 1. Esperar aprobacion de muestras impresas

Despues de presionar `Enviar al SII` en `pdfdteInternet`, el estado queda en revision.

El correo de aprobacion suele venir desde:

```text
certificacion_impresos_dte@sii.cl
```

El mensaje clave es:

```text
La revision de las muestras impresas ha sido APROBADA
```

El mismo correo indica que el Representante Legal debe realizar la declaracion de cumplimiento en la pagina del SII.

## 2. Declaracion de cumplimiento

Ruta usada en certificacion:

```text
https://maullin.sii.cl/cvc_cgi/dte/pe_avance7
```

El portal advierte que al declarar cumplimiento la empresa queda operando en el sistema de facturacion electronica.

Antes de confirmar:

- Verifica que todas las etapas anteriores esten conformes.
- Confirma que el representante legal este autenticado.
- Asegurate de estar listo para obligaciones posteriores, incluyendo informacion electronica de compras y ventas.

Despues de declarar, el resultado esperado aparece en:

```text
https://maullin.sii.cl/cvc_cgi/dte/pe_avance8
```

Mensaje esperado:

```text
El contribuyente [RAZON SOCIAL] Rut [RUT], esta autorizada para operar como emisor de documentos tributarios electronicos.
```

## 3. No saltarse este orden

No solicites CAF productivos ni cambies SimpleAPI a produccion antes de ver el mensaje de autorizacion.

Orden correcto:

1. Muestras impresas aprobadas.
2. Declaracion de cumplimiento.
3. Mensaje de autorizacion como emisor electronico.
4. Solicitud de folios productivos.
5. Configuracion productiva.
6. Primera emision controlada.

## 4. Solicitar CAF de produccion

En ambiente productivo SII:

1. Entra al sitio SII productivo.
2. Ve a timbraje electronico de documentos.
3. Solicita folios para los tipos autorizados.
4. Descarga los CAF XML.
5. Guarda los CAF en una carpeta privada, por ejemplo `caf/produccion/`.

Nunca subas CAF productivos a GitHub.

## 5. Configurar SimpleAPI en produccion

En tus variables locales:

```env
SIMPLEAPI_AMBIENTE=produccion
```

En payloads SimpleAPI:

```json
{
  "Ambiente": 1
}
```

Usa solo:

- Certificado vigente.
- CAF productivo.
- Folio productivo disponible.
- RUT y datos reales del receptor.

## 6. Primera factura controlada

Para la primera emision productiva:

- Usa un documento real de bajo riesgo.
- Revisa receptor, giro, direccion, monto neto, IVA y total.
- Genera DTE.
- Genera y envia sobre.
- Consulta TrackID.
- Guarda XML, PDF y respuesta.
- Verifica que el documento aparezca aceptado.

No automatices emision masiva hasta que la primera emision productiva este aceptada y revisada.

## 7. Control operativo obligatorio

Antes de facturar regularmente, implementa:

- Registro de folios disponibles y usados.
- Respaldo de XML emitidos.
- Respaldo de PDFs enviados a clientes.
- Consulta de estado SII por TrackID.
- Manejo de rechazos.
- Emision de notas de credito/debito.
- Registro de DTE recibidos y acuses, si aplica.
