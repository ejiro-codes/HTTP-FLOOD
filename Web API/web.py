from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import re

app = FastAPI()
app.mount('/static', StaticFiles(directory='static', html=True), name='static')