#guireceipt.py
from tkinter import *
from tkinter import ttk
from receipt import Receipt # https://github.com/UncleEngineer/POS/
from subprocess import Popen
from tkinter import simpledialog
from tkinter import messagebox

GUI = Tk()
GUI.geometry('400x500')
GUI.title('TEST RECEIPT')

L = ttk.Label(GUI,text='Product').pack()
v_product = StringVar()
E1 = ttk.Entry(GUI,textvariable=v_product,font=('Angsana New',15))
E1.pack(pady=10)

L = ttk.Label(GUI,text='Price').pack()
v_price = StringVar()
E2 = ttk.Entry(GUI,textvariable=v_price,font=('Angsana New',15))
E2.pack(pady=20)

L = ttk.Label(GUI,text='Quantity').pack()
v_quan = StringVar()
E3 = ttk.Entry(GUI,textvariable=v_quan,font=('Angsana New',15))
E3.pack(pady=20)

global current
current = []

def AddProduct(event=None):
	product = v_product.get()
	price = int(v_price.get())
	quan = int(v_quan.get())
	total = price * quan
	allpd = [product,quan,total]
	current.append(allpd)
	print('ALL',current)

	res = v_result.get()
	v_result.set(res + '-{} @{} [{}]\n'.format(product,quan,total))

	v_product.set('')
	v_price.set('')
	v_quan.set('')
	E1.focus() #ให้เอาเคอเซอร์ไปไว้ช่องพิมพ์ตัวใหม่

def Clear():
	global current
	current = []


def PrintPDF():
	global current
	total = sum([p[2] for p in current])
	#messagebox.showinfo('TOTAL','รวมสินค้าทั้งหมด: {:,.2f} บาท'.format(total))
	answer = simpledialog.askstring('Cash', 'รวมสินค้าทั้งหมด: {:,.2f} บาท ลูกค้าชำระเงินมาเท่าไร [บาท]?'.format(total))
	Receipt(current,int(answer))
	v_result.set('---------RESULT----------\n')
	Popen('report.pdf',shell=True)

	current = []


BF = Frame(GUI)
BF.pack()
B1 = ttk.Button(BF,text='Add',command=AddProduct).grid(row=0,column=0,ipadx=20,ipady=10)
B2 = ttk.Button(BF,text='Clear',command=Clear).grid(row=0,column=1,ipadx=20,ipady=10)
B3 = ttk.Button(BF,text='Print',command=PrintPDF).grid(row=0,column=2,ipadx=20,ipady=10)

E3.bind('<Return>',AddProduct)

v_result = StringVar()
v_result.set('---------RESULT----------\n')

LR = ttk.Label(GUI,textvariable=v_result,font=('Angsana New',15),foreground='green')
LR.pack(pady=10)


GUI.mainloop()