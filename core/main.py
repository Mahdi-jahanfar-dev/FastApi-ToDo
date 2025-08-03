from fastapi import FastAPI
from .config import settings

app = FastAPI()


@app.get('/')
def main():
    return settings.test