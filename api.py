from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# Quelques données test pour commencer
employees = [
    {"id": 0, "Nom": "Bastonia Light", "Metier": "Catcheuse"},
    {"id": 1, "Nom": "Johnno", "Metier": "Sosie de Elvis Presley"},
    {"id": 2, "Nom": "Brutallax", "Metier": "Empereur du mal"}
]

# Template HTML pour la liste des utilisateurs
html_index = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Liste des Utilisateurs</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { color: #333; }
        table { width: 100%; border-collapse: collapse; }
        th, td { padding: 10px; text-align: left; }
        th { background-color: #f4f4f4; }
        td { border-bottom: 1px solid #ddd; }
        button { padding: 10px 20px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }
        button:hover { background-color: #45a049; }
        a { text-decoration: none; color: #007BFF; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>Liste des Utilisateurs</h1>

    <table border="1">
        <thead>
            <tr>
                <th>ID</th>
                <th>Nom</th>
                <th>Métier</th>
            </tr>
        </thead>
        <tbody>
            {% for user in employees %}
            <tr>
                <td>{{ user.id }}</td>
                <td>{{ user.Nom }}</td>
                <td>{{ user.Metier }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>

    <p><a href="{{ url_for('add_user') }}">Ajouter un nouvel utilisateur</a></p>
</body>
</html>
"""

# Template HTML pour le formulaire d'ajout d'utilisateur
html_add_user = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ajouter un Utilisateur</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { color: #333; }
        form { margin-top: 20px; }
        label { display: inline-block; width: 100px; }
        input { margin-bottom: 10px; padding: 5px; }
        button { padding: 10px 20px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }
        button:hover { background-color: #45a049; }
        a { text-decoration: none; color: #007BFF; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>Ajouter un Utilisateur</h1>

    <form action="/add_user" method="POST">
        <label for="nom">Nom :</label>
        <input type="text" id="nom" name="nom" required>
        <br>
        <label for="metier">Métier :</label>
        <input type="text" id="metier" name="metier" required>
        <br><br>
        <button type="submit">Ajouter</button>
    </form>

    <p><a href="{{ url_for('index') }}">Retour à la liste des utilisateurs</a></p>
</body>
</html>
"""


# Page d'accueil - liste des utilisateurs
@app.route('/')
def index():
    return render_template_string(html_index, employees=employees)


# Page pour ajouter un utilisateur
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        nom = request.form['nom']
        metier = request.form['metier']

        # Générer un nouvel ID
        new_id = employees[-1]['id'] + 1 if employees else 0

        # Créer un nouvel utilisateur
        new_user = {"id": new_id, "Nom": nom, "Metier": metier}

        # Ajouter l'utilisateur à la liste
        employees.append(new_user)

        # Rediriger vers la page d'accueil pour voir la liste mise à jour
        return redirect(url_for('index'))

    # Si c'est une requête GET, afficher le formulaire
    return render_template_string(html_add_user)


# Lancement de l'application Flask
if __name__ == '__main__':
    app.run(debug=True)

# Test