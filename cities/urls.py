from django.urls import path

from .views import HomePageView
from .views import CityAPIView,QHAPIView
from django.urls import path,include
from rest_framework.routers import DefaultRouter


from . import views
urlpatterns = [
    path('view/', CityAPIView.as_view(), name='search_results'),
    path('qh/', QHAPIView.as_view(), name='search_results'),
    path('vitri1/', views.vitri1, name='ind'),
    path('vitri2/', views.vitri2, name='ind'),
    path('vitri3/', views.vitri3, name='ind'),
    path('vitri4/', views.vitri4, name='ind'),
    path('vitri5/', views.vitri5, name='ind'),
    path('vitri6/', views.vitri6, name='ind'),
    path('vitri7/', views.vitri7, name='ind'),
    path('vitri8/', views.vitri8, name='ind'),
    path('vitri9/', views.vitri9, name='ind'),
    path('vitri10/', views.vitri10, name='ind'),
    path('vitri11/', views.vitri11, name='ind'),
    path('vitri12/', views.vitri12, name='ind'),
    path('vitri13/', views.vitri13, name='ind'),
    path('vitri14/', views.vitri14, name='ind'),
    path('vitri15/', views.vitri15, name='ind'),
    path('vitri16/', views.vitri16, name='ind'),
    path('vitri17/', views.vitri17, name='ind'),
    path('vitri18/', views.vitri18, name='ind'),
    path('vitri19/', views.vitri19, name='ind'),
    path('vitri20/', views.vitri20, name='ind'),
    path('vitri21/', views.vitri21, name='ind'),
    path('vitri22/', views.vitri22, name='ind'),
    path('vitri23/', views.vitri23, name='ind'),
    path('vitri24/', views.vitri24, name='ind'),
    path('vitri25/', views.vitri25, name='ind'),
    path('vitri26/', views.vitri26, name='ind'),
    path('vitri27/', views.vitri27, name='ind'),
    path('vitri28/', views.vitri28, name='ind'),
    path('vitri29/', views.vitri29, name='ind'),
    path('vitri30/', views.vitri30, name='ind'),
    path('vitri31/', views.vitri31, name='ind'),
    path('vitri32/', views.vitri32, name='ind'),
    path('vitri33/', views.vitri33, name='ind'),
    path('vitri34/', views.vitri34, name='ind'),
    path('vitri35/', views.vitri35, name='ind'),
    path('vitri36/', views.vitri36, name='ind'),
]