from fastapi import FastAPI, UploadFile, File
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

app = FastAPI(title="Rice Prediction Service")

model = load_model("models/modele_final.keras")  


CLASSES = ["Arborio", "Basmati", "Ipsala", "Jasmine", "Karacadag"]

@app.get("/health")
def health():
    return {"status": "UP"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    img = Image.open(io.BytesIO(contents)).convert("RGB")
    img = img.resize((224, 224))

    x = np.array(img) / 255.0
    x = np.expand_dims(x, axis=0)

    preds = model.predict(x)
    idx = int(np.argmax(preds[0]))

    return {
        "class": CLASSES[idx],
        "confidence": float(preds[0][idx]),
        "probabilities": {
            CLASSES[i]: float(preds[0][i]) for i in range(len(CLASSES))
        }
    }
