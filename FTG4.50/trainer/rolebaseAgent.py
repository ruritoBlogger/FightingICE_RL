from action import Action

class RoleBaseAgent(object):
    """
    ルールベースで行動選択を行うエージェント
    """

    def __init__(self):
        pass

    def get_action(self, data) -> Action:
        """
        現在の状態から最適な行動を求める
        :param data: 現在の状態
        :return: 行動(int)
        """

        if data["opp"]["Energy"] >= 300 and data["self"]["HP"] - data["opp"]["HP"] <= 300:
            return Action.FOR_JUMP

        # TODO: self.gateway.jvm.enumerate.Stateを扱えるようにする
        # 情報が無いので聞く
        else:
            return Action.STAND_B
