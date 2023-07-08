import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def run_linear_convection():
    # 获取输入框的值
    nx = int(entry_nx.get())
    nt = int(entry_nt.get())
    dx = float(entry_dx.get())
    dt = float(entry_dt.get())
    c = 1.0

    # 初始化网格和初始条件
    x = np.linspace(0, nx*dx, nx)
    u0 = np.sin(2 * np.pi * x)  # 初始条件

    # 进行时间迭代计算
    u = u0.copy()  # 当前时间步的值

    for n in range(nt):
        un = u.copy()  # 上一个时间步的值
        for i in range(1, nx-1):
            # 使用一阶向前差分格式计算下一个时间步的值
            u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])

    # 清除之前的绘图
    ax.cla()

    # 绘制结果
    ax.plot(x, u0, label='Initial Condition')
    ax.plot(x, u, label='Final Solution')
    ax.set_xlabel('x')
    ax.set_ylabel('u')
    ax.legend()

    # 更新画布
    canvas.draw()

# 创建主窗口
root = tk.Tk()
root.title("一维线性对流方程求解")
root.geometry("800x600")

# 输入框
label_nx = tk.Label(root, text="空间网格数 nx:")
label_nx.pack()
entry_nx = tk.Entry(root)
entry_nx.pack()

label_nt = tk.Label(root, text="时间步长数 nt:")
label_nt.pack()
entry_nt = tk.Entry(root)
entry_nt.pack()

label_dx = tk.Label(root, text="空间步长 dx:")
label_dx.pack()
entry_dx = tk.Entry(root)
entry_dx.pack()

label_dt = tk.Label(root, text="时间步长 dt:")
label_dt.pack()
entry_dt = tk.Entry(root)
entry_dt.pack()

# 运行按钮
button_run = tk.Button(root, text="运行", command=run_linear_convection)
button_run.pack()

# 创建画布
fig, ax = plt.subplots(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# 运行主循环
root.mainloop()