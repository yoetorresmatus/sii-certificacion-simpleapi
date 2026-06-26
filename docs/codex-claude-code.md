# Trabajar con Codex o Claude Code

Este proceso se puede ejecutar con ayuda de un agente de codigo como Codex o Claude Code, siempre que los secretos se mantengan locales y el usuario humano confirme las acciones legales ante el SII.

## Principio central

El agente puede:

- Leer documentacion.
- Generar scripts.
- Preparar XML/PDF.
- Validar archivos.
- Ordenar carpetas.
- Consultar correos conectados, si el usuario autoriza.
- Guiar la navegacion del portal.

El usuario humano debe:

- Iniciar sesion con certificado cuando corresponda.
- Confirmar declaraciones formales.
- Decidir cuando enviar al SII.
- Autorizar la primera emision productiva.

## Estructura recomendada del proyecto privado

```text
facturacion/
  .env
  certs/
    firmante.pfx
  caf/
    certificacion/
    produccion/
  dte/
    certificacion/
    produccion/
  sobres/
  pdf/
  trackids/
  scripts/
  docs/
```

Agrega un `.gitignore` fuerte desde el primer dia:

```gitignore
.env
certs/
caf/
dte/
sobres/
pdf/
trackids/
*.pfx
*.p12
*.xml
*.pdf
```

## Prompt inicial sugerido

Usa algo asi:

```text
Estoy certificando facturacion electronica SII Chile con SimpleAPI.
Trabaja en modo seguro: no imprimas secretos, no subas XML/PDF/CAF/certificados a Git, no hagas declaraciones legales ni envios finales sin mi confirmacion explicita.

Primero revisa docs/runbook-certificacion.md y checklists/checklist-certificacion.md.
Luego ayudame a avanzar etapa por etapa, dejando un archivo docs/ESTADO.md actualizado con fecha, evidencia, TrackID y siguiente paso.
```

## Reglas para el agente

- No mostrar claves ni contrasenas en pantalla.
- No copiar `.env` al repo publico.
- No enviar al SII sin confirmacion explicita.
- No declarar cumplimiento sin que el usuario confirme.
- No cambiar a `Ambiente: 1` hasta tener autorizacion final.
- No emitir documentos productivos masivos sin primera emision controlada.

## Handoff recomendado

Mantiene un archivo privado:

```text
docs/ESTADO.md
```

Con esta estructura:

```markdown
# Estado certificacion

## Empresa
- RUT:
- Documentos a certificar:
- Proveedor:

## Etapa actual
- Estado:
- Fecha:
- Evidencia:
- Siguiente paso:

## TrackIDs
- Set basico:
- Libro ventas:
- Libro compras:
- Simulacion:

## Archivos finales
- CAF:
- XML:
- PDF:

## Riesgos / pendientes
```

## Flujo practico con agente

1. Crear estructura privada.
2. Completar `.env` local.
3. Descargar CAF de certificacion.
4. Pedir al agente generar DTE del set.
5. Validar XML antes de enviar.
6. Enviar al SII solo con confirmacion.
7. Consultar TrackID.
8. Repetir hasta tener conformidad.
9. Generar PDFs.
10. Validar PDFs con `scripts/validate_pdf_batch.py`.
11. Subir muestras impresas.
12. Esperar correo.
13. Declarar cumplimiento con confirmacion humana.
14. Solicitar CAF productivo.
15. Preparar primera factura real.

## Checklist antes de produccion

Antes de pedir al agente emitir una factura real:

- Empresa autorizada como emisor electronico.
- CAF productivo descargado.
- Folio productivo disponible.
- `SIMPLEAPI_AMBIENTE=produccion`.
- Payload revisado por humano.
- Receptor y montos confirmados.
- Plan de respaldo XML/PDF listo.
- Consulta de estado posterior lista.
