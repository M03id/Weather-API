## Weather API
https://roadmap.sh/projects/weather-api-wrapper-service

A simple Weather API built with Django REST Framework.


### Features
- Fetch weather data from OpenWeather API
- Use environment variables for secrets
- Cache responses with Redis
- Protect API with rate limiting

### Tech Stack
- Django
- Django REST Framework
- Redis
- OpenWeather API

### Setup

1. Clone project
git clone <your-repo-url>
cd Weather_API

2. Create virtual environment
python -m venv env
source env/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Add environment variables
Create a .env file:
WEATHER_API_KEY=your_api_key_here
REDIS_URL=redis://127.0.0.1:6379/1
DEBUG=True

5. Run server
python manage.py runserver
API Endpoint
GET /api/weather/?city=Cairo

### Example Response

{
  "city": "Cairo",
  "temperature": 30,
  "condition": "clear sky"
}

### Rate Limiting
API allows only limited requests per minute per user IP.

### Cache
Weather responses are cached in Redis to reduce external API calls.

