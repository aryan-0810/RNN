# M12-A1 - Reinforcement Learning Assessment

# print("""

# SCENARIO 1

Question:
Explain why Reinforcement Learning is more suitable than traditional
programming for this dispatch system. What key characteristic of RL
allows it to improve its decisions without relying on labelled training data?

Answer:

Reinforcement Learning (RL) is more suitable for an automatic food
delivery dispatch system because the system needs to make decisions in
a changing environment. Traditional programming requires manually
defined rules, such as assigning the nearest rider to an order. These
rules may not always produce the best result because traffic, rider
availability, customer location, and order volume can change.

In Reinforcement Learning, an agent learns by interacting with the
environment. It takes an action, observes the result, and receives a
reward or penalty based on the outcome. For example, assigning a rider
who delivers an order quickly can produce a positive reward, while a
late delivery can produce a negative reward.

The key characteristic of RL is that it learns through trial and error
using rewards and feedback rather than requiring labelled examples of
the correct decision. Over time, the agent learns which actions produce
better long-term rewards and improves its dispatching decisions.
""")

# print("""

# SCENARIO 2

Question:
Compare how a supervised learning model and a Reinforcement Learning
agent each learn to make recommendations. What fundamental difference
in their learning mechanism would justify choosing RL for a continuously
improving recommendation engine?

Answer:

A supervised learning model learns from historical labelled data.
For example, a restaurant recommendation model can be trained using
previous customer orders where the input contains customer information
and the target represents a known outcome, such as whether a customer
ordered or liked a particular restaurant.

A Reinforcement Learning agent learns differently. It interacts with
customers and the recommendation environment, chooses which restaurant
reward based on that response.

The fundamental difference is that supervised learning learns from
fixed labelled examples, while Reinforcement Learning learns from
actions, feedback, and rewards obtained through interaction with the
environment.

RL can therefore be useful for a continuously improving recommendation
engine because it can adapt its recommendations based on new customer
responses instead of depending only on historical training data.
""")

# print("""

# SCENARIO 3

Question:
What distinguishes a Reinforcement Learning system from an unsupervised
learning system when the goal is to continuously improve delivery zone
assignments based on real delivery outcomes?

Answer:

Both Reinforcement Learning and unsupervised learning can work without
labelled data, but they have different objectives.

Unsupervised learning, such as clustering, discovers patterns or groups
in existing data. For example, clustering could group delivery locations
based on geographical distance, order frequency, or customer density.
However, clustering does not directly learn whether a particular zone
assignment produces faster or more efficient deliveries.

Reinforcement Learning makes decisions and learns from the consequences
of those decisions. An RL agent could assign riders to delivery zones,
observe outcomes such as delivery time, distance, and customer
satisfaction, and then receive a reward or penalty.

Therefore, the main difference is that unsupervised learning discovers
patterns in data, whereas Reinforcement Learning learns an action policy
through interaction with the environment and feedback from real outcomes.

RL is particularly useful when the objective is to continuously improve
decisions based on the consequences of previous decisions.
""")

# print("""

# SCENARIO 4

Question:
Identify the agent, environment, set of possible actions, and reward
signal for this delivery dispatch RL system. Justify why your chosen
reward signal directly encourages efficient delivery performance rather
than unintended shortcut behaviour.

Answer:

Agent:
The RL agent is the delivery dispatching system that decides which rider
should be assigned to each incoming food order.

Environment:
The environment is the complete food delivery system. It includes
customers, restaurants, riders, traffic conditions, order locations,
weather conditions, and changing rider availability.

Actions:
The possible actions are the available rider assignments for an incoming
order. For example, the agent can assign Rider A, Rider B, Rider C, or
another available rider.

Reward:
The reward should combine important delivery outcomes rather than using
only one measurement. For example, the system can provide positive
reward for completing deliveries successfully and efficiently, while
giving penalties for long delivery times, excessive travel distance,
late deliveries, cancellations, or poor customer experience.

A suitable reward can conceptually be represented as:

Reward = successful_delivery_reward
- delivery_time_penalty
- distance_penalty
- cancellation_penalty

The reward should include multiple important outcomes because using only
one metric could create unintended shortcut behaviour. For example, if
the agent were rewarded only for reducing delivery distance, it might
choose a rider who is close to the restaurant but cannot complete the
delivery efficiently.

A carefully designed reward encourages the agent to balance delivery
speed, distance, successful completion, and customer experience.
""")

# print("""

# SCENARIO 5

Question:
Using game AI as a reference point, explain the core principle of how
an RL agent learns through interaction with its environment. In what
ways does the delivery dispatch scenario follow this same learning
principle even though it is not a game?

Answer:

In game AI such as chess, an RL agent interacts with the game environment.
It observes the current state, chooses an action, receives a reward or
penalty based on the result, and uses this feedback to improve future
decisions.

For example, a chess agent can make a move and receive positive feedback
when the move contributes to winning the game. Through many interactions,
the agent learns a strategy that increases its long-term reward.

The same principle applies to food delivery dispatching.

The delivery system observes the current state, such as the restaurant
location, customer location, available riders, and traffic conditions.
The agent then chooses a rider assignment. After the delivery, the
system observes the outcome, such as delivery time, distance, successful
completion, and customer satisfaction. The agent receives a reward based
on these outcomes and uses this feedback to improve future assignments.

The main difference is the environment. Chess is a game environment,
while food delivery is a real-world operational environment. However,
the learning principle remains the same:

State -> Action -> Environment Response -> Reward -> Learning

Thus, RL does not require the problem to be a game. It can be applied
whenever an agent makes decisions, observes their consequences, and
learns from feedback.
""")

# print("""

# SCENARIO 6

Question:
Describe how Reinforcement Learning has been applied to recommendation
systems in industry. What advantage does an RL-based recommendation
system offer over a model trained once on historical data, particularly
for customers whose food preferences change over time?

Answer:

Reinforcement Learning has been applied to recommendation and
personalisation systems where platforms continuously choose what content,
products, or services to show users and learn from their responses.

For example, recommendation systems can use user interactions such as
clicks, orders, skips, ratings, viewing time, or repeated purchases 
and use that response as a reward to improve future recommendations.

For a food delivery platform, an RL recommendation agent could recommend
different restaurants or meals to a customer. If the customer orders the
recommended meal, the system can treat this as positive feedback. If the
customer repeatedly ignores or rejects similar recommendations, the
system can reduce their priority in future recommendations.

The main advantage of RL over a model trained once on historical data is
adaptability. A traditional model may continue relying heavily on past
behaviour until it is retrained. An RL system can continuously learn from
new interactions and update its decisions.

This is especially useful when customer preferences change. For example,
a customer who frequently orders pizza may later start preferring healthy
food options. An RL-based recommendation system can detect this change in
behaviour and gradually adjust its recommendations.

Therefore, RL supports continuous learning and adaptation based on
ongoing customer feedback rather than relying only on a fixed historical
dataset.
""")

