# import tkinter as tk
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# def run_linear_convection():
#     # 获取输入框的值
#     nx = int(entry_nx.get())
#     nt = int(entry_nt.get())
#     dx = float(entry_dx.get())
#     dt = float(entry_dt.get())

#     # 获取选择的方程类型
#     equation_type = variable_equation_type.get()

#     # 初始化网格和初始条件
#     x = np.linspace(0, nx*dx, nx)
#     u0 = np.sin(2 * np.pi * x)  # 初始条件

#     # 进行时间迭代计算
#     u = u0.copy()  # 当前时间步的值

#     for n in range(nt):
#         un = u.copy()  # 上一个时间步的值
#         for i in range(1, nx-1):
#             if equation_type == '一维线性对流方程':
#                 # 一维线性对流方程
#                 c = float(entry_c.get())  # 获取对流速度
#                 u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])
#             elif equation_type == '一维扩散方程':
#                 # 一维扩散方程
#                 D = float(entry_D.get())  # 获取扩散系数
#                 u[i] = un[i] + D * dt / (dx**2) * (un[i+1] - 2 * un[i] + un[i-1])

#     # 清除之前的绘图
#     ax.cla()

#     # 绘制结果
#     ax.plot(x, u0, label='Initial Condition')
#     ax.plot(x, u, label='Final Solution')
#     ax.set_xlabel('x')
#     ax.set_ylabel('u')
#     ax.legend()

#     # 更新画布
#     canvas.draw()

# # 创建主窗口
# root = tk.Tk()
# root.title("偏微分方程求解")
# root.geometry("800x600")

# # 输入框
# label_nx = tk.Label(root, text="空间网格数 nx:")
# label_nx.pack()
# entry_nx = tk.Entry(root)
# entry_nx.pack()

# label_nt = tk.Label(root, text="时间步长数 nt:")
# label_nt.pack()
# entry_nt = tk.Entry(root)
# entry_nt.pack()

# label_dx = tk.Label(root, text="空间步长 dx:")
# label_dx.pack()
# entry_dx = tk.Entry(root)
# entry_dx.pack()

# label_dt = tk.Label(root, text="时间步长 dt:")
# label_dt.pack()
# entry_dt = tk.Entry(root)
# entry_dt.pack()

# # 方程类型下拉菜单
# label_equation_type = tk.Label(root, text="方程类型:")
# label_equation_type.pack()
# equation_types = ['一维线性对流方程', '一维扩散方程']
# variable_equation_type = tk.StringVar(root)
# variable_equation_type.set(equation_types[0])
# dropdown_equation_type = tk.OptionMenu(root, variable_equation_type, *equation_types)
# dropdown_equation_type.pack()

# # 对流速度和扩散系数输入框
# label_c = tk.Label(root, text="对流速度 c:")
# label_c.pack()
# entry_c = tk.Entry(root)
# entry_c.pack()

# label_D = tk.Label(root, text="扩散系数 D:")
# label_D.pack()
# entry_D = tk.Entry(root)
# entry_D.pack()

# # 运行按钮
# button_run = tk.Button(root, text="运行", command=run_linear_convection)
# button_run.pack()

# # 创建画布
# fig, ax = plt.subplots(figsize=(6, 4))
# canvas = FigureCanvasTkAgg(fig, master=root)
# canvas.get_tk_widget().pack()

# # 运行主循环
# root.mainloop()


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

    # 获取选择的方程类型
    equation_type = variable_equation_type.get()

    # 初始化网格和初始条件
    x = np.linspace(0, nx*dx, nx)
    u0 = np.sin(2 * np.pi * x)  # 初始条件

    # 进行时间迭代计算
    u = u0.copy()  # 当前时间步的值

    for n in range(nt):
        un = u.copy()  # 上一个时间步的值
        for i in range(1, nx-1):
            if equation_type == 'convection':
                # 一维线性对流方程
                c = float(entry_c.get())  # 获取对流速度
                u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])
            elif equation_type == 'diffusion':
                # 一维扩散方程
                D = float(entry_D.get())  # 获取扩散系数
                u[i] = un[i] + D * dt / (dx**2) * (un[i+1] - 2 * un[i] + un[i-1])

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
root.title("偏微分方程求解")
root.geometry("900x550")

# # 创建计算公式文本框
# text_equation = tk.Text(root, width=30, height=10)
# text_equation.grid(row=0, column=0, padx=10, pady=10, sticky='nw')
# text_equation.insert(tk.END, "一维线性对流方程公式：\n\n")
# text_equation.insert(tk.END, "u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])\n\n")
# text_equation.insert(tk.END, "一维扩散方程公式：\n\n")
# text_equation.insert(tk.END, "u[i] = un[i] + D * dt / (dx**2) * (un[i+1] - 2 * un[i] + un[i-1])")
# text_equation.config(state=tk.DISABLED)

# 创建计算公式文本框
text_equation = tk.Text(root, width=30, height=10)
text_equation.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nw')
text_equation.insert(tk.END, "一维线性对流方程公式：\n\n")
text_equation.insert(tk.END, "u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])\n\n")
text_equation.insert(tk.END, "一维扩散方程公式：\n\n")
text_equation.insert(tk.END, "u[i] = un[i] + D * dt / (dx**2) * (un[i+1] - 2 * un[i] + un[i-1])")
text_equation.config(state=tk.DISABLED)

# 输入框和控件
label_nx = tk.Label(root, text="空间网格数 nx:")
label_nx.grid(row=1, column=0, padx=10, pady=10, sticky='w')
entry_nx = tk.Entry(root)
entry_nx.grid(row=1, column=1)

label_nt = tk.Label(root, text="时间步长数 nt:")
label_nt.grid(row=2, column=0, padx=10, pady=10, sticky='w')
entry_nt = tk.Entry(root)
entry_nt.grid(row=2, column=1)

label_dx = tk.Label(root, text="空间步长 dx:")
label_dx.grid(row=3, column=0, padx=10, pady=10, sticky='w')
entry_dx = tk.Entry(root)
entry_dx.grid(row=3, column=1)

label_dt = tk.Label(root, text="时间步长 dt:")
label_dt.grid(row=4, column=0, padx=10, pady=10, sticky='w')
entry_dt = tk.Entry(root)
entry_dt.grid(row=4, column=1)

label_equation_type = tk.Label(root, text="方程类型:")
label_equation_type.grid(row=5, column=0, padx=10, pady=10, sticky='w')
equation_types = ['convection', 'diffusion']
variable_equation_type = tk.StringVar(root)
variable_equation_type.set(equation_types[0])
dropdown_equation_type = tk.OptionMenu(root, variable_equation_type, *equation_types)
dropdown_equation_type.grid(row=5, column=1, padx=10, pady=10, sticky='w')

label_c = tk.Label(root, text="对流速度 c:")
label_c.grid(row=6, column=0, padx=10, pady=10, sticky='w')
entry_c = tk.Entry(root)
entry_c.grid(row=6, column=1)

label_D = tk.Label(root, text="扩散系数 D:")
label_D.grid(row=7, column=0, padx=10, pady=10, sticky='w')
entry_D = tk.Entry(root)
entry_D.grid(row=7, column=1)

button_run = tk.Button(root, text="运行", command=run_linear_convection)
button_run.grid(row=8, column=0, padx=10, pady=10, sticky='w')

# 创建画布
# fig, ax = plt.subplots(figsize=(6, 4))
# canvas = FigureCanvasTkAgg(fig, master=root)
# canvas.get_tk_widget().grid(row=0, column=2, rowspan=9, padx=10, pady=10)
# 创建画布
fig, ax = plt.subplots(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=0, column=2, rowspan=9, padx=10, pady=0, sticky='nsew')

# 运行主循环
root.mainloop()