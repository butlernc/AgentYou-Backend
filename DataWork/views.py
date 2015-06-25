from django.http import HttpResponse

# Create your views here.

def match(request):
    address = request.POST["address"]
    # match incoming picture by running C++ script
    response = request.POST["address"]
    return HttpResponse(response)
