import gymnasium as gym
import highway_env
from stable_baselines3 import DQN
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import imageio.v2 as imageio  # v2 for consistent API

# Configuration for evaluation video
ENV_ID = "highway-fast-v0"
ENV_CONFIG = {
    "lanes_count": 4,
    "vehicles_count": 45,
    "duration": 100,              # 30 seconds episodes
    "simulation_frequency": 15,
    "policy_frequency": 3,
    "ego_spacing": 1.3,
    "screen_width": 1200,        # higher resolution for video
    "screen_height": 300,
    "scaling": 11.0,
    "collision_reward": -5.0,
    "high_speed_reward": 2.5,
    "right_lane_reward": 0.05
    # double scaling since we doubled resolution (for clarity)
}
FPS = 20                     # recording frames per second
SEED = 42                       # seed to reproduce the same scenario for each agent

# Load the trained models
model_half = DQN.load("dqn_highway_half.zip")
model_full = DQN.load("dqn_highway_final.zip")

# Prepare three environments (one for each stage) with identical initial conditions
env_random = gym.make(ENV_ID, config=ENV_CONFIG, render_mode="rgb_array")
env_half   = gym.make(ENV_ID, config=ENV_CONFIG, render_mode="rgb_array")
env_full   = gym.make(ENV_ID, config=ENV_CONFIG, render_mode="rgb_array")

# Seed each environment so that they start with the same scenario (for fair comparison)
obs_random, info = env_random.reset(seed=SEED)
obs_half,   info = env_half.reset(seed=SEED)
obs_full,   info = env_full.reset(seed=SEED)

frames = []  # will hold frames for the final combined video

# Helper: overlay text label on a frame
def add_label(frame: np.ndarray, text: str) -> np.ndarray:
    """Add a text label to the given frame image (numpy array)."""
    img = Image.fromarray(frame)
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    # Measure text size (Pillow >=10 compatible)
    bbox = draw.textbbox((0, 0), text, font=font)
    txt_width = bbox[2] - bbox[0]
    txt_height = bbox[3] - bbox[1]

    padding = 6
    rect_x0, rect_y0 = 5, 5
    rect_x1 = rect_x0 + txt_width + 2 * padding
    rect_y1 = rect_y0 + txt_height + 2 * padding

    # Background rectangle
    draw.rectangle(
        [rect_x0, rect_y0, rect_x1, rect_y1],
        fill=(0, 0, 0, 180)
    )

    # Text
    draw.text(
        (rect_x0 + padding, rect_y0 + padding),
        text,
        fill=(255, 255, 255),
        font=font
    )

    return np.array(img)


# Run an episode for each agent stage
episode_reward = 0.0
done = truncated = False
step_count = 0

# 1. Untrained Agent (Random Actions)
frames_label = int(2 * FPS)  # show label for 2 seconds
label_text = "Untrained Agent (Random)"
print("[Untrained] Starting evaluation episode...")
# Add initial frame with label displayed for a short duration
initial_frame = env_random.render()
if initial_frame is not None:
    labeled_frame = add_label(initial_frame, label_text)
    for _ in range(frames_label):
        frames.append(labeled_frame)
while not (done or truncated):
    # Take a random action
    action = env_random.action_space.sample()
    obs_random, reward, done, truncated, info = env_random.step(action)
    episode_reward += reward
    frame = env_random.render()
    if frame is not None:
        frames.append(frame)
    step_count += 1
print(f"[Untrained] Episode finished after {step_count} steps, total reward {episode_reward:.2f}")
env_random.close()

# 2. Half-Trained Agent
frames_label = int(2 * FPS)
label_text = "Half-Trained Agent"
obs_half, info = env_half.reset(seed=SEED)  # reset to same initial state
done = truncated = False
episode_reward = 0.0
step_count = 0
print("[Half-Trained] Starting evaluation episode...")
# Initial labeled frame
initial_frame = env_half.render()
if initial_frame is not None:
    labeled_frame = add_label(initial_frame, label_text)
    for _ in range(frames_label):
        frames.append(labeled_frame)
# Run the episode with the half-trained model
while not (done or truncated):
    action, _state = model_half.predict(obs_half, deterministic=True)
    obs_half, reward, done, truncated, info = env_half.step(action)
    episode_reward += reward
    frame = env_half.render()
    if frame is not None:
        frames.append(frame)
    step_count += 1
print(f"[Half-Trained] Episode finished after {step_count} steps, total reward {episode_reward:.2f}")
env_half.close()

# 3. Fully-Trained Agent
frames_label = int(2 * FPS)
label_text = "Fully-Trained Agent"
obs_full, info = env_full.reset(seed=SEED)
done = truncated = False
episode_reward = 0.0
step_count = 0
print("[Fully-Trained] Starting evaluation episode...")
# Initial labeled frame
initial_frame = env_full.render()
if initial_frame is not None:
    labeled_frame = add_label(initial_frame, label_text)
    for _ in range(frames_label):
        frames.append(labeled_frame)
# Run the episode with the fully-trained model
while not (done or truncated):
    action, _state = model_full.predict(obs_full, deterministic=True)
    obs_full, reward, done, truncated, info = env_full.step(action)
    episode_reward += reward
    frame = env_full.render()
    if frame is not None:
        frames.append(frame)
    step_count += 1
print(f"[Fully-Trained] Episode finished after {step_count} steps, total reward {episode_reward:.2f}")
env_full.close()

# Save the combined frames as a GIF (evolution video)
imageio.mimsave("evolution.gif", frames, fps=FPS)
print("Evolution video saved as evolution.gif")

