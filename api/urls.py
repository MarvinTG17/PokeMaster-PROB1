from django.urls import path
from .views import ListPokemon,GetPokemonId,GetPokemonNombre,ListPokedex,GetPokedexId,GetPokedexNombre


urlpatterns = [
    path('pokemon/',ListPokemon.as_view(),name='lista_pokemones'),
    path('pokemon/<int:id>',GetPokemonId.as_view(),name='id_pokemon'),
    path('pokemon/<nombre>',GetPokemonNombre.as_view(),name='nombre_pokemon'),
    path('pokedex/',ListPokedex.as_view(),name='lista_pokedex'),
    path('pokedex/<int:id>',GetPokedexId.as_view(), name='id_pokedex'),
    path('pokedex/<nombre>',GetPokedexNombre.as_view(),name='nombre_pokedex')
]