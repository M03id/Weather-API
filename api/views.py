from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from django.core.cache import cache
from django_ratelimit.decorators import ratelimit
from django.http import JsonResponse
import requests

@ratelimit(key='ip', rate='5/m', block=False)
@api_view(['GET'])
def get_weather(request):

    if getattr(request, 'limited', False):
        return JsonResponse({"error": "Too many requests. Please try again later."}, status=429)

    city = request.GET.get('city')
    
    if not city:
        return Response({"error": "City parameter is required"}, status=400)
    
    catched_data = cache.get(city)
    if catched_data:
        return Response({
            "source": "cahce",
            "data": catched_data
        })

    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid" : settings.WEATHER_API_KEY,
        "units": "metric",
    }

    try:
        response = requests.get(url, params=params)
       
        if response.status_code != 200:
            return Response({"error": "Failed to fetch data"}, status=500)
        
        data = response.json()
        result = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "condition": data["weather"][0]["description"]
            }
        
        cache.set(city, result, timeout=60 * 60 * 12)  # Cache for 12 hours

        return Response({
            "source": "api",
            "data": result  
        })
    except Exception as e:
        return Response({"error": str(e)}, status=500)