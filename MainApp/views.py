from django.shortcuts import render

# Create your views here.

def index(request):
    ''' The homepage for learning log'''
    # Renders whatever is in the html file to the webpage
    return render(request, "MainApp/index.html")

