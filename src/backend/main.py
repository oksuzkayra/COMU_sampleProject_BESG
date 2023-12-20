from fastapi import FastAPI
from pymongo import MongoClient

client = MongoClient("mongodb://root:toor@mongodb:27017")
db = client["search_db"]
collection = db["datas"]

app = FastAPI()

@app.get("/search/{search_text}")
def read_root(search_text):
    result = collection.find({"Traffic Type": f"{search_text}"})
    result_list = []
    for i in result:
        i["_id"] = None
        result_list.append(i)
    return result_list
    
#@app.post("/search")
#def create_item(body:dict):
#    return {"search_text_value": body["search_text"]}