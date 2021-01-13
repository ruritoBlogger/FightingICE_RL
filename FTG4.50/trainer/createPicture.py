from typing import List, Union
import matplotlib.pyplot as plt

def create_image(data: List[Union[float, int]], image_path: str) -> None:
    """
    グラフを生成する

    :param data: グラフにプロットしたいデータ
    :param image_path: 画像の保存先
    """

    plt.clf()
    x = range(len(data))
    plt.plot(x, data)
    plt.savefig(image_path)

if __name__ == '__main__':
    image_path = 'reward.png'

    data = []
    with open('../reward_data.txt') as f:
        for s_line in f:
            data.append(float(s_line.replace('\n', '')))

    create_image(data, image_path)
