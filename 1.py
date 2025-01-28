from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import os
import json

app = FastAPI()

@app.get("/")
def read_root():
    



site = BeautifulSoup(r1.text, "html.parser")
#print(site.prettify())


b2 = site.find("title")
print(b2)

