from fastapi import FastAPI
from env.environment import CloudEnv

app = FastAPI()
env = CloudEnv()

@app.post("/reset")
def reset():
    return {"state": env.reset()}

@app.post("/step")
def step(action: str):
    state, reward, done, _ = env.step(action)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }

@app.get("/")
def home():
    return {"message": "running"}