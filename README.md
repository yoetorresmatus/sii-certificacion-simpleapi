# Certificacion SII con SimpleAPI

Guia practica para completar la certificacion de facturacion electronica en Chile usando SimpleAPI como software de mercado.

Este repositorio nace desde una certificacion real que paso por:

- Postulacion como software de mercado.
- Obtencion de CAF de certificacion.
- Envio de set de pruebas.
- Libro de ventas y compras.
- Set de simulacion.
- Set de intercambio.
- Muestras impresas PDF.
- Revision final del SII.

La idea es que otra empresa no tenga que descubrir el proceso a punta de ensayo y error.

## Que incluye

- Runbook paso a paso del proceso SII.
- Checklist para cada etapa.
- Plantilla `.env.example`.
- Scripts utilitarios para:
  - Validar cantidad de paginas de PDFs.
  - Verificar que las copias cedibles contengan `CEDIBLE`.
  - Extraer la pagina cedible desde un PDF de SimpleAPI `v2/cedible`.
  - Sanitizar nombres/textos para compatibilidad SII.
- Notas de problemas frecuentes y sus soluciones.

## Que NO incluye

Por seguridad y privacidad, este repo no incluye:

- Certificados digitales `.pfx` / `.p12`.
- CAF reales descargados desde SII.
- XML DTE reales.
- PDFs reales de certificacion.
- API keys.
- Cookies, sesiones, claves SII o datos personales.

## Requisitos

- Python 3.10+
- Cuenta SimpleAPI con API key.
- Certificado digital vigente del firmante autorizado.
- CAF de certificacion descargados desde SII.
- Acceso al portal de certificacion SII.

Instalar dependencias:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Flujo corto

1. Completa `templates/.env.example` y guardalo como `.env` local, sin subirlo a Git.
2. Postula en SII como software de mercado.
3. Obtiene folios CAF de certificacion.
4. Genera y envia los sets con SimpleAPI.
5. Declara avance cuando el portal lo solicite.
6. Completa intercambio.
7. Genera PDFs tributarios y cedibles.
8. Sube las muestras impresas.
9. Espera revision.
10. Declara cumplimiento.
11. Recien con autorizacion final, pasa a produccion.

## Advertencia importante

No uses folios ni ambiente de produccion antes de terminar la certificacion. El ambiente de certificacion usa `Ambiente: 0` en SimpleAPI; produccion usa `Ambiente: 1`.

## Documentacion

- [Runbook completo](docs/runbook-certificacion.md)
- [Muestras impresas PDF](docs/muestras-impresas.md)
- [Errores frecuentes](docs/errores-frecuentes.md)
- [Checklist general](checklists/checklist-certificacion.md)

## Licencia

MIT. Usalo, adaptalo y mejora el camino para la siguiente persona.
