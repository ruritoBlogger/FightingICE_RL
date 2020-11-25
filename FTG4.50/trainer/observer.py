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

        # TODO: 添字が合っているかどうか確認する
        for i in range(56):
            if frame_data[i+8]:
                data["self"]["currentAction"] = i+8
                break

        data["self"]["RemainingFrame"] = frame_data[63]

        data["opp"]["HP"] = frame_data[64]
        data["opp"]["Energy"] = frame_data[65]
        data["opp"]["X"] = frame_data[66]
        data["opp"]["Y"] = frame_data[67]
        data["opp"]["SpeedX"] = 0 if frame_data[68] < 0 else 1
        data["opp"]["AbsSpeedX"] = frame_data[69]
        data["opp"]["SpeedY"] = 0 if frame_data[70] < 0 else 1
        data["opp"]["AbsSpeedY"] = frame_data[71]

        for i in range(56):
            if frame_data[i+72]:
                data["self"]["currentAction"] = i+72
                break

        data["opp"]["RemainingFrame"] = frame_data[127]

        data["frame_run"] = frame_data[128]

        # WARNING: 情報を取れてないと0の場合もある
        data["self"]["HitDamage"] = frame_data[129]
        data["self"]["HitAreaNowX"] = frame_data[130]
        data["self"]["HitAreaNowY"] = frame_data[131]

        # TODO: gym_ai.pyの方が謎
        data["self"]["NextHitDamage"] = frame_data[132]
        data["self"]["NextHitAreaNowX"] = frame_data[133]
        data["self"]["NextHitAreaNowY"] = frame_data[134]

        # WARNING: 情報を取れてないと0の場合もある
        data["opp"]["HitDamage"] = frame_data[135]
        data["opp"]["HitAreaNowX"] = frame_data[136]
        data["opp"]["HitAreaNowY"] = frame_data[137]

        # TODO: gym_ai.pyの方が謎
        data["opp"]["NextHitDamage"] = frame_data[138]
        data["opp"]["NextHitAreaNowX"] = frame_data[139]
        data["opp"]["NextHitAreaNowY"] = frame_data[140]

        return data