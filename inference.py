# -------------------------------
# CLOUD OPTIMIZATION ENV LOGIC
# -------------------------------

class CloudOptimizerEnv:
    def __init__(self):
        self.step_count = 0
        self.rewards = []

    def reset(self):
        self.step_count = 0
        self.rewards = []
        return {"status": "reset"}

    def step(self, action="scale_up"):
        self.step_count += 1

        reward = -1.0
        done = False

        if self.step_count == 1:
            reward = 0.0
        if self.step_count == 3:
            reward = -0.5
        if self.step_count >= 10:
            done = True

        self.rewards.append(reward)

        return {
            "step": self.step_count,
            "action": action,
            "reward": reward,
            "done": done
        }

    def run_episode(self):
        self.reset()
        results = []

        while True:
            res = self.step()
            results.append(res)
            if res["done"]:
                break

        return {
            "success": False,
            "steps": len(results),
            "rewards": self.rewards
        }
