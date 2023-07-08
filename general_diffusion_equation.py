# 一维扩散方程

import numpy as np
import matplotlib.pyplot as plt

# 设置空间网格和时间步长
nx = 100  # 空间网格数
nt = 100  # 时间步长数
dx = 1.0  # 空间步长
dt = 0.01  # 时间步长

# 设置速度和扩散系数
c = 1.0  # 对流速度
D = 0.1  # 扩散系数

# 初始化网格和初始条件
x = np.linspace(0, nx*dx, nx)
u0 = np.sin(2 * np.pi * x)  # 初始条件

# 进行时间迭代计算
u = u0.copy()  # 当前时间步的值

for n in range(nt):
    un = u.copy()  # 上一个时间步的值
    for i in range(1, nx-1):
        # 使用一阶向前差分格式计算下一个时间步的值
        u[i] = un[i] - c * dt / dx * (un[i] - un[i-1]) + D * dt / (dx ** 2) * (un[i+1] - 2 * un[i] + un[i-1])

# 绘制结果
plt.plot(x, u0, label='Initial Condition')
plt.plot(x, u, label='Final Solution')
plt.xlabel('x')
plt.ylabel('u')
plt.legend()
plt.show()
