from fastapi import FastAPI 
import pandas as pd
from flask import jsonify


app = FastAPI()

domains = pd.read_excel("domains.xlsx")



@app.get("/")
def read_root():
    js = domains.to_json()
    return js

@app.get("/ips")
def get_ip():
    tojson = domains.to_dict()
    return tojson
def read_ips():
    return(jsonify(get_ip()))

