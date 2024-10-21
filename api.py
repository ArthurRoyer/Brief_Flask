# Import de bibliothèques
import flask
from flask import request, jsonify

# Création de l'objet Flask
app = flask.Flask(__name__)

# Lancement du Débogueur
app.config["DEBUG"] = True

# Quelques données tests pour l’annuaire sous la forme d’une liste de dictionnaires
employees = [
   {"id": 0, "Nom": "Bastonia Light", "Metier": "Catcheuse"},
   {"id": 1, "Nom": "Johnno", "Metier": "Sosie de Elvis Presley"},
   {"id": 2, "Nom": "Brutallax", "Metier": "Empereur du mal"}
]

# Route principale
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Salut les kool kyds !</h1>
<p>Boum on test une API car on apprend !</p>'''

# Route pour récupérer tous les utilisateurs
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(employees)

# Route pour ajouter un utilisateur
@app.route('/users', methods=['POST'])
def add_user():
    # Récupérer les données de la requête POST
    new_user = request.get_json()

    # Générer un nouvel ID
    new_user['id'] = employees[-1]['id'] + 1 if employees else 0

    # Ajouter le nouvel utilisateur à la liste
    employees.append(new_user)

    # Retourner la nouvelle liste d'utilisateurs
    return jsonify(employees), 201

# Lancement de l'application Flask
if __name__ == '__main__':
    app.run()
