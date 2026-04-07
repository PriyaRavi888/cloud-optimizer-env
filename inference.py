class CloudOptimizerEnv:
    def __init__(self):
        self.step_count = 0
        self.rewards = []

    def reset(self):
        self.step_count = 0
        self.rewards = []

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

        return reward, done


def main():
    env = CloudOptimizerEnv()

    print("[START] task=cloud-optimization env=openenv model=rule-based-agent", flush=True)

    env.reset()

    rewards = []

    for step in range(1, 11):
        action = "scale_up"

        reward, done = env.step(action)
        rewards.append(reward)

        print(
            f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error=null",
            flush=True
        )

        if done:
            break

    success = False
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)

    print(
        f"[END] success={str(success).lower()} steps={len(rewards)} rewards={rewards_str}",
        flush=True
    )


if __name__ == "__main__":
    main()
