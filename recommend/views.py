from django.shortcuts import render, redirect
from .models import Smartphone
from .algorithm import calculate

# ../find/
def index(request):
    return render(request, 'recommend/index.html')

# ../find/smartphone
def smartphone(request):
    print(request.method)
    return render(request, 'recommend/smartphone_search.html')

# ../find/smartphone/result
def smartphone_result(request):

    if 'main' not in request.GET:
        return redirect('/') # redirecting

    dictionary = request.GET

    #get calculated list (fit)
    obj = calculate(dictionary)

    context = {
        'objects': obj[:10], #get 10 best smartphones
    }

    return render(request, 'recommend/results.html', context)
    
# ../find/smartphone/<s_id>
def smartphone_detail(request, s_id):
    obj = Smartphone.objects.get(id=s_id)

    context = {
        'object': obj
    }



    return render(request, 'recommend/detail.html', context)