import gym
from gym_fightingice.envs.Machete import Machete

def main():
    env = gym.make("FightingiceDataNoFrameskip-v0", java_env_path="/home/troll/lesson/ken/FTG4.50")

    frame_data = env.reset(p2="MctsAi")
    done = False
    
    while not done:
        if frame_data[67] >= 300 and frame_data[0] - frame_data[66] <= 300:
            frame_data, reward, done, info = env.step(32)


if __name__ == "__main__":
    main()
