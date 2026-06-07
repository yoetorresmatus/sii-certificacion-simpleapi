#!/usr/bin/env python3
"""
Extrae la pagina cedible desde un PDF generado por SimpleAPI v2/cedible.

SimpleAPI puede retornar dos paginas:
  1. Tributaria
  2. Cedible

El portal SII de muestras impresas puede rechazar PDFs con mas de una pagina,
por lo que este script deja un PDF nuevo con solo la pagina cedible.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from pypdf import PdfReader, PdfWriter


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_pdf", type=Path)
    parser.add_argument("output_pdf", type=Path)
    parser.add_argument(
        "--page",
        type=int,
        default=2,
        help="Pagina 1-based a extraer. Por defecto: 2",
    )
    args = parser.parse_args()

    reader = PdfReader(str(args.input_pdf))
    index = args.page - 1
    if index < 0 or index >= len(reader.pages):
        print(f"ERROR: {args.input_pdf.name} tiene {len(reader.pages)} paginas")
        return 1

    page_text = (reader.pages[index].extract_text() or "").upper()
    if "CEDIBLE" not in page_text:
        print("ADVERTENCIA: la pagina extraida no contiene texto CEDIBLE")

    args.output_pdf.parent.mkdir(parents=True, exist_ok=True)
    writer = PdfWriter()
    writer.add_page(reader.pages[index])
    with args.output_pdf.open("wb") as fh:
        writer.write(fh)

    print(f"OK: {args.output_pdf}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
