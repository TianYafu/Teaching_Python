# -*- coding: UTF-8 -*-
from Tkinter import *	#导入Tkinter模块
import sys		#提供退出函数
import tkMessageBox		#提供弹窗功能
import serial			#串口库

root = Tk()						#构造基本窗口
root.geometry = "400x600+0+0"	#制定窗口大小,出现坐标

Speed = StringVar()				#三个参数:速度,串口号,sendFlag防止串口被关闭以前再被打开(一般由于按键速度太快和电脑速度太慢导致)
comnumber = StringVar()
sendFlag = True


def serial_send():		#串口工作函数,被speed_set函数调用	
	global sendFlag
	if((comnumber.get() in ["com1",'com2','com3','com4','com5','com6']) and (sendFlag == True)):	#判断工作状态(防止异常,死机和其他毛病)
		c1 = serial.Serial(comnumber.get(),9600)		#打开串口
		sendFlag = False			#......
		c1.write(Speed.get())	#串口发数据
		c1.close()				#关串口
		sendFlag = True		#............
	else:
		tkMessageBox.showinfo("Error","Working_stat,error\n please check com number and serial port")  	#工作异常弹窗
	

def Speed_set():		#按键工作函数
	print "comnumber = %s,speed = %s"  %(comnumber.get(),Speed.get())		#print大法号,Python好		此行可删
	serial_send()		#调用serial_send函数

def Show_about():		#弹窗
	tkMessageBox.showinfo("About","This Programme is for \n STM_32 class \n designed by \n Tian Yafu,Ren xinyang,Xue bajie")

label1 = Label(text = "Stm32 Computer Control System").pack()		#添加标签

button = Button(root,text = "Speed Set",command = Speed_set).pack()		#按钮

scale = Scale(root,from_ = 1,to = 4,orient = "horizontal",variable = Speed).pack()		#滑动条

label2 = Label(text = "COM Number").pack()			
entry = Entry(root,textvariable = comnumber).pack()			#输入框

button1 = Button(root,text = "Exit",command = sys.exit).pack()		
button2 = Button(root,text = "About",command = Show_about).pack()

root.mainloop()			#程序工作在循环状态
