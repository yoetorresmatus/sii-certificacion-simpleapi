# Runbook de certificacion SII con SimpleAPI

Este documento resume el camino practico para certificar facturacion electronica con SimpleAPI en Chile.

## 0. Preparacion

Antes de comenzar:

- Tener empresa con inicio de actividades y actividades economicas vigentes.
- Tener usuario administrador o representante con acceso SII.
- Tener certificado digital del firmante.
- Tener SimpleAPI key.
- Definir documentos a certificar, por ejemplo:
  - 33: Factura Electronica
  - 34: Factura No Afecta o Exenta Electronica
  - 46: Factura de Compra Electronica
  - 56: Nota de Debito Electronica
  - 61: Nota de Credito Electronica

## 1. Postulacion como software de mercado

En el portal SII de certificacion, postula usando la opcion de software de mercado.

Datos habituales:

- Software: SimpleAPI.
- Documentos: los tipos DTE que emitira la empresa.
- Correo de contacto tecnico/administrativo.
- Usuario administrador.

Revisa que el usuario que firmara tenga permisos para:

- Firmar documentos.
- Enviar documentos.

Un error comun es que el set se genere bien, pero el SII lo rechace o no avance porque el RUT firmante no esta autorizado.

## 2. Obtener folios CAF de certificacion

En ambiente de certificacion SII, solicita timbraje electronico para cada tipo DTE.

Ruta tipica:

1. Entrar a `https://maullin.sii.cl/`.
2. Ir a `Solicitud de Timbraje Electronico de Documentos`.
3. Ingresar RUT contribuyente.
4. Seleccionar documento a timbrar.
5. Descargar CAF XML.

Guarda los CAF localmente en una carpeta privada, por ejemplo `caf/`.

Nunca subas CAF reales a GitHub.

## 3. Set de pruebas

El SII entrega un set con casos y montos esperados. Genera los DTE con SimpleAPI, usando:

- Certificado digital.
- CAF del tipo DTE correspondiente.
- Ambiente certificacion.
- Folios del rango CAF disponible.

Luego arma el sobre `EnvioDTE` y envialo al SII.

Con SimpleAPI REST normalmente intervienen estos endpoints:

- `POST /api/v1/dte/generar`
- `POST /api/v1/envio/generar`
- `POST /api/v1/envio/enviar`
- `POST /api/v1/consulta/envio`
- `POST /api/v1/consulta/dte`

## 4. Libros de ventas y compras

El portal puede solicitar libro de ventas y libro de compras asociados al set.

Recomendacion:

- No improvisar XML a mano salvo que domines los esquemas SII.
- Validar si tu proveedor genera el libro aceptado por SII.
- Si el SII responde errores de schema, confirmar que se esta usando el flujo correcto para certificacion.

## 5. Set de simulacion

Cuando el set de pruebas este conforme, el portal habilita set de simulacion.

Consejos:

- Usa folios vigentes del CAF de certificacion.
- Mantiene montos y referencias consistentes.
- Consulta el TrackID hasta que el portal muestre conformidad.

## 6. Set de intercambio

En el portal de intercambio:

1. Descarga el XML de envio que el SII entrega.
2. Genera:
   - Respuesta de intercambio.
   - Recibo de mercaderias o servicios.
   - Resultado de aprobacion comercial.
3. Sube cada XML en la seccion correspondiente.

Los XML deben estar firmados con el certificado autorizado.

## 7. Muestras impresas

Esta etapa suele ser la mas confusa.

El portal `pdfdteInternet` lista PDFs esperados agrupados por:

- PRUEBA
- SIMULACION

Para Factura Electronica, Factura Exenta, Guia de Despacho y Factura de Compra, el SII pide ejemplar:

- Tributario.
- Cedible.

Notas de credito y debito normalmente van solo como tributarias.

Ver detalle en [Muestras impresas](muestras-impresas.md).

## 8. Revision SII

Cuando todos los PDFs tengan validacion OK, el boton `Enviar al SII` queda habilitado.

Luego de enviar:

- El estado queda en revision.
- Espera correo del SII o cambio en el portal.
- No reenvies mientras esta en revision salvo rechazo.

Correo esperado si queda aprobado:

```text
La revision de las muestras impresas ha sido APROBADA
```

El correo puede indicar que el representante legal debe realizar la declaracion de cumplimiento.

## 9. Declaracion de cumplimiento

Si las muestras impresas quedan conformes, el portal habilita la declaracion final de cumplimiento.

Ruta usada:

```text
https://maullin.sii.cl/cvc_cgi/dte/pe_avance7
```

Lee con cuidado antes de declarar. El portal advierte que al declarar cumplimiento la empresa queda operando en el sistema de facturacion electronica.

Resultado esperado:

```text
El contribuyente [RAZON SOCIAL] Rut [RUT], esta autorizada para operar como emisor de documentos tributarios electronicos.
```

Si ves ese mensaje, la certificacion esta cerrada.

## 10. Produccion

Solo despues de la autorizacion final:

- Solicita CAF de produccion.
- Cambia SimpleAPI a `Ambiente: 1`.
- Usa folios productivos.
- Mantiene un control estricto de folios usados.
- Haz una primera emision controlada antes de automatizar.

Ver detalle en [Paso final y produccion](paso-final-produccion.md).

## 11. Trabajar con Codex o Claude Code

Puedes usar un agente para preparar archivos, revisar errores y mantener el estado del proyecto.

El agente no debe:

- Imprimir secretos.
- Enviar al SII sin confirmacion.
- Declarar cumplimiento sin confirmacion humana.
- Emitir documentos productivos masivos sin una primera prueba controlada.

Ver [Trabajar con Codex o Claude Code](codex-claude-code.md).

## Reglas de oro

- No publiques certificados, CAF, XML reales ni TrackIDs con datos de contribuyente.
- No mezcles folios de certificacion con produccion.
- No edites XML firmados manualmente despues de firmarlos.
- Verifica PDFs antes de subirlos.
- En cedibles, confirma que el PDF contiene la palabra `CEDIBLE`.
- Guarda un estado escrito del proceso con fecha, evidencia y siguiente paso.
- Al pasar a produccion, separa completamente CAF/folios productivos de los de certificacion.
