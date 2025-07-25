import torch
import numpy as np
from transformers import CLIPProcessor, CLIPModel
import os
from dotenv import load_dotenv

load_dotenv()

device = "cuda" if torch.cuda.is_available() else "cpu"
model_name = os.getenv("CLIP_MODEL_NAME")

clip_model = CLIPModel.from_pretrained(model_name).to(device)
clip_processor = CLIPProcessor.from_pretrained(model_name)

def embed_text_clip(text):
    inputs = clip_processor(text=[text], return_tensors="pt", padding=True).to(device)
    with torch.no_grad():
        embedding = clip_model.get_text_features(**inputs).cpu().numpy()[0]
    embedding = embedding / np.linalg.norm(embedding)
    return embedding.tolist()