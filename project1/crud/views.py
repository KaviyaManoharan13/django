""" crud views"""
# from django.http import HttpResponse
import base64
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import Crudsqlite

@api_view(["GET"])
@permission_classes([AllowAny])
def get_image_base64( image_id=None):
    """ handles to get the image"""
    try:
        image_id = 1  # Defaulting image_id to 1 for testing
        if image_id:
            your_model = Crudsqlite.objects.get(pk=image_id)# pylint: disable=E1101
            image_data = your_model.image.read()
            base64_encoded_image = base64.b64encode(image_data)
            base64_image_str = base64_encoded_image.decode("utf-8")
            # Return the Base64 encoded image as a JSON response
        return Response({"base64_image": base64_image_str})
        # else:
        #     # Handle the case when image_id is not provided
        #     # For example, return a 404 Not Found response
        #     return Response({"error": "Image ID not provided"}, status=404)
    except Crudsqlite.DoesNotExist:# pylint: disable=E1101
        # Handle the case when the requested image does not exist
        # For example, return a 404 Not Found response
        return Response({"error": "Image not found"}, status=404)


# import requests
# BASE_URL = 'http://localhost:8000'

# time = '2024-05-13T12:00:00'
# response = requests.get(f'{BASE_URL}/api/time/{time}/')

# if response.status_code == 200:
#     print(response.json())
# else:
#     print(f'Error: {response.status_code} - {response.text}')
