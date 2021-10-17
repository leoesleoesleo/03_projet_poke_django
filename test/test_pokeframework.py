import pytest
from pokemon.formpokemon import Formpokemon
from pokemon.models import Pokemon
from django import urls
from faker import Faker
from django.test import Client, TestCase

fake = Faker()

@pytest.mark.django_db
def test_pokemon_creation():
    """
    test Modelo Django, create objects
    """
    menu = Pokemon.objects.create(
        name='test')
    menu.save()
    assert menu.name == 'test'

def test_form_pokomen():
    """
    test Form Django
    """
    form_data = {
        'name': fake.name(),
        'id_pokemon': 1}
    form = Formpokemon(data=form_data)
    assert form.is_valid()


class UrlsTest(TestCase):
    def setUp(self):
        """
        initialize variables test
        """
        self.list_url_poke_generate = urls.reverse('pokemon_api_generate')
        self.list_url_poke_list = urls.reverse('pokemon_list')
        self.client = Client()

    @pytest.mark.django_db
    def test_ingreso_admin(self):
        """
        test url pokemon_api_generate
        """
        response = self.client.get(self.list_url_poke_generate)
        self.assertEqual(response.status_code, 200)

    @pytest.mark.django_db
    def test_ingreso_usuario(self):
        """
        test url pokemon_list
        """
        response = self.client.get(self.list_url_poke_list)
        self.assertEqual(response.status_code, 200)
