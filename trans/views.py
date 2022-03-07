from django.shortcuts import render
from googletrans import Translator

def index(request):
    context = {}
    if request.method == "POST":
        bf = request.POST.get("bf")
        fr = request.POST.get("fr")
        to = request.POST.get("to")
        
        if bf:
            translator = Translator()

            af = translator.translate(bf, src=fr, dest=to)
            context.update({
                "bf" : bf,
                "fr" : fr,
                "to" : to,
                "af" : af.text
            })
    
    return render(request, "trans/index.html", context)
# Create your views here.
