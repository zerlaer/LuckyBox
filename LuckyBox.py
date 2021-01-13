from tkinter import *
import random

root = Tk()
root.title("LuckyBox                                                                   作者：小明同学")
root.geometry("600x600")

background_image = PhotoImage(file="bg.png")
background = Label(root, image=background_image, bd=0)
background.pack()
data = ["风清扬", "无崖子", "东邪", "西毒", "南帝", "北丐", "张三", "李四"]
going = True
is_run = False


def lottery_roll(one, two):
    global going
    show_member = random.choice(data)
    one.set(show_member)
    if going:
        root.after(50, lottery_roll, one, two)
    else:
        two.set("让我们恭喜 {} ".format(show_member))
        going = True
        return


def lottery_start(one, two):
    global is_run
    if is_run:
        return
    is_run = True
    two.set("下一个幸运儿会是谁呢")
    lottery_roll(one, two)


def lottery_end():
    global going, is_run
    if is_run:
        going = False
        is_run = False


var1 = StringVar(value="即 将 开 始")
label1 = Label(root, textvariable=var1, justify="center", anchor=CENTER, bg="#FF5252", width=14, height=1,
                    fg="#FCE4EC",
                    font="微软雅黑 -30 bold")
label1.place(anchor=NW, x=160, y=180)
var2 = StringVar(value="下一个幸运儿会是谁呢")
label2 = Label(root, textvariable=var2, justify="center", anchor=CENTER, width=18, height=2, bg="#FF5252",
                    font="微软雅黑 -30 bold", foreground="#FCE4EC")
label2.place(anchor=NW, x=120, y=260)
button1 = Button(root, text="开始抽奖", command=lambda: lottery_start(var1, var2), width=10, height=2, bg="#00bcd4",
                 font="楷体 -18 bold")
button1.place(anchor=NW, x=170, y=420)
button2 = Button(root, text="结束抽奖", command=lambda: lottery_end(), width=10, height=2, bg="#00bcd4",
                 font="楷体 -18 bold")
button2.place(anchor=NW, x=320, y=420)

root.mainloop()
