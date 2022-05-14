import tkinter
import tkinter.filedialog
from tkinter.filedialog import askdirectory

import os
from PIL import Image, ImageTk
from torchvision import transforms as transforms

import labelclothes.cloth as cloth
import globalVariance as GV
import fileProcess.colthWrite as colthWrite

# 创建一个界面窗口
win = tkinter.Tk()
win.title("Labeling cloth attributes ... ")
win.geometry("1450x850+50+50")

# 路径
inputDir = "input/100"
outputDir = "output/clothes"

# 距离
nameX = 445
nameXX = [(nameX + 60 + 60 * i) for i in range(16)]
difference = 25


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
    colthWrite.savel(outputDir, GV.fileList[GV.ID])
    GV.ID += 1
    render()

    cloth.NewImage()
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
    line1.place(x=440, y=0)

    line2 = tkinter.Canvas(win)
    line2.create_line(0, 0, 0, 260, width=10)
    line2.place(x=440, y=260)

    line3 = tkinter.Canvas(win)
    line3.create_line(0, 0, 0, 260, width=10)
    line3.place(x=440, y=520)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~上衣~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    label_upper = tkinter.Label(win, text="—————————————————上衣—————————————————")
    label_upper.place(x=450, y=25)

    Ulabel1 = tkinter.Label(win, text="  1.类型")
    Ulabel1.place(x=nameX, y=50)
    button1_1 = tkinter.Button(win, text="西装", command=lambda: cloth.UpperType(1))
    button1_1.place(x=nameXX[0], y=45)
    button1_2 = tkinter.Button(win, text="运动装", command=lambda: cloth.UpperType(2))
    button1_2.place(x=nameXX[1], y=45)
    button1_3 = tkinter.Button(win, text="冲锋衣", command=lambda: cloth.UpperType(3))
    button1_3.place(x=nameXX[2], y=45)
    button1_4 = tkinter.Button(win, text="羽绒服", command=lambda: cloth.UpperType(4))
    button1_4.place(x=nameXX[3], y=45)
    button1_5 = tkinter.Button(win, text="衬衫", command=lambda: cloth.UpperType(5))
    button1_5.place(x=nameXX[4], y=45)
    button1_6 = tkinter.Button(win, text="毛衣", command=lambda: cloth.UpperType(6))
    button1_6.place(x=nameXX[5], y=45)
    button1_7 = tkinter.Button(win, text="卫衣", command=lambda: cloth.UpperType(7))
    button1_7.place(x=nameXX[6], y=45)
    button1_8 = tkinter.Button(win, text="呢大衣", command=lambda: cloth.UpperType(8))
    button1_8.place(x=nameXX[7], y=45)
    button1_9 = tkinter.Button(win, text="皮衣", command=lambda: cloth.UpperType(9))
    button1_9.place(x=nameXX[8], y=45)
    button1_10 = tkinter.Button(win, text="夹克衫", command=lambda: cloth.UpperType(10))
    button1_10.place(x=nameXX[9], y=45)
    button1_11 = tkinter.Button(win, text="背心", command=lambda: cloth.UpperType(11))
    button1_11.place(x=nameXX[10], y=45)
    button1_12 = tkinter.Button(win, text="皮草", command=lambda: cloth.UpperType(12))
    button1_12.place(x=nameXX[11], y=45)
    button1_13 = tkinter.Button(win, text="旗袍", command=lambda: cloth.UpperType(13))
    button1_13.place(x=nameXX[12], y=45)
    button1_14 = tkinter.Button(win, text="打底", command=lambda: cloth.UpperType(14))
    button1_14.place(x=nameXX[13], y=45)
    button1_14 = tkinter.Button(win, text="泳衣", command=lambda: cloth.UpperType(15))
    button1_14.place(x=nameXX[14], y=45)
    button1_14 = tkinter.Button(win, text="T恤", command=lambda: cloth.UpperType(16))
    button1_14.place(x=nameXX[15], y=45)

    Ulabel2 = tkinter.Label(win, text="  2.长度")
    Ulabel2.place(x=nameX, y=50 + difference * 1)
    button2_1 = tkinter.Button(win, text="超短", command=lambda: cloth.UpperLength(1))
    button2_1.place(x=nameXX[0], y=50 + difference * 1 - 5)
    button2_2 = tkinter.Button(win, text="   短   ", command=lambda: cloth.UpperLength(2))
    button2_2.place(x=nameXX[1], y=50 + difference * 1 - 5)
    button2_3 = tkinter.Button(win, text=" 适 中 ", command=lambda: cloth.UpperLength(3))
    button2_3.place(x=nameXX[2], y=50 + difference * 1 - 5)
    button2_4 = tkinter.Button(win, text=" 中 长 ", command=lambda: cloth.UpperLength(4))
    button2_4.place(x=nameXX[3], y=50 + difference * 1 - 5)
    button2_5 = tkinter.Button(win, text="超长", command=lambda: cloth.UpperLength(5))
    button2_5.place(x=nameXX[4], y=50 + difference * 1 - 5)

    Ulabel3 = tkinter.Label(win, text="  3.版型")
    Ulabel3.place(x=nameX, y=50 + difference * 2)
    button3_1 = tkinter.Button(win, text="紧身", command=lambda: cloth.UpperModel(1))
    button3_1.place(x=nameXX[0], y=50 + difference * 2 - 5)
    button3_2 = tkinter.Button(win, text=" 收 腰 ", command=lambda: cloth.UpperModel(2))
    button3_2.place(x=nameXX[1], y=50 + difference * 2 - 5)
    button3_3 = tkinter.Button(win, text=" 直 筒 ", command=lambda: cloth.UpperModel(3))
    button3_3.place(x=nameXX[2], y=50 + difference * 2 - 5)
    button3_4 = tkinter.Button(win, text=" 宽 松 ", command=lambda: cloth.UpperModel(4))
    button3_4.place(x=nameXX[3], y=50 + difference * 2 - 5)
    button3_5 = tkinter.Button(win, text="其他", command=lambda: cloth.UpperModel(5))
    button3_5.place(x=nameXX[4], y=50 + difference * 2 - 5)

    Ulabel4 = tkinter.Label(win, text="  4.领口")
    Ulabel4.place(x=nameX, y=50 + difference * 3)
    button4_1 = tkinter.Button(win, text="毛领", command=lambda: cloth.UpperCollar(1))
    button4_1.place(x=nameXX[0], y=50 + difference * 3 - 5)
    button4_2 = tkinter.Button(win, text="polo领", command=lambda: cloth.UpperCollar(2))
    button4_2.place(x=nameXX[1], y=50 + difference * 3 - 5)
    button4_3 = tkinter.Button(win, text=" 小V领", command=lambda: cloth.UpperCollar(3))
    button4_3.place(x=nameXX[2], y=50 + difference * 3 - 5)
    button4_4 = tkinter.Button(win, text=" 大V领", command=lambda: cloth.UpperCollar(4))
    button4_4.place(x=nameXX[3], y=50 + difference * 3 - 5)
    button4_5 = tkinter.Button(win, text="圆领", command=lambda: cloth.UpperCollar(5))
    button4_5.place(x=nameXX[4], y=50 + difference * 3 - 5)
    button4_6 = tkinter.Button(win, text="翻领", command=lambda: cloth.UpperCollar(6))
    button4_6.place(x=nameXX[5], y=50 + difference * 3 - 5)
    button4_7 = tkinter.Button(win, text="高领", command=lambda: cloth.UpperCollar(7))
    button4_7.place(x=nameXX[6], y=50 + difference * 3 - 5)
    button4_8 = tkinter.Button(win, text="连帽领", command=lambda: cloth.UpperCollar(8))
    button4_8.place(x=nameXX[7], y=50 + difference * 3 - 5)
    button4_9 = tkinter.Button(win, text="无领", command=lambda: cloth.UpperCollar(9))
    button4_9.place(x=nameXX[8], y=50 + difference * 3 - 5)
    button4_10 = tkinter.Button(win, text="U领", command=lambda: cloth.UpperCollar(10))
    button4_10.place(x=nameXX[9], y=50 + difference * 3 - 5)
    button4_11 = tkinter.Button(win, text="其他", command=lambda: cloth.UpperCollar(11))
    button4_11.place(x=nameXX[10], y=50 + difference * 3 - 5)

    Ulabel5 = tkinter.Label(win, text="  5.袖长")
    Ulabel5.place(x=nameX, y=50 + difference * 4)
    button5_1 = tkinter.Button(win, text="无袖", command=lambda: cloth.UpperSleeveLength(1))
    button5_1.place(x=nameXX[0], y=50 + difference * 4 - 5)
    button5_2 = tkinter.Button(win, text=" 短 袖 ", command=lambda: cloth.UpperSleeveLength(2))
    button5_2.place(x=nameXX[1], y=50 + difference * 4 - 5)
    button5_3 = tkinter.Button(win, text=" 中 袖 ", command=lambda: cloth.UpperSleeveLength(3))
    button5_3.place(x=nameXX[2], y=50 + difference * 4 - 5)
    button5_4 = tkinter.Button(win, text="七分袖", command=lambda: cloth.UpperSleeveLength(4))
    button5_4.place(x=nameXX[3], y=50 + difference * 4 - 5)
    button5_5 = tkinter.Button(win, text="长袖", command=lambda: cloth.UpperSleeveLength(5))
    button5_5.place(x=nameXX[4], y=50 + difference * 4 - 5)
    button5_6 = tkinter.Button(win, text="吊带", command=lambda: cloth.UpperSleeveLength(6))
    button5_6.place(x=nameXX[5], y=50 + difference * 4 - 5)
    button5_7 = tkinter.Button(win, text="其他", command=lambda: cloth.UpperSleeveLength(7))
    button5_7.place(x=nameXX[6], y=50 + difference * 4 - 5)

    Ulabel6 = tkinter.Label(win, text="  6.袖肩")
    Ulabel6.place(x=nameX, y=50 + difference * 5)
    button6_1 = tkinter.Button(win, text="直筒", command=lambda: cloth.UpperShouders(1))
    button6_1.place(x=nameXX[0], y=50 + difference * 5 - 5)
    button6_2 = tkinter.Button(win, text="泡泡袖", command=lambda: cloth.UpperShouders(2))
    button6_2.place(x=nameXX[1], y=50 + difference * 5 - 5)
    button6_3 = tkinter.Button(win, text=" 无 袖 ", command=lambda: cloth.UpperShouders(3))
    button6_3.place(x=nameXX[2], y=50 + difference * 5 - 5)
    button6_4 = tkinter.Button(win, text=" 其 他 ", command=lambda: cloth.UpperShouders(4))
    button6_4.place(x=nameXX[3], y=50 + difference * 5 - 5)

    Ulabel7 = tkinter.Label(win, text="  7.袖口")
    Ulabel7.place(x=nameX, y=50 + difference * 6)
    button7_1 = tkinter.Button(win, text="收口", command=lambda: cloth.UpperCuff(1))
    button7_1.place(x=nameXX[0], y=50 + difference * 6 - 5)
    button7_2 = tkinter.Button(win, text="灯笼袖", command=lambda: cloth.UpperCuff(2))
    button7_2.place(x=nameXX[1], y=50 + difference * 6 - 5)
    button7_3 = tkinter.Button(win, text=" 其 他 ", command=lambda: cloth.UpperCuff(3))
    button7_3.place(x=nameXX[2], y=50 + difference * 6 - 5)

    Ulabel8 = tkinter.Label(win, text="  8.前襟")
    Ulabel8.place(x=nameX, y=50 + difference * 7)
    button8_1 = tkinter.Button(win, text="套头", command=lambda: cloth.UpperOpening(1))
    button8_1.place(x=nameXX[0], y=50 + difference * 7 - 5)
    button8_2 = tkinter.Button(win, text=" 纽 扣 ", command=lambda: cloth.UpperOpening(2))
    button8_2.place(x=nameXX[1], y=50 + difference * 7 - 5)
    button8_3 = tkinter.Button(win, text=" 拉 链 ", command=lambda: cloth.UpperOpening(3))
    button8_3.place(x=nameXX[2], y=50 + difference * 7 - 5)
    button8_4 = tkinter.Button(win, text=" 敞 开 ", command=lambda: cloth.UpperOpening(4))
    button8_4.place(x=nameXX[3], y=50 + difference * 7 - 5)
    button8_5 = tkinter.Button(win, text="其他", command=lambda: cloth.UpperOpening(5))
    button8_5.place(x=nameXX[4], y=50 + difference * 7 - 5)

    Ulabel9 = tkinter.Label(win, text="  9.材质")
    Ulabel9.place(x=nameX, y=50 + difference * 8)
    button9_1 = tkinter.Button(win, text="针织", command=lambda: cloth.UpperMaterial(1))
    button9_1.place(x=nameXX[0], y=50 + difference * 8 - 5)
    button9_2 = tkinter.Button(win, text=" 皮 制 ", command=lambda: cloth.UpperMaterial(2))
    button9_2.place(x=nameXX[1], y=50 + difference * 8 - 5)
    button9_3 = tkinter.Button(win, text=" 亚 麻 ", command=lambda: cloth.UpperMaterial(3))
    button9_3.place(x=nameXX[2], y=50 + difference * 8 - 5)
    button9_4 = tkinter.Button(win, text=" 羊 毛 ", command=lambda: cloth.UpperMaterial(4))
    button9_4.place(x=nameXX[3], y=50 + difference * 8 - 5)
    button9_5 = tkinter.Button(win, text="棉质", command=lambda: cloth.UpperMaterial(5))
    button9_5.place(x=nameXX[4], y=50 + difference * 8 - 5)
    button9_6 = tkinter.Button(win, text="其他", command=lambda: cloth.UpperMaterial(6))
    button9_6.place(x=nameXX[5], y=50 + difference * 8 - 5)

    Ulabel10 = tkinter.Label(win, text="10.图形")
    Ulabel10.place(x=nameX, y=50 + difference * 9)
    button10_1 = tkinter.Button(win, text="纯色", command=lambda: cloth.UpperPattern(1))
    button10_1.place(x=nameXX[0], y=50 + difference * 9 - 5)
    button10_2 = tkinter.Button(win, text=" 纹 理 ", command=lambda: cloth.UpperPattern(2))
    button10_2.place(x=nameXX[1], y=50 + difference * 9 - 5)
    button10_3 = tkinter.Button(win, text=" 图 案 ", command=lambda: cloth.UpperPattern(3))
    button10_3.place(x=nameXX[2], y=50 + difference * 9 - 5)
    button10_4 = tkinter.Button(win, text=" 其 他 ", command=lambda: cloth.UpperPattern(4))
    button10_4.place(x=nameXX[3], y=50 + difference * 9 - 5)

    label_upper = tkinter.Label(win, text="记得保存并新增（确认是上衣，不是连衣裙)", fg='red')
    label_upper.place(x=600, y=310)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~裤子~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    label_trousers = tkinter.Label(win, text="—————————————————裤子—————————————————")
    label_trousers.place(x=450, y=330)

    Tlabel1 = tkinter.Label(win, text="  1.类型")
    Tlabel1.place(x=nameX, y=330 + difference * 1)
    Tbutton1_1 = tkinter.Button(win, text="西裤", command=lambda: cloth.TrousersType(1))
    Tbutton1_1.place(x=nameXX[0], y=330 + difference * 1 - 5)
    Tbutton1_2 = tkinter.Button(win, text="牛仔", command=lambda: cloth.TrousersType(2))
    Tbutton1_2.place(x=nameXX[1], y=330 + difference * 1 - 5)
    Tbutton1_3 = tkinter.Button(win, text="休闲裤", command=lambda: cloth.TrousersType(3))
    Tbutton1_3.place(x=nameXX[2], y=330 + difference * 1 - 5)
    Tbutton1_4 = tkinter.Button(win, text="运动裤", command=lambda: cloth.TrousersType(4))
    Tbutton1_4.place(x=nameXX[3], y=330 + difference * 1 - 5)
    Tbutton1_5 = tkinter.Button(win, text="短裤", command=lambda: cloth.TrousersType(5))
    Tbutton1_5.place(x=nameXX[4], y=330 + difference * 1 - 5)
    Tbutton1_6 = tkinter.Button(win, text="丝袜", command=lambda: cloth.TrousersType(6))
    Tbutton1_6.place(x=nameXX[5], y=330 + difference * 1 - 5)
    Tbutton1_7 = tkinter.Button(win, text="喇叭裤", command=lambda: cloth.TrousersType(7))
    Tbutton1_7.place(x=nameXX[6], y=330 + difference * 1 - 5)
    Tbutton1_8 = tkinter.Button(win, text="背带裤", command=lambda: cloth.TrousersType(8))
    Tbutton1_8.place(x=nameXX[7], y=330 + difference * 1 - 5)
    Tbutton1_8 = tkinter.Button(win, text="泳裤", command=lambda: cloth.TrousersType(9))
    Tbutton1_8.place(x=nameXX[8], y=330 + difference * 1 - 5)
    Tbutton1_9 = tkinter.Button(win, text="其他", command=lambda: cloth.TrousersType(10))
    Tbutton1_9.place(x=nameXX[9], y=330 + difference * 1 - 5)

    Tlabel2 = tkinter.Label(win, text="  2.腰线")
    Tlabel2.place(x=nameX, y=330 + difference * 2)
    Tbutton2_1 = tkinter.Button(win, text="高腰", command=lambda: cloth.TrousersWaist(1))
    Tbutton2_1.place(x=nameXX[0], y=330 + difference * 2 - 5)
    Tbutton2_2 = tkinter.Button(win, text="正常", command=lambda: cloth.TrousersWaist(2))
    Tbutton2_2.place(x=nameXX[1], y=330 + difference * 2 - 5)
    Tbutton2_3 = tkinter.Button(win, text=" 低 腰 ", command=lambda: cloth.TrousersWaist(3))
    Tbutton2_3.place(x=nameXX[2], y=330 + difference * 2 - 5)
    Tbutton2_3 = tkinter.Button(win, text=" 无 ", command=lambda: cloth.TrousersWaist(0))
    Tbutton2_3.place(x=nameXX[3], y=330 + difference * 2 - 5)

    Tlabel3 = tkinter.Label(win, text="  3.长度")
    Tlabel3.place(x=nameX, y=330 + difference * 3)
    Tbutton3_1 = tkinter.Button(win, text="  短 ", command=lambda: cloth.TrousersLength(1))
    Tbutton3_1.place(x=nameXX[0], y=330 + difference * 3 - 5)
    Tbutton3_2 = tkinter.Button(win, text="及膝", command=lambda: cloth.TrousersLength(2))
    Tbutton3_2.place(x=nameXX[1], y=330 + difference * 3 - 5)
    Tbutton3_3 = tkinter.Button(win, text="及小腿", command=lambda: cloth.TrousersLength(3))
    Tbutton3_3.place(x=nameXX[2], y=330 + difference * 3 - 5)
    Tbutton3_4 = tkinter.Button(win, text=" 及踝  ", command=lambda: cloth.TrousersLength(4))
    Tbutton3_4.place(x=nameXX[3], y=330 + difference * 3 - 5)

    Tlabel4 = tkinter.Label(win, text="  4.版型")
    Tlabel4.place(x=nameX, y=330 + difference * 4)
    Tbutton4_1 = tkinter.Button(win, text="紧身", command=lambda: cloth.TrousersModel(1))
    Tbutton4_1.place(x=nameXX[0], y=330 + difference * 4 - 5)
    Tbutton4_2 = tkinter.Button(win, text="直筒", command=lambda: cloth.TrousersModel(2))
    Tbutton4_2.place(x=nameXX[1], y=330 + difference * 4 - 5)
    Tbutton4_3 = tkinter.Button(win, text=" 宽 松 ", command=lambda: cloth.TrousersModel(3))
    Tbutton4_3.place(x=nameXX[2], y=330 + difference * 4 - 5)

    Tlabel5 = tkinter.Label(win, text="  5.材质")
    Tlabel5.place(x=nameX, y=330 + difference * 5)
    Tbutton5_1 = tkinter.Button(win, text="雪纺", command=lambda: cloth.TrousersMaterial(1))
    Tbutton5_1.place(x=nameXX[0], y=330 + difference * 5 - 5)
    Tbutton5_2 = tkinter.Button(win, text="皮制", command=lambda: cloth.TrousersMaterial(2))
    Tbutton5_2.place(x=nameXX[1], y=330 + difference * 5 - 5)
    Tbutton5_3 = tkinter.Button(win, text="亚麻", command=lambda: cloth.TrousersMaterial(3))
    Tbutton5_3.place(x=nameXX[2], y=330 + difference * 5 - 5)
    Tbutton5_4 = tkinter.Button(win, text="羊毛", command=lambda: cloth.TrousersMaterial(4))
    Tbutton5_4.place(x=nameXX[3], y=330 + difference * 5 - 5)
    Tbutton5_5 = tkinter.Button(win, text="棉质", command=lambda: cloth.TrousersMaterial(5))
    Tbutton5_5.place(x=nameXX[4], y=330 + difference * 5 - 5)
    Tbutton5_6 = tkinter.Button(win, text="其他", command=lambda: cloth.TrousersMaterial(6))
    Tbutton5_6.place(x=nameXX[5], y=330 + difference * 5 - 5)

    Tlabel6 = tkinter.Label(win, text="  6.图案")
    Tlabel6.place(x=nameX, y=330 + difference * 6)
    Tbutton6_1 = tkinter.Button(win, text="纯色", command=lambda: cloth.TrousersPattern(1))
    Tbutton6_1.place(x=nameXX[0], y=330 + difference * 6 - 5)
    Tbutton6_2 = tkinter.Button(win, text="纹理", command=lambda: cloth.TrousersPattern(2))
    Tbutton6_2.place(x=nameXX[1], y=330 + difference * 6 - 5)
    Tbutton6_3 = tkinter.Button(win, text="图案", command=lambda: cloth.TrousersPattern(3))
    Tbutton6_3.place(x=nameXX[2], y=330 + difference * 6 - 5)
    Tbutton6_4 = tkinter.Button(win, text=" 其 他 ", command=lambda: cloth.TrousersPattern(4))
    Tbutton6_4.place(x=nameXX[3], y=330 + difference * 6 - 5)

    label_trousers = tkinter.Label(win, text="记得保存并新增（确认是裤子，不是连体裤)", fg='red')
    label_trousers.place(x=600, y=510)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~裙~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    label_dress = tkinter.Label(win, text="—————————————————裙子—————————————————")
    label_dress.place(x=450, y=530)

    Dlabel1 = tkinter.Label(win, text="  1.类型")
    Dlabel1.place(x=nameX, y=530 + difference * 1)
    Dbutton1_1 = tkinter.Button(win, text="吊带", command=lambda: cloth.SkirtType(1))
    Dbutton1_1.place(x=nameXX[0], y=530 + difference * 1 - 5)
    Dbutton1_2 = tkinter.Button(win, text="背带", command=lambda: cloth.SkirtType(2))
    Dbutton1_2.place(x=nameXX[1], y=530 + difference * 1 - 5)
    Dbutton1_3 = tkinter.Button(win, text=" 包 臀 ", command=lambda: cloth.SkirtType(3))
    Dbutton1_3.place(x=nameXX[2], y=530 + difference * 1 - 5)
    Dbutton1_4 = tkinter.Button(win, text="A 版", command=lambda: cloth.SkirtType(4))
    Dbutton1_4.place(x=nameXX[3], y=530 + difference * 1 - 5)
    Dbutton1_5 = tkinter.Button(win, text="直筒", command=lambda: cloth.SkirtType(5))
    Dbutton1_5.place(x=nameXX[4], y=530 + difference * 1 - 5)
    Dbutton1_6 = tkinter.Button(win, text="蓬蓬裙", command=lambda: cloth.SkirtType(6))
    Dbutton1_6.place(x=nameXX[5], y=530 + difference * 1 - 5)
    Dbutton1_7 = tkinter.Button(win, text="其他", command=lambda: cloth.SkirtType(7))
    Dbutton1_7.place(x=nameXX[6], y=530 + difference * 1 - 5)

    Dlabel2 = tkinter.Label(win, text="  2.腰线")
    Dlabel2.place(x=nameX, y=530 + difference * 2)
    Dbutton2_1 = tkinter.Button(win, text="高腰", command=lambda: cloth.SkirtWaist(1))
    Dbutton2_1.place(x=nameXX[0], y=530 + difference * 2 - 5)
    Dbutton2_2 = tkinter.Button(win, text="正常", command=lambda: cloth.SkirtWaist(2))
    Dbutton2_2.place(x=nameXX[1], y=530 + difference * 2 - 5)
    Dbutton2_3 = tkinter.Button(win, text=" 低 腰 ", command=lambda: cloth.SkirtWaist(3))
    Dbutton2_3.place(x=nameXX[2], y=530 + difference * 2 - 5)
    Dbutton2_4 = tkinter.Button(win, text=" 无 ", command=lambda: cloth.SkirtWaist(0))
    Dbutton2_4.place(x=nameXX[3], y=530 + difference * 2 - 5)

    Dlabel3 = tkinter.Label(win, text="  3.长度")
    Dlabel3.place(x=nameX, y=530 + difference * 3)
    Dbutton3_1 = tkinter.Button(win, text="  短 ", command=lambda: cloth.SkirtLength(1))
    Dbutton3_1.place(x=nameXX[0], y=530 + difference * 3 - 5)
    Dbutton3_2 = tkinter.Button(win, text="及膝", command=lambda: cloth.SkirtLength(2))
    Dbutton3_2.place(x=nameXX[1], y=530 + difference * 3 - 5)
    Dbutton3_3 = tkinter.Button(win, text="及小腿", command=lambda: cloth.SkirtLength(3))
    Dbutton3_3.place(x=nameXX[2], y=530 + difference * 3 - 5)
    Dbutton3_4 = tkinter.Button(win, text="及踝", command=lambda: cloth.SkirtLength(4))
    Dbutton3_4.place(x=nameXX[3], y=530 + difference * 3 - 5)
    Dbutton3_5 = tkinter.Button(win, text="拖地", command=lambda: cloth.SkirtLength(5))
    Dbutton3_5.place(x=nameXX[4], y=530 + difference * 3 - 5)
    Dbutton3_6 = tkinter.Button(win, text="其他", command=lambda: cloth.SkirtLength(6))
    Dbutton3_6.place(x=nameXX[5], y=530 + difference * 3 - 5)

    Dlabel4 = tkinter.Label(win, text="  4.褶皱")
    Dlabel4.place(x=nameX, y=530 + difference * 4)
    Dbutton4_1 = tkinter.Button(win, text="  有 ", command=lambda: cloth.SkirtFold(1))
    Dbutton4_1.place(x=nameXX[0], y=530 + difference * 4 - 5)
    Dbutton4_2 = tkinter.Button(win, text="  无 ", command=lambda: cloth.SkirtFold(2))
    Dbutton4_2.place(x=nameXX[1], y=530 + difference * 4 - 5)

    Dlabel5 = tkinter.Label(win, text="  5.材质")
    Dlabel5.place(x=nameX, y=530 + difference * 5)
    Dbutton5_1 = tkinter.Button(win, text="针织", command=lambda: cloth.SkirtMaterial(1))
    Dbutton5_1.place(x=nameXX[0], y=530 + difference * 5 - 5)
    Dbutton5_2 = tkinter.Button(win, text="雪纺", command=lambda: cloth.SkirtMaterial(2))
    Dbutton5_2.place(x=nameXX[1], y=530 + difference * 5 - 5)
    Dbutton5_3 = tkinter.Button(win, text=" 皮 制 ", command=lambda: cloth.SkirtMaterial(3))
    Dbutton5_3.place(x=nameXX[2], y=530 + difference * 5 - 5)
    Dbutton5_4 = tkinter.Button(win, text="亚麻", command=lambda: cloth.SkirtMaterial(4))
    Dbutton5_4.place(x=nameXX[3], y=530 + difference * 5 - 5)
    Dbutton5_5 = tkinter.Button(win, text="羊毛", command=lambda: cloth.SkirtMaterial(5))
    Dbutton5_5.place(x=nameXX[4], y=530 + difference * 5 - 5)
    Dbutton5_6 = tkinter.Button(win, text=" 棉 质 ", command=lambda: cloth.SkirtMaterial(6))
    Dbutton5_6.place(x=nameXX[5], y=530 + difference * 5 - 5)
    Dbutton5_7 = tkinter.Button(win, text="其他", command=lambda: cloth.SkirtMaterial(7))
    Dbutton5_7.place(x=nameXX[6], y=530 + difference * 5 - 5)

    Dlabel6 = tkinter.Label(win, text="  6.图案")
    Dlabel6.place(x=nameX, y=530 + difference * 6)
    Dbutton6_1 = tkinter.Button(win, text="纯色", command=lambda: cloth.SkirtPattern(1))
    Dbutton6_1.place(x=nameXX[0], y=530 + difference * 6 - 5)
    Dbutton6_2 = tkinter.Button(win, text="纹理", command=lambda: cloth.SkirtPattern(2))
    Dbutton6_2.place(x=nameXX[1], y=530 + difference * 6 - 5)
    Dbutton6_3 = tkinter.Button(win, text=" 图 案 ", command=lambda: cloth.SkirtPattern(3))
    Dbutton6_3.place(x=nameXX[2], y=530 + difference * 6 - 5)
    Dbutton6_4 = tkinter.Button(win, text="其他", command=lambda: cloth.SkirtPattern(4))
    Dbutton6_4.place(x=nameXX[3], y=530 + difference * 6 - 5)

    label_skirt = tkinter.Label(win, text="记得保存并新增（确认是半身裙，不是连衣裙)", fg='red')
    label_skirt.place(x=600, y=705)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~新增~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    label_dress = tkinter.Label(win, text="—————————————————————————————————————")
    label_dress.place(x=450, y=725)

    buttonUpper = tkinter.Button(win, text="         上 衣         ", command=lambda: cloth.clothType(1))
    buttonUpper.place(x=450, y=305)

    buttonTrousers = tkinter.Button(win, text="         裤 子         ", command=lambda: cloth.clothType(2))
    buttonTrousers.place(x=450, y=510)

    buttonDress = tkinter.Button(win, text="         裙 子         ", command=lambda: cloth.clothType(3))
    buttonDress.place(x=450, y=705)

    buttonDress = tkinter.Button(win, text="   连衣裙   ", command=lambda: cloth.clothType(4))
    buttonDress.place(x=450, y=740)

    buttonDress = tkinter.Button(win, text="   连体裤   ", command=lambda: cloth.clothType(5))
    buttonDress.place(x=530, y=740)

    buttonDress = tkinter.Button(win, text="             保存（新增）             ", command=cloth.NewCloth)
    buttonDress.place(x=640, y=740)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~上一张-下一张~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    buttonPre = tkinter.Button(win, text="<--上一张", command=previousImg)
    buttonPre.place(x=750, y=780)

    buttonNext = tkinter.Button(win, text="下一张-->", command=nextImg)
    buttonNext.place(x=900, y=780)

    win.mainloop()


if __name__ == '__main__':
    main()
