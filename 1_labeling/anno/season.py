import tkinter
import tkinter.filedialog
from tkinter.filedialog import askdirectory

import os
from PIL import Image, ImageTk
from torchvision import transforms as transforms

import labelScene.season as season

import globalVariance as GV
import fileProcess.seasonWrite as seasonWrite

# 路径
inputDir = "input/100"
# inputDir = "input/single"
outputDir = "output/season"

# 创建一个界面窗口
win = tkinter.Tk()
win.title("Labeling season... ")
win.geometry("1200x600+50+50")

# 距离
nameX = 480
nameXX = [(nameX + 100 + 60 * i) for i in range(10)]


def render():
    load = Image.open(os.path.join(GV.dir, GV.fileList[GV.ID]))
    load = transforms.Resize((450, 400))(load)
    render = ImageTk.PhotoImage(load)
    img = tkinter.Label(win, image=render)
    img.image = render
    img.place(x=20, y=100)

    return


def previousImg():
    GV.ID -= 1
    if (GV.ID <= 0):
        GV.ID = 0
    render()

    return


def nextImg():
    seasonWrite.save(outputDir, GV.fileList[GV.ID])
    GV.ID += 1
    render()

    return


def choose_dir():
    GV.dir = askdirectory(title='选择文件夹')
    GV.fileList = os.listdir(GV.dir)
    render()
    return


def main():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~选择文件夹的文本框和按钮~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    e = tkinter.StringVar()
    e_entry = tkinter.Entry(win, width=40, textvariable=e)
    e_entry.place(x=40, y=60)

    button = tkinter.Button(win, text="Open Dir", command=choose_dir)
    button.place(x=360, y=60)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~显示图像~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    label = tkinter.Label(win, text="Image")
    label.place(x=200, y=100)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~画一条线~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    line1 = tkinter.Canvas(win)
    line1.create_line(0, 0, 0, 260, width=10)
    line1.place(x=460, y=0)

    line2 = tkinter.Canvas(win)
    line2.create_line(0, 0, 0, 260, width=10)
    line2.place(x=460, y=260)

    line3 = tkinter.Canvas(win)
    line3.create_line(0, 0, 0, 260, width=10)
    line3.place(x=460, y=520)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~服装连体分体选择~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    label1 = tkinter.Label(win, text="1、季节")
    label1.place(x=nameX, y=220)

    button1_1 = tkinter.Button(win, text="春", command=season.spring)
    button1_1.place(x=nameXX[0], y=210)

    button1_2 = tkinter.Button(win, text="夏", command=season.summer)
    button1_2.place(x=nameXX[1], y=210)

    button1_3 = tkinter.Button(win, text="秋", command=season.autumn)
    button1_3.place(x=nameXX[2], y=210)

    button1_3 = tkinter.Button(win, text="冬", command=season.winter)
    button1_3.place(x=nameXX[3], y=210)

    button1_3 = tkinter.Button(win, text="建议根据服装推测季节", command=season.other)
    button1_3.place(x=nameXX[4], y=210)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~上一张-下一张~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    buttonPre = tkinter.Button(win, text="<--上一张", command=previousImg)
    buttonPre.place(x=600, y=300)

    buttonNext = tkinter.Button(win, text="下一张-->", command=nextImg)
    buttonNext.place(x=800, y=300)

    win.mainloop()


if __name__ == '__main__':
    main()
