from django.http import HttpResponse
# Create your views here.
def homePageView(request):
    return HttpResponse('Hello World!')

# def SabrinaBruja(request):
#     return HttpResponse('Sabrina es bruja')