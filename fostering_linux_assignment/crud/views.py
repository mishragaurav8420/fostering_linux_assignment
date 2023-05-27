import requests
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

def get_movies(request):
    if request.method == 'GET':
        # Make GET request to movie API to retrieve all movies
        response = requests.get('https://my-json-server.typicode.com/horizon-code-academy/fake-movies-api/movies')

        if response.status_code == 200:
            movie_data = response.json()
            return JsonResponse({'movies': movie_data}, status=200)
        else:
            return JsonResponse({'error': 'Failed to retrieve movies'}, status=400)

    # Handle the case when the request method is not GET
    return HttpResponse('Method Not Allowed', status=405)


from django.shortcuts import render, redirect
import requests

def create_movie(request):
    if request.method == 'POST':
        movie_data = {
            "Title": request.POST.get('Title'),
            "Year": request.POST.get('Year'),
            "Runtime": request.POST.get('Runtime'),
            "Poster": request.POST.get('Poster'),
            # Include other movie details
        }

        # Make POST request to movie API
        response = requests.post('https://my-json-server.typicode.com/horizon-code-academy/fake-movies-api/movies', json=movie_data)

        if response.status_code == 201:
            created_movie = response.json()
            return JsonResponse({'message': 'Movie created successfully', 'movie': created_movie}, status=201)
        else:
            return JsonResponse({'error': 'Failed to create movie'}, status=400)

    # Handle the case when the request method is GET
    return render(request, 'create_movie.html')

def retrieve_weather(request):
    if request.method == 'GET':
        city = request.GET.get('city')
        # Make GET request to weather API
        response = requests.get(f'https://api.weatherapi.com/v1/weather?q={city}', params={'key': 'YOUR_WEATHER_API_KEY'})
        if response.status_code == 200:
            weather_data = response.json()
            return JsonResponse({'weather': weather_data}, status=200)
        else:
            return JsonResponse({'error': 'Failed to retrieve weather information'}, status=400)
