# 📚 Plateforme de Traduction IA - TalAIt Translator

Bienvenue dans le dépôt de la **Plateforme de Traduction Fullstack TalAIt**.

Ce projet est une application web moderne utilisant l'IA pour la traduction. Elle est construite sur une architecture sécurisée utilisant Python (FastAPI) pour le Backend et Next.js (App Router) pour le Frontend, le tout conteneurisé avec Docker Compose.

## 🚀 Technologies Utilisées

| Service | Technologie | Rôle Principal |
| :--- | :--- | :--- |
| **Backend (API)** | **Python (FastAPI)** | Authentification (JWT), Gestion des utilisateurs, Logique de traduction (simulée). |
| **Frontend (UI)** | **Next.js 14+** | Interface utilisateur, Routage App Router, Rendu SSR/CSR. |
| **Styling** | **Tailwind CSS** | Design professionnel Dark Mode (Rouge/Gris). |
| **Conteneurisation**| **Docker Compose** | Orchestration des deux services. |

---

## 🛠️ Configuration et Lancement

### Prérequis

1. **Docker** et **Docker Compose** installés.

### Étapes de Lancement

1. **Cloner le dépôt :**
    ```bash
    git clone https://github.com/KarimaChami/Plateforme-de-Traduction-Fullstack-backend.git
    cd Plateforme-de-Traduction-Fullstack
    ```

2. **Configuration des Variables d'Environnement :**

    * Créez le fichier **`translation-backend/.env`** (secrets du JWT) :
        ```env
        SECRET_KEY=votre_cle_jwt_tres_longue_et_securisee
        ALGORITHM=HS256
        ACCESS_TOKEN_EXPIRE_MINUTES=30
        ```

3. **Lancer les Services avec Docker Compose :**

    ```bash
    # Construit les images et lance les conteneurs en arrière-plan
    docker-compose up --build -d
    ```

4. **Accès :**

    * **Frontend (UI) :** `http://localhost:3000`
    * **Backend (API Docs) :** `http://localhost:8000/docs`

##

# 🧠 Backend : API de Traduction (FastAPI)

Ce service est le cerveau de la plateforme. Il est construit avec FastAPI pour gérer l'authentification et servir les endpoints de traduction.

## Caractéristiques Techniques

* **Framework :** FastAPI (hautes performances, gestion asynchrone).
* **Authentification :** JWT (JSON Web Tokens) pour sécuriser les routes.
* **BDD :** SQLite (via SQLAlchemy) pour le stockage des utilisateurs.
* **Sécurité :** Hachage des mots de passe avec `bcrypt`.
* **CORS :** Middleware configuré pour autoriser les requêtes depuis le Frontend (Next.js) sur le port 3000.

## 🚪 Endpoints de l'API

Consultez la documentation interactive sur **`http://localhost:8000/docs`** après le lancement.

| Méthode | Route | Rôle | Sécurité |
| :--- | :--- | :--- | :--- |
| `POST` | `/register` | Crée un nouvel utilisateur. | Publique |
| `POST` | `/login` | Authentifie et émet le JWT. | Publique |
| `POST` | `/translate` | Effectue la traduction. | Nécessite JWT |
| `GET` | `/users/me` | Récupère les données de l'utilisateur actuel. | Nécessite JWT |

## 🐍 Développement Local (Sans Docker)

Pour lancer uniquement le Backend :

1. Avoir Python 3.8+ installé.
2. Dans le dossier `translation-backend/`:
    ```bash
    # Installer les dépendances
    pip install -r requirements.txt
    
    # Lancer le serveur (assurez-vous d'avoir configuré le .env)
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
    ```

---