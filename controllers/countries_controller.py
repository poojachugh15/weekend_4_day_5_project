from flask import Flask, render_template, Blueprint, request, redirect

from models.country import Country
import repositories.country_repository as country_repository

country_blueprint = Blueprint("countries", __name__)

# INDEX
@country_blueprint.route('/')
def index():
    return render_template('index.html')

@country_blueprint.route('/countries', methods=['GET'])
def all_countries():
    all_countries = country_repository.select_all()
    return render_template('/countries/index.html', all_countries=all_countries)

# NEW
@country_blueprint.route('/countries/new', methods=['GET'])
def new_country():
    return render_template('/countries/new.html')

# create
@country_blueprint.route('/countries', methods=['POST'])
def create_country():
    new_country = request.form['name']
    country = Country(new_country)
    country_repository.save(country)
    return redirect('/countries')

# SHOW
@country_blueprint.route('/countries/<id>', methods=['GET'])
def show_country(id):
    country = country_repository.select(id)
    return render_template('/countries/show.html', country=country)


# EDIT
@country_blueprint.route('/countries/<id>/edit', methods=['GET'])
def edit_country(id):
    country = country_repository.select(id)
    return render_template('/countries/edit.html', country=country)