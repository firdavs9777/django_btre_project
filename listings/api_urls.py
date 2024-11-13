# urls.py
from django.urls import path
from .api_views import ListingListView, ListingDetailView, SearchView

urlpatterns = [
    path('api/listings/', ListingListView.as_view(), name='listing-list'),
    path('api/listings/<int:pk>/', ListingDetailView.as_view(), name='listing-detail'),
    path('api/search/', SearchView.as_view(), name='listing-search'),
]
