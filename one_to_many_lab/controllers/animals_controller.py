from flask import Flask, render_template, request, redirect
from models.animal import Animal 

from flask import Blueprint

from repositories import animal_repository, owner_repository

animals_blueprint = Blueprint("animals", __name__)

@animals_blueprint.route("/animals")
def animals():
    animals = animal_repository.select_all()
    return render_template("animals/index.html", all_animals=animals)

@animals_blueprint.route("/animals/<id>/delete", methods=["POST"])
def delete(id):
    animal_repository.delete(id)
    return redirect("/animals")