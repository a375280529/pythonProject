# -*- coding: utf-8 -*-
import tkinter
# 导入消息对话框子模块
import tkinter.messagebox
from tkinter import simpledialog

# 创建主窗口
root = tkinter.Tk()
# 设置窗口大小
#root.minsize(300,300)
root.withdraw()

# # 声明函数
# def okqqq():
#     # 弹出对话框
#     # 返回值为True或者False
#     result = tkinter.messagebox.askokcancel(title = '标题~',message='内容：要吃饭嘛？')
#     print(result)
# # 添加按钮
# btn1 = tkinter.Button(root,text = 'ok',command = okqqq)
# btn1.pack()
#
# # 加入消息循环
# root.mainloop()

if __name__ == '__main__':
    r=""
    while r!="帅":
        r=simpledialog.askstring("颜值调查","你帅不帅",initialvalue="")
