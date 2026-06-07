#!/usr/bin/env python3
"""
Ejemplo minimo para pedir un PDF carta a SimpleAPI desde un XML DTE.

Uso:
  python scripts/simpleapi_pdf_request.example.py dte.xml salida.pdf
  python scripts/simpleapi_pdf_request.example.py dte.xml cedible-v2.pdf --cedible

Este script no incluye credenciales. Lee SIMPLEAPI_KEY desde el entorno.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import requests


API_BASE = "https://api.simpleapi.cl/api/v1"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("xml", type=Path)
    parser.add_argument("output_pdf", type=Path)
    parser.add_argument("--cedible", action="store_true")
    parser.add_argument("--version", choices=["v1", "v2"], default="v2")
    args = parser.parse_args()

    api_key = os.environ.get("SIMPLEAPI_KEY")
    if not api_key:
        print("ERROR: falta SIMPLEAPI_KEY en el entorno")
        return 2

    input_data = {
        "NumeroResolucion": int(os.environ.get("SII_NUMERO_RESOLUCION", "0")),
        "UnidadSII": os.environ.get("SII_UNIDAD", "SANTIAGO"),
        "FechaResolucion": os.environ.get("SII_FECHA_RESOLUCION", "2003-05-16"),
        "Vendedor": os.environ.get("VENDEDOR", "Vendedor"),
        "FormaPago": os.environ.get("FORMA_PAGO", "Credito"),
        "CondicionVenta": os.environ.get("CONDICION_VENTA", "Credito"),
        "PropiedadLogo": "contain",
    }

    suffix = f"/impresion/pdf/carta/{args.version}"
    if args.cedible:
        suffix += "/cedible"

    with args.xml.open("rb") as fh:
        response = requests.post(
            API_BASE + suffix,
            headers={"Authorization": api_key},
            data={"input": json.dumps(input_data, ensure_ascii=False)},
            files={"fileEnvio": (args.xml.name, fh, "application/xml")},
            timeout=90,
        )

    if response.status_code >= 400:
        print(f"ERROR HTTP {response.status_code}: {response.text[:1000]}")
        return 1

    if not response.content.startswith(b"%PDF"):
        print("ERROR: SimpleAPI no retorno un PDF")
        return 1

    args.output_pdf.parent.mkdir(parents=True, exist_ok=True)
    args.output_pdf.write_bytes(response.content)
    print(f"OK: {args.output_pdf}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
