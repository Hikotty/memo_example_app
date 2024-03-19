from django.http import HttpResponse

def alive(request):
    return HttpResponse("Server is alive")