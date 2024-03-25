from django.http import HttpResponse
def homePage(request):
    return HttpResponse("This is a home page.")