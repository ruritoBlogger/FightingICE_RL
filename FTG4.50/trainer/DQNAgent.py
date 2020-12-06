from typing import Dict, List, Union
from gym import spaces
from tensorflow import keras

from action import Action
from state import State

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

        # TODO: 損失関数や最適化アルゴリズムを変更出来るようにする
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

    def predict(self, data: any) -> List[float]:
        """
        現在の状態から最適な行動を予想する

        :param data: 入力(現在の状態)
        """

        # NOTE: 出力値はそれぞれの行動を実施すべき確率
        return self.model.predict(data)

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
    # TODO: モデルの保存や読み込み部分を実装する


    def __init__(self, learning_rate: float, action_size: int) -> None:
        """
        初期化を実施

        :param learning_rate: NNの学習率
        :param action_size: 実施出来るアクションの数
        """
        self.model = NN(learning_rate, action_size)

    def get_action(self, data: List[Union[int, float]], observation_space: spaces) -> Action:
        """
        現在の状態から最適な行動を求める
        :param data: 現在の状態
        :param observation_space: 画面のサイズなどの情報
        :return: 行動(int)
        """

        # TODO: ε-greedy法を実装する

        action_value = self.model.predict(data)

        # NOTE: 一番評価値が高い行動を選択する(Actionにキャストしておく)
        # HACK: numpyに置き換える
        best_action = Action(action_value.index(max(action_value)))

        return best_action

    def update(self, data: any, label: any) -> None:
        """
        選手の学習を実施する

        :param data: 教師データ
        :param label: 教師ラベル
        """

        self.model.fit(data, label)
