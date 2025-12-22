import pdfplumber
import sys

pdf_path = r"c:\Users\WEB STUDIO LINK\OneDrive\Desktop\Restoran Zlatar Novi\jelovnik\vinska-karta-nova.pdf"

try:
    with pdfplumber.open(pdf_path) as pdf:
        print(f"Total pages: {len(pdf.pages)}\n")
        print("="*80)
        
        all_text = []
        for i, page in enumerate(pdf.pages):
            print(f"\n{'='*80}")
            print(f"PAGE {i+1}")
            print('='*80)
            
            text = page.extract_text()
            if text:
                print(text)
                all_text.append(text)
            else:
                print(f"No text found on page {i+1}")
        
        print("\n" + "="*80)
        print("EXTRACTION COMPLETE")
        print("="*80)
        
except Exception as e:
    print(f"Error reading PDF: {e}")
    sys.exit(1)
