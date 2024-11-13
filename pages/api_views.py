from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Example of a simple API view
class IndexApiView(APIView):
    def get(self, request):
        data = {"message": "Welcome to the API index!"}
        return Response(data, status=status.HTTP_200_OK)

class AboutApiView(APIView):
    def get(self, request):
        data = {"about": "This is the API version of the About page."}
        return Response(data, status=status.HTTP_200_OK)
