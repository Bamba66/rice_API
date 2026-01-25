🎯 1. Présentation du projet

Ce projet a pour objectif de :

.Entraîner un modèle de classification d’images (ex : ResNet50)

.Sauvegarder le modèle entraîné

.Recharger le modèle depuis un fichier .keras

.Créer une API FastAPI pour effectuer des prédictions
.Créer une interface Streamlit pour tester le modèle facilement

.Vérifier que l’accuracy reste identique après rechargement

🧠 2. Technologies utilisées

.Python 3.10

.TensorFlow / Keras

.FastAPI

.Uvicorn

.Streamlit

.Docker

.Render (déploiement)

.GitHub (gestion de code)

📁 3. Structure du projet
rice_API/
│
├─ prediction_service/
│   ├─ main.py
│   ├─ model/
│   │   ├─ model_final.keras
│   │   
│   ├─ requirements.txt
│   └─ Dockerfile
├─ ui_service/
│   ├─ app.py  
│   ├─ requirements.txt
│   └─ Dockerfile
├─ Dockerfile
├─ README.md
├─ docker-compose.yml
└─ .gitignore

⚙️ 4. Installation locale
✅ Prérequis

Python 3.10 ou supérieur

Git

Docker (optionnel)

4.1 Cloner le repo
git clone https://github.com/Bamba66/rice_API.git
cd rice_API

4.2 Installer les dépendances
pip install -r prediction_service/requirements.txt

5. Dockerisation
Dockerfile (correct pour Render)
FROM python:3.10-slim

WORKDIR /app

COPY prediction_service/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "prediction_service.app:app", "--host", "0.0.0.0", "--port", "8000"]

🚀 6. Déploiement sur Render

Pour déployer :

Connecter ton repo GitHub à Render

Créer un Web Service

Choisir Docker comme environnement

Indiquer :

Build Command : docker build -t rice_api .

Start Command : uvicorn prediction_service.app:app --host 0.0.0.0 --port 8000

Si Render ne trouve pas requirements.txt, définir :

Root Directory : prediction_service

7-Démarrer l’API FastAPI
uvicorn main:app --host 0.0.0.0 --port 8000

8-Démarrer Streamlit
streamlit run app.py

8. Tests API
8.1 Test avec curl
curl -X POST "http://localhost:8000/predict" \
  -F "file=@/path/to/image.jpg"

8.2 Test via Swagger

Ouvre :

http://localhost:8000/docs
