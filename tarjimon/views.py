from django.shortcuts import render
from .models import Lugat
# Create your views here.

def dictionary(request):
    soz = request.GET.get('q', '') 
    if soz and soz != '':
        natija = Lugat.objects.filter(inglizcha__contains=soz).all()[:3]
        print(natija)
    else:
        natija = None
    return render(request, 'index.html', {'q':soz, 'natija': natija})