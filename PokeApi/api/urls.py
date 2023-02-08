from django.urls import path
from .views import PokemonView,PokedexView


urlpatterns = [
    path('pokemon/',PokemonView.getPokemones,name='lista_pokemones'),
    path('pokemon/<int:id>',PokemonView.getPokemonId,name='id_pokemon'),
    path('pokemon/<nombre>',PokemonView.getPokemonNombre,name='nombre_pokemon'),
    path('pokedex/',PokedexView.getPokedex,name='lista_pokedex'),
    path('pokedex/<int:id>',PokedexView.getPokedexId, name='id_pokedex'),
    path('pokedex/<nombre>',PokedexView.getPokedexNombre,name='nombre_pokedex')
]