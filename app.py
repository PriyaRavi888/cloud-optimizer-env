from fastapi import FastAPI
import sys
import os

sys.path.append(os.path.abspath("."))

from env.environment import CloudEnv

app = FastAPI()
env = CloudEnv()

@app.post("/reset")
def reset():
    state = env.reset()
    return {"status": "ok", "state": state}

@app.get("/")
def root():
    return {"message": "running"}