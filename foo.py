#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter as tk  #补充：如果你用的是Python2，那么很可能库名是Tkinter

"""窗口主体"""
root = tk.Tk()

root.title("Gobang")
root.geometry("760x560")

"""棋子提示"""
side_canvas = tk.Canvas(root, width = 220, height = 50)
side_canvas.grid(row = 0, column = 1)
side_canvas.create_oval(110 - PIECE_SIZE, 25 - PIECE_SIZE,
                        110 + PIECE_SIZE, 25 + PIECE_SIZE,
                        fill = piece_color, tags = ("show_piece") )
"""棋子提示标签"""
var = tk.StringVar()
var.set("执黑棋")
person_label = tk.Label(root, textvariable = var, width = 12, anchor = tk.CENTER, 
                        font = ("Arial", 20) )
person_label.grid(row = 1, column = 1)

"""输赢提示标签"""
var1 = tk.StringVar()
var1.set("")
result_label = tk.Label(root, textvariable = var1, width = 12, height = 4, 
                        anchor = tk.CENTER, fg = "red", font = ("Arial", 25) )
result_label.grid(row = 2, column = 1, rowspan = 2)

"""游戏结束提示标签"""
var2 = tk.StringVar()
var2.set("")
game_label = tk.Label(root, textvariable = var2, width = 12, height = 4, 
                        anchor = tk.CENTER, font = ("Arial", 18) )
game_label.grid(row = 4, column = 1)

"""重置按钮"""
reset_button = tk.Button(root, text = "重新开始", font = 20, 
                          width = 8, command = gameReset)
reset_button.grid(row = 5, column = 1)

"""棋盘绘制"""
#背景
canvas = tk.Canvas(root, bg = "saddlebrown", width = 540, height = 540)
canvas.bind("<Button-1>", coorBack)  #对鼠标进行事件绑定，方便获取点击位置的坐标，下篇会用到
canvas.grid(row = 0, column = 0, rowspan = 6)
#线条
for i in range(15):
    canvas.create_line(32, (35 * i + 38), 522, (35 * i + 38))
    canvas.create_line((35 * i + 32), 38, (35 * i + 32), 528)
#点
point_x = [3, 3, 11, 11, 7]
point_y = [3, 11, 3, 11, 7]
for i in range(5):
    canvas.create_oval(35 * point_x[i] + 28, 35 * point_y[i] + 33, 
                       35 * point_x[i] + 36, 35 * point_y[i] + 41, fill = "black")
#数字坐标
for i in range(15):
    label = tk.Label(canvas, text = str(i + 1), fg = "black", bg = "saddlebrown",
                     width = 2, anchor = tk.E)
    label.place(x = 2, y = 35 * i + 28)
#字母坐标
count = 0
for i in range(65, 81):
    label = tk.Label(canvas, text = chr(i), fg = "black", bg = "saddlebrown")
    label.place(x = 35 * count + 25, y = 2)
    count += 1

"""窗口循环"""
root.mainloop()
