from django.shortcuts import render

# Create your views here.


def index(request):
    template_name = "Dashboard/index.html"
    return render(request, template_name)


def base(request):
    template_name = "base.html"
    return render(request, template_name)