from env.environment import CloudEnv

env = CloudEnv()

state = env.reset()
print("Initial State:", state)

for i in range(5):
    action = "scale_down"
    state, reward, done, _ = env.step(action)
    print("Step:", i+1)
    print("State:", state)
    print("Reward:", reward)
    print("Done:", done)

from env.graders import grade_easy, grade_medium, grade_hard

print("\n--- FINAL SCORES ---")
print("Easy:", grade_easy(state))
print("Medium:", grade_medium(state))
print("Hard:", grade_hard(state))