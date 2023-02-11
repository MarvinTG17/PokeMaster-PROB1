from django.http.response import JsonResponse
#from django.views import View
from rest_framework.views import APIView
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Pokemon,Pokedex

class ListPokemon(APIView):
    def get(self,request):
        pokemons = list(Pokemon.objects.values())
        
        paginator = Paginator(pokemons, 20) 
        page = request.GET.get('page')
        try:
            pokemons = paginator.page(page)
        except PageNotAnInteger:
            pokemons = paginator.page(1)
        except EmptyPage:
            pokemons = paginator.page(paginator.num_pages)

        lista_pokemones = list(pokemons)

        response = {
            'pagina_anterior': None,
            'pagina_siguiente': None,
            #'primera_pagina': None,
            #'ultima_pagina': None,
            'pokemones': lista_pokemones,
        }

        if pokemons.has_previous():
            response['pagina_anterior'] = f'/api/pokemon?page={pokemons.previous_page_number()}'

        if pokemons.has_next():
            response['pagina_siguiente'] = f'/api/pokemon?page={pokemons.next_page_number()}'

        #if pokemons.has_previous() or pokemons.has_next():
            #response['primera_pagina'] = f'/api/pokemon?page={paginator.page(1).number}'
            #response['ultima_pagina'] = f'/api/pokemon?page={paginator.page(paginator.num_pages).number}'
        return JsonResponse(response)
    
class GetPokemonId(APIView):
    def get(self,request,id):
        pokemon = list(Pokemon.objects.filter(id=id).values())
        if len(pokemon)>0:
            pokeid = pokemon[0]
            dato = {"resultado":pokeid}
        return JsonResponse(dato)
    
class GetPokemonNombre(APIView):
    def get(self,request,nombre):
        pokemon = list(Pokemon.objects.filter(identifier=nombre).values())
        if len(pokemon)>0:
            pokeNombre = pokemon[0]
            data = {"resultado":pokeNombre}
        return JsonResponse(data)
    

class ListPokedex(APIView):
    def get(self,request):
        pokedexes = list(Pokedex.objects.values())
        if len(pokedexes)>0:
            datos = {"resultado":pokedexes}
        return JsonResponse(datos)

class GetPokedexId(APIView):    
    def get(self,request,id):
        pokedex = list(Pokedex.objects.filter(id=id).values())
        if len(pokedex)>0:
            pokedexid = pokedex[0]
            dato = {"resultado":pokedexid}
        return JsonResponse(dato)

class GetPokedexNombre(APIView):    
    def get(self,request,nombre):
        pokedex = list(Pokedex.objects.filter(identifier=nombre).values())
        if len(pokedex)>0:
            pokedexNombre = pokedex[0]
            data = {"resultado":pokedexNombre}
        return JsonResponse(data)