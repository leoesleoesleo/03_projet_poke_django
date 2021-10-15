#
# Consumo de PokeApi con Django
Por: Leonardo Patiño Rodriguez
<div align="center">
	<img height="200" src="https://leoesleoesleo.github.io/imagenes/django_pokeapi.png" alt="PokeAPI">
</div>  

## &nbsp; [![pyVersion37](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/download/releases/3.7/)

# Manual de instalación

### Características
<p align="justify">
Características habituales proporcionadas por Django, como la arquitectura MVC, ORM, plantillas, almacenamiento en caché y una interfaz de administración automática. Y celerys que trabaja con colas de tareas asíncrona para trabajos que se basa en el paso de mensajes distribuidos.
</p>
<p align="justify">
PokeAPI proporciona una interfaz API RESTful para objetos altamente detallados creados a partir de miles de líneas de datos relacionados con Pokémon.
Se Cubre específicamente la franquicia de videojuegos. Al usar PokeAPI, puedes consumir información sobre Pokémon, sus movimientos, habilidades, tipos,
grupos de huevos y mucho, mucho más.
</p>

### Pasos

- Clonar repositorio
	```
	git clone https://github.com/leoesleoesleo/backend_test.git
	```
- Crear entorno virtual

    Ejemplo anaconda
	```
	conda create -n poke_django python=3.7.9 
	```
	```
	conda activate poke_django
	```

- Navegar hasta la carpeta del proyecto para instalar dependencias
    ```
    pip install -r requirements.txt
    ```
    
- Migrar la base de datos    
    ```
    python manage.py makemigrations
    ```
    ```
    python manage.py migrate
    ```
- Cargar datos iniciales
    ```
    python manage.py loaddata gestorComidas/fixtures/posts-data.json
    ```
    
- Validar cobertura de la aplicación  
    ```
  coverage run -m pytest -v -p no:cacheprovider --junitxml=junit/test-results.xml --cov=. --cov-report=xml --cov-report=html  
    ```    
    
- Iniciar programa
    ```
    python manage.py runserver
    ```
    ```sh
    127.0.0.1:8000
    ```

##
## MANUAL TÉCNICO

### Contexto

<p align="justify">
  Construya un Comando que reciba como único parámetro un ID, 
  que represente la Cadena de Evolución. Se sugiere utilizar el servicio 
  "evolution-chains" como punto de partida 
  (integrar tantos servicios como sea necesario para completar el requisito) 
  para obtener y almacenar la siguiente información:
  -Nombre
  -Estadísticas base (para las 6 categorías)
  -Altura
  -Peso
  -Identificación
  -Evoluciones
</p>

## Fuentes de datos

Se consume los siguientes servicios de PokeAPI.  
```
https://pokeapi.co/api/v2/evolution-chain/
https://pokeapi.co/api/v2/pokemon/
```

## Arquitectura

Requerimientos Funcionales
-	Construya un Comando que reciba como único parámetro un ID, que represente la Cadena de Evolución.

Requerimientos no Funcionales
-	Las funciones son recursivas para escalar los datos en caso que el servicio reciba una lista de pokemon.
-	Las pruebas unitarias son escalables – (pytest)
-	La Cobertura del programa llega a un 95% (Coverage)
-	El programa se somete a un verificador de código fuente para una mejor calidad. 
-	Las Funciones y métodos están comentados.
-	El programa proporciona logs de información y errores.
-	El programa cuenta con manual de instalación.

#### Detalles del desarrollo

<p align="justify">
Se crean 3 funciones recursivas que consumen los servicios y se encargan de retornar los datos para representarlos en una tabla HTML del template, si no se puede acceder al servicio las funciones retornan las listas vacías.
<ul>
	<li><strong>list_evolution()</strong> Consume el servicio de evolution-chain y retorna dos listas, la primera es la lista de los nombres 
		de los pokemon y la segunda otra lista con las evoluciones relacionadas. 
	</li>
	<li><strong>list_pokemon_details()</strong>Consume el servicio pokemon y retorna 3 listas relacionadas con los detalles del pokemon como
    la altura, el peso y las estadísticas. 
		Estos datos hacen parte de los detalles de los pokemon. 
	</li>
	<li><strong>generate_structure()</strong> Este no consume ningún servicio pero si utiliza las funciones descritas anteriormente  para
		armar y generar el JSON de salida. 
	</li>
</ul>	
</p>

## Patrón de diseño MVT

<p align="justify">
Promueve el acoplamiento débil y la estricta separación entre las piezas de la aplicación, es fácil hacer cambios en un lugar particular sin afectar otras piezas de la aplicación. En las funciones de vista, por ejemplo, se separar la lógica de negocios de la lógica de presentación usando un sistema de plantillas. Con la capa de la base de datos, aplicamos esa misma filosofía para el acceso lógico a los datos.
</p>
<p align="center">
  <a href="#"><img src="https://leoesleoesleo.github.io/imagenes/patron_dise%C3%B1o.png"></a>
</p>

## Diagrama E-R

<p align="center">
  <a href="#"><img src="https://leoesleoesleo.github.io/imagenes/diagrama_er.png"></a>
</p>

## Cobertura

<p align="center">
  <a href="#"><img src="https://leoesleoesleo.github.io/imagenes/cobertura.png"></a>
</p>
