import random
from env.environment import CloudEnv
from env.graders import grade_easy, grade_medium, grade_hard

TASK_NAME = "cloud-optimization"
BENCHMARK = "openenv"
MODEL_NAME = "rule-based-agent"

MAX_STEPS = 10


def log_start():
    print(f"[START] task={TASK_NAME} env={BENCHMARK} model={MODEL_NAME}", flush=True)


def log_step(step, action, reward, done):
    print(
        f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error=null",
        flush=True,
    )


def log_end(success, steps, rewards):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(f"[END] success={str(success).lower()} steps={steps} rewards={rewards_str}", flush=True)


def choose_action(state):
    cpu = state["cpu_usage"]
    cost = state["cost"]
    response = state["response_time"]
    traffic = state["traffic"]
    instances = state["instances"]

    # 🔥 Smart cloud logic

    # If system overloaded → scale up
    if cpu > 85 or response > 450:
        return "scale_up"

    # If underutilized → scale down
    if cpu < 40 and instances > 1:
        return "scale_down"

    # If cost too high → reduce instances carefully
    if cost > 1600 and instances > 1:
        return "scale_down"

    # If traffic suddenly increases → scale up
    if traffic > 400:
        return "scale_up"

    return "do_nothing"

def main():
    env = CloudEnv()
    rewards = []

    log_start()

    state = env.reset()

    success = False

    for step in range(1, MAX_STEPS + 1):
        action = choose_action(state)

        state, reward, done, _ = env.step(action)

        rewards.append(reward)

        log_step(step, action, reward, done)

        if done:
            break

    # Final grading (use medium as main)
    score = grade_medium(state)
    success = score > 0.5

    log_end(success, step, rewards)


if __name__ == "__main__":
    main()