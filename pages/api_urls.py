from django.urls import path
from . import api_views

urlpatterns = [
    path('', api_views.IndexApiView.as_view(), name='index-api'),
    path('about/', api_views.AboutApiView.as_view(), name='about-api'),
]
