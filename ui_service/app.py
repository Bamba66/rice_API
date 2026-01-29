import streamlit as st
import requests
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from PIL import Image
import io

# -----------------------------
# CONFIGURATION PAGE
# -----------------------------
st.set_page_config(
    page_title="Rice Classifier 🌾",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# STYLE PERSONNALISÉ AVANCÉ
# -----------------------------
st.markdown("""
<style>
    /* Dégradé de fond riz doré/vert */
    .stApp {
        background: linear-gradient(135deg, #FFF8E7 0%, #E8F5E8 50%, #D4E4BC 100%);
    }

    /* Header principal */
    .main-header {
        background: linear-gradient(90deg, #2E7D32, #4CAF50);
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        color: white;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }

    /* Titres */
    h1 {
        color: #2E7D32 !important;
        font-size: 3.5em !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 0.5rem;
    }

    h2 {
        color: #1565C0 !important;
        font-size: 2em !important;
        border-bottom: 3px solid #4CAF50;
        padding-bottom: 0.5rem;
    }

    /* Boutons premium */
    div.stButton > button {
        background: linear-gradient(45deg, #4CAF50, #45A049);
        color: white !important;
        height: 3.5em;
        width: 200px;
        border-radius: 25px;
        border: none;
        font-size: 18px;
        font-weight: bold;
        box-shadow: 0 6px 20px rgba(76, 175, 80, 0.4);
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(76, 175, 80, 0.6);
        background: linear-gradient(45deg, #45A049, #4CAF50);
    }

    /* Upload file amélioré */
    .stFileUploader label {
        font-size: 1.2em;
        color: #2E7D32;
        font-weight: bold;
    }
    .stFileUploader > div > div > div > input {
        background-color: white;
        border: 2px dashed #4CAF50;
        border-radius: 15px;
        padding: 1rem;
    }

    /* Cards de résultats */
    .result-card {
        background: linear-gradient(135deg, white, #F1F8E9);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        border-left: 6px solid #4CAF50;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER PERSONNALISÉ
# -----------------------------
st.markdown("""
<div class="main-header">
    <h1>🌾 Classification de riz</h1>
    <p style="font-size: 1.5em; margin: 0;">Classification automatique des variétés de riz</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# -----------------------------
# URL de l'API
# -----------------------------
#API_URL = "http://localhost:8000/predict"
#API_URL = "http://prediction_service:8000/predict"

API_URL = "https://rice-fastapi-prediction.onrender.com/predict"



# -----------------------------
# COLONNES POUR UPLOAD ET PRÉDICTION
# -----------------------------
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<h2> Upload votre image</h2>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "Choisissez une image de riz (JPG, PNG)", 
        type=["jpg", "png", "jpeg"],
        help="Formats supportés : JPG, PNG, JPEG"
    )

with col2:
    st.markdown('<h2> Prédiction</h2>', unsafe_allow_html=True)

if uploaded_file is not None:
    # Affichage de l'image amélioré
    image = Image.open(uploaded_file)
    st.image(image, caption="Image analysée", use_column_width=True, clamp=True)
    
    # Bouton Predict premium
    if st.button("🔮 **Prédire le type de riz**", type="primary"):
        with st.spinner("Analyse en cours... "):
            files = {"file": uploaded_file.getvalue()}
            try:
                response = requests.post(API_URL, files=files, timeout=30)
                
                if response.status_code == 200:
                    result = response.json()
                    
                    # CARD RÉSULTAT PRINCIPAL
                    st.markdown("""
                    <div class="result-card">
                        <h2>Résultat de la prédiction</h2>
                    """, unsafe_allow_html=True)
                    
                    col_r1, col_r2 = st.columns(2)
                    with col_r1:
                        st.success(f"**{result['class']}**")
                        st.metric("Confiance", f"{result['confidence']:.1%}")
                    
                    with col_r2:
                        # GRAPHIQUE PROBABILITÉS
                        probs = result["probabilities"]
                        fig = go.Figure(data=[
                            go.Bar(
                                x=list(probs.keys()),
                                y=list(probs.values()),
                                marker_color=px.colors.sequential.Viridis,
                                text=[f'{v:.1%}' for v in probs.values()],
                                textposition='auto'
                            )
                        ])
                        fig.update_layout(
                            title="Probabilités par classe",
                            xaxis_title="Types de riz",
                            yaxis_title="Probabilité",
                            showlegend=False,
                            height=400,
                            plot_bgcolor='rgba(0,0,0,0)',
                            paper_bgcolor='rgba(0,0,0,0)'
                        )
                        st.plotly_chart(fig, use_container_width=True)
                    
                    st.markdown("</div>", unsafe_allow_html=True)
                    
                    # Détails des probas en tableau
                    st.markdown("### Détails des probabilités")
                    df_probs = [{"Classe": k, "Probabilité": f"{v:.2%}"} for k, v in probs.items()]
                    st.dataframe(df_probs, use_container_width=True)
                
                else:
                    st.error(f" Erreur API: {response.status_code} - {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Impossible de contacter l'API: {str(e)}")
else:
    st.info(" Upload une image pour commencer la classification !")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p> Projet ADM 2025 - Université de Thiès | Powered by MobileNetV2 Transfer Learning</p>
</div>
""", unsafe_allow_html=True)
