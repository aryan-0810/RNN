agent_state = {
    "current_location": "Restaurant",
    "orders_delivered": 0,
    "total_reward": 0
}

total_episodes = 0
total_reward_earned = 0
episode_history = []

def calculate_reward(action):
    rewards = {
        "accept_order": 2,
        "navigate_to_customer": 3,
        "wait": -1,
        "deliver_order": 10,
        "return_to_restaurant": 2
    }
    return rewards.get(action, -2)

def update_state(action, reward):
    agent_state["total_reward"] += reward

    if action == "accept_order":
        agent_state["current_location"] = "Restaurant"
    elif action == "navigate_to_customer":
        agent_state["current_location"] = "Customer Location"
    elif action == "deliver_order":
        agent_state["current_location"] = "Customer Location"
        agent_state["orders_delivered"] += 1
    elif action == "return_to_restaurant":
        agent_state["current_location"] = "Restaurant"

def start_episode():
    global total_episodes, total_reward_earned

    actions = ["accept_order", "navigate_to_customer", "wait", "deliver_order", "return_to_restaurant"]
    episode_reward = 0
    episode_log = []

    print("\nStarting New Delivery Episode")
    print("-" * 50)
    for step, action in enumerate(actions, start=1):
        reward = calculate_reward(action)
        episode_reward += reward
        update_state(action, reward)
        episode_log.append({"step": step, "action": action, "reward": reward})
        print("Step:", step)
        print("Action:", action)
        print("Reward:", reward)
        print("Current Location:", agent_state["current_location"])
        print("Orders Delivered:", agent_state["orders_delivered"])
        print("Cumulative Reward:", episode_reward)
        print()

    total_episodes += 1
    total_reward_earned += episode_reward
    episode_history.append({"episode": total_episodes, "reward": episode_reward, "steps": episode_log})
    print("=" * 50)
    print("EPISODE SUMMARY")
    print("=" * 50)
    for entry in episode_log:
        print("Step:", entry["step"], "| Action:", entry["action"], "| Reward:", entry["reward"])
    print("-" * 50)
    print("Total Episode Reward:", episode_reward)
    print("Orders Delivered:", agent_state["orders_delivered"])
    print("Current Location:", agent_state["current_location"])
    print("=" * 50)

def view_stats():
    print("\nAGENT STATISTICS")
    print("-" * 50)
    average_reward = 0 if total_episodes == 0 else total_reward_earned / total_episodes
    print("Total Episodes Run:", total_episodes)
    print("Total Reward Earned:", total_reward_earned)
    print("Average Reward Per Episode:", round(average_reward, 2))
    print("Current Location:", agent_state["current_location"])
    print("Orders Delivered:", agent_state["orders_delivered"])
    print("Agent Total Reward:", agent_state["total_reward"])
    print("-" * 50)

while True:
    print("\n")
    print("=" * 50)
    print("FOOD DELIVERY RL CONCEPT SIMULATOR")
    print("=" * 50)
    print("1. Start New Delivery Episode")
    print("2. View Agent Stats")
    print("3. Exit")
    print("=" * 50)
    choice = input("Enter your choice: ")
    if choice == "1":
        start_episode()
    elif choice == "2":
        view_stats()
    elif choice == "3":
        print("\nThank you for using the Food Delivery RL Simulator.")
        break
    else:
        print("\nInvalid choice. Please select 1, 2, or 3.")
