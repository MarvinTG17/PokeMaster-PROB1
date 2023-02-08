from django.http.response import JsonResponse
from django.views import View
from django.core.paginator import Paginator,  EmptyPage, PageNotAnInteger
from .models import Pokemon,Pokedex

class PokemonView(View):

    """ def getPokemones(self,request):
        pokemones = list(Pokemon.objects.values())

        paginacion = Paginator(pokemones,20)
        pagina = request.GET.get("page") or 1
        post = paginacion.get_page(pagina)
        pagina_actual = int(pagina)
        paginas = range(1,post.paginator.num_pages + 1)

        if len(pokemones)>0:
            datos = {"paginas":paginas,"pagina_actual":pagina_actual,"resultado":pokemones}
        return JsonResponse(datos) """
    
    def getPokemones(request):
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
    
    def getPokemonId(self,id):
        pokemon = list(Pokemon.objects.filter(id=id).values())
        if len(pokemon)>0:
            pokeid = pokemon[0]
            dato = {"resultado":pokeid}
        return JsonResponse(dato)
    
    def getPokemonNombre(self,nombre):
        pokemon = list(Pokemon.objects.filter(identifier=nombre).values())
        if len(pokemon)>0:
            pokeNombre = pokemon[0]
            data = {"resultado":pokeNombre}
        return JsonResponse(data)
    

class PokedexView(View):
    def getPokedex(self):
        pokedexes = list(Pokedex.objects.values())
        if len(pokedexes)>0:
            datos = {"resultado":pokedexes}
        return JsonResponse(datos)
    
    def getPokedexId(self,id):
        pokedex = list(Pokedex.objects.filter(id=id).values())
        if len(pokedex)>0:
            pokedexid = pokedex[0]
            dato = {"resultado":pokedexid}
        return JsonResponse(dato)
    
    def getPokedexNombre(self,nombre):
        pokedex = list(Pokedex.objects.filter(identifier=nombre).values())
        if len(pokedex)>0:
            pokedexNombre = pokedex[0]
            data = {"resultado":pokedexNombre}
        return JsonResponse(data)