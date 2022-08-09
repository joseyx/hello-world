from django.http import HttpResponse

# Create your views here.
def sabrinaView(request):
    return HttpResponse("Sabrina es rolo de bruja")

def valuView(request):
    return HttpResponse("Valu es cuchi y buena en valorant.")