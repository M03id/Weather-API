from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import requests

@api_view(['GET'])
def get_weather(request):
    city = request.GET.get('city')
    
    if not city:
        return Response({"error": "City parameter is required"}, status=400)
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}"
    params = {
        "appid" : settings.WEATHER_API_KEY,
        "units": "metric",
    }
    print(settings.WEATHER_API_KEY)
    try:
        response = requests.get(url, params=params)
        print(response.status_code)
        print(response.text)
        print(response.json())
        if response.status_code != 200:
            return Response({"error": "Failed to fetch data"}, status=500)
        
        data = response.json()
        result = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "condition": data["weather"][0]["description"]
            }
        return Response(result)
    except Exception as e:
        return Response({"error": str(e)}, status=500)