import gym
from gym_fightingice.envs.Machete import Machete

from observer import Observer
from rolebaseAgent import RoleBaseAgent
from DQNAgent import DQNAgent
from trainer import Trainer

def main():
    env = gym.make("FightingiceDataNoFrameskip-v0", java_env_path="/home/rurito/lesson/ken/FTG4.50")
    # HACK: aciontから自動で取ってこれるようにしておく
    action_size = 56
    learning_rate = 0.1
    batch_size = 10
    episode = 3
    gamma = 0.1

    p2 = "MctsAi"
    env = Observer(env, p2)
    agent = DQNAgent(learning_rate, action_size)
    # agent = RoleBaseAgent()
    trainer = Trainer(env, agent)

    trainer.train(episode, batch_size, gamma)

if __name__ == "__main__":
    main()
