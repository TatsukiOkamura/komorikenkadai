import numpy as np

# 4次元空間の座標
a = np.array([1, 2, 3, 4])
b = np.array([4, 3, 2, 1])

# ユークリッド距離を計算
distance = np.linalg.norm(a - b)

print("ユークリッド距離:", distance)