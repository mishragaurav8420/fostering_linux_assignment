from django.urls import path
from .views import create_movie, retrieve_weather,get_movies

app_name = 'api_integration'
urlpatterns = [
    path('movies/create/', create_movie, name='create_movie'),
    path('movies/get/',get_movies,name='get_movies'),
    path('weather/', retrieve_weather, name='retrieve_weather'),
]
