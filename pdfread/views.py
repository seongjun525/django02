from django.shortcuts import render
import pdfplumber

def index(request):
    context = {}
    if request.method == "POST":
        p = request.FILES.get("pdf")
        pdf = pdfplumber.open(p)

        num = len(pdf.pages) # pdf page 객체들의 리스트
                # page 수만큼 객체들이 존재
        st = "" 

        for i in range(num):
            st += '='*40 + "\n" + f"{i+1}page\n" + '='*40 + "\n"
            st += pdf.pages[i].extract_text() + "\n\n"

        context["st"] = st
    return render(request, "pdfread/index.html", context)

# Create your views here.
