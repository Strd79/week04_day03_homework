from db.run_sql import run_sql
from models.owner import Owner
from models.animal import Animal

def save(owner):
    sql = "INSERT INTO owners (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [owner.first_name, owner.last_name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    owner.id = id
    return owner

def select(id):
    owner = None 
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        owner = Owner(result['first_name'], result['last_name'], result['id'])
    return owner