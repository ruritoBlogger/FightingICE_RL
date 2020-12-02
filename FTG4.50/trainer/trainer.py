import gym
from gym_fightingice.envs.Machete import Machete
from observer import Observer
from rolebaseAgent import RoleBaseAgent

def main():
    env = gym.make("FightingiceDataNoFrameskip-v0", java_env_path="/home/rurito/lesson/ken/FTG4.50")

    frame_data = env.reset(p2="MctsAi")
    observer = Observer()
    agent = RoleBaseAgent()
    done = False
    
    while not done:
        action = agent.get_action(observer.transform(frame_data))
        frame_data, reward, done, info = env.step(action)


if __name__ == "__main__":
    main()
