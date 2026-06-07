#!/usr/bin/env python3
"""
Valida PDFs antes de subir muestras impresas al SII.

Ejemplos:
  python scripts/validate_pdf_batch.py outputs/upload_sii_final
  python scripts/validate_pdf_batch.py outputs/upload_sii_final --require-cedible-text
"""
from __future__ import annotations

import argparse
from pathlib import Path

from pypdf import PdfReader


def pdf_text(reader: PdfReader) -> str:
    chunks: list[str] = []
    for page in reader.pages:
        chunks.append(page.extract_text() or "")
    return "\n".join(chunks)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", type=Path, help="Carpeta con PDFs a validar")
    parser.add_argument(
        "--require-cedible-text",
        action="store_true",
        help="Exige que archivos cuyo nombre contiene cedible incluyan texto CEDIBLE",
    )
    args = parser.parse_args()

    if not args.folder.exists():
        print(f"ERROR: no existe la carpeta {args.folder}")
        return 2

    pdfs = sorted(args.folder.glob("*.pdf"))
    if not pdfs:
        print(f"ERROR: no hay PDFs en {args.folder}")
        return 2

    errors: list[str] = []
    for pdf in pdfs:
        try:
            reader = PdfReader(str(pdf))
        except Exception as exc:
            errors.append(f"{pdf.name}: no se pudo leer PDF ({exc})")
            continue

        pages = len(reader.pages)
        if pages != 1:
            errors.append(f"{pdf.name}: tiene {pages} paginas; SII suele exigir 1")

        is_cedible = "cedible" in pdf.name.lower()
        if args.require_cedible_text and is_cedible:
            text = pdf_text(reader).upper()
            if "CEDIBLE" not in text:
                errors.append(f"{pdf.name}: no contiene texto CEDIBLE")

    print(f"PDF revisados: {len(pdfs)}")
    if errors:
        print("Errores:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: todos los PDFs pasaron la validacion local")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
