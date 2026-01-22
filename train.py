import gymnasium as gym
import highway_env  # noqa: F401 (registers environments)
from stable_baselines3 import DQN
from stable_baselines3.common.monitor import Monitor
from dataclasses import dataclass
from typing import Dict, Any
import matplotlib.pyplot as plt


# =========================
# Configuration
# =========================

@dataclass
class TrainingConfig:
    env_id: str = "highway-fast-v0"
    total_timesteps: int = 40_000  # enough to separate early vs full
    early_fraction: float = 0.2    # 20% checkpoint
    seed: int = 42


CONFIG = TrainingConfig()

# -------------------------
# Environment Configuration
# -------------------------
ENV_CONFIG: Dict[str, Any] = {
    # Traffic & Road
    "lanes_count": 4,
    "vehicles_count": 45,          # medium-dense → learning pressure
    "duration": 60,
    "ego_spacing": 1.2,

    # Dynamics
    "simulation_frequency": 15,
    "policy_frequency": 5,

    # Reward shaping (CRITICAL)
    "collision_reward": -8.0,      # punish crashes hard
    "high_speed_reward": 2.5,      # reward confident driving
    "right_lane_reward": 0.05      # small incentive only
}


# =========================
# Environment Setup
# =========================

env = gym.make(CONFIG.env_id, config=ENV_CONFIG)
env = Monitor(env)  # records episode rewards


# =========================
# Model Setup (DQN)
# =========================

model = DQN(
    policy="MlpPolicy",
    env=env,
    learning_rate=5e-4,
    buffer_size=30_000,
    learning_starts=1_000,
    batch_size=64,
    gamma=0.99,
    train_freq=1,
    gradient_steps=1,
    target_update_interval=500,
    exploration_fraction=0.15,
    exploration_initial_eps=1.0,
    exploration_final_eps=0.05,
    policy_kwargs=dict(net_arch=[256, 256]),
    verbose=1,
    seed=CONFIG.seed
)


# =========================
# Training Logic
# =========================

early_steps = int(CONFIG.total_timesteps * CONFIG.early_fraction)
final_steps = CONFIG.total_timesteps

print(f"\n🚗 Training EARLY checkpoint ({early_steps} steps)")
model.learn(total_timesteps=early_steps)
model.save("dqn_highway_early.zip")

print(f"\n🚀 Training FINAL model ({final_steps - early_steps} more steps)")
model.learn(total_timesteps=final_steps - early_steps)
model.save("dqn_highway_final.zip")

print("\n✅ Training complete. Models saved.")


# =========================
# Training Curve Plot
# =========================

episode_rewards = env.get_episode_rewards()

plt.figure(figsize=(7, 4))
plt.plot(episode_rewards, label="Episode Reward")
plt.xlabel("Episode")
plt.ylabel("Total Reward")
plt.title("Training Reward vs Episodes")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("training_curve.png")

print("📈 training_curve.png saved.")

env.close()
