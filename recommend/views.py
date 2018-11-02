from django.shortcuts import render

# Create your views here.
def find_main(request):
    return render(request, 'recommend/index.html')