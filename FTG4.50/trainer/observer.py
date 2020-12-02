from typing import Dict
import numpy as np

class Observer(object):
    """ gymの環境から欲しい情報を抽出する """
    def __init__(self):
        pass

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