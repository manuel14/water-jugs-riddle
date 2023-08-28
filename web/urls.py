from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jugs_riddle', views.jugs_riddle, name='jugs_riddle'),
    path('jugs_riddle_api', views.jugs_riddle_api, name='jugs_riddle_api'),
]
