import random

class CloudEnv:
    def __init__(self):
        self.state = None
        self.steps = 0
        self.max_steps = 10
        self.traffic = 0

    def reset(self):
        self.traffic = random.randint(100, 500)
        self.state = {
            "cpu_usage": random.randint(50, 90),
            "instances": random.randint(2, 6),
            "response_time": random.randint(200, 500),
            "cost": random.randint(1000, 2000),
            "traffic": self.traffic
        }
        self.steps = 0
        return self.state

    def step(self, action):
        self.steps += 1

        # Traffic changes
        self.traffic += random.randint(-50, 100)

        # Update CPU
        self.state["cpu_usage"] = min(100, self.traffic // self.state["instances"])

        reward = 0

        if action == "scale_up":
            self.state["instances"] += 1
            self.state["cost"] += 200

        elif action == "scale_down" and self.state["instances"] > 1:
            self.state["instances"] -= 1
            self.state["cost"] -= 200

        elif action == "do_nothing":
            reward -= 0.2

        # Response time logic
        if self.state["cpu_usage"] > 80:
            self.state["response_time"] += 50
        else:
            self.state["response_time"] -= 30

        # Reward logic
        if self.state["cpu_usage"] < 70:
            reward += 0.5

        if self.state["cost"] < 1500:
            reward += 0.5

        if self.state["response_time"] > 400:
            reward -= 1

        if self.state["instances"] <= 0:
            reward -= 2

        self.state["traffic"] = self.traffic

        done = self.steps >= self.max_steps

        return self.state, reward, done, {}