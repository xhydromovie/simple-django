from django.shortcuts import render
from .models import Smartphone

# Create your views here.
def index(request):
    return render(request, 'recommend/index.html')

def recommend_detail(request, s_id):
    obj = Smartphone.objects.get(id=s_id)

    context = {
        'object': obj
    }

    return render(request, 'recommend/detail.html', context)