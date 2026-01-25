# Autonomous Driving using Reinforcement Learning (highway-env)

**Awais Ahmed – 2281583**  
**Adam El Kaissi – 2101431**


---
**🔹Visual Proof: Agent Learning Evolution** 
---

The following embedded evolution video provides immediate visual evidence of learning progression across three stages under identical traffic conditions:
1.	Untrained Agent (Random Actions)
2.	Half-Trained Agent (~20% Training)
3.	Fully-Trained Agent (40k Timesteps)




https://github.com/user-attachments/assets/f1708e53-bca8-4b5f-87b0-5c927c0cdf70

The comparison clearly shows the transition from erratic, collision-prone behavior to smooth, anticipatory, high-speed driving.



## 🔹Quick Start: (No Training)
All trained models are already included in this repository.
To run the project and reproduce the results **without training**:

pip install -r requirements.txt

python evaluate.py



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


**🔹 The Math: Custom Reward Function**
---
The learning objective is encoded through a custom reward function designed to balance speed and safety:

---
**R(s,a)=r_speed+r_lane+r_collision**
---
Where:
---
•	High-speed reward (+2.5): Encourages maintaining higher velocities

---
•	Right-lane reward (+0.05): Provides mild lane discipline

---
•	Collision penalty (−8.0): Strongly discourages unsafe behavior

---
The magnitude of the collision penalty dominates the reward signal, ensuring that reckless high-speed strategies are consistently penalized.

---


## 🔹 Training Analysis

### The Graph: Reward vs Episodes 

<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/f9a72796-3792-49d1-ae5d-0e41bbe0f266" />


**Learning Behavior Over Time** 
---

•	Early Phase: Rewards remain low and unstable due to random exploration and frequent collisions.

---
•	 Mid Training: The agent begins to survive longer episodes, indicating improved lane selection and speed modulation. 

---
•	Late Training: Rewards rise steadily and variance decreases, demonstrating a stable policy that balances speed with safety.

---

## 🔹 Behavioral Evaluation (Visual Comparison)

**Training Progress**
---

During early training, the agent behaves similarly to a random policy: frequent collisions, unstable lane changes, and low cumulative reward. As training progresses, the agent learns:

---

•	When to slow down instead of forcing overtakes

---
•	How to exploit open lanes

---
•	How to maintain high speed without aggressive collisions

---
The training reward curve shows a clear upward trend, indicating successful policy improvement.

---
To clearly demonstrate learning progress, we generated a single evolution video comparing three agents under identical initial traffic conditions:

---
1.	Untrained Agent (Random Actions)
---
2.	Half Trained Agent (~20% of training)
   
	---
3.	Fully Trained Agent (40k timesteps)
	
	---
 
**What the visualization shows:**
---
•	 Untrained Agent: Erratic acceleration, poor lane discipline, frequent early collisions.

---
•	 Half Trained Agent: Begins to anticipate traffic but still makes unsafe merges.

---
•	 Fully Trained Agent: Smooth lane changes, anticipatory braking, sustained high-speed travel.

---
Because all agents are evaluated with the same random seed and traffic layout, the behavioral differences can be directly attributed to learning progress rather than environment randomness. This visual evidence strongly complements the training reward curves.



---

## 🔹 Learning Dynamics

### Average Speed
<img width="722" height="272" alt="{2DDC8AB3-E24D-4312-9495-BF8A1F38EC0F}" src="https://github.com/user-attachments/assets/6fa1af8c-cd59-43b4-8a88-f8c5631a94f5" />

Collision Frequency Over Training

<img width="747" height="255" alt="{EDC9708E-22C6-425F-BEF7-9E15F36D93EB}" src="https://github.com/user-attachments/assets/df2f7d23-c118-4054-8ed5-1b2f70e87598" />


As training progresses, the agent achieves higher sustained speeds while dramatically reducing collisions, demonstrating successful multi-objective optimization.

---
## 🔹 Challenges & Failures 
---
**Technical Hurdle: Unsafe Looping and Aggressive Lane Switching**
---
A major challenge encountered during training was the agent developing a looping behavior, repeatedly changing lanes at high speed without making forward progress. This resulted in frequent collisions and poor rewards.

---
 **Cause:**
 ---
•	Overly aggressive exploration 

---
•	Insufficient penalty for unsafe maneuvers 

---
**Solution:**
---

•	Increased the collision penalty to dominate the reward signal 

----
•	Reduced exploration more aggressively

---
•	Adjusted policy frequency to encourage smoother control 

---
After these changes, the agent adopted anticipatory braking and more deliberate lane changes, leading to stable learning and improved performance.


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
- dqn_highway_half/final - Training files for evaluate.py

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

