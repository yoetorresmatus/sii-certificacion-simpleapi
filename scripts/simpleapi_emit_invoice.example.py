#!/usr/bin/env python3
"""
Ejemplo minimo de emision de Factura Electronica 33 con SimpleAPI.

Este archivo es una plantilla educativa. No emitas documentos productivos sin
revisar receptor, montos, folio, CAF y ambiente.

Uso:
  SIMPLEAPI_KEY=... python scripts/simpleapi_emit_invoice.example.py payload.json salida.xml
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import requests


API_URL = "https://api.simpleapi.cl/api/v1/dte/generar"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("payload_json", type=Path)
    parser.add_argument("output_xml", type=Path)
    parser.add_argument("--cert", default=os.environ.get("SII_CERT_FILE", "certs/firmante.pfx"))
    parser.add_argument("--caf", required=True, help="Ruta al CAF XML productivo o de certificacion")
    args = parser.parse_args()

    api_key = os.environ.get("SIMPLEAPI_KEY")
    cert_pass = os.environ.get("SII_CERT_PASS")
    cert_rut = os.environ.get("SII_RUT_FIRMANTE")
    ambiente_name = os.environ.get("SIMPLEAPI_AMBIENTE", "certificacion")
    ambiente = 1 if ambiente_name == "produccion" else 0

    if not api_key or not cert_pass or not cert_rut:
        print("ERROR: faltan SIMPLEAPI_KEY, SII_CERT_PASS o SII_RUT_FIRMANTE")
        return 2

    payload = json.loads(args.payload_json.read_text(encoding="utf-8"))
    payload.setdefault("Certificado", {"Rut": cert_rut, "Password": cert_pass})
    payload["Certificado"]["Rut"] = cert_rut
    payload["Certificado"]["Password"] = cert_pass
    payload["Ambiente"] = ambiente

    cert_path = Path(args.cert)
    caf_path = Path(args.caf)
    if not cert_path.exists():
        print(f"ERROR: no existe certificado {cert_path}")
        return 2
    if not caf_path.exists():
        print(f"ERROR: no existe CAF {caf_path}")
        return 2

    with cert_path.open("rb") as cert_fh, caf_path.open("rb") as caf_fh:
        response = requests.post(
            API_URL,
            headers={"Authorization": api_key},
            data={"input": json.dumps(payload, ensure_ascii=False)},
            files={
                "files": (cert_path.name, cert_fh, "application/x-pkcs12"),
                "files2": (caf_path.name, caf_fh, "application/xml"),
            },
            timeout=90,
        )

    if response.status_code >= 400:
        print(f"ERROR HTTP {response.status_code}: {response.text[:1000]}")
        return 1

    args.output_xml.parent.mkdir(parents=True, exist_ok=True)
    args.output_xml.write_bytes(response.content)
    print(f"OK: {args.output_xml}")
    print(f"Ambiente usado: {ambiente_name} ({ambiente})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
