# Autonomous Driving using Reinforcement Learning (highway-env)

This project focuses on training an autonomous vehicle to navigate dense highway traffic using Reinforcement Learning (RL). The agent is trained to maximize driving speed while avoiding collisions in a dynamic and stochastic environment.

The simulation environment is built using the highway-env library, which provides realistic traffic dynamics and standardized benchmarks for autonomous driving research.

---

## 🔹 Project Objective

Train an agent that drives as fast as possible without crashing.

This objective consists of two competing goals:

- Maximize speed and lane efficiency
- Minimize collisions and unsafe maneuvers

The agent must learn a policy that balances performance and safety under heavy traffic conditions.

---

## 🔹 Core Challenge

### Multi-Objective Decision Making

At every time step, the agent must decide:

- Whether to accelerate to maximize speed
- Whether to slow down or change lanes to avoid collisions

These objectives often conflict, making short-term greedy strategies ineffective. The agent must therefore learn long-term planning through reinforcement learning.

---

## 🔹 Methodology

### Reinforcement Learning Approach (DQN)

The problem is modeled using Deep Q-Learning (DQN), a value-based reinforcement learning algorithm suitable for discrete action spaces such as lane changes and acceleration commands.

The agent learns a Q-function that estimates the long-term reward of actions taken in a given traffic state.

- Algorithm: Deep Q-Network (DQN)
- Framework: Stable-Baselines3

---

## 🔹 Model Architecture

- Multi-Layer Perceptron (MLP)
- Two hidden layers with 256 units each
- ReLU activation function

---

## 🔹 Training Configuration

- Learning rate: 5e-4
- Discount factor (gamma): 0.99
- Replay buffer size: 30,000
- Batch size: 64
- Exploration epsilon: 1.0 → 0.05
- Total training timesteps: 40,000

---

## 🔹 Problem Formulation (MDP)

- State: Ego vehicle speed, position, lane index, and surrounding vehicle observations
- Actions: Accelerate, decelerate, maintain speed, lane change left/right
- Reward: High-speed incentives with strong collision penalties
- Policy: Q-network mapping states to action values

The agent improves its policy through trial-and-error interaction with the environment using experience replay.

---

## 🔹 Environment Setup

The agent is trained and evaluated in the highway-fast-v0 environment configured for medium-to-dense highway traffic.

- Number of lanes: 4
- Number of vehicles: 45
- Episode duration: 60–100 seconds
- Simulation frequency: 15 Hz
- Policy frequency: 3–5 Hz
- Ego vehicle spacing: 1.2–1.3

This configuration introduces limited safe gaps and frequent braking events, forcing the agent to learn defensive yet efficient driving behavior.

---

## 🔹 Reward Design

Reward shaping is used to balance speed and safety:

- High speed reward (+2.5) to encourage fast driving
- Collision penalty (−8.0) to strongly discourage crashes
- Right lane reward (+0.05) for mild lane discipline

The collision penalty dominates the reward signal to ensure unsafe behavior is discouraged.

---

## 🔹 Results and Evaluation

### Training Performance

Early training episodes show low and unstable rewards due to random exploration and frequent collisions. As training progresses, the average episode reward increases and stabilizes, indicating improved driving behavior.

---

## 🔹 Behavioral Evaluation

Three agents are evaluated under identical traffic conditions:

- Untrained agent using random actions
- Half-trained agent trained on approximately 20% of total timesteps
- Fully trained agent trained for 40,000 timesteps

The fully trained agent demonstrates smoother lane changes, anticipatory braking, and sustained high-speed driving with significantly fewer collisions.

---

## 🔹 Repository Artifacts

- train.py – DQN training script
- evaluate.py – Controlled evaluation and visualization
- training_curve.png – Training reward curve
- evolution.gif – Behavioral comparison of learning stages

---

## 🔹 Tools and Technologies

- Python
- highway-env
- Gymnasium
- Stable-Baselines3
- Deep Q-Learning (DQN)

---

## 🔹 Contributors

**Awais Ahmed – 2281583**
- Designed and implemented the reinforcement learning pipeline
- Configured environment and reward shaping
- Trained and tuned the DQN agent

**Adam El Kaissi – 2101431**
- Developed evaluation and visualization pipeline
- Generated comparison video and analysis
- Authored and structured the README
