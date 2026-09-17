agent_state = {
"location": "Restaurant",
"reward": 0,
"step_count": 0
}

action_rewards = {
"accept_order": 2,
"navigate_to_customer": 3,
"wait": -1,
"deliver_order": 10,
"return_to_restaurant": 2
}

actions = [
"accept_order",
"navigate_to_customer",
"wait",
"deliver_order",
"return_to_restaurant"
]

print("=" * 50)
print("FOOD DELIVERY RL EPISODE")
print("=" * 50)

for action in actions:
reward = action_rewards[action]

```
agent_state["reward"] += reward
agent_state["step_count"] += 1

if action == "accept_order":
    agent_state["location"] = "Restaurant"
elif action == "navigate_to_customer":
    agent_state["location"] = "Customer Location"
elif action == "wait":
    agent_state["location"] = "Customer Location"
elif action == "deliver_order":
    agent_state["location"] = "Customer Location"
elif action == "return_to_restaurant":
    agent_state["location"] = "Restaurant"

print("\nStep:", agent_state["step_count"])
print("Action:", action)
print("Reward Received:", reward)
print("Running Total Reward:", agent_state["reward"])
print("Current Location:", agent_state["location"])
```

print("\n" + "=" * 50)
print("FINAL EPISODE SUMMARY")
print("=" * 50)
print("Total Reward:", agent_state["reward"])
print("Total Steps:", agent_state["step_count"])
print("Final Location:", agent_state["location"])
print("=" * 50)
