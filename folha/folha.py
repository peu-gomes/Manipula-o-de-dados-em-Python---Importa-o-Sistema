import pdfplumber
import pandas as pd

def find_pages_with_text(pdf_path, text):
    with pdfplumber.open(pdf_path) as pdf:
        pages_with_text = []
        for i, page in enumerate(pdf.pages):
            if text in page.extract_text():
                pages_with_text.append(i)  # pdfplumber uses 0-indexing for pages
    return pages_with_text

def extract_text_from_pages(pdf_path, pages_with_text):
    with pdfplumber.open(pdf_path) as pdf:
        text_data = []
        for page_num in pages_with_text:
            page = pdf.pages[page_num]
            text = page.extract_text()
            lines = text.split('\n')
            for line in lines:
                text_data.append(line)
    return text_data

pdf_path = "C:\\Users\\ph6br\\Documents\\GitHub\\VersatoCopyCargas\\folha\\Folha Mensal v1.pdf"
text = 'E M P'
pages_with_text = find_pages_with_text(pdf_path, text)

if pages_with_text:
    text_data = extract_text_from_pages(pdf_path, pages_with_text)
    df = pd.DataFrame(text_data, columns=['Texto'])
    print(df.to_string())
else:
    print("Texto não encontrado no PDF")
