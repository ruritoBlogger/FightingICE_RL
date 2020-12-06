import numpy as np

from memory import Memory

class Trainer(object):
    """ 選手の学習や試合の状態を管理する """

    # TODO: agentの基底クラスを実装してアップキャストする
    def __init__(self, env: any, agent: any):
        """
        初期化

        :param env: gymの環境(observerでwrap済み)
        :param agent: 学習させたいagent

        """

        self.env = env
        self.agent = agent
        self.memory = None

    def train(self, episode: int, batch_size: int, gamma: float):
        """
        学習を実施する

        :param episode: 試合数
        :param batch_size: experience replayを実施するときに用いる過去のデータ数
        :param gamma: 価値関数の値をどれだけ重要視するかどうか
        """

        for i in range(episode):

            frame_data = self.env.reset()
            done = False
            self.memory = Memory()

            while not done:
                # TODO: 毎回get_observation_spaceを実行しないようにしておく
                action = self.agent.get_action(frame_data, self.env.get_observation_space())
                next_frame_data, reward, done, info = self.env.step(action)

                # NOTE: experience replayを実施するため試合を回しながら学習させない
                self.memory.add((frame_data, action, reward, next_frame_data))

                frame_data = next_frame_data

            batch = self.memory.sample(batch_size)

            inputs = np.zeros((batch_size, ))
            targets = np.zeros((batch_size, self.env.get_observation_space()))

            # ランダムに取り出した過去の行動記録から学習を実施(=experience replay)
            for j, (frame_data, action, reward, next_frame_data) in enumerate(batch):
                # TODO: 学習させる時と同じやりかたで変形しておく
                inputs[j: j+1] = frame_data

                # TODO: [0]をつける意味を理解する
                expect_Q = self.agent.model.predict(frame_data)[0]
                next_action = expect_Q.index(max(expect_Q))

                # TODO: [0]をつける意味を理解する
                target = reward + gamma * self.agent.model.predict(frame_data)[0][next_action]

                targets[j] = self.agent.predict(frame_data)
                targets[j][action] = target

            self.agent.update(inputs, targets)
