from django.shortcuts import redirect, render, redirect
from django.views.generic import DeleteView, UpdateView
from django.urls import reverse_lazy
from .formpokemon import Formpokemon
from .models import Pokemon
import requests

import logging

log = logging.getLogger(__name__)


POKE_DETAIL = 'https://pokeapi.co/api/v2/pokemon/'
POKE_EVOLUTION = 'https://pokeapi.co/api/v2/evolution-chain/'


def list_evolution(url=POKE_EVOLUTION, id_pokemon=1):
    """
    Recursive function to list the evolutions of the pokemon
    if there is an error it returns an empty list
    """
    v_evo = []
    v_nom = []
    url = f'{url}{id_pokemon}/'
    response = requests.get(url)
    if response.status_code == 200:
        payload = response.json()
        # access pokemon name
        v_nom.append(payload['chain']['species']['name'])
        # access the first evolution
        if payload['chain']['evolves_to']:
            # ask if it has 1 evolution
            evolves_to = payload['chain']['evolves_to'][0]
            v_evo.append(evolves_to['species']['name'])
            # access the following evolution in case you have
            if 'evolves_to' in list(evolves_to.keys()) and evolves_to['evolves_to']:
                v_evo.append(evolves_to['evolves_to'][0]['species']['name'])
    else:
        msg = f"Service error: {url} answer: {response.status_code}"
        log.error(msg)
    return v_nom, v_evo


def list_pokemon_details(url=POKE_DETAIL,id_pokemon=1):
    """
    Recursive function to list the details of the pokemon such as height, weight and stats,
    if there is an error it returns an empty list
    """
    v_height = []
    v_weight = []
    url = f'{url}{id_pokemon}/'
    response = requests.get(url)
    if response.status_code == 200:
        payload = response.json()
        v_height.append(payload['height'])
        v_weight.append(payload['weight'])
        v_stat = [i['stat']['name'] + ' ' + str(i['base_stat']) for i in payload['stats']]
    else:
        msg = f'Service error: {url} answer: {response.status_code}'
        log.error(msg)
    return v_height, v_weight, v_stat


def generate_structure(id_poke=1):
    """
    Generate final structure
    """
    msg = f"Process: {id_poke}"
    log.info(msg)
    # build dic evolution
    try:
        v_nom = list_evolution(id_pokemon=id_poke)[0]
        v_evo = list_evolution(id_pokemon=id_poke)[1]
        v_height = list_pokemon_details(id_pokemon=id_poke)[0][0]
        v_weight = list_pokemon_details(id_pokemon=id_poke)[1][0]
        v_stat = list_pokemon_details(id_pokemon=id_poke)[2]
    except Exception as error:
        msg = f"error with data processing functions {error}"
        log.error(msg)    
    res = {
            'id'         : id_poke,
            'name'       : v_nom,
            'height'     : v_height,
            'weight'     : v_weight,
            'evolutions' : v_evo,
            'stat'       : v_stat
           }

    msg = f"End Process: {res}"
    log.info(msg)

    return res

def generate_pokemon(request):
    """
    it asks the user for the input pokemon id, then makes the call to pokeAPI and inserts
    in the db to have historical calls.
    """
    if request.method == 'GET':
        form = Formpokemon()
        contexto = {
            'form' : form
        }
    else:
        form = Formpokemon(request.POST)
        contexto = {
            'form' : form
        }
    if form.is_valid():
        pok = form.save(commit=False)
        id_poke = form.cleaned_data['id_pokemon']
        api_resp = generate_structure(id_poke=id_poke)
        try:
            evolutions = str(api_resp['evolutions']).replace('[','').replace(']','').replace(',','|').replace("'",'')
            stat = str(api_resp['stat']).replace('[','').replace(']','').replace(',','|').replace("'",'')
        
            pok.name = api_resp['name'][0]
            pok.height = api_resp['height']
            pok.weight = api_resp['weight']
            pok.evolutions = evolutions
            pok.stat = stat
            pok.save()

        except Exception as error:
            msg = f"error while processing and inserting data {error}"
            log.error(msg)

        return redirect('index')
    else:
        msg = "nvalid form"
        log.error(msg)
    return render(request,'formcreate.html',contexto)

def pokemon_list(request):
    """
    List the pokemon saved in the database
    """
    if request.method == 'GET':
        pokemon = Pokemon.objects.all()
        poke_query = pokemon
    else:
        poke_query = ''
    contexto = {
        'poke_query' : poke_query}
    return render(request,'index.html',contexto)

class Pokemon_update(UpdateView):
	"""
	Edita el Pokemon para el rol admin
	"""
	model = Pokemon
	form_class = Formpokemon
	template_name = 'form_update.html'
	success_url = reverse_lazy('index')

class Pokemon_delete(DeleteView):
	"""
	Elimina el Pokemon para el rol admin
	"""
	model = Pokemon
	form_class = Formpokemon
	template_name = 'check_pokemon.html'
	success_url = reverse_lazy('index')
