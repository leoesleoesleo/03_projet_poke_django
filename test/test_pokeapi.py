import pytest
from pokemon.formpokemon import Formpokemon
from pokemon.models import Pokemon
from pokemon.views import *
from mocks.mocks import *
import requests


@pytest.mark.parametrize("url,expected", 
                         [(POKE_DETAIL, 200),
                          (POKE_EVOLUTION, 200)])
def test_api_response(url, expected):
    """
    Test that the apis respond pokeapi
    """
    url = f'{url}1/'
    response = requests.get(url)
    assert response.status_code == expected

@pytest.mark.parametrize("id_pokemon,expected", 
                         [(33, (['slowpoke'], ['slowbro'])),
                         (45, (['exeggcute'], ['exeggutor'])),
                         (96, (['wooper'], ['quagsire'])),
                         (105, (['snubbull'], ['granbull'])),
                         (150, (['mawile'], []))])
def test_list_evolution(id_pokemon, expected):
    """
    Test that the function responds correctly
    """
    assert list_evolution(id_pokemon=id_pokemon) == expected


@pytest.mark.parametrize("id_pokemon,expected",
                         [( 32, data_test32 ),
                         ( 41, data_test41 ),
                         ( 86, data_test86 ),
                         (156, data_test156 )])
def test_list_pokemon_details(id_pokemon,expected):
    """
    test function list_pokemon_details()
    """
    assert list_pokemon_details(id_pokemon=id_pokemon) == expected

@pytest.mark.parametrize("id_poke,expected",
                         [( 66, data_test66 ),
                         ( 85, data_test85 ),
                         ( 87, data_test87 ),
                         ( 92, data_test92 )]
                        )
def test_generate_structure(id_poke,expected):
    """
    test function generate_structure()
    """
    assert generate_structure(id_poke=id_poke) == expected
                