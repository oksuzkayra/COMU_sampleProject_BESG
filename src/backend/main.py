from fastapi import FastAPI
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware
import re


client = MongoClient("mongodb://root:toor@mongodb:27017")
db = client["search_db"]
collection = db["datas"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search/{search_text}")
def read_root(search_text):
    
    regex_pattern = re.compile(f"{search_text}", re.IGNORECASE)

    mongo_query = {
        "$or": [
            {"Attack Signature": regex_pattern},
            {"Protocol": regex_pattern},
            {"Action Taken": regex_pattern},
            {"Packet Type": regex_pattern},
            {"Source IP Address": regex_pattern},
            {"Destination IP Address": regex_pattern},
            {"Alerts/Warnings": regex_pattern},
            {"Traffic Type": regex_pattern},
            {"Severity Level": regex_pattern},
            {"Payload Data": regex_pattern},
            {"Attack Type": regex_pattern},
            {"Timestamp": regex_pattern},
            {"User Information": regex_pattern},
            {"Device Information": regex_pattern},
            {"Geo-location Data": regex_pattern},
            {"Firewall Logs": regex_pattern},
            {"Log Source": regex_pattern},
            {"Network Segment": regex_pattern},
        ]
    }
    
    # MongoDB sorgusunu çalıştır
    result = list(collection.find(mongo_query))
    result_list = []
    for i in result:
        i["_id"] = None
        result_list.append(i)
    return result_list
    
