from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user
from app.auth.forms import CreateUser, Login, PokemonSummons
import requests

from app.models import User, db

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    user_signup = CreateUser()
    if request.method == 'POST':
        if user_signup.validate():
            firstname = user_signup.firstname.data
            lastname = user_signup.lastname.data
            email_address = user_signup.email_address.data
            password = user_signup.password.data

            print(firstname, lastname, email_address, password)

            # initializing user from models.py
            user = User(firstname, lastname, email_address, password)

            # adding user to database
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.signin'))
    return render_template('signup.html', user_signup=user_signup)

@auth.route('/login', methods=['GET', 'POST'])
def signin():
    user_login = Login()
    if request.method =="POST":
        if user_login.validate():
            email = user_login.email_address.data
            password = user_login.password.data

            print(email, password)
            # getting user from database if he/she exists by instantiating the user class from our models
            user = User.query.filter_by(email=email).first()
            if user:
                # db_password = User.query.filter_by(password=password).first()
                if password == user.password:
                    print('Logged in')
                    login_user(user)
                else:
                    print('Incorrect password')
            else:
                print('user doesnt exist')
    return render_template('login.html', user_login=user_login)

@auth.route('/your_pokemon', methods=['GET', 'POST'])
def form():
    pokeform = PokemonSummons()
    if request.method == 'POST':
        if pokeform.validate():
            pokename = pokeform.pokename.data
            usable_pokename = str(pokename)
            # api code below

            ditto = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
            pikachu = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
            snorlax = requests.get('https://pokeapi.co/api/v2/pokemon/snorlax')
            garchomp = requests.get('https://pokeapi.co/api/v2/pokemon/garchomp')
            squirtle = requests.get('https://pokeapi.co/api/v2/pokemon/squirtle')
            charizard = requests.get('https://pokeapi.co/api/v2/pokemon/charizard')

            # Below is the dictionary I will loop through in my fuction for each pokemon only using the values of the dictionary to do so:

            working_dict = {
                'ditto' : ditto.json(),
                'pikachu' : pikachu.json(),
                'snorlax' : snorlax.json(),
                'garchomp' : garchomp.json(),
                'squirtle' : squirtle.json(),
                'charizard' : charizard.json()
            }

            def pokemon_attributes(your_dict):
                if usable_pokename.lower() == 'ditto':
                    final_display = []
                    for value in your_dict.values():
                        pokemon_dict = {}
                        pokemon_name = value['forms'][0]['name']
                        pokemon_dict[pokemon_name] = {
                            'Ability' : value['abilities'][0]['ability']['name'],
                            'Base_experience' : value['base_experience'],
                            'Sprite' : value['sprites']['front_shiny'],
                            'Attack base_stat' : value['stats'][1]['base_stat'],
                            'hp base_stat' : value['stats'][0]['base_stat'],
                            'Defense base_stat': value['stats'][2]['base_stat']
                        }
                        final_display.append(pokemon_dict)
                    return final_display[0]
                elif usable_pokename.lower() == 'pikachu':
                    final_display = []
                    for value in your_dict.values():
                        pokemon_dict = {}
                        pokemon_name = value['forms'][0]['name']
                        pokemon_dict[pokemon_name] = {
                            'Ability' : value['abilities'][0]['ability']['name'],
                            'Base_experience' : value['base_experience'],
                            'Sprite' : value['sprites']['front_shiny'],
                            'Attack base_stat' : value['stats'][1]['base_stat'],
                            'hp base_stat' : value['stats'][0]['base_stat'],
                            'Defense base_stat': value['stats'][2]['base_stat']
                        }
                        final_display.append(pokemon_dict)
                    return final_display[1]
                elif usable_pokename.lower() == 'snorlax':
                    final_display = []
                    for value in your_dict.values():
                        pokemon_dict = {}
                        pokemon_name = value['forms'][0]['name']
                        pokemon_dict[pokemon_name] = {
                            'Ability' : value['abilities'][0]['ability']['name'],
                            'Base_experience' : value['base_experience'],
                            'Sprite' : value['sprites']['front_shiny'],
                            'Attack base_stat' : value['stats'][1]['base_stat'],
                            'hp base_stat' : value['stats'][0]['base_stat'],
                            'Defense base_stat': value['stats'][2]['base_stat']
                        }
                        final_display.append(pokemon_dict)
                    return final_display[2]
                elif usable_pokename.lower() == 'garchomp':
                    final_display = []
                    for value in your_dict.values():
                        pokemon_dict = {}
                        pokemon_name = value['forms'][0]['name']
                        pokemon_dict[pokemon_name] = {
                            'Ability' : value['abilities'][0]['ability']['name'],
                            'Base_experience' : value['base_experience'],
                            'Sprite' : value['sprites']['front_shiny'],
                            'Attack base_stat' : value['stats'][1]['base_stat'],
                            'hp base_stat' : value['stats'][0]['base_stat'],
                            'Defense base_stat': value['stats'][2]['base_stat']
                        }
                        final_display.append(pokemon_dict)
                    return final_display[3]
                elif usable_pokename.lower() == 'squirtle':
                    final_display = []
                    for value in your_dict.values():
                        pokemon_dict = {}
                        pokemon_name = value['forms'][0]['name']
                        pokemon_dict[pokemon_name] = {
                            'Ability' : value['abilities'][0]['ability']['name'],
                            'Base_experience' : value['base_experience'],
                            'Sprite' : value['sprites']['front_shiny'],
                            'Attack base_stat' : value['stats'][1]['base_stat'],
                            'hp base_stat' : value['stats'][0]['base_stat'],
                            'Defense base_stat': value['stats'][2]['base_stat']
                        }
                        final_display.append(pokemon_dict)
                    return final_display[4]
                elif usable_pokename.lower() == 'charizard':
                    final_display = []
                    for value in your_dict.values():
                        pokemon_dict = {}
                        pokemon_name = value['forms'][0]['name']
                        pokemon_dict[pokemon_name] = {
                            'Ability' : value['abilities'][0]['ability']['name'],
                            'Base_experience' : value['base_experience'],
                            'Sprite' : value['sprites']['front_shiny'],
                            'Attack base_stat' : value['stats'][1]['base_stat'],
                            'hp base_stat' : value['stats'][0]['base_stat'],
                            'Defense base_stat': value['stats'][2]['base_stat']
                        }
                        final_display.append(pokemon_dict)
                    return final_display[5]
                else:
                    return 'The pokemon you summoned is not yet available. Please refresh the page and try again.'

            return pokemon_attributes(working_dict)
            # api code end   
    return render_template('your_pokemon.html', pokeform=pokeform)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.signin'))