from django.shortcuts import render

# Create your views here.
def hakkimizda(request):
    return render(request, 'hakkimizda.html',{})

def iletisim(request):
    return render(request, 'iletisim.html',{})