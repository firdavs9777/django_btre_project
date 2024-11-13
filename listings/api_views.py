# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Listing
from .serializers import ListingSerializer

class ListingListView(APIView):
    def get(self, request):
        listings = Listing.objects.all()  # You can filter listings if needed
        serializer = ListingSerializer(listings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ListingDetailView(APIView):
    def get(self, request, pk):
        try:
            listing = Listing.objects.get(pk=pk)
        except Listing.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ListingSerializer(listing)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SearchView(APIView):
    def get(self, request):
        # Search logic (you can add filtering by query parameters)
        query = request.GET.get('q', '')
        listings = Listing.objects.filter(title__icontains=query)  # Adjust the filter as needed
        serializer = ListingSerializer(listings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
