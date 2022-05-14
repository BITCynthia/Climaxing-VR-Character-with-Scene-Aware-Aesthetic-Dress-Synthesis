import tkinter
import tkinter.filedialog
from tkinter.filedialog import askdirectory

import os
from PIL import Image, ImageTk
from torchvision import transforms as transforms

import labelFigure.figure as figure

import globalVariance as GV
import fileProcess.figureWrite as figureWrite

# 路径
inputDir = "input/100"
# inputDir = "input/single"
outputDir = "output/figure"

# 创建一个界面窗口
win = tkinter.Tk()
win.title("Labeling figure... ")
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
    figureWrite.save(outputDir, GV.fileList[GV.ID])
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

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~性别~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    label1 = tkinter.Label(win, text="1、性别")
    label1.place(x=nameX, y=100)

    button1_1 = tkinter.Button(win, text="男", command=lambda: figure.gender(1))
    button1_1.place(x=nameXX[0], y=90)

    button1_2 = tkinter.Button(win, text="女", command=lambda: figure.gender(0))
    button1_2.place(x=nameXX[1], y=90)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~年龄~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    label1 = tkinter.Label(win, text="2、年龄")
    label1.place(x=nameX, y=140)

    button1_1 = tkinter.Button(win, text="儿童", command=lambda: figure.age(1))
    button1_1.place(x=nameXX[0], y=130)

    button1_2 = tkinter.Button(win, text="成年人", command=lambda: figure.age(2))
    button1_2.place(x=nameXX[1], y=130)

    button1_3 = tkinter.Button(win, text="老年", command=lambda: figure.age(3))
    button1_3.place(x=nameXX[2], y=130)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~年龄~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    label1 = tkinter.Label(win, text="3、身高")
    label1.place(x=nameX, y=180)

    button1_1 = tkinter.Button(win, text="矮", command=lambda: figure.height(1))
    button1_1.place(x=nameXX[0], y=170)

    button1_2 = tkinter.Button(win, text="中等", command=lambda: figure.height(2))
    button1_2.place(x=nameXX[1], y=170)

    button1_3 = tkinter.Button(win, text="高", command=lambda: figure.height(3))
    button1_3.place(x=nameXX[2], y=170)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~年龄~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    label1 = tkinter.Label(win, text="4、体型")
    label1.place(x=nameX, y=220)

    button1_1 = tkinter.Button(win, text="偏瘦", command=lambda: figure.shape(1))
    button1_1.place(x=nameXX[0], y=210)

    button1_2 = tkinter.Button(win, text="中等", command=lambda: figure.shape(2))
    button1_2.place(x=nameXX[1], y=210)

    button1_3 = tkinter.Button(win, text="偏胖", command=lambda: figure.shape(3))
    button1_3.place(x=nameXX[2], y=210)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~年龄~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    label1 = tkinter.Label(win, text="5、肤色")
    label1.place(x=nameX, y=260)

    button1_1 = tkinter.Button(win, text="白", command=lambda: figure.skinColr(1))
    button1_1.place(x=nameXX[0], y=250)

    button1_2 = tkinter.Button(win, text="黄", command=lambda: figure.skinColr(2))
    button1_2.place(x=nameXX[1], y=250)

    button1_3 = tkinter.Button(win, text="黑", command=lambda: figure.skinColr(3))
    button1_3.place(x=nameXX[2], y=250)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~年龄~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    label1 = tkinter.Label(win, text="6、发色")
    label1.place(x=nameX, y=300)

    button1_1 = tkinter.Button(win, text="黑", command=lambda: figure.hair(1))
    button1_1.place(x=nameXX[0], y=290)

    button1_2 = tkinter.Button(win, text="黄", command=lambda: figure.hair(2))
    button1_2.place(x=nameXX[1], y=290)

    button1_3 = tkinter.Button(win, text="红", command=lambda: figure.hair(3))
    button1_3.place(x=nameXX[2], y=290)

    button1_4 = tkinter.Button(win, text="其他", command=lambda: figure.hair(4))
    button1_4.place(x=nameXX[3], y=290)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~上一张-下一张~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    buttonPre = tkinter.Button(win, text="<--上一张", command=previousImg)
    buttonPre.place(x=600, y=350)

    buttonNext = tkinter.Button(win, text="下一张-->", command=nextImg)
    buttonNext.place(x=800, y=350)

    win.mainloop()


if __name__ == '__main__':
    main()
