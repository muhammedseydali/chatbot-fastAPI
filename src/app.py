from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI(
    title = "Chatbot API",
    description="a simple chatbot",
    version="0.1"
)


@app.post("/chat", description="chat with RAG Api WITH THIS ENDPOINT")
def chat(message:str):
    return JSONResponse(content={"message": message}, status_code=200)