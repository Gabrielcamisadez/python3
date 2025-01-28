from fastapi import FastAPI 
import pandas as pd
from flask import jsonify
import uvicorn


app = FastAPI()

names = pd.read_csv('password_wordlist.txt')



@app.get("/")
def read_root():
    js = names.to_json()
    return js

@app.get("/ips")
def get_ip():
    tojson = names.to_dict()
    return tojson
def read_ips():
    return(jsonify(get_ip()))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
