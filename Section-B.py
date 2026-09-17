print("TASK 1: DELIVERY REWARD FUNCTION")
print("-" * 50)

def calculate_reward(delivery_time, is_on_time, customer_rating):
    reward = 0
    if is_on_time:
        reward += 10
    else:
        reward -= 5
    reward += customer_rating
    return reward

reward1 = calculate_reward(25, True, 5)
reward2 = calculate_reward(45, False, 3)
reward3 = calculate_reward(30, True, 4)

print("Delivery Time: 25 minutes, On Time: True, Rating: 5")
print("Final Reward:", reward1)

print("Delivery Time: 45 minutes, On Time: False, Rating: 3")
print("Final Reward:", reward2)

print("Delivery Time: 30 minutes, On Time: True, Rating: 4")
print("Final Reward:", reward3)

print("\nTASK 2: AGENT STATE TRACKER")
print("-" * 50)

state = {
"location": "Restaurant",
"orders_delivered": 0,
"total_reward": 0.0,
"is_available": True
}

def update_state(state, new_location, reward_earned):
    state["location"] = new_location
    state["orders_delivered"] += 1
    state["total_reward"] += reward_earned
    return state

updates = [
("Zone A", 12.0),
("Zone B", 10.0),
("Zone C", 8.0),
("Zone D", 15.0)
]

for location, reward in updates:
    update_state(state, location, reward)
print("\nCurrent State:")
print("Location:", state["location"])
print("Orders Delivered:", state["orders_delivered"])
print("Total Reward:", state["total_reward"])
print("Is Available:", state["is_available"])

print("\nTASK 3: ACTION-REWARD EPISODE LOGGER")
print("-" * 50)

possible_actions = [
"accept_order",
"reject_order",
"request_directions",
"mark_delivered"
]

action_rewards = {
"accept_order": 2,
"reject_order": -1,
"request_directions": 0,
"mark_delivered": 10
}

episode_actions = [
"accept_order",
"request_directions",
"accept_order",
"reject_order",
"request_directions",
"mark_delivered"
]

cumulative_reward = 0

for step, action in enumerate(episode_actions, start=1):
    reward = action_rewards[action]
    cumulative_reward += reward
    print("Step:", step)
    print("Action:", action)
    print("Reward Received:", reward)
    print("Cumulative Reward:", cumulative_reward)
    print()

print("Total Episode Reward:", cumulative_reward)

print("\nTASK 4: SIMPLE RL ENVIRONMENT SIMULATOR")
print("-" * 50)

class DeliveryEnvironment:
    def __init__(self):
        self.current_state = {"location": "Restaurant", "pending_orders": 5}
        self.total_reward = 0
        self.step_count = 0

    def step(self, action):
        if action == "deliver_order":
            if self.current_state["pending_orders"] > 0:
                self.current_state["pending_orders"] -= 1
                self.current_state["location"] = "Customer"
                reward = 10
            else:
                reward = -2
        elif action == "wait":
            reward = -1
            self.current_state["location"] = "Restaurant"
        elif action == "navigate_to_zone":
            self.current_state["location"] = "Delivery Zone"
            reward = 2
        else:
            reward = -5
        self.total_reward += reward
        self.step_count += 1
        print("Step:", self.step_count)
        print("Action:", action)
        print("New State:", self.current_state)
        print("Reward:", reward)
        print("Total Reward:", self.total_reward)
        print()
        return reward

environment = DeliveryEnvironment()

actions = [
"navigate_to_zone",
"deliver_order",
"navigate_to_zone",
"deliver_order",
"wait",
"deliver_order"
]

for action in actions:
    environment.step(action)

print("Final State:", environment.current_state)
print("Final Total Reward:", environment.total_reward)
print("Total Steps:", environment.step_count)
