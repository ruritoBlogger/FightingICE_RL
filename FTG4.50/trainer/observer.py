from typing import Dict
import numpy as np
from gym import spaces
from typing import Tuple

class Observer(object):
    """ gymの環境から欲しい情報を抽出する """

    def __init__(self, env: any, p2: any) -> None:
        """
        内部でenvを持つ

        :param env: gymのenv
        :param p2: 対戦相手の情報
        """
        self._env = env
        self.p2 = p2

    def get_observation_space(self) -> spaces:
        """
        画面のサイズの情報を返す

        :return: 画面のサイズの情報
        """
        return self._env.observation_space

    def step(self, action: int) -> Tuple[Dict, float, bool, any]:
        """
        ある状態でActionを取った直後の結果を返す

        :param action: 実施したいAction
        :return: Actionを実施した直後の次の状態, 報酬, ゲームが終了しているかどうか, その他の情報
        """
        n_state, reward, done, info = self._env.step(action)
        return self.transform(n_state), reward, done, info

    def reset(self) -> Dict:
        """
        環境を初期化する

        :return: 初期化直後の状態
        """

        return self.transform(self._env.reset(p2=self.p2))


    def transform(self, frame_data: np.ndarray) -> Dict:
        """
        フレームデータを使いやすいように変形する
        data["self"]で操作キャラのデータを取得出来る
        data["opp"]で敵キャラのデータを取得出来る
        TODO: game_frame_runについて調査(gym_ai.py)
        data["frame_run"]でフレーム？の情報

        :param frame_data: フレームデータ
        :return: 整形したデータ
        """

        data = {"self": {}, "opp": {}, "frame_run": {}}
        data["self"]["HP"] = frame_data[0]
        data["self"]["Energy"] = frame_data[1]
        data["self"]["X"] = frame_data[2]
        data["self"]["Y"] = frame_data[3]
        data["self"]["SpeedX"] = 0 if frame_data[4] < 0 else 1
        data["self"]["AbsSpeedX"] = frame_data[5]
        data["self"]["SpeedY"] = 0 if frame_data[6] < 0 else 1
        data["self"]["AbsSpeedY"] = frame_data[7]
        data["self"]["CurrentAction"] = frame_data[8]
        data["self"]["State"] = frame_data[9]
        data["self"]["RemainingFrame"] = frame_data[10]

        data["opp"]["HP"] = frame_data[11]
        data["opp"]["Energy"] = frame_data[12]
        data["opp"]["X"] = frame_data[13]
        data["opp"]["Y"] = frame_data[14]
        data["opp"]["SpeedX"] = 0 if frame_data[15] < 0 else 1
        data["opp"]["AbsSpeedX"] = frame_data[16]
        data["opp"]["SpeedY"] = 0 if frame_data[17] < 0 else 1
        data["opp"]["AbsSpeedY"] = frame_data[18]
        data["opp"]["CurrentAction"] = frame_data[19]
        data["opp"]["State"] = frame_data[20]
        data["opp"]["RemainingFrame"] = frame_data[21]

        data["frame_run"] = frame_data[22]

        # WARNING: 情報を取れてないと0の場合もある
        data["self"]["HitDamage"] = frame_data[23]
        data["self"]["HitAreaNowX"] = frame_data[24]
        data["self"]["HitAreaNowY"] = frame_data[25]

        # TODO: gym_ai.pyを読んで意味を理解する
        data["self"]["NextHitDamage"] = frame_data[26]
        data["self"]["NextHitAreaNowX"] = frame_data[27]
        data["self"]["NextHitAreaNowY"] = frame_data[28]

        # WARNING: 情報を取れてないと0の場合もある
        data["opp"]["HitDamage"] = frame_data[29]
        data["opp"]["HitAreaNowX"] = frame_data[30]
        data["opp"]["HitAreaNowY"] = frame_data[31]

        # TODO: gym_ai.pyを読んで意味を理解する
        data["opp"]["NextHitDamage"] = frame_data[32]
        data["opp"]["NextHitAreaNowX"] = frame_data[33]
        data["opp"]["NextHitAreaNowY"] = frame_data[34]

        return data