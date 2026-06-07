#!/usr/bin/env python3
"""
Normaliza texto para reducir rechazos por caracteres problematicos en SII.

Nota: no todos los campos legales deben perder acentos o ene. Usa esto para
descripciones, giros comerciales o textos libres cuando tu flujo lo requiera.
"""
from __future__ import annotations

import argparse
import re
import unicodedata


def sanitize(value: str, max_length: int | None = None) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    value = value.replace("ñ", "n").replace("Ñ", "N")
    value = re.sub(r"[^A-Za-z0-9 .,;:/()\\-_%&+]", " ", value)
    value = re.sub(r"\s+", " ", value).strip()
    if max_length:
        value = value[:max_length].rstrip()
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("text")
    parser.add_argument("--max-length", type=int)
    args = parser.parse_args()
    print(sanitize(args.text, args.max_length))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
