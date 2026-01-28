Classification de type de riz – Deep Learning Project
1. Objectif du projet

Ce projet vise à concevoir, entraîner, valider et déployer un système complet de classification automatique des variétés de riz à partir d’images, en utilisant des techniques de Deep Learning et une approche MLOps.

Le projet est structuré de manière à permettre à toute personne externe  de :

comprendre la démarche,

exécuter le code,

tester le modèle,

reproduire l’ensemble de la chaîne, sans connaissance préalable du projet.

2. Vue globale de la démarche 

Le projet suit toutes les étapes suivantes :

Prétraitement des images de grains de riz

Entraînement d’un modèle CNN avec Transfer Learning

Évaluation sur un jeu de test interne

Validation externe sur un dataset public (Kaggle)

Sauvegarde des modèles entraînés

Déploiement du modèle via une API FastAPI

Utilisation du modèle via une interface Streamlit

Conteneurisation et reproductibilité avec Docker

 Toutes ces étapes sont implémentées dans le dépôt.

3. Données utilisées
3.1 Dataset principal (interne)

Images de grains de riz

5 variétés

Utilisé pour :

entraînement

validation interne

test interne

3.2 Dataset de validation externe

Dataset public extrait de Kaggle (≈ 75 000 images)

Utilisé uniquement pour :

tester la capacité de généralisation

comparer les matrices de confusion

Aucun ré-entraînement sur ce dataset

 Cela permet de démontrer que le modèle ne surapprend pas.

4. Modèles de Deep Learning utilisés
4.1 Modèle principal : model_riz

Architecture : MobileNetV2

Approche : Transfer Learning

Pré-entraîné sur : ImageNet

Entraîné sur : dataset interne

Utilisé pour :

l’API FastAPI

l’interface Streamlit

Fichier :

prediction_service/model/modele_finale.keras

4.2 Modèle de validation externe

Même architecture (MobileNetV2)

Évalué sur le dataset Kaggle

Utilisé pour :

comparaison des performances

validation scientifique

Non exposé via l’API

Le modèle utilisé en production est uniquement model_riz.

5. Technologies utilisées

Python 3.10

TensorFlow / Keras

FastAPI

Uvicorn

Streamlit

Docker & Docker Compose

GitHub

Render (déploiement cloud)

6. Structure du projet
rice_API/
│
├── prediction_service/          # Service de prédiction (API)
│   ├── main.py                  # API FastAPI
│   ├── model/
│   │   ├── modele_final.keras      # Modèle principal (production)
│   │   └── model_validation.keras (optionnel)
│   ├── requirements.txt
│   └── Dockerfile
│
├── ui_service/                  # Interface utilisateur
│   ├── app.py                   # Streamlit
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml           # Lancement complet
├── README.md
├── model_riz(1).ipynb
├── validation_externe.ipy
└── .gitignore

7. Étapes pour exécuter le projet (pas à pas)
Étape 1 – Cloner le projet
git clone https://github.com/Bamba66/rice_API.git
cd rice_API

Étape 2 – Installer les dépendances (sans Docker)
pip install -r prediction_service/requirements.txt
pip install -r ui_service/requirements.txt

Étape 3 – Lancer l’API FastAPI
cd prediction_service
uvicorn main:app --host 0.0.0.0 --port 8000


Documentation automatique :

http://localhost:8000/docs

Étape 4 – Lancer l’interface Streamlit
cd ui_service
streamlit run app.py


Interface accessible dans le navigateur :

http://localhost:8501

8. Utilisation de l’application

L’utilisateur charge une image de grain de riz

L’image est envoyée à l’API FastAPI

Le modèle model_riz effectue la prédiction

La variété prédite et le score sont affichés

9. Lancer tout le projet avec Docker (recommandé)
docker-compose up --build


Cette commande :

lance l’API

lance Streamlit

garantit la reproductibilité totale

10. Tests de l’API
Test avec curl
curl -X POST "https://rice-fastapi-prediction.onrender.com/predict" \
  -F "file=@image.jpg"

Test via Swagger
https://rice-fastapi-prediction.onrender.com/docs