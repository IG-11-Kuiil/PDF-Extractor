from google.colab import drive
import os, fitz, camelot, pytesseract, json
from pdf2image import convert_from_path

drive.mount('/content/drive')
drive_dir = '/content/drive/MyDrive'
files = [f for f in os.listdir(drive_dir) if f.lower().endswith('.pdf')]
for i, f in enumerate(files):
    print(f"[{i}] {f}")
idx = int(input("Select PDF by number: "))
drive_pdf_path = os.path.join(drive_dir, files[idx])

def extract_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    results = []
    for i, page in enumerate(doc, start=1):
        text = page.get_text('text').strip()
        if len(text) > 50:
            paras = [p.replace('\n', ' ').strip() for p in text.split('\n\n') if p.strip()]
            tables = []
            try:
                for t in camelot.read_pdf(pdf_path, pages=str(i), flavor='stream'):
                    tables.append(t.df.values.tolist())
            except:
                pass
            results.append({'page': i, 'type': 'digital', 'paragraphs': paras, 'tables': tables})
        else:
            img = convert_from_path(pdf_path, first_page=i, last_page=i, dpi=300)[0]
            ocr = pytesseract.image_to_string(img, lang='hin')
            paras = [line.strip() for line in ocr.split('\n') if line.strip()]
            results.append({'page': i, 'type': 'scanned', 'paragraphs': paras, 'tables': []})
    return results

data = extract_from_pdf(drive_pdf_path)
output_path = os.path.join(drive_dir, 'extracted.json')
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'Extraction complete. JSON saved to {output_path}')
