# Contribuir

Gracias por mejorar esta guia.

## Reglas de seguridad

No abras PRs que incluyan:

- Certificados digitales.
- CAF reales.
- XML DTE reales.
- PDFs reales.
- API keys.
- Cookies o sesiones SII.
- RUTs personales o datos de clientes sin anonimizar.

## Estilo

- Mantener ejemplos genericos.
- Preferir checklists accionables.
- Documentar el error, el sintoma y la solucion.
- Indicar cuando algo depende del proveedor o del portal SII.

## Scripts

Los scripts deben:

- Leer credenciales desde variables de entorno.
- No imprimir secretos.
- Fallar con mensajes claros.
- Ser idempotentes cuando sea posible.
