import pdfplumber

pdf = pdfplumber.open("아뱅.pdf")

num = len(pdf.pages) # pdf page 객체들의 리스트
             # page 수만큼 객체들이 존재

for i in range(num):
    print(pdf.pages[i].extract_text())
# 1페이지 텍스트 추출