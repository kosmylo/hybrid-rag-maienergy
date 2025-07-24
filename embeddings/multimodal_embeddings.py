from transformers import CLIPProcessor, CLIPModel
import torch
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()
CLIP_MODEL_NAME = os.getenv("CLIP_MODEL_NAME")

device = "cuda" if torch.cuda.is_available() else "cpu"
clip_model = CLIPModel.from_pretrained(CLIP_MODEL_NAME).to(device)
clip_processor = CLIPProcessor.from_pretrained(CLIP_MODEL_NAME)

def embed_text_clip(text):
    inputs = clip_processor(text=[text], return_tensors="pt", padding=True).to(device)
    with torch.no_grad():
        embedding = clip_model.get_text_features(**inputs).cpu().numpy()[0]
    return (embedding / np.linalg.norm(embedding)).tolist()