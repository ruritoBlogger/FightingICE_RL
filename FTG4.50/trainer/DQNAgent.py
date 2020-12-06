from action import Action
from state import State
from typing import Dict
from gym import spaces
from tensorflow import keras

class NN(object):
    """ 状態価値関数を予想する """
    def __init__(self, learning_rate: float, action_size: int) -> None:
        """
        NNの初期化をやる

        :param learning_rate: 学習率
        :param action_size: 実施出来る行動の数
        """
        self.learning_rate = learning_rate

        # TODO: モデルの層の構成を簡単に変更出来るようにしておく
        self.model = keras.Sequential([
            keras.layers.Dense(, activation='relu'),
            keras.layers.Dense(action_size, activation='softmax')
        ])

        self.model.compile(optimizer='adam',
                           loss='sparse_categorical_crossentropy',
                           metrics=['accuracy']
                           )

    # TODO: 入力データの型を決める
    def fit(self, data: any, label: any) -> None:
        """
        学習を実施する

        :param data: 教師データ
        :param label: 教師ラベル
        """
        self.model.fit(data, label, epochs=1)

    # TODO: モデルの保存部分を実装する
    #       後パスの型(str or pathlib.Path)を決める
    def save_model(self, model_path: any):
        """
        モデルを保存する

        :param model_path: 保存先のパス
        """
        pass

    # TODO: モデルの読み込み部分を実装する
    #       後パスの型(str or pathlib.Path)を決める
    def load_model(self, model_path: any):
        """
        学習済みのモデルを読み込む

        :param model_path: 読み込みたいモデルのパス
        """
        pass

class DQNAgent(object):
    """
    深層学習を用いて行動選択を行うエージェント
    """

    def __init__(self):
        pass

    def get_action(self, data: Dict, observation_space: spaces) -> Action:
        """
        現在の状態から最適な行動を求める
        :param data: 現在の状態
        :param observation_space: 画面のサイズなどの情報
        :return: 行動(int)
        """




