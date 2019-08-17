from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Hello, site_summary</h1>')
