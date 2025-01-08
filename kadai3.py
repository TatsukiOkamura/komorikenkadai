import matplotlib.pyplot as plt

# データ
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# 散布図を描画
plt.scatter(x, y)

# 軸ラベルを設定
plt.xlabel('X軸ラベル')
plt.ylabel('Y軸ラベル')

# グリッドを表示
plt.grid(True)

# グラフを表示
plt.show()