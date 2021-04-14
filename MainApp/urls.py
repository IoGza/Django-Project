from django.urls import path

from . import views

app_name = 'MainApp'

urlpatterns = [
    # Leaving first argument blank describes home page
    path('', views.index,name='index'),
]