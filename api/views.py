from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_weather(request):
    # Mock weather data
    date = {
        "location": "New York",
        "temperature": "15°C",
        "description": "Partly cloudy"
    }
    return Response(date)