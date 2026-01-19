from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import Response
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter, Histogram, generate_latest
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
from PIL import Image
import io
import time

app = FastAPI(title="Leaf Disease Classification API")

# Instrumenter avec Prometheus
Instrumentator().instrument(app).expose(app)

# Métriques Prometheus personnalisées
prediction_counter = Counter('predictions_total', 'Total number of predictions')
inference_time = Histogram('inference_latency_seconds', 'Inference latency in seconds')
confidence_metric = Histogram('prediction_confidence', 'Prediction confidence scores')

# Chemin du modèle
MODEL_PATH = "model/plant_disease_model.h5"

# Charger le modèle
try:
    model = load_model(MODEL_PATH)
    model_loaded = True
except Exception as e:
    print(f"Error loading model: {e}")
    model = None
    model_loaded = False

# Classes de maladies (à adapter selon votre dataset)
CLASS_NAMES = [
    "healthy",
    "powdery",
    "rust"
]

# Prétraitement
def preprocess_image(image: Image.Image, target_size=(224, 224)):
    image = image.resize(target_size)
    image = img_to_array(image)
    image = image.astype("float32") / 255.0
    image = np.expand_dims(image, axis=0)
    return image

@app.get("/")
async def root():
    return {"message": "Leaf Disease Classification API", "status": "running"}

@app.get("/health")
async def health():
    return {"status": "healthy", "model_loaded": model_loaded}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if not model_loaded:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    start_time = time.time()
    
    try:
        # Lire et prétraiter l'image
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        image_tensor = preprocess_image(image)
        
        # Prédiction
        preds = model.predict(image_tensor)
        predicted_index = np.argmax(preds, axis=1)[0]
        confidence_score = float(np.max(preds))
        predicted_class = CLASS_NAMES[predicted_index]
        
        # Enregistrer les métriques
        latency = time.time() - start_time
        prediction_counter.inc()
        inference_time.observe(latency)
        confidence_metric.observe(confidence_score)
        
        return {
            "class": predicted_class,
            "confidence": round(confidence_score, 4),
            "inference_time_ms": round(latency * 1000, 2)
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")