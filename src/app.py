from fastapi import FastAPI
from src.gemini import google_genai_client

app = FastAPI()

@app.get("/")
def home():
    #dummy root, will remove after rest of the app is done
    return {"message": "Hello Universe!"}

@app.get("/models")
def get_models():
    model_list = []
    for m in google_genai_client.models.list():
        for action in m.supported_actions:
            if action == "generateContent":
                model_list.append(m.name)
    
    print(m.name)
    #response = google_genai_client.models.generate_content(
    #    model="gemini-3-flash-preview",
    #    contents="list down Google Gemini availabel models"
    #)
    return {"response":  model_list}

@app.post("/ask")
def ask_ai():
    pass