import sys
import os

sys.path.append(os.path.abspath("."))
from fastapi import FastAPI
from env.environment import CloudEnv

app = FastAPI()

env = CloudEnv()

@app.post("/reset")
def reset():
    state = env.reset()
    return {"status": "reset successful", "state": state}


@app.get("/")
def root():
    return {"message": "Cloud Optimizer Environment Running"}