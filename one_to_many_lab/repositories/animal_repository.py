from db.run_sql import run_sql
from models.owner import Owner
from models.animal import Animal
import repositories.owner_repository as owner_repository

def save(animal):
    sql = "INSERT INTO animals (name, age, breed, owner_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [animal.name, animal.age, animal.breed, animal.owner.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    animal.id = id
    return animal

def select_all():
    animals = []
    sql = "SELECT * FROM animals"
    results = run_sql(sql)
    for row in results:
        owner = owner_repository.select(row['owner_id'])
        animal = Animal(row['name'], row['age'], row['breed'], owner, row['id'])
        animals.append(animal)
    return animals

def delete(id):
    sql = "DELETE FROM animals WHERE id = %s"
    values = [id]
    run_sql(sql, values)