from fastapi import FastAPI, Form
from src.gemini import google_genai_client
import time

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
def ask_ai(question: str = Form(...)):
    print(f"Got a query: {question}")
    start = time.perf_counter()
    response = google_genai_client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=question
    )
    #to be used with StreamingResponse class of FastAPI
    r'''
    for chunk in response:
        if chunk.text:
            yield chunk.text
    '''
    time_taken = time.perf_counter() - start
    print(f"time taken in Gemini API call: {time_taken:0.2f}s")
    print(f"Sending response: {response.text}")
    return {"response": response.text}
