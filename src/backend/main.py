from fastapi import FastAPI

app = FastAPI()

@app.get("/search/{search_text}")
def read_root(search_text):
    return {"message": f"Hello, FastAPI!{search_text}"}

@app.post("/search")
def create_item(search_text):
    return {"search_text_value": search_text}