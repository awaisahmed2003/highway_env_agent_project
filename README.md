![evolution](https://github.com/user-attachments/assets/6a0ff95f-66db-417e-b12e-0d2c23984e78)
Autonomous Driving in Dense Highway Traffic using Reinforcement Learning

Awais Ahmed – 2281583
Adam El Kaissi – 2101431

Project Overview

This project focuses on training an autonomous vehicle to navigate a dense highway traffic environment using Reinforcement Learning (RL). The agent must balance high-speed driving with collision avoidance, making this a multi-objective optimization problem in a dynamic and stochastic environment.

The simulation environment is built using the highway-env library, which provides realistic traffic dynamics and standardized benchmarks for autonomous driving research.

Objective

Train an agent that drives as fast as possible without crashing.

This translates into two competing goals:

Maximize speed and lane efficiency

Minimize collisions and unsafe maneuvers

The agent must learn an optimal driving policy that balances performance and safety under heavy traffic conditions.

Core Challenge: Multi-Objective Decision Making

At every time step, the agent must decide:

Should it accelerate to maximize speed?

Should it slow down or change lanes to avoid collisions?

These objectives often conflict, making naive greedy strategies ineffective. The solution therefore requires long-term planning rather than short-term gains.

Methodology
Reinforcement Learning Approach (DQN)

The problem is modeled using Deep Q-Learning (DQN), a value-based reinforcement learning algorithm suitable for discrete action spaces such as lane changes and acceleration commands.

The agent learns a Q-function that estimates the long-term reward of taking an action in a given traffic state, allowing it to plan beyond immediate speed gains and avoid future collisions.

Algorithm: Deep Q-Network (DQN)
Framework: Stable-Baselines3

Neural Network Architecture

Multi-Layer Perceptron (MLP)

Hidden layers: [256, 256]

Activation function: ReLU

Key Training Parameters
Parameter	Value
Learning Rate	5e-4
Discount Factor (γ)	0.99
Replay Buffer Size	30,000
Batch Size	64
Exploration (ε)	1.0 → 0.05
Total Timesteps	40,000
Problem Formulation (MDP)
Component	Description
State	Ego vehicle speed, position, lane index, and surrounding vehicle observations
Actions	Discrete actions: accelerate, decelerate, keep speed, lane left/right
Reward	High-speed incentives with strong collision penalties
Policy	Q-network mapping states to action values

The agent improves its policy through trial-and-error interaction with the environment, using experience replay to stabilize learning.

Environment Setup

The agent is trained and evaluated in the highway-fast-v0 environment from the highway-env library, configured to represent medium-to-dense highway traffic.

Environment Configuration
Setting	Value
Lanes	4
Vehicles	45
Episode Duration	60–100 s
Simulation Frequency	15 Hz
Policy Frequency	3–5 Hz
Ego Spacing	1.2–1.3

The dense traffic configuration introduces:

Limited safe gaps

Frequent braking events

High collision risk under aggressive driving

This setup forces the agent to learn anticipatory and defensive behaviors while maintaining speed.

Reward Design

Reward shaping plays a critical role in balancing speed and safety.

Reward Components
Component	Purpose
high_speed_reward (+2.5)	Encourage fast driving
collision_reward (−8.0)	Strongly penalize crashes
right_lane_reward (+0.05)	Mild lane discipline incentive

The collision penalty dominates the reward signal, ensuring unsafe high-speed behavior is consistently discouraged. This results in a learned policy that is confident but risk-aware.

Results and Performance
Training Curves (Quantitative Analysis)

The learning progress of the agent is visualized using the training reward curve recorded during DQN training.

Analysis of Training Curve:

Early episodes show low and unstable rewards due to random exploration and frequent collisions

Average episode reward steadily increases as training progresses

Reward variance decreases over time, indicating policy stabilization

This confirms that the agent is optimizing the reward objective both qualitatively and quantitatively.

Behavioral Evaluation (Visual Comparison)

To demonstrate learning progress, a single evolution video was generated comparing three agents under identical initial traffic conditions:

Untrained Agent (Random Actions)

Half-Trained Agent (~20% of training)

Fully Trained Agent (40,000 timesteps)

Observed Behavior:

Untrained Agent: Erratic acceleration, poor lane discipline, frequent early collisions

Half-Trained Agent: Improved anticipation but occasional unsafe merges

Fully-Trained Agent: Smooth lane changes, anticipatory braking, sustained high-speed driving

Because all agents are evaluated with the same random seed and traffic layout, observed differences are directly attributable to learning progress.

Average Speed Over Training


│          ██████████████
│      ██████████████████
│  ██████████████████████
│
└────────────────────────── Training Time

Collision Frequency Over Training

│ ███████████
│ ██████
│ ██
│
└────────────────────────── Training Time

As training progresses, the agent achieves higher sustained speeds while dramatically reducing collisions, demonstrating successful multi-objective optimization.

Why This Project Matters

Demonstrates real-world autonomous driving challenges

Highlights the importance of reward engineering

Provides hands-on experience with reinforcement learning in dynamic environments

This project mirrors real autonomous driving problems where perfect safety and maximum speed cannot be optimized independently.

Tools and Technologies

Python

highway-env

Gymnasium / OpenAI Gym

Stable-Baselines3

Reinforcement Learning (DQN)

Future Improvements

Incorporate risk-aware or constrained reinforcement learning

Train with multiple traffic styles for robustness

Add curriculum learning with increasing traffic density

Compare multiple RL algorithms side-by-side

Repository Artifacts

train.py – DQN training script

evaluate.py – Controlled evaluation and visualization

training_curve.png – Learning performance over time

evolution.gif – Behavioral comparison of agent learning stages

Member Contributions

This project was completed collaboratively, with responsibilities clearly divided.

Awais Ahmed

Designed and implemented the reinforcement learning pipeline using DQN

Configured the highway-env environment and traffic parameters

Performed model training with early and final checkpoints

Tuned reward shaping to balance speed and safety

Generated trained models and learning artifacts

Adam El Kaissi

Developed the evaluation and visualization pipeline

Implemented controlled comparisons between untrained, half-trained, and fully-trained agents

Generated and annotated the evolution video (GIF)

Analyzed training curves and agent behavior

Authored and structured the project report (README.md)
