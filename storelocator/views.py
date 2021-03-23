from django.shortcuts import render

# Create your views here.
def storeLocatorPage(request):
    return render(request, 'storelocator/storelocator.html')
