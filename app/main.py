from fastapi import FastAPI

app = FastAPI(title="Student API")

@app.get("/")
def home():
    return {
        "Message": "Welcome to Student API"
    }