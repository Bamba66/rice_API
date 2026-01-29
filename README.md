# Classification de types de riz - Projet Analyses de Données Massives

## 1. Présentation du projet

Ce projet a pour objectif de :

- Entraîner un modèle de classification d'images de riz (MobileNetV2)
- Sauvegarder le modèle entraîné
- Recharger le modèle depuis un fichier `.keras`
- Créer une API FastAPI pour effectuer des prédictions
- Créer une interface Streamlit pour tester le modèle facilement
- Vérifier que l'accuracy reste identique après rechargement
- Déployer le système complet sur Render

---

## 2. Technologies utilisées

- Python 3.10
- TensorFlow / Keras
- FastAPI
- Uvicorn
- Streamlit
- Docker
- Render (déploiement)
- GitHub (gestion de code)

---

##  3. Structure du projet

```
rice_API/
│
├── prediction_service/
│   ├── main.py
│   ├── models/
│   │   └── modele_final.keras
│   ├── requirements.txt
│   └── Dockerfile
│
├── ui_service/
│   ├── app.py  
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml
├── README.md
├── modèle_riz(1).ipynb
├── validation_externe.ipynb
└── .gitignore
```

---

##  4. Installation locale

###  Prérequis

- Python 3.10 ou supérieur
- Git
- Docker (optionnel)

### 4.1 Cloner le repo

```bash
git clone https://github.com/Bamba66/rice_API.git
cd rice_API
```

### 4.2 Installer les dépendances

```bash
pip install -r prediction_service/requirements.txt
pip install -r ui_service/requirements.txt
```

---

## 5. Démarrage des services

### 5.1 Démarrer l'API FastAPI

```bash
cd prediction_service
uvicorn main:app --host 0.0.0.0 --port 8000
```

 **Documentation API** : http://localhost:8000/docs

### 5.2 Démarrer Streamlit

```bash
cd ui_service
streamlit run app.py
```

**Interface web** : http://localhost:8501

---

## 6. Dockerisation

### Lancer avec Docker Compose (recommandé)

```bash
docker-compose up --build
```

Cette commande lance automatiquement :
- L'API sur le port 8000
- Streamlit sur le port 8501

---

## 7. Déploiement sur Render

### Pour déployer :

1. Connecter le repo GitHub à Render
2. Créer un **Web Service**
3. Choisir **Docker** comme environnement
4. Configuration automatique via les Dockerfiles

**URLs de production :**
- API : https://rice-api-prediction-mqbf.onrender.com
- UI : https://rice-ui-classification.onrender.com

---

## 8. Tests API

### 8.1 Test avec curl

```bash
curl -X POST "http://localhost:8000/predict" \
  -F "file=@/path/to/image.jpg"
```

### 8.2 Test avec Swagger UI

Ouvre dans ton navigateur :
- Local : http://localhost:8000/docs
- Production : https://rice-api-prediction-mqbf.onrender.com/docs

---

## 9. Résultats du modèle

- **Modèle** : MobileNetV2 (Transfer Learning)
- **Accuracy interne** : 100% sur le jeu de test
- **Validation externe** : Testé sur 75 000 images Kaggle
- **Classes** : Arborio, Basmati, Ipsala, Jasmine, Karacadag

---

## Auteurs

**Groupe B - Master 2 Génie Logiciel**
- Cheikhouna GUEYE
- Fatou FALL
- Sophie FALL

**Encadré par** : Pr. Cheikh SARR  
Université Iba Der Thiam de Thiès - 2025/2026