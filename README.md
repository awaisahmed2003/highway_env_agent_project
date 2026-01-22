# Autonomous Driving using Reinforcement Learning (highway-env)

**Awais Ahmed – 2281583**  
**Adam El Kaissi – 2101431**

---



https://github.com/user-attachments/assets/f1708e53-bca8-4b5f-87b0-5c927c0cdf70




## 🔹 Project Overview

This project focuses on training an autonomous vehicle to navigate a dense highway traffic environment using Reinforcement Learning (RL). The agent must balance high-speed driving with collision avoidance, making this a multi-objective optimization problem in a dynamic and stochastic environment.

The simulation environment is built using the highway-env library, which provides realistic traffic dynamics and standardized benchmarks for autonomous driving research.

---

## 🔹 Objective

Train an agent that drives as fast as possible without crashing.

This translates into two competing goals:

- Maximize Speed & Lane Efficiency
- Minimize Collisions & Unsafe Maneuvers

The agent must learn an optimal driving policy that balances performance and safety under heavy traffic conditions.

---

## 🔹 Core Challenge

### Multi-Objective Decision Making

At every time step, the agent must decide:

- Should it accelerate to maximize speed?
- Should it slow down or change lanes to avoid collisions?

These objectives often conflict, making naive greedy strategies ineffective. The solution requires long-term planning rather than short-term gains.

---

## 🔹 Methodology

### Reinforcement Learning Approach (DQN)

We model the problem using Deep Q-Learning (DQN), a value-based reinforcement learning algorithm suitable for discrete action spaces such as lane changes and acceleration commands.

The agent learns a Q-function that estimates the long-term reward of taking an action in a given traffic state, allowing it to plan beyond immediate speed gains and avoid future collisions.

- Algorithm: Deep Q-Network (DQN)
- Framework: Stable-Baselines3

---

## 🔹 Neural Network Architecture

- Multi-Layer Perceptron (MLP)
- Hidden layers: [256, 256]
- Activation: ReLU

---

## 🔹 Key Training Parameters

| Parameter | Value |
|---------|------|
| Learning Rate | 5e-4 |
| Discount Factor (γ) | 0.99 |
| Replay Buffer Size | 30,000 |
| Batch Size | 64 |
| Exploration (ε) | 1.0 → 0.05 |
| Total Timesteps | 40,000 |

---

## 🔹 Problem Formulation (MDP)

| Component | Description |
|---------|-------------|
| State | Ego vehicle speed, position, lane index, and surrounding vehicle observations |
| Actions | Discrete actions: accelerate, decelerate, keep speed, lane left/right |
| Reward | High-speed incentives with strong collision penalties |
| Policy | Q-network mapping states to action values |

The agent improves its policy through trial-and-error interaction with the environment, using experience replay to stabilize learning.

---

## 🔹 Environment Setup

The agent is trained and evaluated in the highway-fast-v0 environment from the highway-env library, configured to represent medium-to-dense highway traffic.

### Environment Configuration

| Setting | Value |
|-------|-------|
| Lanes | 4 |
| Vehicles | 45 |
| Episode Duration | 60–100 s |
| Simulation Frequency | 15 Hz |
| Policy Frequency | 3–5 Hz |
| Ego Spacing | 1.2–1.3 |

The dense traffic configuration introduces:

- Limited safe gaps
- Frequent braking events
- High collision risk under aggressive driving

This setup forces the agent to learn anticipatory and defensive behaviors while maintaining speed.

---

## 🔹 Reward Design

Reward shaping plays a critical role in balancing speed and safety.

### Reward Components

| Component | Purpose |
|---------|---------|
| high_speed_reward (+2.5) | Encourage fast driving |
| collision_reward (−8.0) | Strongly penalize crashes |
| right_lane_reward (+0.05) | Mild lane discipline incentive |

The collision penalty dominates the reward signal, ensuring that unsafe high-speed behavior is consistently discouraged. This results in a learned policy that is confident but risk-aware.

---

## 🔹 Results & Performance

### Training Curves (Quantitative Analysis)

The learning progress of the agent is visualized using the training reward curve recorded during DQN training.

Analysis of Training Curve:

- Early episodes show low and unstable rewards, corresponding to random exploration and frequent collisions.
- As training progresses, the average episode reward steadily increases, indicating improved lane selection and speed control.
- Reward variance decreases over time, showing that the policy becomes more stable and consistent.

This curve confirms that the agent is not only improving qualitatively (behavior) but also optimizing the reward objective quantitatively.

---

## 🔹 Behavioral Evaluation (Visual Comparison)

To clearly demonstrate learning progress, we generated a single evolution video comparing three agents under identical initial traffic conditions:

1. Untrained Agent (Random Actions)
2. Half Trained Agent (~20% of training)
3. Fully Trained Agent (40k timesteps)

What the visualization shows:

- Untrained Agent: Erratic acceleration, poor lane discipline, frequent early collisions.
- Half Trained Agent: Begins to anticipate traffic but still makes unsafe merges.
- Fully Trained Agent: Smooth lane changes, anticipatory braking, sustained high-speed travel.

Because all agents are evaluated with the same random seed and traffic layout, the behavioral differences can be directly attributed to learning progress rather than environment randomness. This visual evidence strongly complements the training reward curves.

---

## 🔹 Learning Dynamics

### Average Speed
<img width="722" height="272" alt="{2DDC8AB3-E24D-4312-9495-BF8A1F38EC0F}" src="https://github.com/user-attachments/assets/6fa1af8c-cd59-43b4-8a88-f8c5631a94f5" />

Collision Frequency Over Training

<img width="747" height="255" alt="{EDC9708E-22C6-425F-BEF7-9E15F36D93EB}" src="https://github.com/user-attachments/assets/df2f7d23-c118-4054-8ed5-1b2f70e87598" />


As training progresses, the agent achieves higher sustained speeds while dramatically reducing collisions, demonstrating successful multi-objective optimization.

---

## 🔹 Why This Project Matters

- Demonstrates real-world autonomous driving challenges
- Highlights the importance of reward engineering
- Provides hands-on experience with RL in continuous, dynamic environments

This project mirrors real autonomous driving problems where perfect safety and maximum speed cannot be optimized independently.

---

## 🔹 Tools and Technologies

- Python
- highway-env
- Gymnasium / OpenAI Gym
- Reinforcement Learning Algorithms (value-based or policy-based)

---

## 🔹 Future Improvements

- Incorporate risk-aware or constrained RL
- Train with multiple traffic styles for robustness
- Add curriculum learning (increasing traffic density over time)
- Compare multiple RL algorithms side-by-side

---

## 🔹 Conclusion

This project demonstrates that a Deep Q-Learning agent can successfully learn fast yet safe highway driving in dense traffic using carefully designed reward shaping and environment constraints.

By comparing untrained, partially trained, and fully trained agents under identical traffic conditions, we clearly observe:

- Emergent lane selection strategies
- Reduced collision rates
- Sustained high-speed driving

The combination of quantitative rewards and qualitative visual evidence confirms that the learned policy effectively balances speed and safety.

---

## 🔹 Repository Artifacts

- train.py – DQN training script
- evaluate.py – Controlled evaluation & visualization
- training_curve.png – Learning performance over time
- evolution.gif – Behavioral comparison of agent learning stage
- requirements.txt - List of all required dependencies

---

## 🔹 Member Contribution

This project was completed collaboratively, with responsibilities clearly divided to ensure both technical detail and clear presentation.

### Awais

- Designed and implemented the reinforcement learning pipeline using Deep Q-Networks (DQN)
- Configured the highway-env environment and traffic parameters
- Performed model training, including early and final checkpoints
- Tuned reward shaping to balance speed and safety
- Generated trained models and learning artifacts

### Adam

- Developed the evaluation and visualization pipeline
- Implemented controlled comparisons between untrained, half-trained, and fully-trained agents
- Generated and annotated the evolution video (GIF) for qualitative analysis
- Analyzed training curves and agent behavior
- Authored and structured the project report (README.md) with professional Markdown formatting

