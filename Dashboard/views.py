from django.shortcuts import render

# Create your views here.

def index (request):
    template_name = "index"
    return render(request, "Dashboard/index.html")
