import numpy as np
import matplotlib.pyplot as plt

# データ
x = np.random.rand(100)
y = np.random.rand(100)

# 散布図を描画
plt.scatter(x, y)

# 軸ラベルを設定
plt.xlabel('Xlabel')
plt.ylabel('Ylabel')

# グリッドを表示
plt.grid(True)

# グラフを表示
plt.show()