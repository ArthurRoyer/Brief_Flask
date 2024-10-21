
# Brief_Flask - Gestion d'Utilisateurs avec Flask

Ce projet est une application web simple développée avec Flask. Il permet de gérer des utilisateurs via une interface graphique. Vous pouvez lister les utilisateurs existants et ajouter de nouveaux utilisateurs via un formulaire.

## Fonctionnalités

- Afficher la liste des utilisateurs
- Ajouter un nouvel utilisateur via un formulaire HTML

## Prérequis

Avant d'exécuter ce projet, assurez-vous d'avoir installé les éléments suivants :

- Python 3.x
- `pip` (gestionnaire de paquets Python)
- Un environnement virtuel Python (recommandé)

## Installation

1. Clonez ce dépôt sur votre machine locale :

   ```bash
   git clone https://github.com/ArthurRoyer/Brief_Flask.git
   ```

2. Accédez au répertoire du projet :

   ```bash
   cd Brief_Flask
   ```

3. Créez un environnement virtuel (optionnel mais recommandé) :

   ```bash
   python -m venv venv
   ```

4. Activez l'environnement virtuel :

   - Sur **Windows** :

     ```bash
     venv\Scripts\activate
     ```

   - Sur **Linux/Mac** :

     ```bash
     source venv/bin/activate
     ```

5. Installez les dépendances requises :

   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. Lancez l'application Flask :

   ```bash
   python app.py
   ```

2. Accédez à l'application dans votre navigateur en visitant `http://127.0.0.1:5000/` ou `http://localhost:5000/`.

### Routes

- **Page d'accueil** (Liste des utilisateurs) : `http://127.0.0.1:5000/`
  
  Cette page affiche une liste de tous les utilisateurs existants. Un lien est fourni pour ajouter un nouvel utilisateur.

- **Formulaire d'ajout d'utilisateur** : `http://127.0.0.1:5000/add_user`

  Utilisez cette page pour ajouter un nouvel utilisateur via un formulaire. Une fois soumis, l'utilisateur sera ajouté à la liste existante.

## Structure du projet

```
Brief_Flask/
│
├── app.py                  # Fichier principal de l'application Flask
├── requirements.txt        # Fichier listant les dépendances du projet
└── README.md               # Documentation du projet (ce fichier)
```



## Auteurs

- **Arthur Royer** - Créateur du projet
