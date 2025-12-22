import PyPDF2
import sys

pdf_path = r"jelovnik\jelovnik-nove-cene_novembar_2022.pdf"

try:
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        print(text)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
