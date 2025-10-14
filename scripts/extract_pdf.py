from pypdf import PdfReader
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/extract_pdf.py <pdf_path> [pages] [limit]", file=sys.stderr)
        sys.exit(1)
    path = sys.argv[1]
    pages = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    limit = int(sys.argv[3]) if len(sys.argv) > 3 else 20000
    reader = PdfReader(path)
    buf = []
    for i, page in enumerate(reader.pages[:pages]):
        try:
            t = page.extract_text() or ""
        except Exception:
            t = ""
        buf.append(t)
    out = "\n".join(buf)
    if limit:
        out = out[:limit]
    print(out)

if __name__ == "__main__":
    main()

