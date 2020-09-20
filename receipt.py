# receipt.py

# pip install reportlab

from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from datetime import datetime


def Receipt(pdlist,cash=500):
	count = len(pdlist)
	 
	diff = count * 4

	pdfmetrics.registerFont(TTFont('F1','tahomabd.ttf'))
	pdfmetrics.registerFont(TTFont('F2','tahoma.ttf'))

	c = canvas.Canvas('report.pdf') #สร้างไฟล์ pdf
	c.setPageSize((58 * mm, (70 + diff)  * mm))

	###########START#############
	c.setFont('F2',7)
	c.drawString(10 * mm, (60  + diff) * mm,'ใบเสร็จรับเงิน/ใบกำกับภาษีอย่างย่อ')

	textlines = ['บริษัท ซูชิ 999 จำกัด',
				 'ที่อยู่ 19 พหลโยธิน พญาไท กทม. 10400',
				 'เบอร์โทร 02-2345678',
				 'TAX ID: 0105567001000']

	###  Multiple Rows ###
	# center = 58 / 2 = 29
	'''
	text = c.beginText(10 * mm, 80 * mm)
	text.setFont('F2',6)

	for line in textlines:
		text.textLine(line)

	c.drawText(text)
	'''
	###  Center Rows ###
	#c.drawCentredString(29 * mm,60 *mm,'TAX ID: 0105567001111')
	textlines.reverse() # ทำให้ข้อความสลับลำดับก่อนหลัง

	c.setFont('F2',6)

	for i,line in enumerate(textlines):
		c.drawCentredString(29 * mm,(47 + (i*3)  + diff) * mm,line)

	#######TS ID##########

	c.setFont('F2',6)
	c.drawString(10 * mm, (42  + diff) * mm,'TS: 14132412')

	c.drawString(8 * mm, (35  + diff) * mm,'PD')
	c.drawString(28 * mm, (35  + diff) * mm,'QT')
	c.drawString(45 * mm, (35  + diff) * mm,'TTL')
	c.drawString(6 * mm, (33  + diff) * mm,'-'*58) # UNDER LINE

	#######DATE TIME##########
	yth = int(datetime.now().strftime('%Y')) + 543

	dt = datetime.now().strftime('%d/%m/{} %H:%M'.format(yth)) #strftime.org
	c.drawString(30 * mm,(42  + diff) * mm, dt)

	###########PRODUCT LIST#############
	c.setFont('F2',7) #ตั้งค่าฟอนต์ F2 ขนาด 7


	for i,(p,q,t) in enumerate(pdlist): 
		pdname = p
		pdquan = str(q)
		total = '{:,.2f}'.format(t)
		# pdprice = '10.00'
		# c.drawString(7 * mm,65 * mm, '{} @{}'.format(pdname,pdprice)) #ใส่ราคาต่อหน่วยด้วย
		c.drawString(7 * mm,(30 - (i*4) + diff) * mm, pdname)
		c.drawRightString(30 * mm,(30 - (i*4) + diff) * mm, pdquan)
		c.drawRightString(50 * mm,(30 - (i*4) + diff) * mm, total)


	quan = sum([p[1] for p in pdlist])
	total = sum([p[2] for p in pdlist])
	vat = total * (7/107)
	nettotal = total * (100/107)


	finaltext = ['Net Total','Vat 7%','Change','Cash','Total']
	finalnum = [nettotal,vat,cash-total,cash,total]



	for i,(ft,fn) in enumerate(zip(finaltext,finalnum)):
		if ft != 'Total':
			c.drawString(10 * mm, (10 + (i*4)) * mm,ft)
			c.drawRightString(50 * mm,(10 + (i*4)) * mm,'{:,.2f}'.format(fn))
	
	c.setFont('F2',6)
	c.drawString(6 * mm, (13 + (i*4)) * mm,'-'*58) # UNDER LINE
	c.setFont('F2',8)
	c.drawString(10 * mm, (10 + (i*4)) * mm,ft)
	c.drawRightString(50 * mm,(10 + (i*4)) * mm,'{:,.2f}'.format(fn))
	c.drawRightString(30 * mm,(10 + (i*4)) * mm, '{:,d}'.format(quan))

	c.setFont('F2',6)
	c.drawString(6 * mm, 24 * mm,'-'*58) # UNDER LINE
	c.showPage()
	c.save()


if __name__ == '__main__':

	pdlist = [['ส้ม',20,200],['กล้วย',10,70],['แอปเปิ้ล',2,20],
			['ส้ม',20,200],['กล้วย',10,70],['แอปเปิ้ล',2,20],
			['ส้ม',20,200],['กล้วย',10,70],['แอปเปิ้ล',2,20],
			['ส้ม',20,200],['กล้วย',10,70],['แอปเปิ้ล',2,20],
			['ส้ม',20,200],['กล้วย',10,70],['แอปเปิ้ล',2,20],
			['ส้ม',20,200],['กล้วย',10,70],['แอปเปิ้ล',2,20],
			['ส้ม',20,200],['กล้วย',10,70],['แอปเปิ้ล',2,20],
			['ส้ม',20,200],['กล้วย',10,70],['แอปเปิ้ล',2,20],
			['ส้ม',20,200],['กล้วย',10,70],['แอปเปิ้ล',2,20],
			['ส้ม',20,200],['กล้วย',10,70],['แอปเปิ้ล',2,20],
			['ส้ม',20,200],['กล้วย',10,70],['แอปเปิ้ล',2,20],
			['ส้ม',20,200],['กล้วย',10,70],['แอปเปิ้ล',2,20],
			['ส้ม',20,200],['กล้วย',10,70],['แอปเปิ้ล',2,20]]

	Receipt(pdlist,5000)

	# open pdf after run
	from subprocess import Popen
	Popen('report.pdf',shell=True)