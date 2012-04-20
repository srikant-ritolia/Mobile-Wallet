# Author : Srikant Ritolia
# project name :- Mobile Wallet
# contacts : email : srikant.ritolia@gmail.com,  phone no-9886579971

import appuifw
import e32
import time
import os, os.path
import telephone


PATH = u"C:\\Data\\MyApp"
if not os.path.exists(PATH):
	os.makedirs(PATH)


lock = e32.Ao_lock() # creating a lock object
depchoices=[u"Own",u"Taken"]
withchoices=[u"traveling",u"eating",u"laundry",u"stationary",u"for friend",u"others"]
dchoices=[u"to give",u"to take"]
moneychoice=[u"Deposit",u"Withdrawl",u"Balance",u"Dues",u"Mini Statement"]
cardchoice=[u"Store",u"View",u"Remove"]
cardstorechoice=[u"Debit Cards",u"Credit Cards",u"Id Cards"]
rechargechoice=[u"Store",u"Recharge"]
dfriend=[]
dfriendamt=[]
wfriend=[]
wfriendamt=[]
global x,y,z
x=0
y=0
z=0
global d,e;
d=0
e=0


f = file(u"c:\\Data\\MyApp\\test.txt", "w+")
f.close()

def on_exit(): # exit handler
    copy()
	 # does nothing fancy just quits the app


def save(filename, lst):
	f = file(filename, "a")
	for item in lst:
		print >> f, item
	f.close()
	
def count(lst):
	a=0;
	for i in lst:
		a=a+1;
	return a;

def copy():
	global z
	b=[0,0,0,0,0,0,0,0,0,0,0,0,0]
	b[0]=z	
	b[1]=count(dfriend)
	b[2]=count(dfriendamt)
	b[3]=count(wfriend)
	b[4]=count(wfriendamt)
	b[5]=count(debitcardbank)
	b[6]=count(debitcardno)
	b[7]=count(creditcardbank)
	b[8]=count(creditcardnumber)
	b[9]=count(idcardplace)
	b[10]=count(idcardno)
	b[11]=count(rechargeamt)
	b[12]=count(rechargeno)
	save(u"c:\\Data\\MyApp\\test.txt",b)
	save(u"c:\\Data\\MyApp\\test.txt",dfriend)
	save(u"c:\\Data\\MyApp\\test.txt",dfriendamt)
	save(u"c:\\Data\\MyApp\\test.txt",wfriend)
	save(u"c:\\Data\\MyApp\\test.txt",wfriendamt)
	save(u"c:\\Data\\MyApp\\test.txt",debitcardbank)
	save(u"c:\\Data\\MyApp\\test.txt",debitcardno)
	save(u"c:\\Data\\MyApp\\test.txt",creditcardbank)
	save(u"c:\\Data\\MyApp\\test.txt",creditcardnumber)
	save(u"c:\\Data\\MyApp\\test.txt",idcardplace)
	save(u"c:\\Data\\MyApp\\test.txt",idcardno)
	save(u"c:\\Data\\MyApp\\test.txt",rechargeamt)
	save(u"c:\\Data\\MyApp\\test.txt",rechargeno)
	appuifw.note(u"Thank you")
	lock.signal()

def deposit():
	selection = appuifw.selection_list(depchoices,search_field=1)
	global x
	global z
	global d;
	c="check";	
	if(selection==0 or selection==1):
		try:
			x = appuifw.query(u"Enter the amount to be deposited",'number') # get the item to be added
			d=d+x
			z=z+x
			if(selection==1):
				try:
					a=appuifw.query(u"Money was taken from",'text') 
					c=c+a;
				except:
					appuifw.note(u"Invalid entry","error")
					return 
				b=0;
				c=0;
				flag=0;
				for i in dfriend:
					if(a==i):
						dfriendamt[b]=dfriendamt[b]+x
						dfriendamt.append(dfriendamt[b])
						flag=1
					b=b+1;
				if(flag!=1):
					dfriend.append(a)
					dfriendamt.append(x)
				
		except:
			appuifw.note(u"Invalid entry","error")
	

def withdrawl():
	selection=appuifw.selection_list(withchoices,search_field=1)
	global y
	global z
	global e
	if(selection==0 or selection==1 or selection==2 or selection==3 or selection==4 or selection==5): 
		y = appuifw.query(u"Enter the amount you want to withdraw",'number')
		e=e+y
		if((z-y)<0):
			appuifw.note(u"Cannot withdraw  Insufficient balance","error")
			return
		z=z-y
		if(selection==4):
			a=appuifw.query(u"Enter the friends name",'text')
			b=0
			f=0
			flag=0
			flag1=0
			for i in dfriend:
				if(a==i):
					dfriendamt[b]=dfriendamt[b]-y
					flag=1
					if(dfriendamt[b]<0):
						c=dfriendamt[b]*-1
						dfriendamt.remove(dfriendamt[b])
						dfriend.remove(dfriend[b])
						wfriend.append(a)
						wfriendamt.append(c)
					if(dfriend[b]==0):
						dfriendamt.remove(dfriendamt[b])
						dfriend.remove(dfriend[b])
						
				b=b+1
				
			if(flag!=1):
				for i in wfriend:
					if(a==i):
						wfriendamt[f]=wfriendamt[f]+y
						flag1=1
					f=f+1
				if(flag1!=1):
					wfriend.append(a)
					wfriendamt.append(y)
	
def balance():
	global z;
	appuifw.note(u"Your Wallet Balance is %d" %(z))
		

def dues():
	selection=appuifw.selection_list(dchoices,search_field=1)
	if(selection==0):
		p=appuifw.selection_list(dfriend)
		if(p>=0):
			q=dfriendamt[p]
			appuifw.note(u"Amount to give him is %d" % (q))
	if(selection==1):
		p=appuifw.selection_list(wfriend)
		if(p>=0):
			q=wfriendamt[p]
			appuifw.note(u"Amount to take from him %d" % (q))

def ministatement():
	return


		
def money():
	selection=appuifw.selection_list(moneychoice,search_field=1)
	if(selection==0):
		deposit()
	if(selection==1):
		withdrawl()
	if(selection==2):
		balance()
	if(selection==3):
		dues()
	if(selection==4):
		ministatement()
	
		
password=0000
debitcardbank=[]
debitcardno=[]
creditcardbank=[]
creditcardnumber=[]
idcardplace=[]
idcardno=[]
def card():
	c1="cardcheck"
	c2=0
	selection=appuifw.selection_list(cardchoice,search_field=1)
	if(selection==0):
		selection1=appuifw.selection_list(cardstorechoice,search_field=1)
		if(selection1==0):
			try:
				x=appuifw.query(u"Enter the bank name",'text')
				y=appuifw.query(u"Enter your card number",'number')
				c1=c1+x
				c2=c2+y
			except:
				appuifw.note(u"Invalid entry","error")
				return;
			debitcardbank.append(x)
			z=encrypt(y)
			debitcardno.append(z)
			appuifw.note(u"Your card stored in encrypted from","conf")
			
		if(selection1==1):
			try:
				x=appuifw.query(u"Enter the bank name",'text')
				y=appuifw.query(u"Enter your card number",'number')
				c1=c1+x
				c2=c2+y
			except:
				appuifw.note(u"Invalid entry","error")
				return;
			creditcardbank.append(x)
			z=encrypt(y)
			creditcardnumber.append(z)
			appuifw.note(u"Your card stored in encrypted from","conf")
			
		if(selection1==2):
			try:
				x=appuifw.query(u"Enter the place name",'text')
				y=appuifw.query(u"Enter your id number",'number')
				c1=c1+x
				c2=c2+y
			except:
				appuifw.note(u"Invalid entry","error")
				return;
			idcardplace.append(x)
			idcardno.append(y)
			appuifw.note(u"Your id card stored ","conf")
			
	if(selection==1):
		selection1=appuifw.selection_list(cardstorechoice,search_field=1)
		if(selection1==0):
			if has_items(debitcardbank):
				selection2=appuifw.selection_list(debitcardbank,search_field=1)
				z=appuifw.query(u"Enter your password to decrypt",'code')
				if(z!=password):
					appuifw.note(u"Wrong password")
				if(z==password):
					p=decrypt(debitcardno[selection2])
					appuifw.note(u"Card number %d" % (p))
		if(selection1==1):
			if has_items(creditcardbank):
				selection2=appuifw.selection_list(creditcardbank,search_field=1)
				z=appuifw.query(u"Enter your password to decrypt",'code')
				if(z!=password):
					appuifw.note(u"Wrong password")
				if(z==password):
					p=decrypt(creditcardnumber[selection2])
					appuifw.note(u"Card number %d" %(p))
		if(selection1==2):
			if has_items(idcardplace):
				selection2=appuifw.selection_list(idcardplace,search_field=1)
				appuifw.note(u"Id number %d" %(idcardno[selection2]))
	if(selection==2):
		selection1=appuifw.selection_list(cardstorechoice,search_field=1)
		if(selection1==0):
			if has_items(debitcardbank):
				selection2=appuifw.selection_list(debitcardbank,search_field=1)
				debitcardbank.remove(debitcardbank[selection2])
				debitcardno.remove(debitcardno[selection2])
				appuifw.note(u"Your card has been removed","conf")
		if(selection1==1):
			if has_items(debitcardbank):
				selection2=appuifw.selection_list(creditcardbank,search_field=1)
				creditcardbank.remove(creditcardbank[selection2])
				creditcardnumber.remove(creditcardnumber[selection2])
				appuifw.note(u"Your card has been removed","conf")
		if(selection1==2):
			if has_items(idcardplace):
				selection2=appuifw.selection_list(idcardplace,search_field=1)
				idcardplace.remove(idcardplace[selection2])
				idcardno.remove(idcardno[selection2])
				appuifw.note(u"Your card has been removed","conf")
		
		
		
		
	

rechargeamt=[]
rechargeno=[]
def recharge():
	selection=appuifw.selection_list(rechargechoice,search_field=1)
	if(selection==0):
		try:
			x=appuifw.query(u"Enter coupon amount","number")
			y=appuifw.query(u"Enter the recharge serial number","number")
			z=encrypt(y)
			rechargeamt.append(x)
			rechargeno.append(z)
			appuifw.note(u"Your recharge coupon stored in encrypted from","conf")
		except:
			appuifw.note(u"Invalid entry", "error")
	if(selection==1):
		if has_items(rechargeamt):
			b=0;
			for i in rechargeamt:
				a=[u"%d" %(rechargeamt[b])]
				b=b+1
			
			selection1=appuifw.selection_list(a,search_field=1)
			
			z=appuifw.query(u"Enter your password to decrypt",'number')
			if(z!=password):
				appuifw.note(u"Wrong password")
			if(z==password):
				a='*141#'
				b=str(rechargeno[selection1])
				c='#'
				a=a+b+c
				telephone.dial(a)
				appuifw.note(u"Recharged successfully with amount %d" % (rechargeamt[selection1]))
				rechargeamt.remove(rechargeamt[selection1])
				rechargeno.remove(rechargeno[selection1])
					

def encrypt(y):
	c=0
	z=0
	while(y!=0):
		x=y%10
		y=y/10
		if(c%2==0):
			z=z+((x+1)*pow(10,c))
		else:
			z=z+((x-1)*pow(10,c))
		c=c+1
	return z
	
def decrypt(y):
	c=0
	z=0
	while(y!=0):
		x=y%10
		y=y/10
		if(c%2==0):
			z=z+((x-1)*pow(10,c))
		else:
			z=z+((x+1)*pow(10,c))
		c=c+1
	return z
	
def has_items(list): # to check and display errors appropriately
    if list:
        return True
    else:
        appuifw.note(u"Empty",'error')
        return False	

appuifw.app.title=u'Mobile Wallet' #set tite
appuifw.app.menu=[(u'Money',money),(u'Cards',card),(u'Recharge',recharge)]
appuifw.app.exit_key_handler = on_exit # set exit key handler
lock.wait()